# Professional & Technical Portfolio — Decision Log

**Project:** `morrisgpeter.github.io`  
**Last updated:** 2026-10-12

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
| D-009 | 2026-10-10 | Professional positioning | Engineering foundation; initially proposed three expertise pillars, including Data Science & Analytics. | Superseded | D-020 narrows the initial Home presentation to two established professional pillars; data science remains future scope. |
| D-010 | 2026-10-10 | Experience presentation | Organize experience chronologically by company. | Proposed | Easy for recruiters to follow; commercial and delivery achievements can coexist within each role. |
| D-011 | 2026-10-10 | Portfolio presentation | Organize work into case studies with individual project pages. | Proposed | Demonstrate outcomes and support future technical categories. |
| D-012 | 2026-10-10 | Design direction | Classic, restrained corporate style, with clear charts and selective imagery. | Proposed | Professional credibility and readability. |
| D-013 | 2026-10-10 | Language | English first, with potential Portuguese later. | Proposed | Not explicitly confirmed. |
| D-014 | 2026-10-10 | Documentation | Maintain `docs/PROJECT_CONTEXT.md` and `docs/PROJECT_DECISIONS.md`. | Accepted | Preserve alignment across conversations and coding sessions. |
| D-015 | 2026-10-10 | Documentation visibility | Keep `docs/PROJECT_CONTEXT.md` and `docs/PROJECT_DECISIONS.md` in the public GitHub repository until the portfolio website is live; revisit their visibility after launch. | Accepted | Simplifies collaboration and version control during initial development; review whether planning documents should move to private storage after launch. |
| D-016 | 2026-10-10 | Visual identity | Use a dark navy-to-blue gradient Home hero with prominent professional portrait and large typography; keep internal pages predominantly light (white or very light gray), with consistent blue accents. | Accepted | Executive, modern, minimalist, visual and data-driven presentation; selective photos, maps, charts and metrics. |
| D-017 | 2026-10-10 | Home hero messaging | **Title:** “From customer needs to business value”. **Subtitle:** “Understanding customer challenges, shaping the right solutions and leading their delivery to create measurable value and lasting relationships.” | Accepted | Customer-centered message integrating commercial solution development, project delivery, measurable value and long-term relationships. Title capitalization revised to sentence case on 2026-10-10; subtitle unchanged. |
| D-018 | 2026-10-10 | Home page structure | Five sections, in order: **Hero**, **Key Achievements**, **Areas of Expertise**, **Featured Work**, **Professional Journey**. | Accepted | Concise executive overview; dark hero followed by predominantly light sections. This does not yet confirm the separate five-page navigation proposal in D-008. |
| D-019 | 2026-10-10 | Home key achievements & career insights | Feature **25+ Years** (Engineering, Business & Project Leadership), **7 Countries** (International Project Experience), **100+ Stakeholders** (Cross-Functional Engagement), and **6+ Industries** (Cross-Industry Experience). Explore separate charts for portfolio evolution, team leadership and stakeholder engagement (potential radar). | Accepted | Combine cumulative career measures with clearly identified examples of scale. Verify figures, scope, methodology and confidentiality before publication; 100+ stakeholders currently refers to ABB global projects, not a career-wide total. Chart formats and underlying data remain open. |
| D-020 | 2026-10-10 | Home areas of expertise | Initially display only **Project & Program Management** and **Commercial Leadership**, as two equally prominent expertise areas, in that order. Defer **Data Science & Analytics** as a potential third Home area for later evaluation. | Accepted | Focus the Home on established professional strengths. Data science work may still appear as individual technical Portfolio projects as the site grows; reassess a third pillar once relevant projects and outcomes are demonstrated. Order updated in D-023. |
| D-021 | 2026-10-10 | Home expertise card copy | **Commercial Leadership** — “Turning Customer Challenges into Business Opportunities”. Description: “Building trusted customer relationships, identifying opportunities and developing tailored engineering solutions that drive business growth and deliver lasting value.” **Project & Program Management** — “Delivering Complex Projects. Creating Business Value.” Description: “Leading complex engineering projects and multidisciplinary teams, aligning stakeholders and managing risks to deliver reliable solutions, meet customer expectations and achieve business objectives.” | Accepted | Both headings and descriptions were explicitly approved; cards receive equal visual emphasis, side by side on desktop and stacked on mobile. Presentation order is defined by D-023. |
| D-022 | 2026-10-10 | Implementation sequence | Start building the Astro site now, before selecting Featured Work case studies. Implement progressively: development environment, base layout/navigation, hero, Key Achievements, two expertise cards, responsiveness and initial deployment. Add Featured Work content later. | Accepted | User prefers seeing and refining the working site incrementally rather than completing all content planning first. |
| D-023 | 2026-10-10 | Expertise pillar order | Present the two expertise pillars in this exact order: **1. Project & Program Management; 2. Commercial Leadership**. Apply consistently in the Hero eyebrow, Areas of Expertise cards, and future related sections, on desktop and mobile. | Accepted | Prioritize project/program leadership in the visual narrative while retaining equal prominence for commercial leadership. This refines D-020 without changing the two-pillar scope or approved card copy. |

| D-024 | 2026-10-10 | GitHub Pages deployment | Publish the Astro site through **GitHub Actions**, rather than deploying directly from the `main` branch. | Accepted | Astro needs a production build; Pages Source set to GitHub Actions. |
| D-025 | 2026-10-10 | Automated workflow | Keep `.github/workflows/deploy.yml`; trigger on pushes to `main` and allow manual dispatch; use Node.js 22, `npm ci`, `npm run build`, upload `dist/`, then deploy to GitHub Pages. | Accepted | Reproducible builds and automatic publication without committing generated `dist/`. |
| D-026 | 2026-10-10 | Astro production URL | Configure `site: 'https://morrisgpeter.github.io'` in `astro.config.mjs`, with no `base` path. | Accepted | User-site repository is served from the domain root. |
| D-027 | 2026-10-10 | First production deployment | First custom Astro GitHub Actions deployment completed successfully on `main`, commit `b99b5ca`; live Home visually verified at `https://morrisgpeter.github.io/`. | Accepted | Confirms operational publishing pipeline and rendered Home. |
| D-028 | 2026-10-11 | Key Achievements final copy | Four Home metrics in order: **25+ Years** — Engineering & Business Leadership; **11 Projects · 7 Countries** — Global Critical Power & Data Center Delivery; **100+ Stakeholders** — Coordinated Across Global Projects; **6 Industries** — Cross-Industry Experience. | Accepted | Refines D-019, which remains as the historical initial proposal. 11 projects, seven project-delivery countries and 100+ stakeholders relate to ABB global projects; three countries of in-person work are Brazil, New Zealand and Czech Republic. Six industries: Data Centers & Critical Power, Electric Utilities, Oil & Gas, Telecommunications, Mining, Pulp & Paper. Verify public claims and confidentiality in final release review. |
| D-029 | 2026-10-11 | Key Achievements layout | Light-background section directly after Hero; four columns with subtle dividers on desktop, two-column grid/cards on smaller screens; blue icons, navy metrics and smaller supporting text. | Accepted | `Achievements.astro` implemented and visually reviewed on desktop and at 375px mobile viewport; measured viewport/document/body widths all 375px, indicating no horizontal overflow at that width. Pending commit and GitHub publication. |

| D-030 | 2026-10-11 | Certifications & Education content | Create a dedicated English-language **Certifications & Education** page with the subtitle **Continuous learning for greater impact** and three sections: Professional Certifications, Academic Education, and Continuous Professional Development. | Accepted | Selective, executive presentation rather than a complete training catalogue. |
| D-031 | 2026-10-11 | Professional certifications | Feature **PMP®** (PMI; issued April 2025; valid through April 2028) and **PSM I** (Scrum.org; issued November 2025), with their original badge images and **Verify Credential** links exclusively to Credly. | Accepted | PMP: https://www.credly.com/badges/40e3fb6d-937a-4479-a67f-bbd3026aa5bc ; PSM I: https://www.credly.com/badges/89bcaf52-15e6-4ad1-99d8-1ee939d0bb67 . User tested both links locally. |
| D-032 | 2026-10-11 | Academic education | Show three qualifications in reverse chronological order: **Postgraduate Studies in Data Science & Big Data** (UFBA, 2021–2023); **Specialization in Digital Signal Processing** (IME, 1995–1996); **Bachelor's Degree in Electrical Engineering** (UFBA, 1989–1993). Include the original UFBA and IME institutional coats of arms. | Accepted | Use `public/images/education/ufba.png` for two cards and `ime.png` for one; do not display academic course hours or long descriptions. |
| D-033 | 2026-10-11 | Development credential metric | Show **15** with label **Professional Development Credentials**, followed by **Leadership · Project Management · Agile · AI · Sustainability · Business Transformation**. | Superseded | The 15-credential count and six topic areas remain valid, but the decision to exclude a training-hours indicator was revised by D-036. |
| D-034 | 2026-10-11 | Certifications page layout | Use a light, restrained executive design: two certification cards with badges, three education cards with coats of arms, and a centered development metric. Keep desktop layout compact (roughly two screens), and stack cards on mobile. | Superseded | Initial layout approved; revised compact three-card layout and section ordering are recorded in D-037. |
| D-035 | 2026-10-11 | Certifications page implementation and validation | Implement `src/pages/certifications-education.astro` using existing layout, plus badge assets in `public/images/certifications/` and education images in `public/images/education/`. | Accepted | User confirmed local rendering and both external links; `npm run build` completed successfully, generating `/certifications-education/index.html` and `/index.html`. Commit, push, and production verification still pending. |


| D-036 | 2026-10-12 | Professional development metrics and timeframe | Show **15 Professional Development Credentials** and **170+ Hours of Professional Development** as two prominent metrics. Present **Last 2 years** in the related development-area strip, not in the metrics card. | Accepted | 15 excludes the separately featured PMP and PSM I. The hours figure is deliberately rounded from the previously consolidated 172.75 hours; do not display false precision. |
| D-037 | 2026-10-12 | Certifications & Education v6 layout | Order: introduction → **Professional Certifications & Development** (three equal-height desktop cards: PMP, PSM I, and metrics) → linked **Continuous Professional Development** topic strip → **Academic Education** (three cards). Use matching light-blue category chips **Project Management**, **Agile & Scrum**, and **Professional Development**. Remove the metrics card's redundant title and leading icon; retain only two metric icons. | Accepted | Compact layout approved on desktop and at 375px mobile width; mobile cards stack, the two metrics remain side by side, and six SVG topic icons form two rows of three. Keep the existing Home and shared styling unchanged. |
| D-038 | 2026-10-12 | Credly profile and development themes | Add **View All Credentials** in the Continuous Professional Development topic strip, linking to the public Credly profile. Display six topic-specific SVG icons for Leadership, Project Management, Agile, AI, Sustainability, and Business Transformation. | Accepted | Profile: https://www.credly.com/users/morrisgpeter/badges/credly . Keep individual PMP and PSM I verification links. |
| D-039 | 2026-10-12 | Intro visual and quotation — deferred | Remove the former introductory quote **“Learning today to create greater impact tomorrow.”** and its placeholder. Consider a landscape image featuring mountains and a winding road, and select a **new** introductory quotation in a later release. | Accepted | Neither the landscape nor a replacement quote is approved for publication yet; track both as future enhancements. |
| D-040 | 2026-10-12 | Certifications & Education v6 validation | Approve the v6 desktop and 375px mobile screenshots and the successful local production build, which generated `/index.html` and `/certifications-education/index.html`. | Accepted | This verifies local implementation only; commit, push, GitHub Actions deployment, and live-site checks remain pending. |

| D-041 | 2026-10-12 | Contact page content | Use **CONTACT CHANNELS** eyebrow and **Get in Touch** title; retain “Great opportunities begin with meaningful conversations.” The introduction covers project/program management, commercial leadership, business development and sales, and critical infrastructure; omit “partnerships”. Close with “Always open to connecting with professionals and organizations worldwide.” | Accepted | Concise executive messaging, avoiding consecutive sentences starting with I. |
| D-042 | 2026-10-12 | Contact channels | Display three icon-and-text links, **Email**, **LinkedIn**, and **Portfolio** (with GitHub icon), without cards, explanatory copy, arrow symbols, or a contact form. Email uses `mailto:morrisgpeter@hotmail.com`; LinkedIn `https://www.linkedin.com/in/morrisgpeter/`; Portfolio `https://github.com/morrisgpeter`. Do not show the email address as secondary text. | Accepted | Minimal, consistent presentation; GitHub profile is the destination rather than a repository list. |
| D-043 | 2026-10-12 | Contact visual design and location | Light internal-page style, compact spacing, small portrait using `/images/hero-portrait-transparent.png`, and responsive channel links. Show **Location & Mobility** as **New Zealand | Open to international opportunities.** on desktop, allowing natural wrapping on mobile. | Accepted | Desktop and mobile screenshots approved; no implication of residence in two countries. |
| D-044 | 2026-10-12 | Contact release and navigation | Contact v5 published at `/contact`; shared `Header.astro` links to Contact and `/certifications-education`, alongside existing navigation. Email, LinkedIn, Portfolio and cross-page navigation tested; mobile layout reviewed. Commit `bdf7c49` pushed to `main`; user confirmed live publication and GitHub Project issue statuses updated for #14, #36–#38. | Accepted | Confirms published Contact milestone, not a full site-wide navigation audit. |
| D-045 | 2026-10-12 | GitHub profile roadmap | After primary site pages, enhance GitHub profile with a professional profile README, pinned repositories, consistent branding, portfolio website link, and organized technical projects (including analytics/data science as relevant). | Accepted | Future improvement; not part of Contact v5 release. |

## Key discussions

### Professional identity

The portfolio should communicate the intersection of **project/program management** and **commercial leadership**, grounded in engineering. **Data Science & Analytics** is a future avenue supported by academic training and technical projects, but is **not** a Home expertise pillar in the initial release (D-020). Reconsider it later when demonstrable projects and results support the positioning.

### Home page

**Confirmed hero messaging (D-017):**

> From customer needs to business value
>
> Understanding customer challenges, shaping the right solutions and leading their delivery to create measurable value and lasting relationships.

**Confirmed visual identity (D-016):** Dark blue gradient and professional portrait on the Home; light internal pages. Portrait treatment should remain natural, with a navy jacket and a subtle smile.

**Confirmed Home structure (D-018):** Hero → Key Achievements → Areas of Expertise → Featured Work → Professional Journey.

**Confirmed Key Achievements (D-028, refining D-019):** **25+ Years** — Engineering & Business Leadership; **11 Projects · 7 Countries** — Global Critical Power & Data Center Delivery; **100+ Stakeholders** — Coordinated Across Global Projects; **6 Industries** — Cross-Industry Experience. The 11 projects, seven countries and 100+ stakeholders refer to ABB global project work, not necessarily career-wide totals. Physical work took place in Brazil, New Zealand and Czech Republic; this is distinct from the seven countries of project delivery. Publication claims and confidentiality remain subject to final review. Layout accepted in D-029.

**Confirmed Home expertise (D-020, D-023):** First **Project & Program Management**, then **Commercial Leadership**. These are the only two initial Home pillars. Data Science & Analytics is deferred for later evaluation; it can still be included in technical Portfolio work.

**Approved expertise card copy (D-021), in presentation order:**

**Project & Program Management** — *Delivering Complex Projects. Creating Business Value.*

> Leading complex engineering projects and multidisciplinary teams, aligning stakeholders and managing risks to deliver reliable solutions, meet customer expectations and achieve business objectives.

**Commercial Leadership** — *Turning Customer Challenges into Business Opportunities*

> Building trusted customer relationships, identifying opportunities and developing tailored engineering solutions that drive business growth and deliver lasting value.

**Implementation approach (D-022):** Begin developing the site with Astro before finalizing Featured Work. Build and review one section at a time. The Astro development environment is now operational; Header and Hero have been separated into components, with shared styles in `src/styles/global.css`. Expertise and BaseLayout are now implemented. Key Achievements is implemented and locally reviewed (D-028–D-029), awaiting publication. The first Astro production deployment succeeded on 2026-10-10 (D-027).

**Career Insights to investigate:** a portfolio-value evolution chart (using comparable, clearly defined measures), a team-leadership evolution chart (distinguishing direct/indirect management from stakeholder coordination), and a stakeholder engagement radar chart (dimensions and defensible scoring methodology still to be defined). Industry coverage may be shown visually with sector icons. Verify accuracy and confidentiality before publication.

### Certifications & Education (D-030–D-040)

The dedicated `/certifications-education` page presents **Professional Certifications & Development** (PMP, PSM I, and a third metrics card), a **Continuous Professional Development** topic strip, then **Academic Education**. The metrics are **15 Professional Development Credentials** (excluding the two featured certifications) and **170+ Hours of Professional Development**, with **Last 2 years** shown in the topic strip. The strip contains six topic-specific SVG icons and a **View All Credentials** link to the user's Credly profile; individual PMP and PSM I verification links remain. Three education cards use original UFBA and IME institutional coats of arms. The intro quote and image placeholder were removed; a mountain/winding-road landscape and a newly selected quote are future ideas, not approved assets or copy. The v6 desktop and 375px mobile views were accepted; local production build succeeded on 2026-10-12. Commit/push and live deployment verification remain pending (D-036–D-040).

### Contact (D-041–D-044)

The published `/contact` v5 page uses a compact, light executive layout, small transparent portrait, direct icon-and-label links (Email, LinkedIn, Portfolio), and a one-line desktop location statement: **New Zealand | Open to international opportunities.** No contact form or verbose card descriptions. Shared Header navigation includes Contact and Certifications & Education. User validated desktop/mobile, links, cross-page navigation and the public deployment (commit `bdf7c49`). GitHub Project issues #14 and #36–#38 were updated by the user.

### GitHub profile — future enhancement (D-045)

Create a professional GitHub profile README, pin relevant repositories, align branding with the Astro site, link back to the portfolio and organize technical work. This is roadmap work, not yet implemented.

### Experience versus Portfolio

Proposed distinction: **Experience** explains career progression and responsibilities; **Portfolio** provides deeper evidence through selected project case studies. Avoid duplicating the same information verbatim.

### Deployment milestone (2026-10-10)

GitHub Pages now uses the custom Astro workflow `.github/workflows/deploy.yml` (D-024–D-027). The first successful deployment used commit `b99b5ca` on `main`; the public Home was visually checked. Future pushes to `main` trigger a new build and deployment. The `dist/` directory is Git-ignored. The local macOS Bash PATH still needs a permanent fix for `/opt/homebrew/bin`.

The documentation-visibility review anticipated by D-015 is now due because the website is live; **no new visibility decision has been made**.

## Open decisions / next discussion

1. Finalize the remaining site-wide navigation as About, Experience and Portfolio pages are implemented; Contact and Certifications & Education links are now live.
2. Determine where the approved Home expertise cards link (Experience, Portfolio, or filtered views).
3. Reevaluate Data Science & Analytics as a possible third Home expertise area in a later release; individual technical Portfolio projects remain possible.
4. Confirm language(s) and whether multilingual support is needed from the outset.
5. Confirm the final hero photograph asset and image usage/permission policy (overall visual direction is accepted in D-016).
6. Recheck Key Achievements evidence, precise scope and confidentiality before version 1.0; approved copy and layout are documented in D-028 and D-029. Select first-release projects separately.
7. Define comparable data and formats for portfolio evolution, team leadership, and stakeholder radar charts; distinguish team management from stakeholder coordination.
8. Review public visibility of the `docs/` planning files now that the site is live (D-015).
9. Make the local Node.js/npm PATH persistent in the macOS VS Code Bash environment.
10. Consider the deferred Certifications & Education introduction enhancements: mountain/winding-road landscape image and a new quote (D-039).
11. Plan the accepted GitHub profile enhancement after primary pages (D-045).
12. Evaluate proposed visual storytelling elements: origins and dual citizenship, places lived, Brazil regional activity map, global ABB/data-center project map, selected clients, technologies, multicultural greetings, and project-methodology chart (Waterfall/Agile/Hybrid). Confirm accuracy, permissions, and confidentiality before publication.

## Change management

When a decision is confirmed or revised:

1. Add or update an entry with the date, status, and reason.
2. Mark replaced decisions **Superseded** rather than silently erasing them.
3. Update `PROJECT_CONTEXT.md` if the change affects the overall vision or architecture.
4. Commit both files to Git alongside the relevant changes.
