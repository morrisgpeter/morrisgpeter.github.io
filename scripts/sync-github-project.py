#!/usr/bin/env python3
"""Safely reconcile planned GitHub issues and Project V2 fields.

Default is read-only dry run. --apply creates missing issues and fills in
project membership/fields for managed issues. Existing issue content and
execution status are never overwritten.
"""
import argparse
from datetime import date
import json
import re
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
MARKER_RE = re.compile(r"<!--\s*Portfolio Sync Key:\s*([a-zA-Z0-9_-]+)\s*-->")
SELECT_FIELDS = ("priority", "phase", "size")
DATE_FIELDS = ("start_date", "target_date")
REMOTE_FIELD_NAMES = {"start_date": "start date", "target_date": "target date"}
FIELDS = SELECT_FIELDS + DATE_FIELDS + ("status",)


def gh(*args, parse_json=True):
    result = subprocess.run(["gh", *map(str, args)], text=True, capture_output=True)
    if result.returncode:
        raise RuntimeError(f"gh {' '.join(map(str, args[:3]))} failed: {result.stderr.strip()}")
    if parse_json:
        return json.loads(result.stdout)
    return result.stdout.strip()


def load(name):
    with (HERE / name).open(encoding="utf-8") as f:
        return json.load(f)


def issue_marker(key):
    return f"<!-- Portfolio Sync Key: {key} -->"


def read_remote(repo, project):
    issues = gh("issue", "list", "--repo", repo, "--state", "all", "--limit", "1000", "--json", "number,title,body,state,url")
    data = gh("project", "item-list", project["number"], "--owner", project["owner"], "--limit", "1000", "--format", "json")
    items = {}
    for item in data.get("items", []):
        content = item.get("content") or {}
        if content.get("type") == "Issue" and content.get("repository") == repo:
            num = content.get("number")
            if num in items:
                raise ValueError(f"Duplicate project entries for issue #{num}")
            items[num] = item
    return issues, items


def validate(plan, config, issues):
    repo = config["project"]["repository"]
    if plan.get("repository") != repo:
        raise ValueError("Repository mismatch between plan and config")
    if plan.get("sync_policy", {}).get("delete_issues") is not False:
        raise ValueError("Safety requirement: delete_issues must be false")
    keys, numbers = set(), set()
    existing_by_number = {i["number"]: i for i in issues}
    remote_keys = {}
    for issue in issues:
        found = MARKER_RE.findall(issue.get("body") or "")
        if len(found) > 1:
            raise ValueError(f"Multiple sync markers in issue #{issue['number']}")
        if found:
            key = found[0]
            if key in remote_keys:
                raise ValueError(f"Duplicate remote sync key {key}")
            remote_keys[key] = issue
    for item in plan["issues"]:
        key, title = item.get("key"), item.get("title")
        if not key or not re.fullmatch(r"[a-zA-Z0-9_-]+", key) or not title:
            raise ValueError(f"Invalid issue key/title: {item}")
        if key in keys:
            raise ValueError(f"Duplicate plan key {key}")
        keys.add(key)
        number = item.get("number")
        if number is not None:
            if not isinstance(number, int) or number in numbers:
                raise ValueError(f"Invalid/duplicate issue number: {number}")
            numbers.add(number)
            if number not in existing_by_number:
                raise ValueError(f"Protected/planned issue #{number} is missing; refusing to recreate")
            if key in remote_keys and remote_keys[key]["number"] != number:
                raise ValueError(f"Key {key} points to a different issue")
        if item.get("managed") is False and number is None:
            raise ValueError(f"Unmanaged issue {key} must have a number")
        for field in SELECT_FIELDS + ("status",):
            if field in item and item[field] not in config["fields"][field]["options"]:
                raise ValueError(f"Invalid {field} for {key}: {item[field]}")
        for field in DATE_FIELDS:
            if field in item:
                try:
                    date.fromisoformat(item[field])
                except (TypeError, ValueError) as exc:
                    raise ValueError(f"Invalid {field} for {key}: {item[field]}") from exc
        if all(f in item for f in DATE_FIELDS) and item["start_date"] > item["target_date"]:
            raise ValueError(f"Start date after target date for {key}")
        if item.get("managed") is not False:
            if number is None and key not in remote_keys:
                matches = [i for i in issues if i["title"] == title]
                if matches:
                    raise ValueError(f"Existing issue with title '{title}' has no matching sync marker; manual review needed")
    return remote_keys, existing_by_number


def plan_actions(plan, config, issues, items, remote_keys, by_number):
    actions = []
    for entry in plan["issues"]:
        key = entry["key"]
        protected = entry.get("managed") is False
        issue = by_number.get(entry.get("number")) if entry.get("number") is not None else remote_keys.get(key)
        if protected:
            actions.append(("KEEP", entry, issue, None))
            continue
        if issue is None:
            actions.append(("CREATE", entry, None, None))
            continue
        project_item = items.get(issue["number"])
        if project_item is None:
            actions.append(("ADD_PROJECT", entry, issue, None))
            continue
        changes = []
        for field in SELECT_FIELDS + DATE_FIELDS:
            expected = entry.get(field)
            remote_name = REMOTE_FIELD_NAMES.get(field, field)
            if expected is not None and project_item.get(remote_name) != expected:
                changes.append(field)
        if changes:
            actions.append(("SET_FIELDS", entry, issue, changes))
        else:
            actions.append(("KEEP", entry, issue, None))
    return actions


def add_to_project(issue_url, config):
    p = config["project"]
    return gh("project", "item-add", p["number"], "--owner", p["owner"], "--url", issue_url, "--format", "json")["id"]


def set_field(item_id, field, value, config):
    p, spec = config["project"], config["fields"][field]
    command = ["project", "item-edit", "--id", item_id,
               "--project-id", p["id"], "--field-id", spec["id"]]
    if field in DATE_FIELDS:
        command.extend(["--date", value])
    else:
        command.extend(["--single-select-option-id", spec["options"][value]])
    gh(*command, parse_json=False)


def apply(plan, config, actions):
    repo = config["project"]["repository"]
    for kind, entry, issue, fields in actions:
        if kind == "KEEP":
            continue
        if kind == "CREATE":
            body = (entry.get("body") or "").rstrip() + "\n\n---\n" + issue_marker(entry["key"]) + "\n"
            url = gh("issue", "create", "--repo", repo, "--title", entry["title"], "--body", body, parse_json=False)
            print(f"  Created {url}", flush=True)
            # A retry will identify this issue by marker, even if subsequent steps fail.
            item_id = add_to_project(url, config)
            print(f"  Added to project: {item_id}", flush=True)
            for field in FIELDS:
                if field in entry:
                    set_field(item_id, field, entry[field], config)
        elif kind == "ADD_PROJECT":
            item_id = add_to_project(issue["url"], config)
            print(f"  Added #{issue['number']} to project: {item_id}", flush=True)
            for field in SELECT_FIELDS + DATE_FIELDS:
                if field in entry:
                    set_field(item_id, field, entry[field], config)
            # Do not overwrite Status of an existing issue.
        elif kind == "SET_FIELDS":
            # Look up item ID again: no changes to content or status.
            data = gh("project", "item-list", config["project"]["number"], "--owner", config["project"]["owner"], "--limit", "1000", "--format", "json")
            match = [i for i in data.get("items", []) if (i.get("content") or {}).get("number") == issue["number"] and (i.get("content") or {}).get("repository") == repo]
            if len(match) != 1:
                raise ValueError(f"Cannot uniquely identify project item for #{issue['number']}")
            for field in fields:
                set_field(match[0]["id"], field, entry[field], config)
            print(f"  Updated {', '.join(fields)} on #{issue['number']}", flush=True)


def main():
    parser = argparse.ArgumentParser(description="Safe GitHub Projects issue synchronization")
    modes = parser.add_mutually_exclusive_group()
    modes.add_argument("--dry-run", action="store_true")
    modes.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    config, plan = load("github-project-config.json"), load("issues-plan.json")
    issues, items = read_remote(config["project"]["repository"], config["project"])
    remote_keys, by_number = validate(plan, config, issues)
    actions = plan_actions(plan, config, issues, items, remote_keys, by_number)
    print(f"\nGitHub Project #{config['project']['number']} | {'APPLY' if args.apply else 'DRY RUN'}")
    print("=" * 65)
    for kind, entry, issue, fields in actions:
        suffix = f" #{issue['number']}" if issue else ""
        detail = f" ({', '.join(fields)})" if fields else ""
        print(f"[{kind}]{suffix} {entry['title']}{detail}")
    print("=" * 65)
    print(f"Planned: {len(actions)} | Create: {sum(a[0] == 'CREATE' for a in actions)} | Existing project items: {len(items)}")
    print("Protected issues (managed: false) are not changed, including #3 and #4.")
    if not args.apply:
        print("No changes made. Run --apply only after reviewing this plan.")
        return
    # Preflight completed. Each write is individually retryable.
    apply(plan, config, actions)
    print("Synchronization completed. Re-run --dry-run to verify.")


if __name__ == "__main__":
    try:
        main()
    except (RuntimeError, ValueError, KeyError, OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        sys.exit(1)
