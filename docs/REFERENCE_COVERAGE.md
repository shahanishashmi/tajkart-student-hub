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

The attachment folder contained the ZIP and prompt text but no accompanying screenshot, so the audit does not infer layout details from a missing image. The complete source-to-destination record, file counts, statuses, and remaining work are in the machine-readable [reference category map]({{ '/data/reference_coverage.yml' | relative_url }}). Per-language source index membership and Tajkart content status for all **57 locale records** are in the [language coverage map]({{ '/data/language_coverage.yml' | relative_url }}). The maps are deliberately separate: the source language-index codes describe archive files, while Tajkart `language` metadata uses standard tags such as `en`, `hi`, and `ur`.

## Content taxonomy coverage

| Inspected reference area | Tajkart destination | Current Tajkart coverage |
|---|---|---|
| Books indexed by programming language and subject; localized book lists | [Reading guides]({{ '/learning/books/' | relative_url }}) and [language paths]({{ '/learning/languages/' | relative_url }}) | Twelve original subject reading guides and eleven introductory programming-language paths. No third-party book list is reproduced. |
| Courses grouped across languages and technical topics | [Courses and study plans]({{ '/learning/courses/' | relative_url }}) | Three original self-guided plans with modules, assignments, checks, project work, rubrics, and completion criteria. No external course catalogue. |
| Podcasts and screencasts | [Active viewing guide]({{ '/learning/podcasts-screencasts/' | relative_url }}) | Original practice and note-taking method plus a schema for future verified metadata; no channels or episodes are listed. |
| Interactive programming tutorials | [Interactive learning]({{ '/learning/interactive-tutorials/' | relative_url }}) | An active practice routine and a four-question browser quiz. No arbitrary code execution. |
| Programming playgrounds | [Playground guide]({{ '/learning/playgrounds/' | relative_url }}) and [project briefs]({{ '/learning/projects/' | relative_url }}) | Safety guidance and six reproducible project specifications; no third-party directory or server-side execution. |
| Cheatsheets | [Original quick references]({{ '/learning/cheatsheets/' | relative_url }}) | Ten Tajkart-authored references covering languages, Git/CLI, SQL, web, data structures, testing, security, and deployment. |
| Problem sets and competitive programming | [Programming practice set]({{ '/learning/problem-sets/' | relative_url }}) | Nine original tasks span arrays, strings, hashing, search, sorting, recursion, trees, graphs, and SQL; canonical solutions are tested. No contest or ranking catalogue. |
| Programming language and framework topics | [Programming language paths]({{ '/learning/languages/' | relative_url }}) | Eleven beginner paths plus six lessons with tested Python examples. Other paths remain introductory roadmaps, not full language courses. |
| Computer science and software subject index (46 subject entries; 47 headings including Index) | [Expanded subject map]({{ '/learning/subjects/' | relative_url }}) | Every subject entry is mapped into seven learner-facing strands below. This is a roadmap, not a claim of completed courses for every subject. |
| IDEs and developer tools | [Git lesson]({{ '/learning/lessons/git-small-commits/' | relative_url }}) and [subject map]({{ '/learning/subjects/' | relative_url }}) | Focused Git introduction and tool topics; no general product directory. |
| Search and resource discovery | README links to language/subject indexes and an external search site. | Local, Liquid-generated search index over Tajkart pages; all-token matching, relevance ranking, type/category/language/difficulty/provenance filters, and visible source/review status. 70 source resources are indexed. |
| Multilingual indexes and translations | Locale-specific book, course, cast, interactive, playground, and contributor-document lists. | 57 source locale records are tracked independently by content type. Tajkart has one Hindi and one Urdu translation draft; both await fluent review. |
| Professional development | [Career Hub]({{ '/careers/' | relative_url }}) | Five original guides cover resumes, portfolios, interviews, internship preparation, professional email, and entry-level learning paths. No active jobs are listed. |
| Scholarships, internships, student deals | [Student Offers]({{ '/offers/' | relative_url }}) | Verification and disclosure policy; no active offer listings. These are Tajkart additions, not reference categories. |
| Contribution guides and templates | Contribution/CLA guidance, onboarding, code of conduct, issue and PR conventions, and translated docs. | Tajkart contribution/editorial docs, code of conduct, issue forms, PR template, and lesson template. Explicit contributor reuse permission remains an open decision. |
| Automated validation and repository workflows | Seven workflows, URL checks, list/RTL linting, PR reporting, issue labels, conflict detection, stale handling, and a custom RTL/LTR script. | One SHA-pinned Pages workflow runs source checks, Python and Node tests, front-matter parsing, Jekyll build, generated HTML checks, and deployment with job-scoped permissions. CI has not yet run on this local batch; matching local checks pass. |

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
| Navigation and discovery | Large README links to language/subject lists and an external dynamic search site; static pages are generated from Markdown. | Responsive site navigation, a Liquid-generated search index, client-side filters, and internal subject/format pages. |
| Content conventions | Alphabetized Markdown resource entries, attribution/creator and format/access notes, authoritative links, license checks, and genre-specific inclusion rules. | Original lesson standards, worked examples, practice/hints, source checks for time-sensitive statements, and no external catalogue without separate review. |
| Contributor documentation | Contribution agreement, contribution guide, onboarding guide, code of conduct, and many translations. | Tajkart contribution guide, content standards, content schema, editorial review, copyright policy, code of conduct, issue forms, PR template, and translation checklist. Hindi and Urdu translations are drafts pending fluent review. |
| Scripts | RTL/LTR Markdown linter plus a language/marker configuration. | Source validator checks metadata, unique IDs/routes, prerequisites, Python snippets, and local Markdown links. A generated HTML checker verifies links, search index, landmarks, labels, IDs, and image alt attributes in CI. |
| Automation | Seven workflows cover list linting, changed-file URL checks, RTL/LTR linting, PR reports/comments, merge conflicts, issue pin labels, and stale PRs; a local composite action formats URL-check reports. | Tajkart's own workflow runs route/schema checks, solution tests, JavaScript syntax checks, YAML parsing, Jekyll build, generated HTML checks, then deploys only `main` to Pages. Third-party actions are SHA-pinned and Dependabot checks action and Bundler updates. No reference workflow code was copied. |
| Action security | The snapshot uses version tags such as `actions/checkout@v7`, `tj-actions/changed-files@v46`, and write-enabled issue/PR/stale automations; refs are not full SHA pins throughout. | Build has read-only contents permission. Only the main-branch deploy job receives `pages: write` and `id-token: write`; unnecessary issue/PR automation is omitted. |

## Coverage limits and remaining work

The taxonomy check is complete for the inspected snapshot: all 46 subject entries (47 headings including Index), source format counts, and 57 locale records are mapped. Current metadata identifies 70 searchable resources: 68 in English and two draft translations. The repository contains six lessons, 12 subject guides, 11 language paths, three courses, ten cheatsheets, nine detailed problems, six project briefs, two interactive resources, five career guides, and verified-resource guidance. This is an authored first library, not a complete treatment of every mapped subject or language. Technical review, fluent Hindi/Urdu review, intermediate and advanced curricula, project implementations, manual accessibility review, and verified third-party resource listings remain open work.

The local source validator, unit tests, production Jekyll build, and generated-HTML checks pass. The current published site remains the last deployed revision until a reviewed change is pushed and CI succeeds. See the [full audit]({{ '/docs/REFERENCE_AUDIT/' | relative_url }}), [architecture]({{ '/docs/ARCHITECTURE/' | relative_url }}), and [licensing review]({{ '/docs/LICENSING_REVIEW/' | relative_url }}).

The archive was an architecture and taxonomy reference only. If Tajkart later links or quotes an external work, document its source and applicable rights separately; the upstream CC BY 4.0 notice does not transfer ownership of third-party works linked from its lists.
