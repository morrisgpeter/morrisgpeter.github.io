import json
from pathlib import Path
from datetime import date

# Localização do arquivo de planejamento
BASE_DIR = Path(__file__).resolve().parent
PLAN_FILE = BASE_DIR / "issues-plan.json"

# Cronograma aprovado
# Formato: Size, Start date, Target date

SCHEDULE = {
    "development-environment": (None, "2026-10-10", "2026-10-10"),
    "home-page": ("L", "2026-10-10", "2026-10-25"),
    "about-page": ("M", "2026-10-26", "2026-11-01"),
    "professional-experience": ("M", "2026-11-02", "2026-11-08"),
    "project-portfolio": ("XL", "2026-11-09", "2026-11-22"),
    "certifications-education": ("S", "2026-11-23", "2026-11-26"),
    "contact-page": ("S", "2026-11-27", "2026-11-29"),
    "responsive-accessibility": ("M", "2026-11-30", "2026-12-06"),
    "seo-performance": ("S", "2026-12-07", "2026-12-10"),
    "final-review": ("S", "2026-12-11", "2026-12-13"),
}


def main():
    # Carregar planejamento atual
    plan = json.loads(PLAN_FILE.read_text(encoding="utf-8"))

    # Verificar se todas as Issues estão no cronograma
    issues = plan["issues"]
    keys = [issue["key"] for issue in issues]

    if len(keys) != len(set(keys)):
        raise ValueError("Duplicate issue keys found")

    if set(keys) != set(SCHEDULE):
        raise ValueError("Issue keys do not match the approved schedule")

    # Validar datas e estimativas antes de alterar o arquivo
    for key, (size, start, target) in SCHEDULE.items():
        if size is not None and size not in {"XS", "S", "M", "L", "XL"}:
            raise ValueError(f"Invalid size for {key}: {size}")

        if date.fromisoformat(start) > date.fromisoformat(target):
            raise ValueError(f"Invalid date range for {key}")

    # Atualizar planejamento
    for issue in issues:
        size, start, target = SCHEDULE[issue["key"]]

        if size is not None:
            issue["size"] = size

        issue["start_date"] = start
        issue["target_date"] = target

    plan["version"] = "1.1"

    # Salvar arquivo atualizado
    PLAN_FILE.write_text(
        json.dumps(plan, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8"
    )

    print("Planning updated successfully.")
    print(f"Issues updated: {len(issues)}")
    print("Target completion: 2026-12-13")
    print("GitHub was not modified.")


if __name__ == "__main__":
    main()