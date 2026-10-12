# Roadmap — Professional & Technical Portfolio

**Project:** `morrisgpeter.github.io`  
**Technology:** Astro · VS Code · GitHub Pages  
**Updated:** 2026-10-12  
**Purpose:** Build a professional portfolio that demonstrates experience, capabilities, measurable results, and selected projects. Technical work can be added progressively.

> **Working method:** Develop one section at a time, review it locally, then commit and publish through GitHub Actions. Proposed content and visuals are not automatically approved decisions; record confirmed changes in `docs/PROJECT_DECISIONS.md`.

## Overview

| Stage | Activity | Status |
| --- | --- | --- |
| 1 | Development environment and publication | ✅ Complete |
| 2 | Complete the Home page | 🟡 In progress |
| 2a | Certifications & Education (GitHub Issues #33–#35) | 🟡 Implemented and validated locally; publication pending |
| 3 | Build About | ⬜ Pending |
| 4 | Build Experience | ⬜ Pending |
| 5 | Develop Portfolio | ⬜ Pending |
| 6 | Build Contact | ⬜ Pending |
| 7 | Add data visualizations and charts | ⬜ Pending |
| 8 | Refine navigation and responsiveness | ⬜ Pending |
| 9 | SEO, performance, and accessibility | ⬜ Pending |
| 10 | Final review and version 1.0 | ⬜ Pending |

## 1. Development environment and publication — complete

- [x] Configure Git and GitHub.
- [x] Install and configure VS Code, Astro, Node.js, and npm.
- [x] Configure Homebrew and Conda in the Bash environment.
- [x] Configure GitHub Pages and automated deployment through GitHub Actions.
- [x] Update project context and decision documentation.
- [x] Publish the site at `https://morrisgpeter.github.io`.

**Result:** Working development environment and live website. Documentation update committed as `aa96d60`.

## 2. Complete the Home page — current priority

**Goal:** Create an executive overview that communicates positioning, results, expertise, and routes to more detailed pages.

**Approved Home section order:**

| Order | Section | Purpose | Status |
| --- | --- | --- | --- |
| 1 | Hero | Professional introduction and positioning | ✅ Implemented |
| 2 | Key Achievements | Selected career and project metrics | 🟡 Implemented locally; publication pending |
| 3 | Areas of Expertise | Two primary areas | ✅ Implemented |
| 4 | Featured Work | Selected projects | ⬜ Pending |
| 5 | Professional Journey | Career overview | ⬜ Pending |

### 2.1 Hero — implemented

**Approved title:**

> From customer needs to business value

**Approved subtitle:**

> Understanding customer challenges, shaping the right solutions and leading their delivery to create measurable value and lasting relationships.

**Visual direction:** Dark navy/blue gradient, prominent professional portrait, large typography. Revisit fine details after completing the remaining sections.

### 2.2 Key Achievements — implemented locally, publication pending

| Metric | Label |
| --- | --- |
| **25+ Years** | Engineering & Business Leadership |
| **11 Projects · 7 Countries** | Global Critical Power & Data Center Delivery |
| **100+ Stakeholders** | Coordinated Across Global Projects |
| **6 Industries** | Cross-Industry Experience |

- [x] Agree final wording and clarify metric scope (D-028).
- [x] Approve visual presentation (D-029).
- [x] Implement `Achievements.astro` and integrate it between Hero and Areas of Expertise.
- [x] Review desktop and 375px mobile layouts; confirm no horizontal overflow at 375px.
- [ ] Commit and push the implementation and documentation; verify GitHub Actions deployment.
- [ ] Recheck underlying evidence and publication/confidentiality permissions as part of final release review.

**Scope:** 11 projects, seven project-delivery countries and 100+ stakeholders refer to ABB global project work. Seven countries does not mean seven countries of in-person work (three: Brazil, New Zealand, Czech Republic). The six industries are Data Centers & Critical Power, Electric Utilities, Oil & Gas, Telecommunications, Mining, and Pulp & Paper.

### 2.3 Areas of Expertise — implemented

Two equally prominent pillars, **in this exact order on desktop and mobile**:

1. **Project & Program Management** — *Delivering Complex Projects. Creating Business Value.*
2. **Commercial Leadership** — *Turning Customer Challenges into Business Opportunities*

- [ ] Decide where the cards should link (Experience, Portfolio, or another destination).

**Future consideration:** Data Science & Analytics is not an initial Home pillar; reconsider later.

### 2.4 Featured Work — pending

Candidate projects **for evaluation**, not yet selected for publication:

- ABB — Global Critical Power / Data Centers.
- Fibra Engenharia — Distribution Automation.
- Aton Engenharia — Oil & Gas Remote Monitoring.
- Telenge — Telecommunications Infrastructure.

- [ ] Select three or four projects.
- [ ] Verify claims, imagery, client references, and confidentiality.
- [ ] Create summary cards with project context and results.
- [ ] Link cards to detailed Portfolio case studies when available.

### 2.5 Professional Journey — pending

- [ ] Design a concise career timeline.
- [ ] Highlight companies, sectors, and evolution of responsibilities.
- [ ] Keep it distinct from the detailed Experience page.

**Stage deliverable:** Complete, responsive Home page.


## 2a. Certifications & Education — local implementation complete; publication pending

**Goal:** Present key professional certifications, academic education, and ongoing professional development in a concise, verifiable format. This dedicated page is implemented at `/certifications-education` and is distinct from the still-pending About page.

**Approved content and design (D-030–D-040; v6):**

- **Professional Certifications & Development:** Three matching desktop cards: PMP® (PMI, April 2025–April 2028), PSM I (Scrum.org, November 2025), and a two-metric card. The first two use original badges and tested individual Credly verification links. Category chips read **Project Management**, **Agile & Scrum**, and **Professional Development**.
- **Development metrics:** **15 Professional Development Credentials** (excluding PMP and PSM I) and **170+ Hours of Professional Development**, rounded from the consolidated 172.75 hours. The metrics card has no redundant heading or leading icon.
- **Continuous Professional Development topic strip:** Appears immediately below the three cards. Includes **Last 2 years**, a **View All Credentials** link to `https://www.credly.com/users/morrisgpeter/badges/credly`, and six theme-specific SVG icons: Leadership · Project Management · Agile · AI · Sustainability · Business Transformation.
- **Academic Education:** Appears after the development strip. Three cards: UFBA Data Science & Big Data (2021–2023), IME Digital Signal Processing (1995–1996), and UFBA Electrical Engineering (1989–1993), with institutional coats of arms.
- **Presentation:** Compact, light-background desktop layout; three stacked certification/development cards on mobile, with side-by-side metrics; six theme icons in a 3 × 2 mobile grid. Desktop and 375px mobile screenshots reviewed and approved. No Home or global-style changes required.
- **Intro:** Removed the previous inspirational quotation and image placeholder. A mountain-and-winding-road landscape and a **new, yet-to-be-chosen** quote are deferred enhancements, not approved publication content.

**GitHub Issues:**

- [x] **#33 — Validate Education & Certifications:** content, badges, institutional images, metric, and direct Credly URLs agreed.
- [x] **#34 — Implement Certifications & Education Page:** page and assets added locally; desktop and mobile visually reviewed; `npm run build` succeeded again on 2026-10-12 for v6, generating two static routes.
- [x] **#35 — Review Credentials & Links:** user tested both Credly links successfully; local page reviewed.
- [ ] Commit and push page, image assets, and documentation to `main`.
- [ ] Verify GitHub Actions deployment and the live page after push.
- [ ] Consider linking the page in site navigation during the wider navigation review; no navigation change has yet been approved.

**Result so far:** v6 visually approved and locally built; publication not yet confirmed. Issue checklists describe completed local work, not GitHub issue closure.

**Deferred enhancements (future release):**

- [ ] Select and incorporate a suitable landscape image showing mountains and a winding road.
- [ ] Choose and approve a new introductory quotation; do not restore the removed draft quotation by default.

## 3. About — pending

**Goal:** Present the professional profile beyond a conventional CV.

Suggested topics:

- Professional Profile and Philosophy.
- Engineering Background.
- Education & Certifications.
- International Experience.
- Languages.

- [ ] Agree on content and narrative.
- [ ] Select suitable photos or geographic elements.
- [ ] Implement and review the page.

**Stage deliverable:** Complete About page.

## 4. Experience — pending

**Goal:** Show career progression, responsibilities, and measurable outcomes rather than simply reproducing a CV.

| Company | Main focus |
| --- | --- |
| ABB | Global Projects, Critical Power, Data Centers |
| Fibra Engenharia | Commercial Leadership, Utilities, Automation |
| Aton Engenharia | Engineering Projects, Solutions, Business Development |
| Telenge | Telecommunications Infrastructure, Engineering Management |

For each company, consider **context → responsibilities → achievements → results → relevant technologies and capabilities**.

- [ ] Agree on chronological presentation and page design.
- [ ] Draft and verify company-specific content.
- [ ] Implement the Experience page.

**Stage deliverable:** Structured professional experience.

## 5. Portfolio — pending

**Goal:** Demonstrate capabilities through evidence-based case studies.

**Proposed case-study format:** **Overview → Challenge → Solution → Results**.

- [ ] Select professional projects for the first release.
- [ ] Verify data, attributions, and publication permissions.
- [ ] Build Portfolio overview and individual case-study pages.
- [ ] Plan future categories: Data Analytics, Programming, Research & Publications.

**Stage deliverable:** Portfolio with selected professional projects.

## 6. Contact — pending

**Goal:** Make professional contact easy.

Suggested content: LinkedIn, GitHub, professional email, general location, and an appropriate availability statement.

- [ ] Confirm which contact details to publish.
- [ ] Implement contact links and any call-to-action.
- [ ] Test links and mobile layout.

**Stage deliverable:** Functional Contact page.

## 7. Data visualizations and charts — pending

Only use graphics that communicate **relevant, verifiable** information.

| Visualization | Purpose |
| --- | --- |
| World map | International experience |
| Evolution chart | Portfolio or responsibility growth |
| Timeline | Career progression |
| Leadership chart | Team scale and management scope |
| Industry overview | Cross-industry experience |
| Technical photos | Project context |

- [ ] Identify defensible datasets and definitions.
- [ ] Distinguish direct team leadership from stakeholder coordination.
- [ ] Select charting tools and formats.
- [ ] Review confidentiality and visual accessibility.

**Stage deliverable:** Useful visual storytelling integrated into relevant pages.

## 8. Navigation and responsiveness — pending

- [ ] Confirm final page names and navigation (Home, About, Experience, Portfolio, Contact remain a proposal).
- [ ] Test desktop, tablet, and mobile.
- [ ] Review menu behavior, typography, spacing, and images.
- [ ] Check internal/external links and chart readability.

**Stage deliverable:** Consistent navigation and responsive experience.

## 9. SEO, performance, and accessibility — pending

- [ ] Add page titles and descriptions.
- [ ] Configure social sharing metadata and sitemap.
- [ ] Optimize images and page performance.
- [ ] Use semantic HTML and appropriate contrast.
- [ ] Test keyboard navigation and accessibility.

**Stage deliverable:** Technically polished website.

## 10. Final review and version 1.0 — pending

- [ ] Proofread all English content.
- [ ] Verify figures, dates, results, and attribution.
- [ ] Confirm rights to photos, client references, and project information.
- [ ] Test links and layouts on multiple devices.
- [ ] Update project documentation and release notes.
- [ ] Revisit whether `docs/PROJECT_CONTEXT.md` and `docs/PROJECT_DECISIONS.md` should remain public.
- [ ] Create an identifiable version 1.0 release in GitHub.

**Stage deliverable:** Professional portfolio version 1.0.

## Suggested execution phases

| Phase | Stages | Outcome |
| --- | --- | --- |
| **A — Presentation** | 2–3 | Home and About |
| **B — Evidence** | 4–7 | Experience, Portfolio, Contact, visualizations |
| **C — Quality** | 8–10 | Refinement and version 1.0 |

Navigation, responsiveness, accessibility, and content verification should also be addressed incrementally during earlier stages.

## Immediate next action

**Publish Certifications & Education v6 (Issues #33–#35)**

1. Replace `docs/PROJECT_DECISIONS.md` and `docs/PORTFOLIO_ROADMAP.md` with the updated versions.
2. Run `git status` and review `git diff` (including any unrelated untracked files).
3. Stage only the new page, its four image assets, and the two documentation files; commit and push to `main`.
4. Verify GitHub Actions deployment and the live `/certifications-education` page.
5. Confirm whether the earlier Key Achievements publication checklist is now complete; update its pending status only after checking.
6. Continue with the next prioritized GitHub Project issue; Featured Work remains pending.

---

**Related documents:** `docs/PROJECT_CONTEXT.md` and `docs/PROJECT_DECISIONS.md` are the authoritative references for project context and accepted decisions. This roadmap tracks execution and should be updated as work progresses.
