# Professional & Technical Portfolio — Decision Log

**Project:** `morrisgpeter.github.io`  
**Last updated:** 2026-10-10

## Status legend

- **Accepted** — explicitly agreed in discussion.
- **Proposed** — recommended but not yet explicitly approved.
- **Open** — needs discussion or confirmation.
- **Superseded** — replaced by a later decision.

## Decision register

| ID | Date | Topic | Decision / direction | Status | Rationale / notes |
| --- | --- | --- | --- | --- | --- |
| D-001 | 2026-10-10 | Portfolio purpose | Build a professional **and** technical portfolio. | Accepted | It should grow beyond an online CV. |
| D-002 | 2026-10-10 | Release priority | Focus initially on the professional portfolio. | Accepted | Technical work can be added progressively. |
| D-003 | 2026-10-10 | Technology | Use Astro with VS Code. | Accepted | Lightweight and suitable for a portfolio. |
| D-004 | 2026-10-10 | Publishing | Use existing GitHub Pages repository `morrisgpeter.github.io`. | Accepted | Git/GitHub workflow already established. |
| D-005 | 2026-10-10 | Responsive design | Support desktop and mobile layouts. | Accepted | One responsive site rather than separate versions. |
| D-006 | 2026-10-10 | Evidence | Include charts, quantitative indicators, and potentially photographs/images. | Accepted | Demonstrate measurable outcomes visually. |
| D-007 | 2026-10-10 | Future scope | Add data science, R, Python, research, and publications later. | Accepted | Design for growth without rebuilding the site. |
| D-008 | 2026-10-10 | Navigation | Home, About, Experience, Portfolio, Contact. | Proposed | Hybrid multipage structure; exact names and layout remain open. |
| D-009 | 2026-10-10 | Professional positioning | Engineering foundation; Commercial Leadership, Project & Program Management, and Data Science & Analytics as complementary business-results pillars. | Proposed | Reflect breadth without treating all areas as equally mature. |
| D-010 | 2026-10-10 | Experience presentation | Organize experience chronologically by company. | Proposed | Easy for recruiters to follow; commercial and delivery achievements can coexist within each role. |
| D-011 | 2026-10-10 | Portfolio presentation | Organize work into case studies with individual project pages. | Proposed | Demonstrate outcomes and support future technical categories. |
| D-012 | 2026-10-10 | Design direction | Classic, restrained corporate style, with clear charts and selective imagery. | Proposed | Professional credibility and readability. |
| D-013 | 2026-10-10 | Language | English first, with potential Portuguese later. | Proposed | Not explicitly confirmed. |
| D-014 | 2026-10-10 | Documentation | Maintain `docs/PROJECT_CONTEXT.md` and `docs/PROJECT_DECISIONS.md`. | Accepted | Preserve alignment across conversations and coding sessions. |
| D-015 | 2026-10-10 | Documentation visibility | Keep `docs/PROJECT_CONTEXT.md` and `docs/PROJECT_DECISIONS.md` in the public GitHub repository until the portfolio website is live; revisit their visibility after launch. | Accepted | Simplifies collaboration and version control during initial development; review whether planning documents should move to private storage after launch. |
| D-016 | 2026-10-10 | Visual identity | Use a dark navy-to-blue gradient Home hero with prominent professional portrait and large typography; keep internal pages predominantly light (white or very light gray), with consistent blue accents. | Accepted | Executive, modern, minimalist, visual and data-driven presentation; selective photos, maps, charts and metrics. |
| D-017 | 2026-10-10 | Home hero messaging | **Title:** “From Customer Needs to Business Value”. **Subtitle:** “Understanding customer challenges, shaping the right solutions and leading their delivery to create measurable value and lasting relationships.” | Accepted | Customer-centered message integrating commercial solution development, project delivery, measurable value and long-term relationships. English copy approved verbatim. |

## Key discussions

### Professional identity

The portfolio should communicate the intersection of **commercial leadership** and **project/program management**, grounded in engineering. **Data Science & Analytics** is an additional avenue for business results, supported by academic training and future technical work. The initial presentation should not overstate data science professional experience.

### Home page

**Confirmed hero messaging (D-017):**

> From Customer Needs to Business Value
>
> Understanding customer challenges, shaping the right solutions and leading their delivery to create measurable value and lasting relationships.

**Confirmed visual identity (D-016):** Dark blue gradient and professional portrait on the Home; light internal pages. Portrait treatment should remain natural, with a navy jacket and a subtle smile.

Proposed content blocks: professional introduction (possibly with portrait), key figures, expertise, performance/results charts, and featured projects. Examples and specific figures require validation prior to publication.

### Experience versus Portfolio

Proposed distinction: **Experience** explains career progression and responsibilities; **Portfolio** provides deeper evidence through selected project case studies. Avoid duplicating the same information verbatim.

## Open decisions / next discussion

1. Confirm the final five-page navigation or revise it.
2. Determine relative emphasis of Commercial Leadership vs Project & Program Management on the Home page.
3. Decide how Data Science & Analytics appears in the initial release.
4. Confirm language(s) and whether multilingual support is needed from the outset.
5. Finalize the hero photograph asset and image usage/permission policy (overall visual direction is accepted in D-016).
6. Select first-release projects and approved metrics.
7. Define how charts are produced and maintained.
8. Evaluate proposed visual storytelling elements: origins and dual citizenship, places lived, Brazil regional activity map, global ABB/data-center project map, selected clients, technologies, multicultural greetings, and project-methodology chart (Waterfall/Agile/Hybrid). Confirm accuracy, permissions, and confidentiality before publication.

## Change management

When a decision is confirmed or revised:

1. Add or update an entry with the date, status, and reason.
2. Mark replaced decisions **Superseded** rather than silently erasing them.
3. Update `PROJECT_CONTEXT.md` if the change affects the overall vision or architecture.
4. Commit both files to Git alongside the relevant changes.
