---
layout: page
title: Technical SEO and indexing audit
description: Evidence-based audit of Tajkart's canonical host, page metadata, sitemap, robots behavior, Google verification, deployment state, and owner actions.
permalink: /docs/SEO_TECHNICAL_AUDIT/
---

**Audit date:** 2026-10-16  
**Repository:** `shahanishashmi/tajkart-student-hub`  
**Worktree base:** `main` at `3913f88b66c172f68eff36fecd2e857405ea1a48`  
**Scope:** Local Jekyll configuration/build, public URL behavior, canonical metadata, sitemap/robots behavior, Google verification file, and search-engine owner steps.

This audit separates local build evidence from public deployment evidence. Neither a valid page response nor a sitemap submission proves that Google or Bing indexed a URL. No search-engine account was accessed.

## A. Findings and dispositions

| Severity | Finding and evidence | Disposition |
|---|---|---|
| High | The supplied Google verification URL returned HTTP 404 on the deployed project site. The exact token file was absent from the repository before this work. | Added `googlef0a0d65fc3e621d7.html` at the repository root with the exact supplied bytes. A local production build confirms it is copied unchanged. Public access still needs a separately authorized deployment; Search Console verification remains for the owner. |
| High | The deployed project host serves both HTTPS and HTTP with HTTP 200 and no redirect. The Pages API could not be read anonymously; the last recorded setting says HTTPS enforcement is off. | No Pages setting was changed, as instructed. The owner must resolve HTTPS enforcement separately. Do not call the deployment secure-release ready. |
| High | The personal-domain alternatives are not viable canonical destinations from current probes: `shahanishashmi.me` and `www.shahanishashmi.me` failed TLS hostname validation over HTTPS; the HTTP personal-domain project path returned a GitHub Pages 404; `learn.shahanishashmi.me` did not resolve. | Kept the working, repository-configured `github.io` project URL as canonical. No DNS, CNAME, custom-domain, or Pages change was made. |
| Medium | Before edits, 73 of 127 generated HTML documents used the same site-wide meta description. | Added page-specific descriptions to the previously generic pages. The two draft Hindi/Urdu translations remain non-indexable until fluent review; no review state was changed. A local check confirms all 124 sitemap pages have unique descriptions between 53 and 146 characters. |
| Medium | Draft translations, content templates, and the 404 page were not useful search results. The prior sitemap included pages that should not be indexed. | Added `noindex, follow` and `sitemap: false` to the two draft translations and two templates; the 404 page is also excluded. Sitemap validation enforces the exclusion. |
| Medium | The homepage had few direct, crawlable links into the learning areas. | Added ordinary HTML links to Explore, courses, programming, mathematics/practice, projects/exercises, guides, careers, and cheatsheets. Existing educational content and external-candidate separation remain intact. |
| Medium | The generated project-path `robots.txt` previously contained only a sitemap directive. The origin-root `https://shahanishashmi.github.io/robots.txt` currently returns 404 and is outside this repository's project path. | Added a project-path `robots.txt` with `User-agent: *`, `Allow: /`, and the absolute sitemap URL. This project file cannot configure the origin-root robots policy; GitHub Pages host-level control is outside this repository. With no root robots file, Google documents that crawling is allowed by default unless other controls apply. |
| Low | SEO metadata and sitemap behavior had no generated-output regression check. | Added `scripts/validate_seo.py`, five focused Python tests, and a CI validation step. The strict local build validates 129 HTML pages and exactly 124 indexable sitemap URLs. |

No structured data was added. No external learning material, directory candidate, or other resource was copied or promoted. The existing root license is unchanged.

## B. Canonical decision and live URL evidence

The selected canonical root is `https://shahanishashmi.github.io/tajkart-student-hub/`. It is the configured Jekyll origin plus `/tajkart-student-hub`, belongs to the repository's GitHub Pages project, and was the only tested candidate serving the deployed site with valid TLS and the expected canonical tags. `_config.yml` already had the correct `url` and `baseurl`; it was preserved.

The following relevant probes were run on 2026-10-16. Public routes reflect the deployed site at probe time, which predates the current local A–Z/Phase 2/SEO worktree.

| URL | Result / final URL | Redirect and TLS evidence | Body/content evidence |
|---|---|---|---|
| `https://shahanishashmi.github.io/tajkart-student-hub/` | HTTP 200; final URL unchanged. | Zero redirects; TLS certificate validated. | Deployed homepage HTML, `lang="en"`, one canonical to the same project URL, unique title/description, no `noindex`. |
| `http://shahanishashmi.github.io/tajkart-student-hub/` | HTTP 200; final URL unchanged. | Zero redirects; plaintext HTTP remains available. | Deployed page is served over HTTP; HTTPS is not enforced at the host. |
| `https://shahanishashmi.me/tajkart-student-hub/` | No HTTP response obtained. | TLS validation failed with a certificate hostname mismatch (curl exit 60). | No page body fetched. |
| `http://shahanishashmi.me/tajkart-student-hub/` | HTTP 404; final URL unchanged. | Zero redirects. | GitHub Pages 404 response. |
| `https://www.shahanishashmi.me/tajkart-student-hub/` | No HTTP response obtained. | TLS validation failed with a certificate hostname mismatch (curl exit 60). | No page body fetched. |
| `https://learn.shahanishashmi.me/` | No HTTP response obtained. | DNS lookup failed (curl exit 6). | No page body fetched. |
| `https://shahanishashmi.github.io/tajkart-student-hub/googlef0a0d65fc3e621d7.html` | HTTP 404; final URL unchanged. | Zero redirects; valid TLS to the canonical host. | Standard GitHub Pages 404 HTML; supplied verification text was not present in the deployed body. |
| `https://shahanishashmi.github.io/tajkart-student-hub/sitemap.xml` | HTTP 200; final URL unchanged. | Zero redirects; valid TLS. | Valid sitemap XML with 123 unique project-host URLs; no unexpected host/base-path URLs were found. |
| `https://shahanishashmi.github.io/tajkart-student-hub/robots.txt` | HTTP 200; final URL unchanged. | Zero redirects; valid TLS. | Only the sitemap directive was present in the deployed response. |
| `https://shahanishashmi.github.io/robots.txt` | HTTP 404; final URL unchanged. | Zero redirects; valid TLS. | The repository project cannot publish this host-root file from its `/tajkart-student-hub/` path. |

The public `/explore/` route also returned 404 because the local Explore changes have not been deployed. `/learning/courses/` and `/careers/` returned HTTP 200. No public content update was initiated.

HEAD responses for the deployed homepage and Python variables lesson showed no `X-Robots-Tag` header. Their HTML has no `noindex` directive. The Google proof URL response was a 404 HTML page, not the token. These header/content checks describe only the public deployment at probe time.

## C. Local SEO changes

- Added the exact Google proof file at the repository root. Its required bytes are `google-site-verification: googlef0a0d65fc3e621d7.html`, without a newline.
- Added project-path `robots.txt` and an explicit `sitemap.xml` Jekyll source. The sitemap uses generated collections/pages, canonical absolute URLs, and Jekyll's `/tajkart-student-hub` base path. It excludes the verification token, 404, draft translations, and templates.
- Added page-specific descriptions where the previous site-wide fallback duplicated generic copy, and added a conditional `robots` meta directive in the default layout.
- Marked the two unreviewed translations and reusable templates `noindex, follow` and `sitemap: false`. Their content/review status was not altered.
- Added homepage links to major learning areas using ordinary links.
- Added strict generated SEO validation and regression tests, then integrated the check into GitHub Actions. The workflow change will only run if a future authorized CI event occurs.

The public host root and its root-level robots file cannot be configured by this project-path Jekyll build. Search engines may crawl the project URL under the host's default behavior, but this repository cannot make an origin-root robots policy or HTTPS redirect effective. Google's [robots.txt specification](https://developers.google.com/crawling/docs/robots-txt/robots-txt-spec) defines the file at the root of the protocol/host; when no file exists there, crawling is allowed unless another rule applies.

### SEO delta file inventory

The following files changed as part of this SEO increment. The earlier A–Z and Phase 1/Phase 2 worktree edits remain intact; they are recorded separately in the accumulated worktree section of the [master audit]({{ '/docs/MASTER_AUDIT_REPORT/' | relative_url }}). No files were deleted.

Changed SEO integration and reporting files:

- `.github/workflows/pages.yml` — run the generated SEO validator after generated HTML validation.
- `_layouts/default.html` — render the explicit robots directive when a page declares one.
- `index.md` — add direct, crawlable homepage links into learning areas.
- `docs/index.md` — add SEO audit/setup links and a page-specific description.
- `docs/MASTER_AUDIT_REPORT.md` — record this SEO result in the consolidated audit.
- `scripts/validate_html.py` — treat the exact plain-text Google token as a verification file, not a generated HTML document.
- `404.md`, `CONTRIBUTING.md`, `COPYRIGHT.md`, `docs/CONTENT_STANDARDS.md`, `docs/ROADMAP.md` — add descriptions; `404.md` is also excluded from the sitemap and marked noindex.
- `learning/cheatsheets/containers-deployment.md`, `learning/cheatsheets/data-structures.md`, `learning/cheatsheets/debugging-testing.md`, `learning/cheatsheets/git-cli.md`, `learning/cheatsheets/java.md`, `learning/cheatsheets/javascript-typescript.md`, `learning/cheatsheets/networking-security.md`, `learning/cheatsheets/python.md`, `learning/cheatsheets/sql.md`, `learning/cheatsheets/web.md` — add page-specific descriptions.
- `learning/courses/algebra-foundations.md`, `learning/courses/data-structures.md`, `learning/courses/web-development.md` — add page-specific descriptions.
- `learning/guides/computer-architecture.md`, `learning/guides/computer-networks.md`, `learning/guides/cybersecurity-basics.md`, `learning/guides/data-structures-algorithms.md`, `learning/guides/databases-and-sql.md`, `learning/guides/devops-cloud.md`, `learning/guides/object-oriented-programming.md`, `learning/guides/operating-systems.md`, `learning/guides/programming-foundations.md`, `learning/guides/software-engineering-testing.md`, `learning/guides/system-design.md`, `learning/guides/web-development.md` — add page-specific descriptions.
- `learning/languages/c.md`, `learning/languages/cpp.md`, `learning/languages/go.md`, `learning/languages/html-css.md`, `learning/languages/java.md`, `learning/languages/javascript-typescript.md`, `learning/languages/php.md`, `learning/languages/python.md`, `learning/languages/rust.md`, `learning/languages/shell-scripting.md`, `learning/languages/sql.md` — add page-specific descriptions.
- `learning/lessons/algorithm-efficiency.md`, `learning/lessons/git-small-commits.md`, `learning/lessons/problem-solving-loops.md`, `learning/lessons/python-functions.md`, `learning/lessons/python-intermediate-collections.md`, `learning/lessons/python-intermediate-json.md`, `learning/lessons/python-intermediate-testing.md`, `learning/lessons/python-intermediate-validation.md`, `learning/lessons/python-lists-dictionaries.md`, `learning/lessons/python-variables.md` — add page-specific descriptions.
- `learning/problem-sets/algebra-foundations-check.md`, `learning/problem-sets/array-total.md`, `learning/problem-sets/binary-search.md`, `learning/problem-sets/factorial-recursion.md`, `learning/problem-sets/first-duplicate.md`, `learning/problem-sets/graph-reachability.md`, `learning/problem-sets/insertion-sort.md`, `learning/problem-sets/math-foundations-check.md`, `learning/problem-sets/sql-session-summary.md`, `learning/problem-sets/string-vowel-count.md`, `learning/problem-sets/tree-height.md` — add page-specific descriptions.
- `learning/projects/flashcard-quiz.md`, `learning/projects/folder-audit.md`, `learning/projects/mock-resource-api.md`, `learning/projects/python-study-log.md`, `learning/projects/reading-tracker.md`, `learning/projects/student-portfolio.md`, `learning/projects/study-session-database.md` — add page-specific descriptions.
- `learning/translations/hindi/python-variables.md`, `learning/translations/urdu/python-variables.md`, `templates/LEARNING_GUIDE_TEMPLATE.md`, `templates/OFFER_TEMPLATE.md` — mark draft/template pages `noindex, follow` and exclude them from the sitemap; template descriptions explain their reusable purpose.

Added files:

- `googlef0a0d65fc3e621d7.html` — exact owner-supplied verification text.
- `robots.txt` and `sitemap.xml` — project-path crawl guidance and generated canonical sitemap.
- `scripts/validate_seo.py` and `tests/test_seo.py` — output checks and five regression tests.
- `docs/SEO_TECHNICAL_AUDIT.md` and `docs/SEO_SEARCH_CONSOLE_SETUP.md` — evidence and owner steps.

## D. Google verification status

The file was absent before this change. It now exists locally and the strict production build verified that the generated root file exists and matches the exact supplied bytes. The public verification URL was checked before this local change and returned HTTP 404 with the standard GitHub Pages error body. Account ownership is **not verified**. The owner must publish the reviewed worktree through the separately authorized deployment process, confirm the token URL returns the exact line, and click **Verify** in Search Console.

## E. Sitemap and robots status

- Local production sitemap: valid XML, HTTPS canonical origin, correct project base path, 124 unique URLs, no duplicate URLs or host/path mismatches.
- The 124 generated sitemap URLs map to indexable generated HTML pages. The 404, two draft translations, and two templates are excluded. Every included page has one canonical matching its sitemap URL and a unique title/description.
- The local sitemap emits no `lastmod` values because this build has no trusted page modification timestamp metadata to publish.
- Local project-path robots file allows crawling and advertises `https://shahanishashmi.github.io/tajkart-student-hub/sitemap.xml`.
- Public deployed sitemap currently has 123 URLs and returned HTTP 200. Public deployed project-path robots returned HTTP 200 with only a sitemap line. These public results describe the older deployment, not the current local output.
- Public origin-root robots returned 404. This is a host-level boundary; a path-prefixed project repository cannot publish it.

## F. Build and tests

The following checks ran against this local worktree on 2026-10-16. GitHub Actions has not run for these local changes.

| Command/check | Result |
|---|---|
| `python scripts/validate_site.py` | Pass: 142 Markdown files, 129 routes, 91 searchable resources. |
| `python scripts/solution_coverage.py --check` | Pass (exit 0): 33 questions and matching answer/explanation/test evidence; all remain pending human review. |
| `python scripts/import_reference_resources.py --check` | Pass: 120 source lists, 10,796 appearances, 10,583 candidates, zero exceptions. This was validation only; the source migration was not repeated. |
| `python scripts/reference_catalog_audit.py --check` | Pass: all 233 manifest paths, 120 included lists, and 113 documented exclusions validate. |
| `python -m unittest discover -s tests -v` | Pass: 85 tests, including five new SEO regression tests. |
| `node --check assets/js/site.js`; `node --check assets/js/learning-tools.js` | Pass. |
| `node tests/search_test.js`; `node tests/navigation_test.js`; `node tests/learning_tools_test.js` | Pass. |
| `ruby scripts/validate_front_matter.rb` | Pass: 132 Markdown front matters and five YAML files parsed. |
| `$env:JEKYLL_ENV='production'; bundle exec jekyll build --strict-front-matter --destination <unique temporary directory>` | Pass: strict production build; existing optional `faraday-retry` middleware notice only. Repository `_site/` was not used as destination. |
| `python scripts/validate_html.py <temporary directory>` | Pass: 129 generated HTML pages, 91 authored search records, 10,583 unverified reference candidates. |
| `python scripts/validate_seo.py <temporary directory>` | Pass: 129 HTML pages, 124 indexable sitemap URLs, exact Google token, canonical/OG metadata and robots checks. |
| Headless Chrome `--dump-dom` on generated homepage, Python variables lesson, and verification file | Pass: homepage title and ordinary Explore/math links render; lesson canonical is correct and not noindex; exact verification text is displayed. This inspects the local generated files, not the public deployment. |
| `git diff --check` | Pass; Git printed existing CRLF/LF normalization notices only. |

The headless pass checks rendered DOM content, not visual layout, mobile reflow, screen-reader behavior, or learner usability. Earlier platform smoke evidence is recorded separately in the master audit.

The generated `googlef0a0d65fc3e621d7.html` is plain verification text rather than HTML; structural HTML validation intentionally skips that exact filename. The SEO validator separately checks its exact bytes.

## G. Indexing state and remaining owner actions

**Local build:** 129 generated HTML pages and 124 indexable sitemap URLs validated separately from hosting. **Public deployment:** the existing canonical homepage and sitemap respond, while the verification file and newer Explore route currently return 404. **Google/Bing indexing:** unknown; no account reports were provided or inspected.

After an authorized deployment, follow [Search Console and webmaster setup]({{ '/docs/SEO_SEARCH_CONSOLE_SETUP/' | relative_url }}): add the URL-prefix property `https://shahanishashmi.github.io/tajkart-student-hub/`, verify with the deployed HTML file, inspect the homepage and selected original lessons, submit the actual sitemap, request indexing for a small set of pages, then monitor Page indexing/Sitemaps reports. Add the canonical URL in Bing Webmaster Tools, complete a Bing-offered verification method, submit the same deployed sitemap, and inspect Bing's actual reports. Verification, sitemap submission, live URL tests, and indexing are separate states.

No commit, push, deployment, DNS change, custom-domain change, GitHub Pages setting change, or account access was performed. The root license and all earlier learning/reference worktree changes were preserved.

### Current Git status

- Branch: `main`
- HEAD: `3913f88b66c172f68eff36fecd2e857405ea1a48`
- Staged paths: 0
- Modified tracked paths: 100
- Untracked paths: 18
- Deleted paths: 0

The modified/untracked totals include the accumulated earlier learning, Phase 1, Explore, and A–Z work as well as this SEO increment. No status entries were staged. The SEO delta paths are enumerated above; the earlier change inventory is preserved in the master audit.
