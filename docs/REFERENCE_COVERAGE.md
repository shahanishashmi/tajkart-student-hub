---
layout: page
title: Reference coverage audit
description: How the proposed reference archive informs Tajkart's original information architecture.
permalink: /docs/REFERENCE_COVERAGE/
---

## Audit scope and source snapshot

The reference supplied for this rebuild, `free-programming-books-main.zip`, was inspected on 2026-10-14. Its SHA-256 is `a57382573afb96eed8623f41884e049b12b9fab54dcf43815629437906abd1e`; the ZIP does not contain Git metadata. Its upstream repository reference is pinned here to the official [EbookFoundation/free-programming-books snapshot](https://github.com/EbookFoundation/free-programming-books/tree/2574d859ecf34dd8d1643cc5c7c9f11ae99f845c), branch `main`, commit `2574d859ecf34dd8d1643cc5c7c9f11ae99f845c`. The archive was listed and its relevant Markdown/config/license files were read without executing its scripts or importing its resource lists or implementation. It has top-level `books` (48 Markdown files), `courses` (41), `casts` (21), `more` (10), `docs` (94), `scripts` (2), `.github` (10), and `_includes` (1), plus root configuration, README, license, and favicon.

Its README divides resources into six formats: books, courses, interactive tutorials, playgrounds, podcasts/screencasts, and problem sets/competitive programming. It also links cheatsheets and indexes books by programming language, subject, and translated editions. The English subject index has 46 subject entries and 47 level-three headings including its `Index` heading. The archive has 48 Markdown files under `books`, 41 under `courses`, and 21 under `casts`, including its indexes and multilingual lists. Resource entries point to third-party works; the archive is primarily a curated directory, not a set of textbooks bundled in the ZIP.

The upstream README states that repository files are licensed under **Creative Commons Attribution 4.0 International (CC BY 4.0)**, matching its [LICENSE](https://github.com/EbookFoundation/free-programming-books/blob/2574d859ecf34dd8d1643cc5c7c9f11ae99f845c/LICENSE). Attribution for the source taxonomy labels reproduced in the comparison below: *Free Programming Books*, Free Ebook Foundation, CC BY 4.0, [source snapshot](https://github.com/EbookFoundation/free-programming-books/tree/2574d859ecf34dd8d1643cc5c7c9f11ae99f845c). The headings are grouped and adapted to compare coverage; no linked resource entries, descriptions, prose, code, branding, templates, or workflow implementations are included. The archive license does not grant rights to the separate books, courses, websites, or other works linked from those lists. Read [Tajkart copyright guidance]({{ '/copyright/' | relative_url }}) for this project's rights boundary.

## Content taxonomy coverage

| Inspected reference area | Tajkart destination | Current Tajkart coverage |
|---|---|---|
| Books indexed by programming language and subject; localized book lists | [Reading guides]({{ '/learning/books/' | relative_url }}) and [language paths]({{ '/learning/languages/' | relative_url }}) | Original reading method and language selection advice. No third-party book list and no translated library yet. |
| Courses grouped across languages and technical topics | [Four-week foundations plan]({{ '/learning/courses/' | relative_url }}) | One original, non-accredited self-study plan; no external course catalogue. |
| Podcasts and screencasts | [Active viewing guide]({{ '/learning/podcasts-screencasts/' | relative_url }}) | Original study method; no channel or episode listings. |
| Interactive programming tutorials | [Interactive learning]({{ '/learning/interactive-tutorials/' | relative_url }}) | Predict-run-observe-change routine and an original answer-checking loop exercise. |
| Programming playgrounds | [Playground guide]({{ '/learning/playgrounds/' | relative_url }}) | Safe experiment guidance; no embedded code execution or third-party playground directory. |
| Cheatsheets | [Python starter reference]({{ '/learning/cheatsheets/' | relative_url }}) | One original Python quick reference. |
| Problem sets and competitive programming | [Programming practice set]({{ '/learning/problem-sets/' | relative_url }}) | Five original introductory exercises with hints/answers; no competitive-programming catalogue yet. |
| Programming language and framework topics | [Programming language paths]({{ '/learning/languages/' | relative_url }}) | Original choice guidance and beginner material; lessons currently cover Python, not every indexed language. |
| Computer science and software subject index (46 subject entries; 47 headings including Index) | [Expanded subject map]({{ '/learning/subjects/' | relative_url }}) | Every subject entry is mapped into seven learner-facing strands below. This is a roadmap, not a claim of completed courses for every subject. |
| IDEs and developer tools | [Git lesson]({{ '/learning/lessons/git-small-commits/' | relative_url }}) and [subject map]({{ '/learning/subjects/' | relative_url }}) | Focused Git introduction and tool topics; no general product directory. |
| Professional development | [Career Hub]({{ '/careers/' | relative_url }}) | Original resume/portfolio and interview guides, project communication, and opportunity-safety guidance. No active jobs are listed. |
| Scholarships, internships, student deals | [Student Offers]({{ '/offers/' | relative_url }}) | Verification and disclosure policy; no active offer listings. These are Tajkart additions, not reference categories. |

### All 46 subject entries, grouped for Tajkart navigation

| Tajkart strand | Reference subject entries mapped |
|---|---|
| Theory and foundations | 0 - Meta-Lists; Algorithms & Data Structures; Computer Science; Compiler Design; Computer Organization and Architecture; Mathematics; Regular Expressions; Standards; Theoretical Computer Science |
| Languages and paradigms | Object Oriented Programming; Partial Evaluation; Programming; Programming Paradigms; Workflow |
| Data and intelligent systems | Artificial Intelligence; Computer Vision; Data Science; Database; Information Retrieval; Machine Learning; Search Engines; Quantum Computing |
| Systems and infrastructure | Cloud Computing; Containers; Embedded Systems; Networking; Operating Systems; Parallel Programming; Web Services |
| Software practice | IDE and editors; Licensing; Open Source Ecosystem; Professional Development; Software Architecture; Version Control Systems; Web Performance |
| Safety and resilience | Reverse Engineering; Security & Privacy |
| Applications and emerging fields | Blockchain; Cellular Automata; Competitive Programming; Game Development; Graphics Programming; Graphical User Interfaces; Misc; Prompt Engineering |

## Website architecture and engineering practices

| Reference area | Observed design | Tajkart equivalent / decision |
|---|---|---|
| Static website | Jekyll, Minimal remote theme, Kramdown, `jekyll-remote-theme`, `jemoji`, and `jekyll-relative-links`; includes a favicon and custom head partial. | GitHub Pages-compatible Jekyll with Tajkart-owned layouts, CSS, SVG favicon, SEO metadata, stable permalinks, and configured project `baseurl`. |
| Navigation and discovery | Large README links to language/subject lists and an external dynamic search site; static pages are generated from Markdown. | Responsive site navigation, searchable lesson index, topic filter, and internal subject/format pages. |
| Content conventions | Alphabetized Markdown resource entries, attribution/creator and format/access notes, authoritative links, license checks, and genre-specific inclusion rules. | Original lesson standards, worked examples, practice/hints, source checks for time-sensitive statements, and no external catalogue without separate review. |
| Contributor documentation | Contribution agreement, contribution guide, onboarding guide, code of conduct, and many translations. | Tajkart contribution guide, content standards, copyright guide, roadmap, and templates. Translations and a learner review process remain future work. |
| Scripts | RTL/LTR Markdown linter plus a language/marker configuration. | Dependency-free site validator for metadata, Python example syntax, routes, and local Markdown links. No RTL linter is needed until Tajkart publishes RTL material. |
| Automation | Seven workflows cover list linting, changed-file URL checks, RTL/LTR linting, PR reports/comments, merge conflicts, issue pin labels, and stale PRs; a local composite action formats URL-check reports. | Tajkart's own build-and-deploy workflow runs content/link/code checks and Jekyll builds on pull requests; it deploys only `main` to Pages. Third-party actions are pinned to full commit SHAs and Dependabot checks action and Bundler updates. No reference workflow code was copied. |
| Action security | The snapshot uses version tags such as `actions/checkout@v7`, `tj-actions/changed-files@v46`, and write-enabled issue/PR/stale automations; refs are not full SHA pins throughout. | Build has read-only contents permission. Only the main-branch deploy job receives `pages: write` and `id-token: write`; unnecessary issue/PR automation is omitted. |

## Coverage limits and remaining work

The taxonomy check is complete for the inspected snapshot: all 46 subject entries (47 headings including Index) and each top-level resource format have been accounted for above. Tajkart's authored library remains intentionally smaller: one four-week plan, four lessons, one cheatsheet, one five-question set, and original guidance pages. The topic map is not a claim that every subject has a course. Language translations, a fuller language-specific lesson collection, external resource listings, more problem sets, and a formal accessibility review remain open roadmap items.

The archive was an architecture and taxonomy reference only. If Tajkart later links or quotes an external work, document its source and applicable rights separately; the upstream CC BY 4.0 notice does not transfer ownership of third-party works linked from its lists.
