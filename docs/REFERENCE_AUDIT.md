---
layout: page
title: Repository and reference audit
description: Findings from the Tajkart working-tree review and the supplied Free Programming Books snapshot.
permalink: /docs/REFERENCE_AUDIT/
---

## Scope and evidence

This audit records the repository and reference archive reviewed on 2026-10-14. The local project is `D:\Projects\tajkart-student-hub`; the supplied archive is `D:\GITHUB PUBLIC HELP\free-programming-books-main.zip`. The archive SHA-256 is `a57382573afb96eed8623f41884e049b12b9fab54dcf43815629437906abd1e`. It has no Git metadata, so its upstream identity is cross-referenced to the official [EbookFoundation/free-programming-books snapshot at commit `2574d859ecf34dd8d1643cc5c7c9f11ae99f845c`](https://github.com/EbookFoundation/free-programming-books/tree/2574d859ecf34dd8d1643cc5c7c9f11ae99f845c).

The ZIP was read as data only. Its scripts, GitHub Actions, and source entries were not executed or copied. The two screenshots supplied in this conversation were inspected: the README screenshot shows the source repository's resource categories; the deployment screenshot shows an older failed PR deployment among later successful deployments. The upstream README and LICENSE were also checked at the pinned commit; see the [official README](https://github.com/EbookFoundation/free-programming-books/blob/2574d859ecf34dd8d1643cc5c7c9f11ae99f845c/README.md) and [LICENSE](https://github.com/EbookFoundation/free-programming-books/blob/2574d859ecf34dd8d1643cc5c7c9f11ae99f845c/LICENSE).

## Tajkart repository state

| Check | Observation |
|---|---|
| Branch and baseline | Branch `main`, at `7b63a7d` (`Build Tajkart Student Hub learning site`); this was the same commit as `origin/main` when inspected. The preceding history includes the repository merge and foundation commits. |
| Remote | `origin` is `https://github.com/shahanishashmi/tajkart-student-hub.git`. |
| Working tree | Not clean: 47 tracked files are modified and 61 untracked paths are shown by `git status` (those paths contain 93 untracked files; 108 status entries total; none staged). This is a larger batch than the 26-file estimate in the release prompt. No reset or cleanup was used. This audit and implementation remain local and uncommitted. |
| Static site | Jekyll with the GitHub Pages gem bundle, Kramdown, custom Tajkart layouts, and GitHub Pages deployment. `_config.yml` sets the project URL and `/tajkart-student-hub` base path. |
| Content | Markdown pages organized by learning format, language, subject, project, career, and opportunity guidance. Search metadata is YAML front matter; the locale and reference maps live under `data/`. |
| Discovery | A Liquid-generated `/search-index.json` is built from pages marked `searchable: true`; browser JavaScript filters the resulting local index. |
| Quality workflow | `.github/workflows/pages.yml` validates source content, tests Python solutions and search behavior, checks JavaScript and YAML/front matter, builds Jekyll, validates generated HTML, and deploys successful `main` builds. The deploy job has the Pages permissions it needs; build checks are read-only. |
| Existing rights notice | `LICENSE` is a project-specific all-rights-reserved notice for original Tajkart-authored content, not a permissive open-source grant. It was inspected and left unchanged. |

The current source inventory, architecture decisions, implementation coverage, and rights notes are detailed in [Architecture]({{ '/docs/ARCHITECTURE/' | relative_url }}), [Reference coverage]({{ '/docs/REFERENCE_COVERAGE/' | relative_url }}), and [Licensing review]({{ '/docs/LICENSING_REVIEW/' | relative_url }}).

## Reference repository structure

The ZIP contains 245 members including directory entries. Its principal Markdown collections are `books` (48 files), `courses` (41), `casts` (21), `more` (10), and `docs` (94). It also contains ten `.github` files, two scripts, one include, the root README, Jekyll configuration, LICENSE, and favicon. The README groups material into books, cheatsheets, courses, interactive programming resources, problem sets/competitive programming, podcasts/screencasts, and programming playgrounds. Books are indexed by language and subject and include localized lists; courses, casts, and other lists have their own language variants. The inspected subject index has 46 subject entries (47 level-three headings including its `Index` heading). The archive locale codes and per-category membership are recorded in [the language coverage map]({{ '/data/language_coverage.yml' | relative_url }}).

The reference also documents contributor onboarding and list-format rules, a code of conduct and translated variants, and automation for URL checks, list linting, RTL/LTR review, pull-request reporting, merge-conflict detection, issue labels, and stale items. Its Jekyll configuration uses a remote Minimal theme and plugins for emoji and relative links; its README points to a separate search website. Tajkart uses the categories and maintenance needs as requirements, while keeping its own design, implementation, and static search.

## Live GitHub and deployment cross-check

The supplied repository URL and screenshots were checked against GitHub's public API on 2026-10-14. The default branch is `main`, and its current head is still `2574d859ecf34dd8d1643cc5c7c9f11ae99f845c`, the same commit as the ZIP's recorded upstream snapshot. The repository reported 399,021 stars and 66,939 forks at that check; those counts change over time. The current GitHub tree has the same principal folders: `.github`, `_includes`, `books`, `casts`, `courses`, `docs`, `more`, and `scripts`. The current public Pages home page is reachable at [ebookfoundation.github.io/free-programming-books](https://ebookfoundation.github.io/free-programming-books/); the linked [search app](https://ebookfoundation.github.io/free-programming-books-search/) is a separate JavaScript application.

The deployment screenshot shows 5,538 deployment records and includes an older failed deployment for “Add AIBook to Artificial Intelligence” (PR #13517). The newest GitHub Pages deployment returned `success` for `main` at the audited head commit on 2026-10-12. This is a historical failure followed by later successful deployments, not evidence that the latest published revision is failing. Deployment records should not be confused with distinct source changes or current build failures.

There are seven checked-in workflow YAML files under `.github/workflows` in the pinned tree. GitHub's Actions API displayed twelve workflow entries at the same time, including Copilot/Dependabot and Pages entries with `dynamic/...` paths, plus an `Auto Label Issues and PRs` entry pointing to `label.yml`, which is absent from the pinned Git tree. The file tree is the reliable inventory of versioned workflow code; the Actions tab can also expose service-managed or historical workflow records. Tajkart's coverage table counts checked-in source workflows, not the Actions UI records.

## Tajkart production-readiness run

The current project is Jekyll/GitHub Pages, not a Node build: `package.json` is absent; `Gemfile` pins `github-pages` 232. The initial local build command could not start because Ruby/Bundler were missing. RubyInstaller Ruby 3.3.12 with MSYS2/Devkit was then installed through WinGet to match CI's Ruby 3.3 line. `bundle install --jobs 4 --retry 3` resolved 100 gems, and `Gemfile.lock` now records both `x64-mingw-ucrt` and `x86_64-linux` platforms for Windows and Actions. The exact Windows setup commands are in [Build and deploy]({{ '/docs/DEPLOYMENT/' | relative_url }}).

| Check | Result on this local worktree |
|---|---|
| `python scripts/validate_site.py` | Pass: 112 Markdown files, 99 routes, 70 searchable resources; zero missing titles/required fields, duplicate resource IDs/routes, invalid curated source URLs, unknown references, Python syntax errors, or broken local Markdown links. |
| Resource metadata | 70 search entries with complete required search fields and unique IDs: 68 original English resources and 2 translations; 0 third-party resource entries and 0 external learning links in `learning/`, `careers/`, or `offers/`. The translation drafts reference original ID `python-variables-001`, with draft/pending status. |
| `python -m unittest discover -s tests -v` | Pass: 16 tests (8 Python exercise solutions, 7 provenance/rights metadata checks, and 1 SQLite SQL example). |
| `node --check assets/js/site.js`; `node --check tests/search_test.js`; `node tests/search_test.js` | Pass: syntax checks and focused browser-DOM harness for all-token matching, exact-title relevance, original/translation/external filtering, external attribution, draft labeling, and no-results state. |
| `ruby scripts/validate_front_matter.rb` | Pass: 102 Markdown front-matter blocks and 5 YAML configuration/inventory files parsed. |
| `bundle exec jekyll build` (`JEKYLL_ENV=production`) | Pass on Ruby 3.3.12; generated 99 HTML routes and a 70-entry search index. Logs contain a non-blocking notice about optional Faraday v2 retry middleware. |
| `python scripts/validate_html.py _site` | Pass against actual Jekyll output: 99 pages; internal links and fragments, unique IDs, labelled controls, language/landmarks, and search provenance metadata are valid. |
| `git diff --check` | Pass; only Git's existing LF-to-CRLF working-copy notices were reported. |

The first generated-output check surfaced unlabeled disabled checkboxes in the editorial checklist/roadmap and an extensionless static-file detection bug for the license page. The checklists now use readable status text, and the generated-site checker recognizes extensionless files. The final build and output validation pass after those fixes. Search now ranks title matches ahead of tags and summaries; source/review status is visible and filterable. Empty, loading, and fetch-error states are present in the search UI.

Rights review found no third-party learning-resource records to attribute or verify; the schema and validator require verified status, creator, HTTP(S) source URL, source-check date, attribution, rights note/state, and named terms for licensed material before future external entries can be searchable. No repository prose, code, curated entries, or translations were copied from the reference. The Hindi/Urdu translation bodies were not rewritten; only provenance metadata was added. This automated check is not a human originality review.

## Release gate closure (2026-10-14)

| Gate | Evidence and result | Status |
|---|---|---|
| Local CI-equivalent checks | The commands and results above were run on this worktree. Local runtimes were Python 3.14.6, Node 24.19.0, and Ruby 3.3.12; the Pages workflow selects Python 3.12, Node 24, and Ruby 3.3. | Local pass; GitHub-hosted Actions pending. Python was newer than the workflow runtime, so hosted CI remains necessary. The current worktree is uncommitted; no push, dispatch, or deployment was performed. |
| External URL crawl | A sequential standard-library crawl scanned repository Markdown, YAML, JSON, HTML, CSS, JavaScript, and `Gemfile` URLs; 18 unique non-test URLs were checked with an 8-second timeout, one retry, 0.5-second spacing, redirect tracking capped at eight, and a one-byte-range GET fallback when HEAD was blocked. All 18 returned HTTP 200 after redirect handling; three redirected. There were 0 HTTP failures, blocked responses, timeouts, or network failures. The subsequent deployment diagnosis added three unique official GitHub documentation URLs; a separate sequential HEAD check used an 8-second timeout and 0.5-second spacing, and all three returned HTTP 200 with no redirects. This gives 21 checked unique URLs across the two bounded checks. These URLs are repository/reference/tooling citations, not a catalogue of learning resources; `learning/`, `careers/`, and `offers/` contain no third-party learning links. | Reachability pass for these URLs on this date; time-sensitive destinations still need a human source/content check. |
| Accessibility | `python scripts/validate_html.py _site` passed its structural checks for language attributes, one main landmark, heading-level jumps, duplicate IDs, image alt attributes, labelled form controls, local links/fragments, and search metadata. Code inspection found visible keyboard focus styles, a skip link, responsive layout rules, reduced-motion handling, labels and live status text for search, and `aria-expanded` state for the mobile menu. WCAG contrast-ratio spot checks of key CSS pairs measured 13.99:1 for body ink, 5.64:1 for muted text on the paper background, 7.00:1 for dark teal links, 7.30:1 for white button text, 4.92:1 for the white brand mark, and 3.30:1 for the focus outline against the soft panel. No Lighthouse, axe, or pa11y CLI or browser executable was found via PowerShell command lookup. | Automated structure, selected palette measurements, and code inspection pass; full-page contrast, keyboard operation, screen-reader behavior, zoom/reflow, and phone/tablet review remain human checks. |
| Jekyll routes, search, and assets | The production build generated 99 HTML routes and a 70-entry local search index. The generated-output validator resolved internal links and fragments. A separate read-only scan checked all 1,780 local `href`/`src` references across generated pages, including stylesheets, scripts, icons, and page routes; there were no missing targets or base-path mismatches. `_config.yml` currently targets `https://shahanishashmi.github.io` with `/tajkart-student-hub`; generated paths use `relative_url`. There is no checked-in `CNAME`. | Local candidate paths pass. GitHub Pages settings and the target for the next deployment are not confirmed. |
| Published endpoint probe | On 2026-10-14, `https://shahanishashmi.github.io/tajkart-student-hub/` returned 200 only after redirecting to `http://shahanishashmi.me/tajkart-student-hub/`. Direct HTTPS to that custom-domain route failed certificate hostname validation. The public GitHub Pages API endpoint returned 404. The redirected site's canonical tag still names the `github.io` URL; its CSS and JavaScript returned 200 over HTTP, while `/tajkart-student-hub/search-index.json` returned 404. This is the previously published revision, not the current local candidate. | Blocker: confirm repository Pages/custom-domain settings, repair HTTPS/TLS for the actual target, and align the canonical `url`/`baseurl` with that target before treating deployment as verified. Do not infer a current candidate deployment from the older published page. |
| Human content and rights review | No outside learning resources are currently listed. All searchable original content remains marked drafted/pending; the two Hindi/Urdu translations remain draft/pending. The code and examples have automated tests, but those tests are not an expert review. | Pending: technical correctness, attribution/originality and rights boundaries, and fluent translation review. |
| Final diff | `git status` showed 47 modified tracked files, 61 untracked status paths (93 untracked files), and no staged changes before this documentation update; the scope includes the full existing implementation batch. Workflow, Jekyll config, layouts, styles, JavaScript, validators, schemas, tests, and file inventory were inspected; automated source and generated-site checks cover the authored Markdown set. | No unexpected file classes or staged changes found. Technical/content review remains pending; still uncommitted. No commit, push, or deploy was made. |

The bounded crawler's 18 passing responses establish reachability only; they do not establish technical correctness, endorsement, availability of linked material, or licensing. Its three redirects were followed and recorded; the Pages-host-to-HTTP-custom-domain redirect is separately treated as a deployment blocker above. An `example.test` search-test fixture was excluded from the crawl.

Files edited during the release-gate pass: `docs/REFERENCE_AUDIT.md` and `docs/IMPLEMENTATION_PLAN.md`. Both were already untracked then; that pass added no new files and staged nothing. The later deployment recovery diagnosis is documented separately in `docs/DEPLOYMENT.md`; this audit row now includes the three official documentation URLs added there and checked afterward.

## Findings and decisions

1. **The reference is primarily a curated directory.** Tajkart can keep its learning value in original lessons, guided study, examples, practice, projects, and career material while adding external links only after their official source and rights are checked.
2. **Coverage must be reported by category and language.** The source archive spans multiple resource types and 57 source locale records. Tajkart currently has 70 searchable pages (68 English, one Hindi draft, one Urdu draft), not complete translated catalogues. The two translations still need fluent human review.
3. **Indexes are not proof of curriculum depth.** Tajkart has 12 subject reading guides and 11 introductory programming-language paths; many mapped topics and languages still need original lessons, examples, and review.
4. **Static hosting fits the current scope.** Search, navigation, quizzes, and project briefs can run without accounts or server-side learner-code execution. A genuine code runner would require a separately reviewed isolation design.
5. **Rights are separate at each layer.** The upstream README and LICENSE identify CC BY 4.0 for eligible files in that repository. Individual books, courses, websites, images, and linked works keep their own terms. Tajkart's existing notice is preserved; no reference entries or prose were imported.
6. **The local build gate passes; the full release gate remains open.** Source validation, code tests, production Jekyll build, and generated-output checks now pass locally. GitHub Actions has not run on this uncommitted batch; human technical, translation, accessibility, and contributor-rights review also remain open.

## Next implementation tasks

1. Confirm the GitHub Pages target and HTTPS/custom-domain configuration; align `url` and `baseurl` if the verified target differs from the repository Pages URL.
2. Run the configured GitHub Actions workflow on a review branch and fix any Jekyll, rendered-link, search-index, or HTML findings.
3. Complete a human technical review of the six lessons, three course plans, language paths, and canonical exercise solutions; publish the review status honestly.
4. Have fluent Hindi and Urdu reviewers check the two translation drafts and their RTL rendering.
5. Perform keyboard, zoom/reflow, contrast, mobile, and screen-reader review on the built website.
6. Decide and document contribution permission terms before accepting substantial third-party-authored material; the current repository does not include a formal contributor license agreement.
7. Add external books, courses, media, or opportunities only as individually verified records with their own source, status, last-checked date, and rights metadata.

The reviewable batch is local; no commit or push was made by this audit.

## Live sources

- [Current repository README](https://github.com/EbookFoundation/free-programming-books/blob/main/README.md)
- [Current GitHub Pages site](https://ebookfoundation.github.io/free-programming-books/)
- [Current search application](https://ebookfoundation.github.io/free-programming-books-search/)
- [Current main branch API](https://api.github.com/repos/EbookFoundation/free-programming-books/branches/main)
- [Checked-in workflow tree at the audited commit](https://api.github.com/repos/EbookFoundation/free-programming-books/contents/.github/workflows?ref=2574d859ecf34dd8d1643cc5c7c9f11ae99f845c)
- [GitHub Pages deployment history API](https://api.github.com/repos/EbookFoundation/free-programming-books/deployments?environment=github-pages&per_page=8)

## Current comparison with upstream main (2026-10-15)

I reread the official [upstream README](https://github.com/EbookFoundation/free-programming-books/blob/main/README.md) and checked its `main` tree on 2026-10-15. The checked head was `4c301cce10db10026d632606b5167a9d1b8cd4ec` (`docs(kn): fix contribution guide navigation links`, 2026-10-14). This updates the 2026-10-14 snapshot recorded earlier in this report. The current tree is not the same snapshot as the supplied ZIP. Its tree contains 48 Markdown files under `books`, 41 under `courses`, 21 under `casts`, 94 under `docs`, 10 under `more`, and seven workflow files under `.github/workflows`; these are file counts, not counts of individual resources.

The README currently groups the directory into books, cheatsheets, online courses, interactive programming resources, problem sets/competitive programming, podcasts/screencasts, and browser playgrounds. It also links multilingual indexes and contributor translations. Tajkart uses those areas as an information-architecture reference, but its existing library is mostly original learning material rather than a mirror of upstream's external-resource catalogue. No upstream resource entries, prose, code, or workflow implementation were copied.

### Coverage status

| Upstream area | Tajkart status | What exists now | What remains for comparable coverage |
|---|---|---|---|
| Books and subject indexes | **Partial; no book catalogue** | A reading guide, 12 original subject guides, and 11 introductory language paths. | Curated book entries by subject/language, each with a verified source, attribution, current link, and rights note. |
| Courses | **Partial; original study plans** | Three self-guided plans for foundations, data structures, and web development. | A curated directory of external courses by topic/language, if that is a product goal, with individual source and rights review. |
| Cheatsheets | **Original content present** | Ten Tajkart-authored cheatsheets. | Human technical review and additional focused references where useful; upstream-linked cheat sheets are not catalogued. |
| Interactive resources | **Partial** | An original practice routine and four-question browser quiz; no arbitrary code execution. | More interaction types or a verified directory of external interactive tutorials. Browser and assistive-technology review is still open. |
| Problem sets / competitive programming | **Original practice present; catalogue partial** | Nine authored problem specifications; eight Python solutions and one SQL solution have automated tests. | Human solution review, more difficulty tiers, and optionally verified contest/problem-set directories. |
| Podcasts / screencasts | **Guide only** | An original viewing and note-taking guide plus metadata schema. | Verified channels or episodes with language, topic, source, and last-checked date. |
| Programming playgrounds | **Guide and project briefs only** | Safety guidance and six reproducible project briefs. | Verified browser-playground directory if desired. There is no hosted code runner. |
| Language coverage and translations | **Partial; drafts only** | Eleven English introductory paths and one Hindi plus one Urdu translation draft. `data/language_coverage.yml` tracks the 57 locale records found in the earlier source snapshot; those records are not translated Tajkart pages. | Fluent Hindi/Urdu review, more translated lessons, and accurate per-language coverage before claiming multilingual catalogue parity. |
| Subject taxonomy | **Mapped, not fully taught** | The 46 subject entries from the earlier source snapshot are mapped into seven Tajkart strands; 12 original subject guides have been written. | Add reviewed lessons and exercises for uncovered subjects. A taxonomy map does not mean complete curriculum coverage. |
| Search and discovery | **Implemented for Tajkart's own pages** | A generated local index with 70 resources, relevance ordering, filters, provenance, and draft-status labels. | External-resource records are currently zero. Add them only if wanted and individually verified; the upstream README links to a separate search application. |
| Contributor guidance and rights | **Core guidance present; permission policy incomplete** | Contribution/editorial guidance, code of conduct, templates, content schema, and a review workflow. | Decide and document the permission terms for outside contributions before accepting substantial third-party-authored material. Tajkart's license remains separate from upstream's CC BY 4.0 repository-file license; linked works keep their own terms. |
| Automation and maintenance | **Core site checks implemented; narrower automation** | One SHA-pinned GitHub Pages workflow covers source validation, tests, Jekyll, generated HTML checks, and deployment. | Upstream also maintains list/URL and RTL/LTR checks plus PR/issue housekeeping workflows. Add only checks justified by Tajkart's content and contributor volume; do not copy its workflow implementation by default. |
| Careers and student offers | **Tajkart-specific addition** | Five career guides and an offer-verification policy; no active job or offer listings are claimed. | Human review and individually verified listings if this area is expanded. These categories are not upstream parity items. |

### Audit conclusion and release evidence

**Built:** Tajkart has its own Jekyll site, original first-library content across the major learning formats, local search, metadata and rights validation, tests, generated-page checks, and a Pages deployment workflow. The local validator reports 112 Markdown files, 99 routes, and 70 searchable resources. The earlier detailed inventory remains in [reference coverage]({{ '/docs/REFERENCE_COVERAGE/' | relative_url }}) and [content progress]({{ '/docs/CONTENT_PROGRESS/' | relative_url }}).

**Partly built:** Most upstream categories have an original guide, practice format, or local analogue, but that does not provide the same breadth as upstream's multilingual curated directory. Tajkart currently has no verified third-party learning-resource entries. Its 57-locale map describes the earlier reference snapshot, not Tajkart translation completion.

**Still needed:** Human technical review, fluent Hindi/Urdu review, manual keyboard/screen-reader/mobile accessibility review, an explicit contributor-permission decision, and any desired expansion of external resource catalogues. These are release/editorial decisions, not missing build features.

The hosting result is separate from content coverage: GitHub Actions and the Pages deploy job succeeded for commit `a83766c26c97e13767f307176c0883df7cd2023b`, but the deployed URL currently resolves through an HTTP custom-domain redirect and direct HTTPS has a certificate hostname failure. The HTTPS hostname/configuration remains a release blocker; see [deployment recovery evidence]({{ '/docs/DEPLOYMENT/' | relative_url }}). A successful workflow is not equivalent to secure deployment acceptance.

No content was copied from upstream during this comparison. This audit edit is local and uncommitted; no commit, push, DNS edit, Pages setting change, or deployment was made.
