# Professional & Technical Portfolio — Project Context

**Project:** Peter Morris professional and technical portfolio  
**Repository:** `morrisgpeter/morrisgpeter.github.io`  
**Live site:** `https://morrisgpeter.github.io/`  
**Last updated:** 2026-10-29

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


## Home Key Achievements — review requested (2026-10-25)

The user flagged the Home screenshot and requested a future review of the four currently published indicators: **25+ Years**, **11 Projects · 7 Countries**, **100+ Stakeholders**, and **6 Industries**. Reconcile the figures and their meanings with the expanded ABB Experience evidence before proposing replacements. **Twenty orders are not necessarily twenty distinct projects**; ordered MVA and delivered MW/MVA are different measures. Preserve existing Home copy and layout until revised indicators are explicitly agreed. Track execution in `PORTFOLIO_ROADMAP.md`.


## Experience — Fibra publication and approved refinements (2026-10-25)

**Published baseline:** Fibra Experience, including SFibra Digital Innovation, was committed as `43dd16d`, pushed to `main`, and subsequently confirmed functioning on the public GitHub Pages Experience page by the user. This updates the older pending-release wording in the SFibra section above.

**Approved Business Impact presentation:** Five equal-priority indicators in `src/components/experience/fibra/FibraExperience.astro`:

| Indicator | Title | Supporting copy |
| --- | --- | --- |
| **8.5×** | Services Contract Growth | Scaling the engineering services portfolio |
| **39** | MV Substation Automation Projects | Strengthening power distribution infrastructure |
| **2,760** | Reclosers Deployed | Grid modernization program |
| **50+** | Professionals | Through project management teams |
| **>95%** | Commissioning Data Accuracy | Reduced rework through SFibra |

The relative **8.5×** growth metric replaces **USD 8.5M** and removes the six-year headline to avoid misleading absolute-value comparisons. **39** refers to **MV Substation Automation Projects**, not the number of municipalities or a claim that exactly 39 substations were fully automated. Do not conflate contract growth with annual revenue. Source equivalence and disclosure remain release checks.

**Approved Building & Scaling Fibra revisions:** `src/components/experience/fibra/FibraTimeline.astro` retains seven milestones and the Bahia/Sergipe geographic footprint. Three milestones have revised copy:

| Period | Milestone | Description |
| --- | --- | --- |
| **2012–2013** | Delivery Capability | Building project execution capacity and operational processes. |
| **2013–2014** | Commercial Development | Initial contracts, customer relationships and portfolio development. |
| **2017–2018** | Portfolio Diversification | Expansion into additional services and business opportunities. |

The other timeline milestones remain unchanged. User reviewed desktop/mobile screenshots and approved the presentation. The public-facing note saying figures were historical estimates based on an interview and subject to final evidence review was removed as inappropriate internal-process copy; maintain internal source checks instead. Punctuation is consistent. `FibraSFibra.astro` is unchanged.

**Release status for this refinement:** Visual review complete; a final local production build, Git commit/push and live-site confirmation of these specific changes have not yet been provided.


## Experience / Commercial Expertise — Commercial Growth Process architecture (2026-10-25)

The user approved relocating **Commercial Growth Process** from the Fibra Engenharia Experience chapter to a future **Commercial Expertise** area. Fibra Experience retains its two specific commercial narratives, **Commercial Development in Action** and **Distributed Solar Journey**. The process represents capabilities used at Fibra and developed across the wider career (including Telenge, Aton, Fibra and ABB), rather than an asserted formal company methodology.

The four-stage reference is **Market Opportunities → Solution Development → Commercial Execution → Business Expansion**, with the existing skill labels preserved in `PROJECT_DECISIONS.md` (D-106–D-107). Remove the process-only UI/data/styles from `src/components/experience/fibra/FibraCommercial.astro` while preserving the approved Sankey-inspired chart and responsive solar timeline. Review the current Commercial Expertise structure before any new integration or redesign. This architectural decision is accepted; no new code deployment is implied.

## Experience — Fibra Commercial Risk Management (approved 2026-10-26)

The user approved the **COMMERCIAL RISK MANAGEMENT / Protecting a Fixed-Price Contract** case-study card. Its desktop layout uses three columns: left-side explanation of the August 2014 BRL-priced proposal and December fixed-price contract, a central **USD/BRL EXCHANGE RATE** chart, and right-side **Strategic Actions** / **Business Outcomes**. The chart covers monthly averages from **Jul 2014 to Jul 2015** and marks **Proposal** (blue, August 2014), **Signed** (turquoise, December 2014), and a muted **Planned delivery** window. Source text attributes the series to **Banco Central do Brasil, SGS 3698 (monthly average USD selling rate)** and explicitly says that the currency movement illustrates market context, not Fibra's actual cost exposure.

The approved narrative describes negotiations with US- and Israel-based suppliers, anticipated purchase orders, and group-company import channels. Actions are **Anticipated purchase orders** and **Imported through group companies**; outcomes are **Maintained margins** and **Delivered on schedule**. Blue/turquoise chart accents were adjusted to match the page's existing design system, and the user approved the final screenshot. Preserve this presentation unless a future change is requested. Screenshot approval alone does not establish the component filename, production build, Git commit, live deployment, accessibility compliance, data verification or disclosure clearance.


## Experience — Fibra People & Culture (approved 2026-10-26)

The **PEOPLE & CULTURE / Developing Teams and Building Lasting Relationships** section is visually approved on desktop and mobile. The approved narrative specifies mentoring approximately **three project managers** and coordinating multidisciplinary teams of **more than 50 professionals through delegated leadership**; it does **not** imply 50 direct reports. Three light-blue cards cover **Mentoring and Knowledge Sharing**, **Empowering Teams**, and **Long-Term Relationships**. The third card uses the final blue-outline **three-person circular network** SVG (not the superseded handshake/link attempts); the first two icons remain unchanged. The accompanying Fibra-branded team image is explicitly labeled **Illustrative image**.

The reviewed final component source is `FibraRiskPeople_RelationshipNetwork_v5_FIXED.astro`, intended to replace `src/components/experience/fibra/FibraRiskPeople.astro`. The same component also contains the previously approved **Commercial Risk Management** card, which must not be modified as part of this update. User-approved screenshots establish visual/content acceptance, **not** successful build, commit/push, live publication, accessibility or disclosure clearance. See D-112–D-115.


## Aton Engenharia — Forest Fire Monitoring representative case (2026-10-27)

**Content architecture:** Build a dedicated professional case study at `/cases/forest-fire-monitoring` before attempting to reconstruct the complete Aton Engenharia Experience chapter. The Aton Experience summary contains a **Featured Case Study** card linking to the standalone case. This supports the broader distinction between Experience (career scope) and case studies (detailed evidence).

**Files / structure discussed:**
- `src/pages/cases/forest-fire-monitoring.astro` — case-study route.
- `src/components/cases/forest-fire-monitoring/ForestCaseHero.astro` — approved responsive hero.
- `src/components/cases/forest-fire-monitoring/ForestOpportunity.astro` — next planned section, not yet confirmed as implemented.
- `public/images/cases/forest-fire-monitoring/forest-fire-monitoring-hero-panorama.jpg` — adapted panoramic historical installation photograph.
- `public/images/cases/forest-fire-monitoring/logos/` — provisional client-logo assets; replace/verify official artwork and usage rights before final release.

**Approved public-facing framing:** **Forest Fire Monitoring**; **From observation to a profitable business.**; **Product · Project · Commercial Management**; **Aton Engenharia · 2007–2012**. The Experience card uses **FEATURED CASE STUDY**, **Forest Fire Monitoring**, the same subtitle, **24 monitoring towers · +1,400 km² monitored · 4 international corporate clients**, and **Explore Case Study →**. Four corporate client groups: **Saint-Gobain, Gerdau, ArcelorMittal, WestRock**. These figures describe the monitoring business case, not all Aton projects.

**Historical narrative and attribution:** During a visit to Veracel's forestry operation in southern Bahia with RedePetro Bahia, the user observed human-staffed fire-watchtower practices and discussed triangulation with the monitoring manager. This prompted an opportunity to use remotely controlled cameras, communications and software for forest surveillance. The idea was developed with support from Aton leadership and a technical team; an initial solution was operational by 2007. The user led concept, requirements, initial project delivery and commercial development, then delegated later project execution. The service/rental model involved Aton's upfront equipment investment, customer installation/survey charges and recurring fees. Historical estimates of 18–24-month payback are **estimates**, not verified realized payback. Do not describe the solution as fully automated fire detection without evidence.

**Photography and design:** The approved hero uses a dark photographic treatment with an adapted panoramic historical installation image, responsive typography and a client-logo strip. The next section, **The Opportunity — Seeing What Others Didn’t**, should use a light background and a three-part layout: concise narrative, a conventional watchtower photograph, and a simple visual transition from human observation to remote monitoring/location estimation. Historical conventional-watchtower photographs were taken in **2007 at a prospective customer's facilities**, **not at Veracel** and **not of Aton's installed monitoring towers**. The full-tower photograph is preferred as the main image. Caption and adaptation disclosures must remain accurate.

**Status:** Hero and Featured Case Study card visually approved in discussion (desktop/mobile hero; desktop card screenshot). No independent confirmation here of final case production build, Git commit, GitHub Pages deployment or asset rights. Preserve approved ABB and Fibra sections.

### Forest Fire Monitoring — current section progress (2026-10-29)

This update supersedes the earlier paragraph identifying **The Opportunity** as the next unimplemented section. The case has an approved **01 — The Opportunity** section and an approved **02 — From Idea to Solution** presentation. The preferred **ForestSolution.astro v12** retains larger images and vertical scrolling; the compressed v13 was not accepted.

**03 — Business Model & Commercial Development**: version **7** is approved for desktop and mobile. Its local component is `src/components/cases/forest-fire-monitoring/ForestBusinessModel.astro`, imported/used by `src/pages/cases/forest-fire-monitoring.astro` (verify final integration in the Git diff). The user's `git status` on 2026-10-29 shows the case page modified and the new component untracked; this confirms local working-tree changes only, not a production build or publication.

Preserve all earlier approved ABB/Fibra sections, and do not stage unrelated scripts, cache files or Fibra logo images as part of this case-study commit.


### Forest Fire Monitoring — Sections 04–05 approved and release status (2026-10-29)

This checkpoint **supersedes earlier pending-release notes for Section 03** and the earlier roadmap entry that Section 04 was not yet planned. **Section 03 — Business Model & Commercial Development v7** was committed and pushed to `main` as **`97f8824`** (`feat: add forest monitoring business model and economics`), together with project documentation. The local `npm run build` succeeded (six pages). Live-site verification of that deployment is not independently recorded.

**04 — Operational Footprint / 24 Towers Across Brazil:** Desktop/mobile visual and content direction **approved**. A Brazil map with state boundaries and client-colored markers illustrates the historical geographic footprint. Four corporate groups — **Saint-Gobain, Gerdau, ArcelorMittal, WestRock** — account for **24 monitoring towers** across **seven operations**, monitoring approximately **1,400 km²** of forest areas. Distinguish corporate groups, operations, towers, and monitored area. Map positions should be derived from documented operating locations rather than treating illustrative screenshot positions as exact coordinates. Legend: Saint-Gobain blue, Gerdau orange, ArcelorMittal red, WestRock green.

**05 — Business Impact / An Established Business:** Desktop/mobile visual and narrative **approved**. Communicates the transition from a developed monitoring solution to an established commercial offering, using three summary cards: **4 Corporate clients**, **24 Towers operational**, and **Profitable business**. The approved narrative describes business profitability, initial investment recovery, customer expansion and Aton's continuing forest-sector offering. **Evidence gate:** profitability, actual investment recovery, expansion and present-day service availability require supporting confirmation before they are treated as independently verified facts; do not use the Section 03 *projected* 18–24-month payback as proof of realized recovery.

**Release boundary:** Approval of Sections 04 and 05 is **content/design approval**, not confirmation of their local build, commit, push, live publication, exact source filenames, or map-data verification. Preserve Sections 01–03 and all approved ABB/Fibra work. Next: confirm exact components and page imports, check desktop/mobile and accessibility, run build, inspect diff, stage only intended files, commit/push, and verify live site.


### Forest Fire Monitoring — Industry Recognition and Commercial Expertise follow-up (2026-10-29)

**Release checkpoint:** The five-section Forest Fire Monitoring case was committed and pushed as `1907d76`, and the user confirmed the live page. This supersedes the earlier pending-publication wording for Sections 04–05.

**06 — Industry Recognition / Sharing Expertise Beyond Project Delivery:** Approved after desktop and mobile visual review. A responsive timeline documents participation in forest-fire prevention and control conferences in **2007, 2015, 2017 and 2018**, with historical photographs for 2007, 2015 and 2018 and a text-only 2017 entry. The 2007 event occurred during Aton Engenharia; the later events occurred while working at Fibra Engenharia. These appearances primarily reflect the sharing of **technical expertise in forest-fire monitoring and detection**, not necessarily official commercial representation of either company. Component: `src/components/cases/forest-fire-monitoring/ForestIndustryRecognition.astro`; historical photos: `public/images/forest-industry-recognition/`. Visual approval does not itself confirm Section 06 commit, push or production deployment. Preserve approved Sections 01–05.

**Future Commercial Expertise page:** When developing **Commercial Leadership / Commercial Expertise**, assess a concise reference to these conferences as evidence of technical credibility, industry engagement, relationship-building and thought leadership that can support consultative business development. Link back to the case-study timeline rather than duplicating all four events. **Do not portray the 2015–2018 participation as Fibra sales activity, customer acquisition, or formal company representation without evidence.** Placement and wording remain to be designed and approved alongside the deferred Commercial Growth Process.
