# Professional & Technical Portfolio — Decision Log

**Project:** `morrisgpeter.github.io`  
**Last updated:** 2026-10-31

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

## ABB Global Footprint — accepted decisions (2026-10-23)

| D-070 | 2026-10-23 | Regional footprint structure | Replace a single world map with selectable North America, Europe and Oceania regional maps; show counts of distinct locations, not MW, on region selectors. | Accepted | Better geographic legibility. |
| D-071 | 2026-10-23 | Footprint activity categories | Retain filters for All locations, Projects, Manufacturing, Suppliers, Technology Demonstrations; distinguish categories by color. | Accepted | Map itself carries the information. |
| D-072 | 2026-10-23 | Project circle semantics | Blue bubble **area** conveys total ordered MW for a project location; numeral inside gives project count; explanatory legend retained. | Accepted | Do not confuse ordered and delivered capacity. |
| D-073 | 2026-10-23 | Regional selectors | Use recognizable, subtle geographic silhouette SVGs at left of region label and location count; do not show regional MW totals. | Accepted | Replace unsuitable emojis and abstract silhouettes. |
| D-074 | 2026-10-23 | Geographic precision | Use regional framing and near-geographic marker placement, US state boundaries on North America, and avoid connection lines; keep distinct circles where possible. | Accepted | Regional map should reduce visual displacement. |
| D-075 | 2026-10-23 | North America data | Add supplier in Wytheville, Virginia, USA; regional location count becomes 10 (Europe 7, Oceania 2). | Accepted | Confirmed addition; avoid confusing locations with project count. |
| D-076 | 2026-10-23 | Regional approval | North America, Europe and Oceania maps visually accepted on desktop and mobile; Oceania shows Sydney and Napier, with Napier on New Zealand North Island. | Accepted | Mobile considered acceptable; future refinement deferred. |
| D-077 | 2026-10-23 | Information density | Remove detailed project panel, Browse locations dropdown and location table; preserve interactive map and legend. | Accepted | Avoid excessive specificity and repetition. |
| D-078 | 2026-10-23 | Section heading | Use Global Footprint with restrained/no ABB Critical Power eyebrow; subtitle should remain one line when space permits and wrap responsively. | Accepted | Cleaner section hierarchy. |
| D-079 | 2026-10-23 | Tooltip content | Projects: `City, ISO alpha-3 country · N projects · X MW`; other categories: `City, ISO alpha-3 country`. No repeated category or ordered-capacity wording. | Accepted | Concise; legend already defines symbols. |
| D-080 | 2026-10-23 | Tooltip behavior | Tooltips appear only after hover/focus/marker selection; no automatic tooltip on changing region/filter. Constrain popovers within map bounds on desktop/mobile; avoid duplicate native browser tooltip. | Accepted | Fix unintended first-marker popovers and clipped edges; v22 approved. |
| D-081 | 2026-10-23 | Footprint milestone | Mark the ABB Global Footprint component **complete for the current design iteration** at v22. | Accepted | Does not imply code committed/published or confidentiality/QA clearance. |

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


### Global Footprint deferred work / release gates (2026-10-23)

- Optional later visual pass: inspect clusters (e.g., Fargo/Ellendale, Brno, Napier), tooltip readability at narrow widths, and region selector spacing. **Not a blocker for the accepted iteration.**
- Validate the 10/7/2 distinct-location inventory and exact cities/coordinates against source data; confirm the meaning and provenance of ordered MW and project counts.
- Review confidentiality, client/site attribution, and supplier disclosure before public release; the map is illustrative, not proof of personal travel or exact facility coordinates.
- Run build, keyboard/focus/touch and accessibility checks; verify real-device mobile interaction and publication status separately.


## ABB Portfolio Growth — accepted decisions (2026-10-23)

| ID | Date | Topic | Decision / direction | Status | Rationale / notes |
| --- | --- | --- | --- | --- | --- |
| D-082 | 2026-10-23 | ABB growth section scope | Retain only section heading/intro, two headline indicators, one cumulative ordered-capacity chart and a **Key Initiatives** panel; omit energy equivalents and separate Orders and Deliveries panels. | Accepted | Keep the story focused on project scale and professional contributions. |
| D-083 | 2026-10-23 | Metrics and definitions | Display **1.2 GVA Total Ordered Capacity** and **USD 255M Total Order Value** for **2021–Oct 2026**; no order count or precise decimals on the page. Underlying source totals: **1,208.25 MVA** and **USD 255.41M** across 20 orders. | Accepted | Rounded display; nominal ordered capacity is not delivered power and order value is not recognized revenue. |
| D-084 | 2026-10-23 | Chart and time basis | **Cumulative MV UPS Order Capacity (MVA)** with stepwise cumulative capacity from **Jan 2023 to Oct 2026**, using **order-issue dates** and including pre-2023 orders in the baseline; vertical axis in **MVA**. Subtitle: **Cumulative portfolio capacity (MVA) and key initiatives supporting project delivery and governance.** | Accepted | Accurate time representation; distinguish order dates from scheduled delivery dates. |
| D-085 | 2026-10-23 | Professional milestones | Show four numbered milestones directly on the curve: **Aug 2023 VAT Resolution**, **Nov 2024 Delivery Workflow**, **Jan 2025 Business Model Workshop**, **4 Aug 2025 Product Documentation Package**. Link to the descriptive **Key Initiatives** panel. | Accepted | Contextualize governance and process contributions without implying causation of sales growth; workshop documents remain confidential. |
| D-086 | 2026-10-23 | Visual copy and layout | Heading **Scaling MV UPS to 1.2 GVA**; blue/light visual identity; two indicator cards; milestone labels on desktop; retain close chronological placement of markers 2 and 3 while separating their labels. | Accepted | User approved desktop screenshots. |
| D-087 | 2026-10-23 | Mobile behavior | Fit the entire 2023–2026 plot within the mobile card **without horizontal scrolling**; hide plot milestone titles, retain numbered markers and selectable date buttons; display Key Initiatives in one column. | Accepted | User approved mobile screenshots after responsive correction; markers 2/3 are close but distinguishable. |
| D-088 | 2026-10-23 | Approval versus publication | Consider the **PortfolioGrowth** desktop/mobile visual iteration accepted; do not infer build success, Git commit, GitHub Pages deployment, accessibility compliance or disclosure authorization. | Accepted | Release checks remain independent. |

**Source and consistency note:** The source spreadsheet was used in the working discussion; verify it again before any data revisions. Earlier ABB figures (e.g., MW delivered/planned or ~USD 70M for a narrower period) represent different metrics and must not replace or be merged with the newly approved ordered-MVA/order-value series without reconciling definitions.


## ABB Experience — approved sequence and publication (2026-10-23)

| ID | Date | Topic | Decision / direction | Status | Rationale / notes |
| --- | --- | --- | --- | --- | --- |
| D-089 | 2026-10-23 | ABB chapter section order | Present sections in this order: **ABB introduction → Project Delivery Scale & Portfolio Value → Global Footprint → Key Contributions → Stakeholders Across the Project Lifecycle → Data Center Power Flow → Business Impact**. | Accepted | Establish role, scale and geographic reach first; then explain contributions, organizational/technical complexity and outcomes. No component content changes intended. |
| D-090 | 2026-10-23 | ABB Experience implementation and live verification | Commit `936c826` added `src/components/experience/PortfolioGrowth.astro` and reordered `src/pages/experience.astro`; push to `main` succeeded and the user confirmed the published page displays correctly. | Accepted (implemented) | Updates D-088’s earlier *not-yet-confirmed* commit/publication status. Does not establish an independent build log, accessibility audit, source-data verification or confidentiality authorization. |


## Fibra Engenharia — SFibra Digital Innovation (approved 2026-10-24)

| ID | Date | Topic | Decision / direction | Status | Rationale / notes |
| --- | --- | --- | --- | --- | --- |
| D-091 | 2026-10-24 | SFibra narrative | Approve the section heading **Connecting field execution to customer value** and the introduction describing the integrated installation, configuration, commissioning and testing workflow. | Accepted | Connect operational needs with customer value. |
| D-092 | 2026-10-24 | SFibra challenge | Add **The Challenge** before the three stages, explaining that fragmented records, inconsistent field documentation and manual processes contributed to errors, rework, delays and administrative effort; emphasize standardization, data accuracy, traceability and customer visibility. | Accepted | Describe actual operational problems, not only potential risks. |
| D-093 | 2026-10-24 | SFibra solution visualization | Retain the approved three-stage responsive presentation: **Field Operations & Commissioning**, **Digital Platform**, **Customer Visibility & Acceptance**; retain four benefit indicators: **Operational Efficiency**, **Data Quality**, **End-to-End Traceability**, **Customer Visibility**. | Accepted | User visually reviewed desktop presentation and previously accepted mobile responsiveness. |
| D-094 | 2026-10-24 | SFibra individual contribution | Describe leadership from concept through implementation, **acting as Product Owner and Product Manager**: product vision, app and portal functionality, technical/commercial feasibility, development, deployment and adoption coordination. | Accepted | Describes responsibilities exercised, not necessarily formal job titles or personal coding. |
| D-095 | 2026-10-24 | SFibra value and disclosure | Retain **Business Value** explaining reduced manual documentation/rework, stronger consistency/traceability, customer transparency and differentiated proposals. Retain the note identifying all illustrated interfaces, identifiers and map markers as conceptual, not original system records. No unverified numeric gains. | Accepted | Credible, evidence-conscious case study. |
| D-096 | 2026-10-24 | SFibra review status | **FibraSFibra_Text_Approved_v12.astro** accepted in discussion after visual review and final challenge-copy refinement. | Accepted (local design/content) | Local replacement, production build, commit/push and public deployment are not yet verified. |


## Home Key Achievements — pending review (2026-10-25)

| ID | Date | Topic | Decision / direction | Status | Rationale / notes |
| --- | --- | --- | --- | --- | --- |
| D-097 | 2026-10-25 | Home Key Achievements update | Revisit the four Home indicators shown in the screenshot, comparing their definitions and evidence with the expanded ABB Experience portfolio; propose updated copy only after validation. | Open | User requested this as a reminder, **not** approval of replacement values. Keep D-028 as the existing accepted copy until revised. Distinguish projects from orders and ordered capacity from delivered capacity; check confidentiality and responsive presentation. |


## Fibra Engenharia — Business Impact and Timeline refinements (2026-10-25)

| ID | Date | Topic | Decision / direction | Status | Rationale / notes |
| --- | --- | --- | --- | --- | --- |
| D-098 | 2026-10-25 | Fibra Business Impact growth metric | Replace **USD 8.5M / six-year framing** with **8.5× — Services Contract Growth — Scaling the engineering services portfolio**. | Accepted (visually reviewed) | Emphasize relative business expansion without implying a specific annual revenue, portfolio ceiling or directly comparable absolute value; confirm comparable underlying contract measures during evidence review. |
| D-099 | 2026-10-25 | Fibra infrastructure metric | Use **39 — MV Substation Automation Projects — Strengthening power distribution infrastructure**. | Accepted (visually reviewed) | Emphasize technical project scope rather than municipality count; do not equate projects with 39 fully automated substations. |
| D-100 | 2026-10-25 | Fibra remaining impact indicators | Use **2,760 — Reclosers Deployed — Grid modernization program**; **50+ — Professionals — Through project management teams**; **>95% — Commissioning Data Accuracy — Reduced rework through SFibra**. | Accepted (visually reviewed) | Approved five-indicator presentation; preserve precise titles and supporting text. |
| D-101 | 2026-10-25 | Fibra timeline revisions | **2012–2013 Delivery Capability — Building project execution capacity and operational processes.**; **2013–2014 Commercial Development — Initial contracts, customer relationships and portfolio development.**; **2017–2018 Portfolio Diversification — Expansion into additional services and business opportunities.** | Accepted (visually reviewed) | Distinguish early operational capability, commercial development and later diversification; keep the other four milestones and Bahia/Sergipe map. |
| D-102 | 2026-10-25 | Fibra visual review and internal note | Accept five-column desktop/stacked mobile Business Impact and seven-event responsive timeline; remove public note about historical estimates and evidence review; standardize timeline punctuation. | Accepted (visually reviewed) | Clean executive presentation; evidence validation remains an internal release check. `FibraSFibra.astro` unchanged. |
| D-103 | 2026-10-25 | Fibra/SFibra published baseline | Fibra Experience and SFibra were committed as **`43dd16d`**, pushed to `main`, and confirmed functioning on GitHub Pages by the user. | Accepted (published baseline) | Updates the earlier pending-release note in D-096. This does not confirm publication of the later D-098–D-102 refinements, which still require build/commit/push/live verification. |

**Approved exact five-indicator copy:**

| Indicator | Title | Supporting copy |
| --- | --- | --- |
| **8.5×** | Services Contract Growth | Scaling the engineering services portfolio |
| **39** | MV Substation Automation Projects | Strengthening power distribution infrastructure |
| **2,760** | Reclosers Deployed | Grid modernization program |
| **50+** | Professionals | Through project management teams |
| **>95%** | Commissioning Data Accuracy | Reduced rework through SFibra |

**Refined timeline copy:**

| Period | Milestone | Description |
| --- | --- | --- |
| **2012–2013** | Delivery Capability | Building project execution capacity and operational processes. |
| **2013–2014** | Commercial Development | Initial contracts, customer relationships and portfolio development. |
| **2017–2018** | Portfolio Diversification | Expansion into additional services and business opportunities. |

**Outstanding:** Confirm successful production build, inspect final diff, commit/push the two updated Astro files and documentation, and verify the live site. Independently verify supporting metric definitions, permissions, accessibility and source evidence.


## Fibra Engenharia — Commercial Development in Action (2026-10-25)

| ID | Date | Topic | Decision / direction | Status | Rationale / notes |
| --- | --- | --- | --- | --- | --- |
| D-104 | 2026-10-25 | Commercial Development chart, current version | **Accept the current “Commercial Development in Action” visualization as final for this iteration**, without further changes. Keep the **Strategic Account Development** and **New Customer Development** paths, structured around **Initial Solutions → Account Development → Business Expansion**. Preserve the current desktop horizontal and mobile vertical layouts. | Accepted (visual design) | User explicitly chose to finish with the existing version. This is not a new claim of build, commit, publication or accessibility verification. |
| D-105 | 2026-10-25 | Commercial Development chart, deferred review | **Record an optional future review** of chart clarity, mobile vertical length, flow routing, ribbon proportions, terminology and representation of commercial competencies (sales, business development, account management and bid/proposal). **Do not change the accepted chart now.** | Open (deferred) | Future refinement only, not a blocker for the current design. Revalidate historical claims before changing labels or relationships. |

**Interpretation note:** The graphic's ribbon widths indicate *illustrative relative commercial significance*, not financial values. Preserve the existing explanatory note and do not infer measured revenue shares from the flows.


## Fibra Engenharia — Commercial Growth Process relocation (2026-10-25)

| ID | Date | Topic | Decision / direction | Status | Rationale / notes |
| --- | --- | --- | --- | --- | --- |
| D-106 | 2026-10-25 | Commercial Growth Process placement | **Remove Commercial Growth Process from Fibra Experience and reserve it for the future Commercial Expertise area.** Keep **Commercial Development in Action** and **Distributed Solar Journey** in Fibra. | Accepted (architecture) | Fibra Experience should focus on specific achievements; Commercial Expertise should describe cross-career capabilities. Do not imply the four-stage process was a formal methodology institutionalized at Fibra. |
| D-107 | 2026-10-25 | Commercial Growth Process future integration | Preserve the existing four-stage content as a reference; inspect the actual Commercial Expertise layout before choosing its final placement, copy or presentation. | Accepted (deferred implementation) | Avoid duplication and premature redesign. No Commercial Expertise implementation or publication is implied. |

**Preserved process reference (not yet approved as final Commercial Expertise copy):**

1. **Market Opportunities:** Market Intelligence; Opportunity Identification; Customer Needs Assessment.
2. **Solution Development:** Solution Selling; Technical Feasibility; Financial & Payback Analysis.
3. **Commercial Execution:** Bid & Proposal Management; Cost Estimation & Pricing; Contract Negotiation.
4. **Business Expansion:** Key Account Management; Contract Expansion; Portfolio Diversification.

**Scope:** This decision approves relocation and removal from the Fibra component, not a redesigned process or a new page.

## Fibra Engenharia — Commercial Risk Management approval (2026-10-26)

| ID | Date | Topic | Decision / direction | Status | Rationale / notes |
| --- | --- | --- | --- | --- | --- |
| D-108 | 2026-10-26 | Fixed-price contract case-study layout | Approve **COMMERCIAL RISK MANAGEMENT / Protecting a Fixed-Price Contract** with three desktop columns: contract story; USD/BRL chart; Strategic Actions and Business Outcomes. | Accepted (visual design) | User explicitly approved the latest screenshot. Preserve approved composition and typography. |
| D-109 | 2026-10-26 | Currency chart styling and source | Use **USD/BRL EXCHANGE RATE**, monthly average **Jul 2014 – Jul 2015**, portfolio-blue line, blue **Proposal** (Aug 2014) and turquoise **Signed** (Dec 2014) markers with matching labels/guides, and muted **Planned delivery** shading. Cite **Banco Central do Brasil, SGS series 3698**, monthly average USD selling rate; clarify market context versus actual Fibra exposure. | Accepted (visual design and copy) | Replaces the earlier visually inconsistent green Signed marker; does not independently verify source data. |
| D-110 | 2026-10-26 | Commercial risk response and outcomes | Retain **Anticipated purchase orders** and **Imported through group companies** as Strategic Actions, and **Maintained margins** and **Delivered on schedule** as Business Outcomes. Retain contract story: August 2014 BRL-priced proposal, December signing at original fixed prices, US/Israel supplier negotiations and proactive procurement. | Accepted (case-study narrative) | Distinguish commercial response from exchange-rate chart, which is contextual rather than a measurement of realized exposure. |
| D-111 | 2026-10-26 | Design freeze and release verification | Treat the latest Commercial Risk Management card screenshot as the approved visual iteration; make no further changes unless requested. Verify build, component path, responsive/mobile QA, Git commit/push, live publication, data accuracy, accessibility and disclosure separately. | Accepted (visual iteration; release checks open) | Visual approval is not evidence of deployment or final technical QA. |


## Fibra Engenharia — People & Culture final approval (2026-10-26)

| ID | Date | Topic | Decision / direction | Status | Rationale / notes |
| --- | --- | --- | --- | --- | --- |
| D-112 | 2026-10-26 | Leadership scale and narrative | Approve **PEOPLE & CULTURE / Developing Teams and Building Lasting Relationships** with approximately **three project managers mentored** and **more than 50 multidisciplinary professionals coordinated through delegated leadership**. Retain autonomy, accountability, knowledge sharing and long-term professional relationships. | Accepted (content) | Distinguish indirect team coordination from direct line management; avoid implying 50 direct reports. |
| D-113 | 2026-10-26 | Three leadership pillars | Retain **Mentoring and Knowledge Sharing**, **Empowering Teams**, and **Long-Term Relationships**, with the approved concise descriptions; preserve the illustrative Fibra team image and **Illustrative image** disclosure. | Accepted (visual/content) | User approved the desktop and mobile layouts and the balanced text/card/image composition. |
| D-114 | 2026-10-26 | Long-Term Relationships icon | Replace unsuccessful handshake/link concepts with a **three-person circular network SVG**, using blue outlined figures and connecting arcs. Preserve the first two cards and icons. | Accepted (final visual iteration) | The corrected three-card component was visually reviewed on desktop and mobile and approved; the intermediate version that removed two cards is superseded and must not be reused. |
| D-115 | 2026-10-26 | Fibra Risk & People release boundary | Preserve the already approved **Commercial Risk Management** section unchanged while updating **People & Culture**. Treat visual/content approval as distinct from build, Git commit/push, public deployment and final accessibility/source QA. | Accepted (release scope) | Use `src/components/experience/fibra/FibraRiskPeople.astro` as the target path; final reviewed source provided as `FibraRiskPeople_RelationshipNetwork_v5_FIXED.astro`. |

**Approved People & Culture paragraph:**

> Developed and mentored approximately three project managers, coordinating multidisciplinary teams of more than 50 professionals through delegated leadership. Promoted autonomy, accountability, and knowledge sharing while building trusted professional relationships that extended beyond individual projects.

**Approved pillar descriptions:**

- **Mentoring and Knowledge Sharing:** Mentored project managers and shared practical experience to strengthen leadership capabilities.
- **Empowering Teams:** Delegated responsibilities across project teams, encouraging autonomy and accountability.
- **Long-Term Relationships:** Built trust and professional connections that continued beyond individual projects.


## Aton Engenharia — Forest Fire Monitoring case study (2026-10-27)

| ID | Date | Topic | Decision / direction | Status | Rationale / notes |
| --- | --- | --- | --- | --- | --- |
| D-116 | 2026-10-27 | Case-first Aton architecture | Develop **Forest Fire Monitoring** as a standalone representative case before expanding the full Aton Experience chapter. | Accepted | Case content can later inform a concise Aton career summary without duplicating the full narrative. |
| D-117 | 2026-10-27 | Case route and hero | Use `/cases/forest-fire-monitoring` with a responsive dark photographic hero: **Forest Fire Monitoring** / **From observation to a profitable business.** / **Product · Project · Commercial Management** / **Aton Engenharia · 2007–2012**. | Accepted (visual iteration) | Hero desktop/mobile visually reviewed; use `ForestCaseHero.astro`. Adapted panorama requires disclosure. |
| D-118 | 2026-10-27 | Business-scale indicators | Show **24 monitoring towers**, **+1,400 km² monitored**, **4 international corporate clients**. Name **Saint-Gobain, Gerdau, ArcelorMittal, WestRock** as the four client groups. | Accepted | Do not confuse corporate groups with individual installations or claim the metrics cover all Aton operations. Client-logo assets remain provisional until rights/accuracy verification. |
| D-119 | 2026-10-27 | Aton Experience entry point | Include a visually distinct **FEATURED CASE STUDY — Forest Fire Monitoring** card within the Aton Experience chapter, with the approved subtitle, three indicators and **Explore Case Study →** link. | Accepted (visual iteration) | User shared a desktop screenshot and accepted the card. Do not modify approved ABB or Fibra chapters. |
| D-120 | 2026-10-27 | Opportunity section layout | Use **The Opportunity — Seeing What Others Didn’t** with a three-part desktop composition: discovery narrative, historical conventional watchtower photo, and progression from human observation toward remote cameras and location estimation; stack on mobile. | Accepted (design direction) | Use the 2007 full-tower photo as primary; photographs were taken at a prospective customer's facilities, **not** at Veracel. Implementation and exact diagram labels remain to be reviewed. |
| D-121 | 2026-10-27 | Evidence and publication boundaries | Distinguish historical photographs from adapted/generated assets; describe the business model and discovery accurately; avoid unverified automated-detection, triangulation-accuracy, realized-payback or customer-permission claims. | Accepted (content integrity) | Hero background adapted from historical installation photo; verify client logos, publication permissions, data and captions before final release. Visual acceptance is not build/deployment confirmation. |

**Implementation/release status:** The hero and Aton Featured Case Study card are visually approved; no independent build, commit/push or live deployment confirmation is recorded here for the new case. The Opportunity remains the next implementation milestone.

## Aton Engenharia — Forest Fire Monitoring: progress and Business Model approval (2026-10-29)

| ID | Date | Topic | Decision / direction | Status | Rationale / notes |
| --- | --- | --- | --- | --- | --- |
| D-122 | 2026-10-29 | Opportunity and solution progress | **The Opportunity** and **From Idea to Solution** have progressed beyond the planning status recorded in D-120 and the earlier implementation-status note. Preserve the approved **ForestSolution.astro v12**; the compressed v13 was rejected. | Accepted (visual iterations) | Earlier notes describing The Opportunity as not implemented are historical and superseded by this progress update. |
| D-123 | 2026-10-29 | Business Model & Commercial Development | Approve **Section 03 — Business Model & Commercial Development**, **version 7**, for desktop and mobile. | Accepted (visual iteration) | Implemented locally through `ForestBusinessModel.astro` and changes to the case page, as evidenced by user-provided `git status`; production build, commit, push and deployment remain unverified. |

**Release scope:** Stage only `src/components/cases/forest-fire-monitoring/ForestBusinessModel.astro`, `src/pages/cases/forest-fire-monitoring.astro` and intentionally updated documentation for this commit. Do not include unrelated untracked scripts, `__pycache__` or Fibra logo images without separate review.


## Aton Engenharia — Forest Fire Monitoring: Sections 04–05 approval and updated release record (2026-10-29)

| ID | Date | Topic | Decision / direction | Status | Rationale / notes |
| --- | --- | --- | --- | --- | --- |
| D-124 | 2026-10-29 | Section 03 release | **Business Model & Commercial Development v7** was committed and pushed as **`97f8824`** (`feat: add forest monitoring business model and economics`); `npm run build` succeeded (six pages). | Accepted (committed/pushed) | Supersedes D-123's earlier pending-commit status. Live deployment not separately verified. |
| D-125 | 2026-10-29 | Section 04 Operational Footprint | Approve **24 Towers Across Brazil**: Brazil map with state borders and colored client markers, showing **four corporate groups**, **24 towers**, **approximately 1,400 km²** and **seven operations**. Legend: Saint-Gobain blue, Gerdau orange, ArcelorMittal red, WestRock green. | Accepted (content/visual design) | Seven operations are distinct from four client groups. Verify geographic markers against documented operation locations; screenshot coordinates are not authoritative. |
| D-126 | 2026-10-29 | Section 05 Business Impact | Approve **An Established Business**, with cards **4 Corporate clients**, **24 Towers operational**, **Profitable business** and narrative about profitability, recovered initial investment, customer expansion and Aton's continued forest-sector activity. | Accepted (content/visual design) | Do not equate Section 03's projected payback with actual recovered investment. Validate financial and present-day business assertions before final external disclosure. |
| D-127 | 2026-10-29 | Sections 04–05 release boundary | Keep Operational Footprint and Business Impact as separate sections; do not change approved Sections 01–03, ABB or Fibra. | Accepted (scope) | Approval is not proof of build, commit, push, deployment, source-data accuracy or image/logo permissions for Sections 04–05. |

**Current status:** Sections **01–05 are approved** for this case-study iteration. Section 03 is committed/pushed; Sections 04–05 still require independent implementation/release verification. Earlier notes stating Section 04 was unplanned are superseded.


## Forest Fire Monitoring — Industry Recognition and future Commercial Expertise (2026-10-29)

| ID | Date | Topic | Decision / direction | Status | Rationale / notes |
| --- | --- | --- | --- | --- | --- |
| D-128 | 2026-10-29 | Forest case publication checkpoint | Sections 01–05 were committed/pushed as `1907d76` and verified on the live site by the user. | Accepted (published) | Supersedes the earlier Sections 04–05 pending-release checkpoint; source-data and rights reviews remain independent. |
| D-129 | 2026-10-29 | Section 06 — Industry Recognition | Approve **Sharing Expertise Beyond Project Delivery** as a responsive 2007 / 2015 / 2017 / 2018 conference timeline; use historical photos for 2007, 2015 and 2018, with text only for 2017. | Accepted (visual/content) | Desktop and mobile screenshots approved; no Section 06 commit/push/live verification is implied. Emphasize knowledge sharing rather than commercial delivery. |
| D-130 | 2026-10-29 | Commercial Expertise cross-reference | During future **Commercial Expertise** development, evaluate referencing the conference and symposium appearances as evidence of technical authority, industry engagement and relationship-building, preferably with a link to the Forest Fire Monitoring case. | Accepted (future consideration; presentation open) | 2007 took place during Aton; 2015, 2017 and 2018 during Fibra. Participation was chiefly as a technical specialist; do not imply official Fibra commercial representation or attribute sales results to the events without evidence. Coordinate with D-106–D-107 and avoid repeating the full timeline. |

**Next release action:** Verify Section 06 build, intended assets and source diff; stage only relevant files and documentation, commit/push, and confirm the live page.


## Aton Engenharia Experience — Introduction (2026-10-30)

| ID | Date | Topic | Decision / direction | Status | Rationale / notes |
| --- | --- | --- | --- | --- | --- |
| D-131 | 2026-10-30 | Aton Experience architecture | Develop the Aton Experience incrementally, retaining the standalone Forest Fire Monitoring case. Chapter order: Introduction, Key Achievements, Project Footprint, Major Projects Timeline, Featured Case Studies, Other Selected Projects. | Accepted (structure) | Preserve ABB, Fibra and Telenge. Do not duplicate the full forest case study. |
| D-132 | 2026-10-30 | Aton Introduction | Approve **Engineering Solutions for Complex Challenges**, Aton logo, **Senior Project Manager — Sales & Solutions**, September 2003–January 2012, and five diagonal sector panels: Utilities, Telecom, Oil & Gas, Forestry, Mining. | Accepted (desktop/mobile visual design) | Layout, typography, hierarchy and responsiveness accepted. Do not redesign without a new request. |
| D-133 | 2026-10-30 | Introduction image follow-up | Defer improvement of the Utilities photo; verify reuse rights, attribution and disclosure for all five photographs. | Pending (asset quality/rights) | Visual approval does not establish permission to publish the photographs. |

**Release boundary:** The approved Introduction is not independently confirmed built, committed, pushed or deployed by this documentation update. Next design task: **Key Achievements**.


## Aton Engenharia Experience — Key Achievements (2026-10-30)

| ID | Date | Topic | Decision / direction | Status | Rationale / notes |
| --- | --- | --- | --- | --- | --- |
| D-134 | 2026-10-30 | Aton Key Achievements visual review | Accept the completed **Key Achievements** section on **desktop and mobile**. Preserve the reviewed metrics, wording, component and responsive presentation unless a subsequent change is explicitly requested. | Accepted (desktop/mobile visual design) | The approved screenshot/source is the reference for exact metric labels; this documentation checkpoint does not independently validate the final numbers or text. |
| D-135 | 2026-10-30 | Aton next design milestone | Proceed to **Project Footprint — Engineering Solutions Across Brazil**, with sector filters and locations grounded in historical project evidence. | Accepted (sequence / next task) | Do not modify the approved Introduction or Key Achievements while planning the map. |

**Release boundary:** Introduction and Key Achievements are visually approved. Verify exact files, production build, Git diff, commit/push, live deployment, source data and disclosure independently before marking them published.


## Aton Engenharia Experience — Project Footprint (2026-10-31)

| ID | Date | Topic | Decision / direction | Status | Rationale / notes |
| --- | --- | --- | --- | --- | --- |
| D-136 | 2026-10-31 | Aton Project Footprint v11 | Accept **Automation & Telecom Solutions Across Brazil** with responsive Brazil map and interactive **All sectors / Telecommunications / Utilities / Oil & Gas / Forestry / Mining** filters. Preserve approved desktop/mobile presentation. | Accepted (visual/content) | Final reviewed candidate `AtonProjectFootprint_v11.astro`; implementation target `src/components/experience/aton/AtonProjectFootprint.astro`, with `atonFootprintData.ts`. |
| D-137 | 2026-10-31 | Geographic representation | Telecommunications: **17 states** shaded; Utilities: **15 regions**; Oil & Gas: **20 regions + 3 offshore regions**; Forestry: **10 regions**; Mining: **4 locations**. Markers represent approximate geographic references, not exact sites or individual projects. Exclude Veracel Eunápolis from installed forestry operations. | Accepted (data framing) | Retain disclosure that locations may overlap and do not necessarily represent individual projects. Offshore points are illustrative. |
| D-138 | 2026-10-31 | Aton next milestone and release gate | Mark Project Footprint complete for this design iteration and proceed next to **Major Projects Timeline**. | Accepted (sequence) | Build, commit/push, deployment, external GeoJSON dependency, accessibility and disclosure checks remain separate; do not claim publication solely from visual approval. |


## Aton Engenharia Experience — Major Projects Timeline and PMO responsibility (2026-10-31)

| ID | Date | Topic | Decision / direction | Status | Rationale / notes |
| --- | --- | --- | --- | --- | --- |
| D-139 | 2026-10-31 | Major Projects Timeline design | Accept **MAJOR PROJECTS TIMELINE / Selected Projects & Initiatives** as a simplified responsive Gantt-style chart for 2003–2012 with six sector selections (All sectors and five industries), without the selected-project details panel. | Accepted (visual/interaction) | Desktop and mobile reviewed; user confirmed filters work. Latest reviewed iteration identified as v3. |
| D-140 | 2026-10-31 | Timeline historical scope | Include ten selected projects/initiatives; use **2007–2008** for Hydroelectric Power Plant Integration, **2007–2012** for Forest Fire Monitoring, and **2009–2012** for Oil & Gas Automation & Surveillance. Retain the historical-period and non-exhaustive-portfolio disclaimer. | Accepted (content) | Avoid interpreting broad initiative bars as exact individual contract dates; standalone forest case remains independent. |
| D-141 | 2026-10-31 | Aton portfolio governance | Record **2009–January 2012** responsibility for project governance across **all Aton automation and telecommunications projects**, beginning when taking over Oil & Gas Automation & Surveillance. | Accepted (historical responsibility) | Company portfolio-level PMO/governance scope, not solely the Oil & Gas project; incorporate into the professional evolution narrative, without changing the approved timeline chart. |
| D-142 | 2026-10-31 | Timeline release boundary and next section | Preserve approved Timeline v3; verify source/build/commit/push/live page independently. Proceed to Featured Case Studies and Other Selected Projects in separate design steps. | Accepted (sequence) | Visual approval is not proof of production release or accessibility/data/rights clearance. |


## MVP strategy and Aton Experience v1 completion (2026-10-31)

| ID | Date | Topic | Decision / direction | Status | Rationale / notes |
| --- | --- | --- | --- | --- | --- |
| D-143 | 2026-10-31 | Portfolio MVP / v1.0 scope | Prioritize a complete, coherent **professional portfolio MVP (v1.0)** over exhaustively documenting every historical project. Finish essential site pages and release QA before expanding optional project detail. | Accepted | Deliver a usable whole site first; additional case studies can be added incrementally after the MVP. This refines the initial Portfolio planning without canceling the long-term professional/technical vision. |
| D-144 | 2026-10-31 | Aton Experience v1 completion | Consider **Aton Engenharia Experience complete for the MVP** with five published sections: Introduction, Key Achievements, Project Footprint, Major Projects Timeline, and Featured Case Studies v3. The Featured card links to the published standalone Forest Fire Monitoring case. | Accepted (published; user verified) | Featured card v3 includes desktop/mobile vertical indicator dividers; user confirmed the published page works. No new Aton components required for v1.0; final site-wide accessibility, evidence, image rights and disclosure QA remain open. |
| D-145 | 2026-10-31 | Defer additional Aton projects | Move **Other Selected Projects** and additional detailed Aton case studies to **post-MVP / v2.0**, to be selected and added progressively as historical evidence becomes available. | Accepted (deferred) | Avoid duplicating Timeline content or blocking site completion. This supersedes D-131 and D-142 only as to the requirement to build Other Selected Projects during the initial release; earlier decisions remain historical. |
| D-146 | 2026-10-31 | Next Experience chapter | Develop **Telenge** next, in a separate conversation, using MVP scope: professional narrative, responsibilities and evidence-based highlights; no requirement to create individual project case studies now. | Accepted | Complete the fourth company chapter before revisiting optional enhancements. |

**Release interpretation:** Aton chapter is complete for MVP content and verified live by the user; this is not certification of full-site v1.0 release or of remaining accessibility, historical-source, copyright and confidentiality checks.


## Telenge Experience and four-company MVP milestone (2026-10-31)

| ID | Date | Topic | Decision / direction | Status | Rationale / notes |
| --- | --- | --- | --- | --- | --- |
| D-147 | 2026-10-31 | Telenge historical scope | Present **Engineering Manager, May 1997–September 2003**, with engineering and in-house team leadership, contract financial accountability, customers and bid/proposal involvement. | Accepted | Do not invent team sizes or imply formal job-title changes. |
| D-148 | 2026-10-31 | Telenge infrastructure evidence | Distinguish **310+ Bahia PSTN localities (Telemar/PAM)**, **4,250+ km optical network installations in Bahia**, **~600 km Salvador–Maceió buried fiber maintenance (Intelig; 24-hour restoration commitment)**, and **~3,500 km² Petrobras radio coverage in municipalities of BA/PE/RN/CE**. | Accepted | The optical installation metric excludes separate OPGW services; optical maintenance and restoration are one contract. No statewide radio-coverage claim. |
| D-149 | 2026-10-31 | Telenge final chapter structure | Retain **Introduction → Key Projects & Contracts → Project Footprint**. Remove **Infrastructure at Scale** to prevent repetition. | Accepted (MVP design) | Supersedes the earlier proposed four-section arrangement; no separate Telenge case study required for v1.0. |
| D-150 | 2026-10-31 | Telenge Project Footprint | Approve Northeast Brazil geographic visualization with **All Infrastructure** and four category selectors: **PSTN, Optical Networks, Optical Maintenance, Radio Communications**. | Accepted (visual/interaction) | Map points and routes are approximate references, not exact installations; do not imply complete state coverage or map undocumented OPGW locations. |
| D-151 | 2026-10-31 | Experience MVP completion | Mark **ABB, Fibra Engenharia, Aton Engenharia and Telenge Telecomunicações** chapters complete for MVP v1.0 content/design. Freeze further Experience refinements until requested. | Accepted | Site-wide v1.0 release, Git commit/push and final technical/evidence/rights QA are separate milestones and remain unverified here. |

**Release checkpoint:** Review the local Git working tree, run `npm run build`, commit/push intended code and these documentation changes, and verify GitHub Pages. Do not treat approval of screenshots as confirmation of a successful deployment.


## Home — MVP v1.0 final approval (2026-10-31)

| ID | Date | Topic | Decision / direction | Status | Rationale / notes |
| --- | --- | --- | --- | --- | --- |
| D-152 | 2026-10-31 | Home MVP completion | **Approve and close the current Home page for MVP v1.0**, preserving its existing content, section composition and executive visual direction. | Accepted (content/visual design) | User explicitly confirmed final approval; no further Home redesign unless requested. |
| D-153 | 2026-10-31 | Home PMP® seal and responsiveness | Retain the **PMP® badge/seal** and the approved desktop/mobile responsive refinements as part of the Home baseline. | Accepted (visual design) | Preserve the final reviewed version; no unrequested changes to badge or responsive layout. |
| D-154 | 2026-10-31 | Home metrics and release boundary | Keep the four existing **Key Achievements** indicators unchanged pending any separately approved evidence review. Distinguish Home design acceptance from build, commit/push, live deployment and final site-wide QA. | Accepted (scope/release boundary) | D-097 remains an optional pending verification/review, not authorization to replace published values. |

**Next release action:** Update the three project documents in the local repository, inspect `git status` and `git diff`, run `npm run build`, stage intended Home/documentation files, commit and push to `main`, then verify GitHub Pages. These actions are **not** claimed as completed by this log entry.
