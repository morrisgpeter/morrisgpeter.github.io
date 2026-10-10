# Professional & Technical Portfolio — Project Context

**Project:** Peter Morris professional and technical portfolio  
**Repository:** `morrisgpeter/morrisgpeter.github.io`  
**Live site:** `https://morrisgpeter.github.io/`  
**Last updated:** 2026-10-10

## Purpose

Build a professional and technical portfolio that communicates professional experience, capabilities, and measurable business outcomes. The first release will focus on the professional portfolio. Over time, the site will expand to include technical projects, programming, data analysis, research, and publications.

The website should be more than an online CV: it should explain what was achieved, why it mattered, and how engineering, commercial leadership, project delivery, and analytical capabilities contributed.

## Audience

Primary initial audience: recruiters, hiring managers, and professional contacts assessing senior commercial, project/program management, and infrastructure experience. A future secondary audience includes technical collaborators and people interested in data science and programming projects.

## Professional positioning — agreed for the initial Home

- **Engineering** is the technical foundation.
- The Home presents two equally prominent areas, in this exact order:
  1. **Project & Program Management** — delivery, stakeholders, risks, quality, and business outcomes.
  2. **Commercial Leadership** — business development, strategic sales, accounts, contracts, and growth.
- **Data Science & Analytics** is deferred as a possible third Home pillar; it may appear in future technical portfolio projects. Do not imply equivalent seniority in all three disciplines.
- Show how engineering, commercial leadership, and project delivery contribute together to business value.

**Approved Home hero title (sentence case):** “From customer needs to business value”

**Approved subtitle:** “Understanding customer challenges, shaping the right solutions and leading their delivery to create measurable value and lasting relationships.”

**Visual direction:** dark navy-to-blue gradient Home hero with prominent professional portrait; predominantly light internal pages. Preserve responsive desktop and mobile layouts.

**Planned Home sections:** Hero → Key Achievements → Areas of Expertise → Featured Work → Professional Journey. This is an agreed content plan, not a claim that every section is already implemented.

## Technology — agreed

| Area | Choice |
| --- | --- |
| Framework | Astro |
| Editor | Visual Studio Code |
| Runtime/tooling | Node.js and npm |
| Version control | Git |
| Source hosting | GitHub |
| Site hosting | GitHub Pages |
| Public URL | `https://morrisgpeter.github.io/` |
| Production branch | `main` |
| Deployment | GitHub Actions → GitHub Pages |
| Workflow | `.github/workflows/deploy.yml` |
| Build output | `dist/` (Git-ignored) |

The site must work well on both desktop and mobile. React and Next.js are not needed for the initial version. Implementation details for charts and other components remain open.

## Deployment and current implementation — verified 2026-10-10

- **Status:** Astro Home publicly accessible, with the intended hero, portrait, header, styles, and two expertise cards visible. First custom GitHub Actions deployment succeeded on commit `b99b5ca` (workflow run #1, about 35 seconds).
- **GitHub Pages source:** GitHub Actions (replaces direct branch publishing).
- **Trigger:** push to `main`, with optional manual `workflow_dispatch`.
- **Build job:** checkout repository, set up Node.js 22, run `npm ci`, `npm run build`, configure Pages, and upload `./dist`.
- **Deploy job:** deploy the uploaded artifact to the `github-pages` environment.
- **Astro configuration:** `astro.config.mjs` sets `site: 'https://morrisgpeter.github.io'`; no `base` is needed for this user-site repository.
- **Local build:** `npm run build` succeeded; output is static and generates `dist/`. `dist/` is excluded from Git.
- **Current implemented files:** `src/components/Header.astro`, `Hero.astro`, `Expertise.astro`; `src/layouts/BaseLayout.astro`; `src/pages/index.astro`; `src/styles/global.css`; `astro.config.mjs`.
- **Home expertise order:** (1) Project & Program Management; (2) Commercial Leadership, in the hero eyebrow and cards, on desktop and mobile.

### Local development and publication commands

```bash
npm install       # when dependencies need to be installed
npm run dev       # local development, typically localhost:4321
npm run build     # verify production build

git status
git add <files>
git commit -m "Describe the change"
git push origin main   # triggers automatic deployment
```

**Local environment follow-up:** macOS Bash currently finds Node.js/npm after `export PATH="/opt/homebrew/bin:$PATH"`; make this persistent in the appropriate shell startup configuration after checking the shell setup. Local Node.js version observed: 26.11.1; GitHub Actions uses Node.js 22.

**Documentation follow-up:** these `docs/` files are currently tracked publicly. The earlier decision was to revisit visibility once the site went live; that review is now due, not yet resolved.


## Content direction — agreed

- Begin with professional experience and results.
- Use numerical indicators and charts where meaningful.
- Consider professional photography and relevant project/equipment imagery.
- Present commercial and delivery outcomes, not only duties.
- Expand later with R, Python, Data Science, and publications.
- Review commercial figures, client references, and images for confidentiality and permission before publication.

## Information architecture — proposed

A hybrid multipage site with a summary-oriented Home and detailed pages:

1. **Home** — introduction, key figures, expertise, results, selected work.
2. **About** — professional background, education, credentials, capabilities.
3. **Experience** — chronological company/career history, showing commercial and delivery contributions.
4. **Portfolio** — selected work, with individual project pages and room for future technical categories.
5. **Contact** — professional contact channels.

These five page names and the precise navigation structure are **proposals**, not final decisions.

### Portfolio evolution — proposed

- Professional Projects (initial)
- Data Analytics (future)
- Programming (future)
- Research & Publications (future)

Possible professional project case-study format: **Overview → Challenge → Solution → Results**.

## Potential examples to validate before publishing

- Global Critical Power portfolio: approximately USD 70M; 11 projects; seven countries.
- Critical Power annual capacity figures: 2023 62.5 MW; 2024 12.5 MW; 2025 147.5 MW; 2026 545 MW (2026 is a planned/forecast figure, not necessarily completed delivery).
- Distribution automation: 2,760 reclosers.
- Commercial contract expansion: approximately USD 1M to USD 8.5M over six years, plus approximately USD 5M in additional business over two years.
- Wind-pattern analysis for wind farm investment: candidate future data analytics case study.

These are **candidate content facts**, not approval to publish. Verify definitions, timeframes, attribution, units, and confidentiality.

## Working principles

- Agree on the site structure and content strategy before coding.
- Record confirmed decisions separately from open proposals.
- Favor a classic, credible professional presentation over a flashy design.
- Make metrics understandable with clear context and labels.
- Use the documentation in `docs/` as shared project context for future AI-assisted work.

## Open questions

- Final navigation/page structure.
- Whether to add Data Science & Analytics as a third Home pillar in a later release (not part of the initial Home).
- Language strategy: English first was suggested but not confirmed.
- Further typography and image refinements within the accepted dark Home / light internal-page direction.
- Which metrics, photos, and projects are cleared for public use.
- Charting library and interaction level.
- Review whether project planning documents should remain in the public repository after launch.
- Make the Node.js/npm PATH persistent for future VS Code Bash sessions.
