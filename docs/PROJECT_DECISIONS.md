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

**Confirmed Key Achievements (D-019):** 25+ Years; 7 Countries; 100+ Stakeholders; 6+ Industries. Labels and numerical scope must be validated before publishing. In particular, the 100+ stakeholder figure is associated with ABB projects, not the whole career.

**Confirmed Home expertise (D-020, D-023):** First **Project & Program Management**, then **Commercial Leadership**. These are the only two initial Home pillars. Data Science & Analytics is deferred for later evaluation; it can still be included in technical Portfolio work.

**Approved expertise card copy (D-021), in presentation order:**

**Project & Program Management** — *Delivering Complex Projects. Creating Business Value.*

> Leading complex engineering projects and multidisciplinary teams, aligning stakeholders and managing risks to deliver reliable solutions, meet customer expectations and achieve business objectives.

**Commercial Leadership** — *Turning Customer Challenges into Business Opportunities*

> Building trusted customer relationships, identifying opportunities and developing tailored engineering solutions that drive business growth and deliver lasting value.

**Implementation approach (D-022):** Begin developing the site with Astro before finalizing Featured Work. Build and review one section at a time. The Astro development environment is now operational; Header and Hero have been separated into components, with shared styles in `src/styles/global.css`. Next: extract Expertise and implement BaseLayout.

**Career Insights to investigate:** a portfolio-value evolution chart (using comparable, clearly defined measures), a team-leadership evolution chart (distinguishing direct/indirect management from stakeholder coordination), and a stakeholder engagement radar chart (dimensions and defensible scoring methodology still to be defined). Industry coverage may be shown visually with sector icons. Verify accuracy and confidentiality before publication.

### Experience versus Portfolio

Proposed distinction: **Experience** explains career progression and responsibilities; **Portfolio** provides deeper evidence through selected project case studies. Avoid duplicating the same information verbatim.

## Open decisions / next discussion

1. Confirm the final five-page navigation or revise it (Home section structure is already accepted).
2. Determine where the approved Home expertise cards link (Experience, Portfolio, or filtered views).
3. Reevaluate Data Science & Analytics as a possible third Home expertise area in a later release; individual technical Portfolio projects remain possible.
4. Confirm language(s) and whether multilingual support is needed from the outset.
5. Confirm the final hero photograph asset and image usage/permission policy (overall visual direction is accepted in D-016).
6. Validate Key Achievements (25+ Years, 7 Countries, 100+ Stakeholders, 6+ Industries), including source, scope, and confidentiality; select first-release projects later, after the initial Home is implemented.
7. Define comparable data and formats for portfolio evolution, team leadership, and stakeholder radar charts; distinguish team management from stakeholder coordination.
8. Evaluate proposed visual storytelling elements: origins and dual citizenship, places lived, Brazil regional activity map, global ABB/data-center project map, selected clients, technologies, multicultural greetings, and project-methodology chart (Waterfall/Agile/Hybrid). Confirm accuracy, permissions, and confidentiality before publication.

## Change management

When a decision is confirmed or revised:

1. Add or update an entry with the date, status, and reason.
2. Mark replaced decisions **Superseded** rather than silently erasing them.
3. Update `PROJECT_CONTEXT.md` if the change affects the overall vision or architecture.
4. Commit both files to Git alongside the relevant changes.
