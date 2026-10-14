---
layout: page
title: Tajkart architecture
description: The current static-site structure, content flow, discovery layer, and release checks.
permalink: /docs/ARCHITECTURE/
---

## System overview

Tajkart is a static Jekyll site. Markdown and YAML are the source of truth; Jekyll turns pages and metadata into static routes and a JSON search index; browser JavaScript adds search and quiz behavior. GitHub Actions validates pull requests and deploys successful updates to GitHub Pages.

**Build flow:** Markdown pages and YAML front matter + content/locale registries → source validators → Jekyll/Liquid → static routes and `search-index.json` → browser search and quizzes → GitHub Pages. GitHub Actions runs the validators and build before deployment.

## Repository responsibilities

| Path | Responsibility |
|---|---|
| `learning/` | Original guides, courses, language paths, lessons, cheatsheets, activities, problem sets, projects, and translation drafts. Category README files are maintainer notes and are excluded from the generated site. |
| `careers/`, `offers/`, `about/` | Career preparation, opportunity verification guidance, and project/founder information. No unverified live opportunities are published. |
| `data/reference_coverage.yml` | Source-category-to-Tajkart mapping, coverage state, and remaining work. |
| `data/language_coverage.yml` | Source locale codes grouped by resource type and Tajkart's current language status. |
| `data/*.schema.json` | Record shapes for future verified resources and opportunities. |
| `search-index.json` | Liquid template that emits pages whose front matter sets `searchable: true`, with provenance and review state. It is generated at build time, not a hand-maintained copy of every page. |
| `_layouts/`, `_includes/` | Shared page, lesson, and home layouts; related-resource and metadata fragments. |
| `assets/css/site.css`, `assets/js/site.js`, `assets/favicon.svg` | Tajkart design system, responsive/RTL-aware presentation, client-side search and quiz behavior, and vector favicon. |
| `scripts/`, `tests/` | Source/route/content validation, front matter parsing, generated HTML validation, and tests for canonical examples and solutions. |
| `.github/workflows/pages.yml` | Pull-request checks and main-branch GitHub Pages build/deploy. Actions are pinned to commit SHAs. |
| `docs/`, `templates/`, `.github/` | Writing and rights policies, editorial process, deployment guidance, contribution templates, and reusable page templates. |

## Content and route model

Substantive pages use YAML front matter for a stable `id`, title, permalink, content type, category, BCP 47 language, provenance (`original`, `translation`, or `external`), difficulty, tags, objectives, prerequisites, and content/review states. Original work is the site-wide default; translation pages point to their original resource and carry an explicit translation status. External entries identify their creator, official URL, attribution, and resolved rights basis. The field rules and allowed states are documented in [Content schema]({{ '/docs/CONTENT_SCHEMA/' | relative_url }}). Routes use explicit permalinks and a trailing slash for pages. `_config.yml` supplies the production URL and project `baseurl`; Liquid `relative_url` filters preserve links when the project is hosted under that subpath.

Content statuses describe drafting and validation, while review statuses describe human review. A resource marked searchable appears in the Liquid index; the browser interface can filter by text, type, category, language, difficulty, and provenance. Query matches are ranked by title, tags, then summary; results show their original/translation/external status. External entries link to the credited source. `assets/js/site.js` does not send learner code to a server. The quiz evaluates fixed answer choices in the browser.

The locale map preserves reference filename codes separately from Tajkart language tags. This avoids treating archive filename conventions as site metadata and makes incomplete translations visible. Translation status is tracked per locale and content type rather than inferred from an index page.

## Validation and deployment flow

The Pages workflow runs the Python source validator, Python solution tests, JavaScript syntax check, Ruby front matter/YAML validator, Bundler installation, a production Jekyll build, and generated HTML checks. Pull requests run checks but do not deploy. A successful push or manual dispatch on `main` packages the built site and deploys it through GitHub Pages. Build permissions are read-only; the deploy job separately receives `pages: write` and `id-token: write`.

Local contributors can use the commands in [README]({{ '/' | relative_url }}) and [deployment instructions]({{ '/docs/DEPLOYMENT/' | relative_url }}). The local environment now uses Ruby 3.3.12 and a cross-platform `Gemfile.lock`; the production Jekyll build and generated-output checker pass. GitHub Actions build and deploy passed for committed SHA `a83766c`; later uncommitted documentation edits have not run through hosted CI. The deployed host still has an HTTPS/hostname blocker; see the [next-phase roadmap]({{ '/docs/ROADMAP_NEXT_PHASE/' | relative_url }}).

## Design constraints and growth points

- Keep the site static while lessons, indexes, and search can meet learner needs.
- Do not execute arbitrary learner-submitted source code on the server.
- Keep external resources optional, verified, attributed, and distinct from Tajkart-authored material.
- Expand content in reviewable units; an index entry alone does not mean its subject is taught.
- Before adding contributor-authored content at scale, decide and publish explicit reuse and contribution permission terms. See [Licensing review]({{ '/docs/LICENSING_REVIEW/' | relative_url }}).
- Add category-specific schema checks only when the content formats and editorial requirements are stable enough to validate accurately.
