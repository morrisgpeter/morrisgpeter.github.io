# Professional & Technical Portfolio — Project Context

**Project:** Peter Morris professional and technical portfolio  
**Repository:** `morrisgpeter/morrisgpeter.github.io`  
**Live site:** `https://morrisgpeter.github.io/`  
**Last updated:** 2026-10-24

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

## Deployment and current implementation — updated 2026-10-12

- **Status:** Astro Home publicly accessible. Dedicated Certifications & Education v6 and Contact v5 pages have also been published and visually confirmed by the user. First custom GitHub Actions deployment succeeded on commit `b99b5ca` (workflow run #1, about 35 seconds).
- **GitHub Pages source:** GitHub Actions (replaces direct branch publishing).
- **Trigger:** push to `main`, with optional manual `workflow_dispatch`.
- **Build job:** checkout repository, set up Node.js 22, run `npm ci`, `npm run build`, configure Pages, and upload `./dist`.
- **Deploy job:** deploy the uploaded artifact to the `github-pages` environment.
- **Astro configuration:** `astro.config.mjs` sets `site: 'https://morrisgpeter.github.io'`; no `base` is needed for this user-site repository.
- **Local build:** `npm run build` succeeded; output is static and generates `dist/`. `dist/` is excluded from Git.
- **Implemented files (selected):** `src/components/Header.astro`, `Hero.astro`, `Expertise.astro`, `Achievements.astro`; `src/layouts/BaseLayout.astro`; `src/pages/index.astro`, `contact.astro`, `certifications-education.astro`; `src/styles/global.css`; `astro.config.mjs`.
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


### Published page milestones (2026-10-12)

- **Certifications & Education v6:** `/certifications-education` published and visually verified. Features PMP and PSM I Credly verification, three academic education entries, 15 development credentials and 170+ professional-development hours, with a six-topic strip and Credly profile link. See `PROJECT_DECISIONS.md` D-030–D-040.
- **Contact v5:** `/contact` published and verified after commit `bdf7c49`. Executive copy begins with **Get in Touch** beneath **CONTACT CHANNELS**; three direct icon/label links: Email (`mailto:morrisgpeter@hotmail.com`), LinkedIn (`https://www.linkedin.com/in/morrisgpeter/`), and Portfolio (`https://github.com/morrisgpeter`, GitHub icon). No contact form, cards, explanatory captions or arrow glyphs. Uses `/images/hero-portrait-transparent.png` and **New Zealand | Open to international opportunities.** User confirmed link functionality, desktop/mobile rendering, cross-page navigation, public release and GitHub Project updates for #14, #36–#38. See D-041–D-044.
- **Shared Header:** navigation updated to reach Contact and Certifications & Education; remaining site-wide navigation will evolve with unfinished pages.
- **Future GitHub profile enhancement:** professional profile README, pinned repositories, visual alignment, website link and organized technical projects (D-045). Not yet implemented.

### Certifications & Education — pending review (2026-10-15)

The published development metrics are **15 Professional Development Credentials** and **170+ Hours of Professional Development** (rounded from 172.75 hours). The current design places **Last 2 years** in the separate development topic strip, which does not clearly establish that both metrics refer to that timeframe. **Proposed, not yet approved or implemented:** place a concise, accurate timeframe directly with both metrics under **Continuous Professional Development**; consider shortening labels to **Development Credentials** and **Learning Hours**, and removing the redundant **Professional Development** chip. First verify that all 15 credentials and all counted hours belong to the chosen period (for example, 2025–2026). See `PROJECT_DECISIONS.md` D-046.


## About Me — approved specification and implementation (updated 2026-10-20)

**Planning:** Issue #19 content planning was completed. About Me is now implemented and visually reviewed, with final QA and issue status verification still pending. Do not infer GitHub issue closure from page implementation.

**Exact opening:** **Engineering Expertise. Entrepreneurial Mindset. Global Perspective.** Set on three lines, on a light internal-page background.

**Approved narrative:** Preserve the full original five-section English text, without paraphrasing: **My Professional Journey**, **An Entrepreneurial Perspective**, **How I Lead**, **A Global Perspective**, **What Connects It All**. The full authoritative copy must be retained in `docs/ABOUT_ME_APPROVED_NARRATIVE.md`; it is not embedded in the baseline Context/Decisions files.

**Approved layout, in order:**

1. Light typographic About Me opening, with the three-part headline.
2. My Professional Journey narrative and **The Evolution of My Professional Focus**: three independent smooth flat-bottom bands, navy Engineering, light-blue Project & Program Management, orange Commercial Leadership, spanning 1997–2026 and the four companies. Fifteen recorded year/percentage observations and methodology note are in `PROJECT_DECISIONS.md` D-049 and its About Me specification section.
3. An Entrepreneurial Perspective narrative with **2012 — Co-founded Fibra Engenharia** and **Building a business from the ground up.**
4. How I Lead narrative on subtle blue-gray background with five numbered principles: Empowerment, Collaboration, Transparency, Accountability, Hands-on Leadership.
5. A Global Perspective narrative with geographic map showing **Brazil** (professional experience/business development), **New Zealand** (coordination and FAT base), project-delivery locations, customer home countries represented at New Zealand FATs, partner manufacturers, and ABB manufacturing locations. Multiple distinct countries across these roles, not equivalent to seven delivery countries or physical work locations; the original planning count should be rechecked against the implemented marker list. Add **25+ — Languages in which I can say “Good morning”**, never implying fluency.
6. What Connects It All narrative and an **Engineering / Business / People → Value Creation** illustration, positioned left of the narrative on desktop.

**Visual approach:** Executive, spacious, minimal, primarily light backgrounds and navy accents. Implemented graphics include the professional-focus chart, leadership philosophy diagram, world map and value-creation illustration. Charts/maps should be responsive, geographically/data accurate, and accessible. Preserve Home and other page decisions unchanged. Validate confidentiality before release.

**Implementation status:** About Me has been coded and visually reviewed. The Global Perspective section and map asset were committed and pushed as `a29a6e2` (2026-10-20). The final What Connects It All section was subsequently confirmed by the user on the live website; the specific commit is not recorded here. Final mobile, accessibility and content QA remain pending.


### About Me — final visual decisions and completed refinements (2026-10-20)

- **Global Perspective:** map heading **An International Network**, subtitle **Projects, customers and manufacturing across the globe.** Map legend uses ring-and-dot symbols matching the markers. Brazil's role remains **Experience & business**; New Zealand's role/legend is **Global Project Management**, with a tooltip explaining international project coordination, customer relationships and FAT in New Zealand. Customer FAT markers indicate customer origins; the FAT took place in New Zealand.
- **Project indicators:** 7 countries with project deliveries; 11 global projects; 110+ stakeholders across teams; 767.5 MW MV UPS capacity (2023–2026). Review period and delivered-versus-planned wording before final public claims.
- **Closing section:** **What Connects It All** uses the approved three-paragraph narrative and a three-part **Engineering / Business / People** diagram centered on **Value Creation**. Desktop layout has the illustration on the left and text on the right.
- **Completed Fibra visual refinement:** user replaced the logo image, retaining the filename, so only **Fibra** branding appears. The displayed size and proportions were reviewed and approved; user verified the result.

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
5. **Contact** — professional contact channels (**implemented and published**).

The original five-page navigation remains a **proposal** for the unfinished pages. Contact and Certifications & Education are already published and linked from the shared Header.

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

- Final navigation/page structure for remaining About, Experience and Portfolio pages; Contact and Certifications & Education links are operational.
- Whether to add Data Science & Analytics as a third Home pillar in a later release (not part of the initial Home).
- Language strategy: English first was suggested but not confirmed.
- Further typography and image refinements within the accepted dark Home / light internal-page direction.
- Which metrics, photos, and projects are cleared for public use.
- Final mobile/accessibility testing for the implemented About Me chart, map and illustrations.
- Confirm `docs/ABOUT_ME_APPROVED_NARRATIVE.md` remains synchronized with the final approved About Me copy.
- Review whether project planning documents should remain in the public repository after launch.
- Make the Node.js/npm PATH persistent for future VS Code Bash sessions.
- Validate the actual timeframe for the 15 development credentials and 170+ hours; review and implement the proposed metrics-card clarity improvements (D-046).


## Experience — ABB Global Footprint (approved 2026-10-23)

**Component:** `src/components/experience/GlobalProjectFootprint.astro`; approved iteration: `GlobalProjectFootprint_v22.astro`. **Status:** visual/interaction scope accepted by the user for this iteration; publication, full automated QA, and disclosure approval are separate checks.

- The ABB Experience chapter includes a **Global Footprint** visualization showing project-related activity, not personal travel or exact facilities. Three selectable regional views: **North America**, **Europe**, **Oceania**. Current interface shows **10**, **7**, and **2** distinct locations respectively (counts are locations, not projects).
- Activity filters: All locations, Projects, Manufacturing, Suppliers, Technology Demonstrations. Map markers use blue capacity-scaled circles with the number of projects inside; green, orange, purple markers represent the other activities. A concise legend explains circle area (ordered MW) and number (project count).
- Regional buttons include recognizable geographic silhouette SVGs, left-aligned with the region name and location count; **no MW total** in these buttons. North America shows US state borders; other maps retain regional geographic context.
- Tooltips only appear on deliberate hover/focus or selection; changing region/filter must not automatically open a tooltip. Tooltips must remain inside the map at edges, including mobile. Project tooltip copy is concise: `City, ISO alpha-3 country · N projects · X MW`; nonproject markers display `City, ISO alpha-3 country` only. Do not repeat activity category or 'ordered capacity' in the tooltip.
- The detail card, Browse locations dropdown/table, and duplicated specific project data below the map were removed. Keep the map as the primary information surface. The top subtitle is intended as a single line when width permits, naturally wrapping on narrower screens. ABB branding in the small section eyebrow was removed/deemphasized.
- Locations include supplier **Wytheville, Virginia, USA**. North America project markers were repositioned to better reflect city coordinates; Europe markers around Brno and Oceania's Napier manufacturing/technology markers remain close, without connecting lines. Map positions remain **approximate**.
- Responsive screenshots were reviewed for all three regions, with mobile accepted as sufficient for this release; future polish may revisit map readability and clustered markers.
- Important: **ordered capacity may include future deliveries**, and is not necessarily delivered capacity. Revalidate city list, project count, unit counts, capacity definitions, confidentiality, and permissions before publishing externally.


## Experience — ABB Project Delivery Scale & Portfolio Value (approved 2026-10-23)

**Component:** `src/components/experience/PortfolioGrowth.astro`. **Status:** committed and pushed to `main` as `936c826` on 2026-10-23 together with the ABB section reordering; user confirmed the updated live Experience page. Automated build details, accessibility audit and confidentiality authorization have not been independently verified.

- **Approved heading:** **PROJECT DELIVERY SCALE & PORTFOLIO VALUE** / **Scaling MV UPS to 1.2 GVA**. Intro: “Cumulative ordered capacity and key initiatives that strengthened delivery governance and operational readiness during a period of accelerated growth.”
- **Summary cards:** **1.2 GVA — Total Ordered Capacity** and **USD 255M — Total Order Value**, both covering **2021–Oct 2026**. Do not show order count or precise figures in the public-facing cards. Source spreadsheet analyzed in discussion: `ABB_Project_Orders_2021-2026(2).xlsx`, 20 orders, total **1,208.25 MVA** and **USD 255.41M**; retain full precision only for internal calculations. These are **nominal ordered capacity** and **total order value**, not delivered/installed capacity or recognized revenue.
- **Chart:** **Cumulative MV UPS Order Capacity (MVA)**, subtitle **“Cumulative portfolio capacity (MVA) and key initiatives supporting project delivery and governance.”** Time axis begins **Jan 2023**, ends **Oct 2026**; orders before Jan 2023 remain in the cumulative baseline. Vertical axis is in **MVA**; ordered capacity evolves as a **step chart** using order-issue dates, not scheduled delivery dates. Upper-right summary may read **Oct 2026 · 1.2 GVA**.
- **Four milestones:** **Aug 2023 — Cross-Border VAT Resolution**; **Nov 2024 — MV UPS Project Delivery Workflow**; **Jan 2025 — Business Model Workshop** (presented lessons learned and delivery workflow to senior representatives of Sales, Service, Business Units, Project Management, Marketing and Product Management); **4 Aug 2025 — Product Documentation Package** (publication date confirmed). Milestones are independent professional initiatives, not order events or proof that they caused order growth.
- **Interaction and responsiveness:** numbered markers link to the **Key Initiatives** descriptive panel. Desktop retains short labels near markers. Mobile fits the **entire 2023–2026 curve** without horizontal scrolling, hides marker titles within the plot, retains numbered markers and date buttons, and stacks initiative descriptions. User approved screenshots of both layouts.
- **Scope:** only this ABB Experience section was revised; other Experience sections were not intentionally changed. The previously proposed energy equivalents and Orders and Deliveries panels are excluded.
- **Release gates:** verify source calculations, order issue dates, rounding, confidentiality/disclosure permissions for commercial figures and internal initiatives, keyboard/focus/touch accessibility and `npm run build` evidence as part of final QA. Code commit/push and user confirmation of live rendering are complete. Review older ABB figures in this file (e.g., 767.5 MW, ~USD 70M) separately: they use different definitions/time windows and must not be silently conflated with **1.2 GVA ordered capacity / USD 255M order value**.


## Experience — ABB approved section sequence (2026-10-23)

The ABB chapter in `src/pages/experience.astro` follows this **approved, published order**:

1. **ABB introduction / Global Sales Project Engineer**
2. **Project Delivery Scale & Portfolio Value**
3. **Global Footprint**
4. **Key Contributions**
5. **Stakeholders Across the Project Lifecycle**
6. **Data Center Power Flow**
7. **Business Impact**

**Narrative rationale:** role → portfolio scale → international reach → individual contributions → stakeholder coordination → technical context → business outcomes. Only section placement was intentionally changed; approved component content and interactions were retained. The reordering and new `PortfolioGrowth.astro` were committed and pushed as `936c826` (`feat: add ABB portfolio growth chart and reorganize experience sections`). The user confirmed the resulting live Experience page on 2026-10-23. This confirmation does not replace final accessibility, source-data or confidentiality checks.


## Experience — Fibra SFibra Digital Innovation (approved 2026-10-24)

**Component:** `src/components/experience/fibra/FibraSFibra.astro`. Approved candidate: `FibraSFibra_Text_Approved_v12.astro`. The user approved the section's English copy and reviewed the desktop visuals; responsive design had been accepted in earlier review. **This is not confirmation of a Git commit, build or live deployment.**

- **Story:** SFibra addressed errors, rework, delays and administrative effort caused by fragmented field records, inconsistent documentation and manual processes during growing utility field operations.
- **Flow:** Field Operations & Commissioning → Digital Platform → Customer Visibility & Acceptance. Customer operations accepted the service; SFibra recorded acceptance details and generated email notifications.
- **Benefits:** Operational Efficiency, Data Quality, End-to-End Traceability, Customer Visibility. Business Value also includes stronger customer transparency and differentiated Fibra engineering proposals. Avoid unverified numerical improvement claims.
- **My Contribution:** User directly conceived the solution and defined mobile-app and customer-portal features, evaluated technical/commercial feasibility, coordinated development and implementation, acting as Product Owner and Product Manager. This refers to functions performed, not necessarily formal titles or software programming.
- **Visual integrity:** Keep approved illustrations and responsive CSS; maintain the disclosure that workflow visuals, equipment identifiers and map markers are conceptual reconstructions, not original system records.
- **Release checks:** Copy approved v12 into the project component, run `npm run build`, review local desktop/mobile, check `git diff`, then commit and push. Verify GitHub Actions/live rendering and relevant confidentiality/rights separately.
