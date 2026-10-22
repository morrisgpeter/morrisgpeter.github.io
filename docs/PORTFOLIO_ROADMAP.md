# Roadmap — Professional & Technical Portfolio

**Project:** `morrisgpeter.github.io`  
**Technology:** Astro · VS Code · GitHub Pages  
**Updated:** 2026-10-23  
**Purpose:** Build a professional portfolio that demonstrates experience, capabilities, measurable results, and selected projects. Technical work can be added progressively.

> **Working method:** Develop one section at a time, review it locally, then commit and publish through GitHub Actions. Proposed content and visuals are not automatically approved decisions; record confirmed changes in `docs/PROJECT_DECISIONS.md`.

## Overview

| Stage | Activity | Status |
| --- | --- | --- |
| 1 | Development environment and publication | ✅ Complete |
| 2 | Complete the Home page | 🟡 In progress |
| 2a | Certifications & Education (GitHub Issues #33–#35) | ✅ v6 published and visually verified on GitHub Pages (2026-10-12) |
| 3 | Build About | 🟡 Implemented and published; visual review completed, mobile/accessibility QA pending |
| 4 | Build Experience | 🟡 In progress — ABB chapter and StakeholderNetwork v6 reviewed |
| 5 | Develop Portfolio | ⬜ Pending |
| 6 | Build Contact | ✅ Complete — v5 published, tested; GitHub Project issues updated (2026-10-12) |
| 7 | Add data visualizations and charts | ⬜ Pending |
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

- [x] Agree on chronological presentation and page design: Executive Career Timeline and one Experience page linking to separately published case studies.
- [ ] Draft and verify remaining company-specific content (ABB, Fibra, Aton, Telenge); ABB chapter planning is underway.
- [ ] Complete and publish the Experience page; verify production build and live deployment.

### ABB chapter — design and implementation progress (2026-10-23)

**Approved page direction:** Executive Career Timeline, latest employer first (ABB → Fibra Engenharia → Aton Engenharia → Telenge), with concise employer chapters and separate, progressively published case studies. Do not create dead links to unpublished cases. Avoid repeating the Home/About headline metrics unnecessarily.

**ABB chapter content sequence under development:** ABB role/context → annual MV UPS capacity chart (2023: 62.5 MW; 2024: 12.5 MW; 2025: 147.5 MW; 2026: 545 MW; verify planned versus delivered wording) → discreet ~USD 70M portfolio value (2022–2025; validate publication) → authorized technical illustration/photo with HiPerGuard as the primary project product → Key Contributions → Business Impact → Global Project Footprint → published case-study links.

**Key Contributions:** Global Project Delivery; Customer & Cross-functional Leadership; Technical Compliance & External Coordination; FAT & Customer Acceptance. FAT work is **coordination** of customers and internal teams across HiPerGuard, SureWave, AVC and PCS100 UPS-I, **not execution of technical tests**. Do not describe certification/supplier interactions as commercial negotiations or financial governance.

**Business Impact headings:** Supporting Portfolio Growth and Customer Confidence; Managing Complexity Across Global Projects. Delivery-performance improvement belongs under Global Project Delivery, not as a third Business Impact block.

**Global Project Footprint candidate locations:** Austin, Bossier City, El Cajon, Ellendale and Fargo (USA); Quebec City (Canada); Brno (Czechia); Brussels (Belgium); Kecskemét (Hungary); London (UK); Napier (New Zealand); Sydney (Australia). These are **12 cities in 7 countries and 3 continents**; the role of each city must be validated before assigning markers or implying project installations, travel, FAT, manufacturing, or customer locations. This broader location list must not be conflated with the separate seven project-delivery-country metric.

**StakeholderNetwork.astro — v6 APPROVED after desktop and mobile screenshot review:**

- Heading: **Stakeholders Across the Project Lifecycle**; subtitle: **Connecting strategic decisions, management coordination and operational execution.**
- A three-section **lightbulb** on the left (desktop) and centered above the stakeholder groups (mobile), labeled **Strategic**, **Management**, **Operational** directly inside its segments. These headings are intentionally omitted from the corresponding right-side cards to avoid repetition.
- Three light-blue groups of function-specific outline icons and labels; five strategic, six management and seven operational functions (18 total). Desktop displays horizontal rows; 375px mobile uses two-column cards. The bulb must remain visible on mobile.
- **Strategic (5):** Customers; Sales; Business units; Finance; Legal & contracts.
- **Management (6):** Project management; Product management; Agile units; Supply chain & procurement; Operations; Service.
- **Operational (7):** Engineering; Quality; Manufacturing & IPU; Planning & fulfilment; Logistics; Customer service; Site & commissioning support.
- This is an illustrative **collaboration-interface map**, not a reporting hierarchy or claim of direct line management. Icon adjustments were made for Supply chain & procurement and other functions; v6 screenshots show consistent iconography and readable mobile labels.
- [x] User approved StakeholderNetwork v6 after desktop and mobile visual review on 2026-10-23.
- [ ] Confirm component is committed and deployed; screenshots alone do not establish a production release or accessibility audit.
- [ ] Verify keyboard/screen-reader interpretation, mobile behavior on additional widths and any site-wide performance impact.

**Next planned component:** `DataCenterPowerFlow.astro`, a technical visualization of medium-voltage UPS power supply to a data center. Concept and technical content require review before implementation; not yet approved.

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

**Continue the ABB Experience chapter after the StakeholderNetwork v6 visual approval; keep About Me QA, remaining Home and Portfolio work open.**

1. Confirm whether the earlier Home Key Achievements publication checklist is complete; update its status only after checking.
2. Review the GitHub Project board and confirm the status of Issues #13 and #33–#35; do not infer issue closure from site publication.
3. Final About Me section is visually confirmed on the live site; perform the pending mobile/accessibility review; Featured Work remains pending.
4. During a future refinement of Certifications & Education, evaluate the deferred landscape image (mountains and winding road) and select a new introductory quotation. Neither is part of v6.
5. Confirm StakeholderNetwork v6 build/commit/deployment and accessibility; then scope `DataCenterPowerFlow.astro` without treating the design as already approved. Continue site-wide navigation review as pages are implemented.

---

**Related documents:** `docs/PROJECT_CONTEXT.md` and `docs/PROJECT_DECISIONS.md` are the authoritative references for project context and accepted decisions. This roadmap tracks execution and should be updated as work progresses.
