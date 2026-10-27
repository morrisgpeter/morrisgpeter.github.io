# Roadmap — Professional & Technical Portfolio

**Project:** `morrisgpeter.github.io`  
**Technology:** Astro · VS Code · GitHub Pages  
**Updated:** 2026-10-27  
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


## Home — Key Achievements indicators review (pending, 2026-10-25)

- [ ] Revisit the four indicators currently displayed on the Home page: **25+ Years**, **11 Projects · 7 Countries**, **100+ Stakeholders**, **6 Industries**.
- [ ] Reconcile project count, countries, stakeholder count and scope against the updated ABB Experience portfolio evidence; do not automatically substitute order counts for project counts or ordered MVA for delivered capacity.
- [ ] Agree revised wording, metric definitions, timeframes and disclosure suitability before editing `src/components/Achievements.astro`.
- [ ] Review desktop/mobile, run `npm run build`, commit and verify live publication after approval.

**Status:** Reminder recorded; no changes to Home indicators approved or implemented yet.


## Fibra Experience — Business Impact & Timeline refinement (2026-10-25)

**Previous publication confirmed:** Fibra Experience and SFibra were committed as `43dd16d`, pushed to `main`, and confirmed working on GitHub Pages by the user. This supersedes the earlier pending-publication checklist in the SFibra milestone above; final accessibility, evidence and disclosure checks remain open.

- [x] Approve five revised Business Impact indicators and their exact copy:

| Indicator | Title | Supporting copy |
| --- | --- | --- |
| **8.5×** | Services Contract Growth | Scaling the engineering services portfolio |
| **39** | MV Substation Automation Projects | Strengthening power distribution infrastructure |
| **2,760** | Reclosers Deployed | Grid modernization program |
| **50+** | Professionals | Through project management teams |
| **>95%** | Commissioning Data Accuracy | Reduced rework through SFibra |

- [x] Approve revised Building & Scaling Fibra milestones:

| Period | Milestone | Description |
| --- | --- | --- |
| **2012–2013** | Delivery Capability | Building project execution capacity and operational processes. |
| **2013–2014** | Commercial Development | Initial contracts, customer relationships and portfolio development. |
| **2017–2018** | Portfolio Diversification | Expansion into additional services and business opportunities. |

- [x] Visually review desktop and mobile layouts; user accepted the five-indicator arrangement, seven-event timeline and geographic footprint.
- [x] Remove the internal-facing historical-estimates/evidence-review note from the public Business Impact interface; retain evidence verification as an internal release task.
- [x] Standardize punctuation of the revised timeline descriptions, including Portfolio Diversification.
- [ ] Run `npm run build` after final local replacement and confirm successful compilation.
- [ ] Inspect `git diff`, commit and push only the two modified Astro components and updated project documentation.
- [ ] Confirm the revised Business Impact and timeline are live on GitHub Pages.
- [ ] Reconfirm that 8.5× compares equivalent services-contract measures and that 39 refers to MV substation automation projects (not necessarily 39 fully automated substations).

**Status:** Copy and responsive visuals approved; final revision's build, commit and publication not yet confirmed. The SFibra component itself remains unchanged.


## Fibra Experience — Commercial Development in Action (accepted, 2026-10-25)

- [x] Accept the current **Commercial Development in Action** chart and close this design iteration without further changes.
- [x] Retain the two commercial-development paths: **Strategic Account Development** and **New Customer Development**.
- [x] Retain the chart's three-stage story: **Initial Solutions → Account Development → Business Expansion**, including the current solution and account labels.
- [x] Retain the responsive presentation: left-to-right flow on desktop and vertically arranged paths on mobile.
- [x] Retain the qualification: **“Illustrative relative commercial significance. Not based on financial values.”** Flow widths are illustrative and must not be read as audited financial quantities.
- [ ] **Future review (deferred, not a blocker):** Revisit the chart's visual clarity, mobile height/readability, flow routing, relative ribbon widths and whether its labels adequately communicate sales, business development, key account management and bid/proposal capabilities. Recheck historical accuracy before revising the narrative.
- [ ] Independently verify build, repository commit/push, live publication, accessibility and disclosure suitability if not already confirmed.

**Status:** **Current visual version accepted as final for this iteration.** Future improvement is recorded as an optional review; no immediate chart changes are requested. Acceptance does not independently establish deployment or technical QA.


## Fibra Experience — Commercial Growth Process relocation (approved, 2026-10-25)

- [x] Decide to move **Commercial Growth Process** out of Fibra Experience into the future **Commercial Expertise** area.
- [x] Preserve **Commercial Development in Action** and **Distributed Solar Journey** in Fibra Experience; both visual iterations were approved.
- [x] Preserve the existing four-stage process content in `PROJECT_DECISIONS.md` as a reference for future reuse.
- [ ] Remove the process markup, data and process-only styles from `src/components/experience/fibra/FibraCommercial.astro`, without changing the approved diagrams or solar timeline.
- [ ] Inspect the Commercial Expertise implementation/architecture before integrating or redesigning the process; avoid duplicate skills content.
- [ ] Review local desktop/mobile and run `npm run build`; inspect the diff, commit/push and verify publication.
- [ ] Confirm the solar image has the agreed concise caption **AI-generated illustration**; this is a separate pending content adjustment, not a prerequisite for relocating the process.

**Status:** Relocation decision accepted. Component removal can be prepared separately; integration into Commercial Expertise remains deferred. No build, commit or publication is claimed here.

## Fibra Experience — Commercial Risk Management (approved visual iteration, 2026-10-26)

- [x] Approve the three-column desktop case-study card **COMMERCIAL RISK MANAGEMENT / Protecting a Fixed-Price Contract**: contract context and individual contribution at left; USD/BRL exchange-rate chart in the middle; Strategic Actions and Business Outcomes at right.
- [x] Approve chart presentation: **USD/BRL EXCHANGE RATE**, monthly average **Jul 2014 – Jul 2015**, line in portfolio blue, **Proposal** marker in blue (August 2014), **Signed** marker in turquoise (December 2014), and a subtle **Planned delivery** band. The proposal/signed labels, dots and guide lines use coordinated colors consistent with the page palette.
- [x] Retain chart source attribution: **Banco Central do Brasil, SGS series 3698 (monthly average USD selling rate)**. Explain that the exchange-rate trend is market context, **not Fibra's actual cost exposure**.
- [x] Retain the narrative: August 2014 BRL-priced proposal, December fixed-price contract signing, coordination with US- and Israel-based suppliers, anticipated purchase orders, and use of group-company import channels to protect margins and delivery commitments.
- [x] Retain right-hand items: **Strategic Actions** — Anticipated purchase orders; Imported through group companies. **Business Outcomes** — Maintained margins; Delivered on schedule.
- [x] User visually approved the latest screenshot and requested no further changes to the accepted design.
- [ ] Verify the implemented Astro component's exact filename, mobile rendering, build, commit/push and live publication separately; these were not established by the screenshot approval.
- [ ] Validate exchange-rate points, milestone timing, historical assertions, source citation/link, accessibility and any necessary disclosure approvals before final release.

**Status:** Content and visual presentation approved for the current iteration. Do not revise the approved card without a new request.


## Fibra Experience — People & Culture (final visual approval, 2026-10-26)

- [x] Approve the leadership-scale narrative: approximately **3 project managers mentored** and **50+ professionals** coordinated via delegated leadership; avoid implying direct reporting lines.
- [x] Approve the three pillar cards and their copy: **Mentoring and Knowledge Sharing**, **Empowering Teams**, **Long-Term Relationships**.
- [x] Replace the unclear handshake/link icon with a **three-person circular network SVG**; preserve the first two icons/cards.
- [x] Visually review and accept desktop/mobile layouts, spacing, image, and **Illustrative image** label.
- [x] Freeze the approved **Commercial Risk Management** content and layout; do not change it while applying People & Culture updates.
- [ ] Place the reviewed final source at `src/components/experience/fibra/FibraRiskPeople.astro` and inspect the Git diff for unintended changes, particularly the Commercial Risk Management section.
- [ ] Run `npm run build`, check mobile/desktop and accessibility, commit and push, then confirm the live page.
- [ ] Check the status of other Fibra refinements and the separate **Commercial Growth Process** removal before deciding which additional files to include in the same commit.

**Status:** People & Culture visual/content design approved. Build, commit and deployment not yet verified.


## Aton Engenharia — Forest Fire Monitoring case study (2026-10-27)

**Scope:** Develop a standalone case study first, then decide which elements belong in the shorter Aton Experience summary. Do not expand the full Aton chapter until the case is consolidated.

- [x] Define the standalone case route: `src/pages/cases/forest-fire-monitoring.astro`.
- [x] Review and approve the dark photographic hero on desktop and mobile; component: `src/components/cases/forest-fire-monitoring/ForestCaseHero.astro`.
- [x] Approve hero framing: **Forest Fire Monitoring** / **From observation to a profitable business.** / **Product · Project · Commercial Management**.
- [x] Retain the case indicators **24 monitoring towers**, **+1,400 km² monitored**, and **4 international corporate clients**.
- [x] Identify the four corporate client groups: **Saint-Gobain, Gerdau, ArcelorMittal, WestRock**.
- [x] Review and approve the **Featured Case Study** card inside Aton Experience, with **Explore Case Study →** linking to the standalone page; user supplied a desktop screenshot.
- [x] Agree the next section's visual direction: **The Opportunity — Seeing What Others Didn’t**; three-part desktop composition (discovery narrative, historical watchtower photograph, observation-to-remote-monitoring concept), stacked on mobile.
- [ ] Confirm final source files and image filenames in the local repository; preserve approved ABB and Fibra components.
- [ ] Implement and visually review **The Opportunity** and subsequent case-study sections one at a time.
- [ ] Check the case-study page and Experience-card link on desktop/mobile; run `npm run build`.
- [ ] Verify photograph provenance, client-logo rights, metric scope, historical claims and disclosure suitability.
- [ ] Commit/push case-study files and documentation; verify live GitHub Pages deployment and link navigation.
- [ ] After completing the case, assess what to summarize in the broader Aton Experience chapter.

**Historical-image distinction:** The conventional watchtower photographs were taken in 2007 at a prospective customer's facilities; they are **not** photographs from the Veracel visit and **not** photographs of Aton's remote-monitoring equipment. The hero panorama was adapted from a historical installation photograph; preserve a clear image-adaptation disclosure.

**Status:** Hero and Aton featured-card visual iterations approved. The Opportunity structure agreed; implementation, production build, commit/push and public deployment of the case are not independently verified by these records.
