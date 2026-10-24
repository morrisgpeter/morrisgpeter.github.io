# Roadmap — Professional & Technical Portfolio

**Project:** `morrisgpeter.github.io`  
**Technology:** Astro · VS Code · GitHub Pages  
**Updated:** 2026-10-24  
**Purpose:** Build a professional portfolio that demonstrates experience, capabilities, measurable results, and selected projects. Technical work can be added progressively.

> **Working method:** Develop one section at a time, review it locally, then commit and publish through GitHub Actions. Proposed content and visuals are not automatically approved decisions; record confirmed changes in `docs/PROJECT_DECISIONS.md`.

## Overview

| Stage | Activity | Status |
| --- | --- | --- |
| 1 | Development environment and publication | ✅ Complete |
| 2 | Complete the Home page | 🟡 In progress |
| 2a | Certifications & Education (GitHub Issues #33–#35) | ✅ v6 published and visually verified on GitHub Pages (2026-10-12) |
| 3 | Build About | 🟡 Implemented and published; visual review completed, mobile/accessibility QA pending |
| 4 | Build Experience | 🟡 In progress — ABB growth chart and approved chapter order published and visually confirmed; full Experience/page QA pending |
| 5 | Develop Portfolio | ⬜ Pending |
| 6 | Build Contact | ✅ Complete — v5 published, tested; GitHub Project issues updated (2026-10-12) |
| 7 | Add data visualizations and charts | 🟡 In progress — About and ABB Experience visualizations implemented; site-wide QA pending |
| 8 | Refine navigation and responsiveness | 🟡 In progress — Contact and Certifications links tested; site-wide review pending |
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


## 2a. Certifications & Education — v6 published (2026-10-12)

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
- [x] Commit and push v6 page changes and documentation to `main` (publication confirmed on public site).
- [x] Verify the v6 page on the public GitHub Pages website (Safari screenshot, 2026-10-12).
- [x] Add Certifications & Education to the shared Header navigation; verified across pages during Contact v5 testing.

**Result:** v6 built successfully, approved on desktop and 375px mobile, and visually confirmed on the public GitHub Pages site on 2026-10-12. This confirms the live page, not a separate audit of the GitHub Actions run or issue status. GitHub issue closure is tracked separately.

**Deferred enhancements (future release):**

- [ ] Select and incorporate a suitable landscape image showing mountains and a winding road.
- [ ] Choose and approve a new introductory quotation; do not restore the removed draft quotation by default.

## 3. About — implemented; final review pending

**Goal:** Present the professional profile beyond a conventional CV.

**Published milestone:** The interactive Global Perspective implementation was committed and pushed to `main` as `a29a6e2` on 2026-10-20, including `src/pages/about.astro` and `public/images/global-perspective-map-v3.svg`. The final **What Connects It All** section was subsequently implemented, visually reviewed, and confirmed by the user on the live website. The specific commit containing the final section has not been identified in these records.

**Implemented and visually reviewed sections, in order:**

1. About opening: **Engineering Expertise. Entrepreneurial Mindset. Global Perspective.**
2. **My Professional Journey** and the interactive **The Evolution of My Professional Focus** chart.
3. **An Entrepreneurial Perspective**, including the Fibra logo and 2012 co-founder feature.
4. **How I Lead**, with five leadership principles and an unscored visual philosophy diagram.
5. **A Global Perspective**, with interactive country markers, role details, legend, four project indicators, and the 25+ multilingual greetings feature.
6. **What Connects It All**, with **Engineering**, **Business**, and **People** converging on **Value Creation**. Final reviewed layout: illustration left, narrative right on desktop.

**Approved map refinements:** subtitle **Projects, customers and manufacturing across the globe.**; ring-and-dot legend symbols matching map markers; Brazil remains **Experience & business**; New Zealand becomes **Global Project Management**, with the tooltip describing international project coordination, customer relationships and FAT in New Zealand. Customer FAT countries identify delegation origins, not FAT locations.

**Pending review:**

- [x] Remove **“Engenharia”** from the displayed Fibra logo while preserving the **Fibra** identity; user replaced the image file, retaining the existing filename, and verified the result.
- [x] Review the displayed Fibra logo size and proportions in the entrepreneurial side card; user confirmed the final appearance meets expectations.
- [x] Confirm the final **What Connects It All** section appears on the public website; user provided a live-site screenshot. (Specific commit not recorded.)
- [ ] Test the full About page on mobile, including chart, map, markers, tooltips and keyboard navigation.
- [ ] Recheck figures, map country roles, accessibility and publication/confidentiality requirements.
- [ ] Update GitHub Issues #20 and #21 based on their actual status.

**Stage deliverable:** Published About page with final quality review completed.

## 4. Experience — in progress

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
- [ ] Complete and release the Experience page (ABB Global Footprint and Portfolio Growth iterations visually approved).

**Stage deliverable:** Structured professional experience.

## 5. Portfolio — pending

**Goal:** Demonstrate capabilities through evidence-based case studies.

**Proposed case-study format:** **Overview → Challenge → Solution → Results**.

- [ ] Select professional projects for the first release.
- [ ] Verify data, attributions, and publication permissions.
- [ ] Build Portfolio overview and individual case-study pages.
- [ ] Plan future categories: Data Analytics, Programming, Research & Publications.

**Stage deliverable:** Portfolio with selected professional projects.

## 6. Contact — complete (v5 published 2026-10-12)

**Goal:** Make professional contact easy with a minimal executive layout.

- [x] **#36 — Define Contact Information & Links:** Email, LinkedIn and Portfolio (GitHub profile); location **New Zealand | Open to international opportunities.**
- [x] **#37 — Implement Contact Page:** `src/pages/contact.astro`, **CONTACT CHANNELS / Get in Touch**, compact portrait (`hero-portrait-transparent.png`), three icon-and-label links, no cards or form.
- [x] **#38 — Test Contact Navigation & Responsiveness:** external/mail links tested, desktop/mobile screenshots approved, shared Header navigation verified between Home, Contact and Certifications & Education.
- [x] **#14 — Complete the Contact Page:** commit `bdf7c49` pushed to `main`; user confirmed the live v5 page and updated GitHub Project issue statuses.

**Result:** Functional, responsive Contact page published at `/contact`.


## Future improvement — GitHub Profile Enhancement (accepted)

**Timing:** After the main professional portfolio pages; not required for Contact v5.

- [ ] Create a professional GitHub profile README.
- [ ] Pin and describe selected repositories.
- [ ] Align GitHub profile branding with the Astro portfolio.
- [ ] Link the published website from the GitHub profile.
- [ ] Organize technical projects, including data science and analytics where relevant.

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

**Complete the remaining About Me mobile/accessibility and content checks, then continue Experience, Portfolio and remaining Home work.**

1. Confirm whether the earlier Home Key Achievements publication checklist is complete; update its status only after checking.
2. Review the GitHub Project board and confirm the status of Issues #13 and #33–#35; do not infer issue closure from site publication.
3. Final About Me section is visually confirmed on the live site; perform the pending mobile/accessibility review; Featured Work remains pending.
4. During a future refinement of Certifications & Education, evaluate the deferred landscape image (mountains and winding road) and select a new introductory quotation. Neither is part of v6.
5. Continue site-wide navigation review as About, Experience and Portfolio pages are implemented; Contact and Certifications & Education are now linked.

---

**Related documents:** `docs/PROJECT_CONTEXT.md` and `docs/PROJECT_DECISIONS.md` are the authoritative references for project context and accepted decisions. This roadmap tracks execution and should be updated as work progresses.


## ABB Experience — Global Footprint milestone (2026-10-23)

- [x] Agree on three selectable maps: North America, Europe, Oceania.
- [x] Add regional silhouette SVGs, activity filters, blue capacity-scaled project circles, and clear legend.
- [x] Add US state boundaries and supplier at Wytheville, Virginia; improve regional positioning.
- [x] Review desktop and mobile visualizations for all three regions; accept current mobile experience.
- [x] Remove detailed Browse locations table and duplicated location/project cards.
- [x] Simplify tooltips to city/country plus project count and MW only for project markers.
- [x] Correct auto-opening tooltips and map-edge clipping in v22; user accepted current iteration.

**Status:** Global Footprint design iteration **complete / accepted**. This is not confirmation of a Git commit, deployment, final accessibility audit, or public-data authorization.

**Deferred / before publication:**
- [ ] Verify current `GlobalProjectFootprint.astro` matches approved v22 and run `npm run build`.
- [ ] Check keyboard accessibility, focus, hover and tap behavior, and mobile tooltip boundaries.
- [ ] Validate city coordinates, 10/7/2 location counts, project counts, ordered MW, and future-delivery definitions.
- [ ] Obtain disclosure/confidentiality approval for specific customer, supplier, and project data.
- [ ] Revisit clustered marker layout and map responsiveness only if future QA shows an issue.
- [ ] Commit and publish approved implementation; verify the live site and update GitHub Project issue status separately.


## ABB Experience — Project Delivery Scale & Portfolio Value milestone (2026-10-23)

- [x] Agree on ordered-capacity and order-value definitions, including distinction from delivered capacity.
- [x] Implement `src/components/experience/PortfolioGrowth.astro` with **1.2 GVA** ordered capacity and **USD 255M** order value (2021–Oct 2026); do not show order count or exact decimals.
- [x] Present cumulative ordered capacity as an **MVA step chart** from Jan 2023 through Oct 2026, including older orders in the baseline.
- [x] Add four dated professional milestones and interactive **Key Initiatives** descriptions.
- [x] Visually review and approve desktop version, including separated milestone titles 2 and 3.
- [x] Fix mobile chart clipping: show the entire curve without horizontal scrolling; hide titles inside mobile plot while keeping numbered markers, buttons and descriptions.
- [x] Review and accept mobile screenshots.

**Status:** ABB Portfolio Growth section **committed and pushed** with the revised ABB section order in `936c826` (2026-10-23); user confirmed the updated live Experience page. Accessibility, source-data and disclosure reviews remain outstanding.

**Remaining release checks:**
- [ ] Confirm source totals (**1,208.25 MVA**, **USD 255.41M**) and issue dates against `ABB_Project_Orders_2021-2026(2).xlsx` before future changes.
- [ ] Run `npm run build` and test keyboard/focus/touch behavior and small-screen accessibility.
- [ ] Verify permission to publish portfolio commercial totals and descriptions of internal ABB initiatives.
- [x] Commit and push the accepted code (`936c826`); user confirmed the updated live Experience page. GitHub Actions run details were not separately reviewed.
- [ ] Reconcile separate historical MW delivered/planned claims in About/Global Footprint with this ordered-MVA chart during final content QA.


## ABB Experience — section order and publication milestone (2026-10-23)

- [x] Approve the ABB chapter sequence: **Introduction → Project Delivery Scale & Portfolio Value → Global Footprint → Key Contributions → Stakeholders Across the Project Lifecycle → Data Center Power Flow → Business Impact**.
- [x] Reorder the sections in `src/pages/experience.astro` without intentionally changing the approved component content.
- [x] Commit the reordered page and new `PortfolioGrowth.astro` as **`936c826`** and push to `main`.
- [x] Confirm the resulting Experience page is displayed correctly on the live site (user confirmation, 2026-10-23).
- [ ] Complete final ABB/Experience source-data, confidentiality, accessibility and cross-device QA; verify build and GitHub Actions logs if needed.

**Status:** ABB chapter order and Portfolio Growth implementation **published and visually accepted**. This does **not** mark the entire Experience page or its final release checks complete.


## Fibra Experience — SFibra Digital Innovation milestone (2026-10-24)

- [x] Approve the narrative: challenge → three-stage digital workflow → four operational benefits → My Contribution → Business Value.
- [x] Approve **The Challenge** wording describing actual errors, rework, delays and administrative effort due to fragmented records, inconsistent documentation and manual processes.
- [x] Approve **My Contribution** describing acting as Product Owner and Product Manager, from product concept and functionality definition to feasibility, development, deployment and adoption.
- [x] Visually review desktop SFibra section; earlier responsive/mobile presentation accepted. Retain conceptual-illustration disclosure and avoid unverified percentages.
- [ ] Copy `FibraSFibra_Text_Approved_v12.astro` to `src/components/experience/fibra/FibraSFibra.astro` in the local repository.
- [ ] Run `npm run build`, inspect local page and `git diff`; commit and push approved component and documentation.
- [ ] Verify GitHub Actions publication and live Experience page; perform final accessibility, evidence and disclosure checks separately.

**Status:** SFibra design and copy accepted; implementation in the user's repository and public publication are not yet confirmed.
