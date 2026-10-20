# Professional & Technical Portfolio — Decision Log

**Project:** `morrisgpeter.github.io`  
**Last updated:** 2026-10-20

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

| D-046 | 2026-10-15 | Certifications & Education — development metrics timeframe clarity | Make the timeframe for **15 development credentials** and **170+ learning hours** immediately visible alongside both figures. Proposed copy: **Continuous Professional Development** with a concise timeframe line; shorten metric labels to **Development Credentials** and **Learning Hours**; consider removing the redundant **Professional Development** chip from the metrics card. | Proposed | Current layout shows **Last 2 years** only in the separate topic strip (D-036), which does not clearly qualify the metrics. Verify the actual date range covered by all 15 credentials and the 172.75-hour source total before choosing **2025–2026**, **Last 2 years**, or another precise label. Preserve D-036 as the approved published baseline until a revised design is explicitly accepted and implemented. |

| D-047 | 2026-10-15 | About Me narrative | Preserve the complete five-section approved English narrative verbatim: **My Professional Journey**, **An Entrepreneurial Perspective**, **How I Lead**, **A Global Perspective**, **What Connects It All**. | Accepted | Narrative is distinct from the Experience page and must not be rewritten during implementation without explicit approval. The approved source text should be kept in `docs/ABOUT_ME_APPROVED_NARRATIVE.md` (ensure it is present in the repository before coding). |
| D-048 | 2026-10-15 | About Me opening and layout | Use **About Me** with the exact opening line **Engineering Expertise. Entrepreneurial Mindset. Global Perspective.**, displayed as three expressive lines on a light background. Follow with the five approved narrative sections in order. | Accepted | Executive, typography-led internal page; no large duplicate Home portrait. |
| D-049 | 2026-10-15 | Professional focus evolution chart | Under **My Professional Journey**, use **The Evolution of My Professional Focus**, subtitle **How engineering, project management and commercial responsibilities have shaped my career.** Three separate, smooth, flat-bottom area bands (not stacked): Engineering navy, Project & Program Management light blue, Commercial Leadership orange. X-axis 1997–2026, companies Telenge, Aton, Fibra Engenharia, ABB. | Accepted | Use the 15 user-provided observations recorded below, with a common percentage scale; each recorded year totals 100%. Smooth interpolation is illustrative, not measured annual data. Include a clear methodology note. |
| D-050 | 2026-10-15 | Entrepreneurship feature | In **An Entrepreneurial Perspective**, show a restrained typographic **2012** highlight with **Co-founded Fibra Engenharia** and **Building a business from the ground up.** | Accepted | Reinforce the entrepreneurship chapter without repeating Experience-page financial KPIs. |
| D-051 | 2026-10-15 | Leadership section | Use a subtly differentiated light blue-gray background and five compact, numbered principles: **Empowerment**, **Collaboration**, **Transparency**, **Accountability**, **Hands-on Leadership**. Preserve the approved narrative text. | Accepted | Desktop horizontal presentation, responsive stacking/wrapping; no large icons or colorful cards. See approved descriptions below. |
| D-052 | 2026-10-15 | Global perspective map | Create an executive-style geographic world map with country markers, legend, category differentiation, grouped markers for overlaps, and New Zealand highlighted as coordination/FAT base. Include **Brazil** as professional experience and business development. | Accepted | Concept approved; implement from validated geographic data, not the generated mockup. Distinguish delivery countries, customer headquarters represented at FATs in New Zealand, partner manufacturing, ABB manufacturing, Brazil career base, and New Zealand coordination/FAT base. No implication of personal travel to all locations. |
| D-053 | 2026-10-15 | Multicultural highlight | Under **A Global Perspective**, show **25+** with **Languages in which I can say “Good morning”** and optional supporting line **Small gestures can build meaningful connections across cultures.** | Accepted | Refers to greetings, **not** language fluency. |
| D-054 | 2026-10-15 | About Me section sequence and visual restraint | Sequence: opening → My Professional Journey + chart → An Entrepreneurial Perspective + 2012 feature → How I Lead + five principles → A Global Perspective + map + 25+ greetings → What Connects It All + quiet typographic closing. | Accepted | Primarily white/light, navy accents, measured whitespace, mobile-responsive. No additional charts or photos in initial implementation. |
| D-055 | 2026-10-15 | About Me workflow | Content and visual planning for GitHub Issue **#19** considered complete in discussion; next stage is Issue **#20 Implement About Me Page**. | Accepted | GitHub issue status and repository files are **not** automatically updated; commit documentation and update GitHub Project manually. |

| D-056 | 2026-10-20 | About Me implementation milestone | The Global Perspective page changes and `global-perspective-map-v3.svg` were committed and pushed as `a29a6e2`; final **What Connects It All** section was subsequently implemented and visually confirmed on the public site. | Accepted | Live visual confirmation was provided later; the exact commit for the final section is not recorded. |
| D-057 | 2026-10-20 | Global Perspective visual and labels | Use **An International Network** and **Projects, customers and manufacturing across the globe.** Legend icons match ring-and-dot map markers. Brazil retains **Experience & business**; New Zealand uses **Global Project Management** for its marker role, accessible label and legend, retaining the description of international coordination, customer relationships and FAT in New Zealand. | Accepted | Avoid implying that all business experience was in Brazil or that FAT took place in customer countries. |
| D-058 | 2026-10-20 | Global Perspective metrics and layout | Present four indicators: **7** countries with project deliveries, **11** global projects, **110+** stakeholders across teams, **767.5 MW** MV UPS capacity (2023–2026), in a pale-blue card visually aligned with the **25+** greetings card. | Accepted | Metric definitions and the distinction between delivered and planned capacity require final verification before v1.0. |
| D-059 | 2026-10-20 | What Connects It All final presentation | Preserve the approved three-paragraph closing text and pair it with a **Value Creation** illustration linking **Engineering**, **Business**, and **People**. On desktop, illustration appears left and narrative right. | Accepted | Visually reviewed by user on the public site; exact commit not recorded. This refines the typography-only closing in D-054. |
| D-060 | 2026-10-20 | Fibra logo refinement | Remove **“Engenharia”** from the displayed Fibra logo while preserving **Fibra** branding, and review its displayed size and proportions. | Accepted (implemented) | User replaced the image while retaining its filename, approved the revised card appearance, and verified the result. |
| D-061 | 2026-10-20 | Professional focus chart implemented design | The implemented chart is an interactive **100% stacked area** chart with an illustrative transition at 2020 and a revised 2021 allocation, superseding D-049's earlier independent-band/15-observation specification. | Accepted | Preserve actual implementation and approved methodology; verify exact observation values in `about.astro` before changing the source data. |
| D-062 | 2026-10-20 | About Me live visual confirmation | The **What Connects It All** section with illustration left and narrative right, and the updated **Fibra** logo card, were visually verified by the user on the public website. | Accepted | The About Me visual design is approved; final mobile, accessibility, data and confidentiality QA remain open. The specific commit for the closing section is not recorded here. |

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

**Review pending (D-046, proposed 2026-10-15):** The two metrics need a directly associated timeframe; the current **Last 2 years** label in the separate topic strip is easy to miss. Validate the date range for all 15 credentials and the 172.75 hours before approving copy such as **2025–2026**. Proposed refinements are shorter metric labels and removal of the redundant chip. No code or published page change is confirmed.

### Contact (D-041–D-044)

The published `/contact` v5 page uses a compact, light executive layout, small transparent portrait, direct icon-and-label links (Email, LinkedIn, Portfolio), and a one-line desktop location statement: **New Zealand | Open to international opportunities.** No contact form or verbose card descriptions. Shared Header navigation includes Contact and Certifications & Education. User validated desktop/mobile, links, cross-page navigation and the public deployment (commit `bdf7c49`). GitHub Project issues #14 and #36–#38 were updated by the user.

### GitHub profile — future enhancement (D-045)

Create a professional GitHub profile README, pin relevant repositories, align branding with the Astro site, link back to the portfolio and organize technical work. This is roadmap work, not yet implemented.

### Experience versus Portfolio

Proposed distinction: **Experience** explains career progression and responsibilities; **Portfolio** provides deeper evidence through selected project case studies. Avoid duplicating the same information verbatim.

### Deployment milestone (2026-10-10)

GitHub Pages now uses the custom Astro workflow `.github/workflows/deploy.yml` (D-024–D-027). The first successful deployment used commit `b99b5ca` on `main`; the public Home was visually checked. Future pushes to `main` trigger a new build and deployment. The `dist/` directory is Git-ignored. The local macOS Bash PATH still needs a permanent fix for `/opt/homebrew/bin`.

The documentation-visibility review anticipated by D-015 is now due because the website is live; **no new visibility decision has been made**.


### About Me — approved implementation specification (D-047–D-055)

**Opening (exact):** Engineering Expertise. Entrepreneurial Mindset. Global Perspective.

**Approved narrative:** Preserve the full five-section English draft exactly as previously approved. Its complete text is **not included in these two baseline documentation files**; retain a separate `docs/ABOUT_ME_APPROVED_NARRATIVE.md` as the authoritative copy before implementation.

**Chart title:** The Evolution of My Professional Focus  
**Subtitle:** How engineering, project management and commercial responsibilities have shaped my career.  
**Explanatory note:** Illustrative distribution of professional responsibilities based on key career stages; percentages indicate relative focus and total 100% at each recorded year.

| Company | Year | Engineering % | Project & Program Management % | Commercial Leadership % |
| --- | ---: | ---: | ---: | ---: |
| Telenge | 1997 | 70 | 30 | 0 |
| Telenge | 2000 | 65 | 35 | 0 |
| Telenge | 2001 | 60 | 30 | 10 |
| Aton | 2003 | 40 | 40 | 20 |
| Aton | 2005 | 30 | 45 | 25 |
| Aton | 2006 | 25 | 40 | 35 |
| Aton | 2009 | 10 | 50 | 40 |
| Fibra | 2012 | 5 | 45 | 50 |
| Fibra | 2014 | 5 | 50 | 45 |
| Fibra | 2015 | 20 | 30 | 50 |
| Fibra | 2016 | 20 | 40 | 40 |
| ABB | 2021 | 100 | 0 | 0 |
| ABB | 2022 | 20 | 70 | 10 |
| ABB | 2024 | 10 | 60 | 30 |
| ABB | 2026 | 10 | 75 | 15 |

**Leadership principles (exact approved short copy):**

1. **Empowerment:** Give people autonomy, encourage ownership, and support their development.
2. **Collaboration:** Listen actively, involve others, and build solutions together.
3. **Transparency:** Share information responsibly and maintain clear expectations.
4. **Accountability:** Take responsibility for commitments, decisions, and results.
5. **Hands-on Leadership:** Stay engaged, understand challenges, and support teams when needed.

**Map data (historical planning categories; see D-057 for the implemented New Zealand label; categories are not necessarily physical work locations):**

| Category | Countries / locations |
| --- | --- |
| Professional Experience & Business Development | Brazil |
| Project Delivery Locations | United States, Canada, United Kingdom, Czech Republic, Belgium, Australia |
| Customer FAT Participation — customer-company home countries; customer representatives attended FATs in New Zealand | Oman, South Korea, Malaysia, Taiwan, Japan, United Kingdom, Canada, Belgium, Philippines |
| Partner Manufacturing Facilities | Hungary, Czech Republic, Finland, Italy |
| ABB Manufacturing Facilities | Czech Republic, Mexico, United States |
| Global Project Coordination & FAT | New Zealand |

**Historical planning count (recheck against the implemented marker list):** 18 distinct named countries/territories across all categories (16 unique outside Brazil and New Zealand, plus Brazil and New Zealand). Taiwan is listed separately as provided for geographic visualization; this is not a political characterization. The generated concept image is illustrative and contains inaccurate metrics/possible placements; it must not be reused as authoritative data. The ABB Home **7 Countries** metric is a separate, approved project-delivery scope and must not be replaced by the map's wider relationship count.

**Implementation notes:** responsive accessible SVG or equivalent map, tooltips/legend and keyboard-accessible country information if interactive; show overlapping roles without hiding categories; verify geography, permissions, and any confidentiality concerns. Do not imply FATs occurred in the customer-company countries.

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

13. Validate the timeframe and review the proposed Certifications & Education metrics-card copy/layout (D-046); implement only after approval.
14. Complete About Me final mobile/accessibility and content QA; final section has been visually verified live (D-056–D-062); preserve the approved narrative source.
15. Recheck map country roles, metric definitions and confidentiality as part of final QA; complete mobile and keyboard-accessibility tests.
16. Fibra logo refinement completed and visually verified (D-060, D-062).

## Change management

When a decision is confirmed or revised:

1. Add or update an entry with the date, status, and reason.
2. Mark replaced decisions **Superseded** rather than silently erasing them.
3. Update `PROJECT_CONTEXT.md` if the change affects the overall vision or architecture.
4. Commit both files to Git alongside the relevant changes.
