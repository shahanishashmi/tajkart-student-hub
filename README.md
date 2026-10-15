# Tajkart Student Hub

**Learn. Practice. Build. Grow.**

Tajkart is an evolving, student-first learning platform. It brings original study guides, lessons, learning paths, practice, projects, and career guidance together so students can find a starting point and choose a next step.

The project is led by **Shah Anis Hashmi, Founder & Educator**. Tajkart is a static site built with Jekyll. Its learning material is still being reviewed; automated checks do not replace an educator, fluent translator, or accessibility reviewer.

## Contents

- [Explore Tajkart](#explore-tajkart)
- [A student learning path](#a-student-learning-path)
- [Feature status](#feature-status)
- [External resources and attribution](#external-resources-and-attribution)
- [Run Tajkart locally](#run-tajkart-locally)
- [Repository map](#repository-map)
- [Content quality and review](#content-quality-and-review)
- [Languages and accessibility](#languages-and-accessibility)
- [Deployment](#deployment)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License and acknowledgements](#license-and-acknowledgements)

## Explore Tajkart

- [Choose a student learning goal](getting-started.md)
- [Explore resources by 18 student-facing categories](explore.md)
- [Learning library](learning/index.md)
- [Courses and study plans](learning/courses/index.md)
- [Study planner](learning/planner/index.md)
- [Practice and problem sets](learning/problem-sets/index.md)
- [Interactive learning](learning/interactive-tutorials/index.md)
- [Projects and playground guidance](learning/projects/index.md)
- [Books and reading guides](learning/books/index.md)
- [Programming language paths](learning/languages/index.md)
- [Computer science subjects](learning/subjects/index.md)
- [Cheatsheets](learning/cheatsheets/index.md)
- [Podcasts and screencasts guidance](learning/podcasts-screencasts/index.md)
- [Study skills](learning/study-skills/index.md)
- [Career preparation](careers/index.md)
- [Student offers guidance](offers/index.md)

## A student learning path

1. Start with [a learning goal](getting-started.md), such as academic study, programming, a portfolio project, or career preparation.
2. Choose a subject guide, lesson, or [self-guided course](learning/courses/index.md). Course plans are flexible drafts, not accredited programs.
3. Practise with a [problem set](learning/problem-sets/index.md) or an [interactive exercise](learning/interactive-tutorials/index.md). Some questions support answer checking; open-ended code tasks are compared with reference solutions rather than automatically scored.
4. Use hints and worked explanations where provided, then revisit a prerequisite lesson if needed.
5. Try a [project brief](learning/projects/index.md) to apply the ideas. The portfolio tool can keep learner-written draft notes in the current browser.
6. Optionally use the [study planner](learning/planner/index.md) to review course sessions and save self-reported checkmarks in this browser.

Planner checkmarks, quiz attempts, and portfolio notes are local to the browser. Tajkart has no learner accounts, cross-device sync, server-side progress storage, or hosted code runner. Local completion and quiz evidence do not establish mastery.

## Feature status

| Area | Available now | Status and limits |
|---|---|---|
| Lessons and subject guides | Original computing lessons, introductory language paths, and a short English mathematics and algebra sequence. | Useful starting material; curriculum breadth is incomplete and human technical review is pending. |
| Courses and planner | Self-guided paths with prerequisites, linked resources, estimated sessions, and optional local checkmarks. | Planner uses authored course metadata; estimates and sequencing need educator review. Progress is not synced. |
| Practice and solutions | Problem sets, a code-reading quiz, and a structured algebra assessment with hints and worked explanations. | Selected answer behavior has automated tests. Many open-ended prompts need manual comparison; educational review is pending. |
| Search | Search for Tajkart resources by text and metadata. An optional control searches a separate reference-link index. | The default index covers Tajkart resources. Reference links remain unverified candidates. |
| Projects and portfolio | Project specifications with milestones and rubrics; optional browser-local portfolio draft notes. | Briefs are not finished applications. Draft notes are not published, synced, or certified. |
| Careers and opportunities | Original career guidance and advice for checking offers. | No live job, internship, scholarship, or discount listings are claimed. |
| Hindi and Urdu | One draft translation of a Python lesson in each language; RTL-aware layout support. | Both translations need fluent review. This is not a translated course catalogue. |

For source-derived counts and test evidence, see the [master audit report](docs/MASTER_AUDIT_REPORT.md) and [content progress report](docs/CONTENT_PROGRESS.md).

## External resources and attribution

Tajkart includes a separate, opt-in index of **10,583 candidate links** extracted from the pinned [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books) listing snapshot. The listing data includes source attribution and is identified under CC BY 4.0; its linked books, courses, videos, and websites are separate works.

Every imported destination remains marked unverified, with rights and access not assessed. The candidate index is not an approved recommendation catalogue, and the reference listing license does not grant permission to reproduce the linked works. No full external-link or rights review has been completed. See the [reference migration and rights evidence](docs/MASTER_AUDIT_REPORT.md#reference-migration) before using or updating this data.

## Run Tajkart locally

### Prerequisites

- Ruby 3.3.x and Bundler
- Python 3
- Node.js (CI currently uses Node 24)

There is no npm or `package.json` build. Jekyll and the GitHub Pages gem provide the site build.

```sh
git clone https://github.com/shahanishashmi/tajkart-student-hub.git
cd tajkart-student-hub
bundle install
bundle exec jekyll serve
```

Open the local address printed by Jekyll. On Windows, RubyInstaller with its MSYS2 development kit is required; see the [Windows setup and deployment guide](docs/DEPLOYMENT.md).

### Build and validate

Run the relevant checks from the repository root:

```sh
python scripts/validate_site.py
python scripts/import_reference_resources.py --check
python scripts/solution_coverage.py --check
python -m unittest discover -s tests -v
node --check assets/js/learning-tools.js
node --check assets/js/site.js
node tests/learning_tools_test.js
node tests/search_test.js
node tests/navigation_test.js
ruby scripts/validate_front_matter.rb
bundle exec jekyll build
python scripts/validate_html.py _site
```

The source validator checks routes, metadata, prerequisites, examples, and local Markdown links. The solution coverage command checks the generated question-level report. The Jekyll build writes generated files to `_site/`; the HTML validator checks that output. Automated passes do not certify teaching accuracy, translation quality, rights, or accessibility conformance.

If problem sets or structured assessments change, update the question-level section of the audit with:

```sh
python scripts/solution_coverage.py --write
```

## Repository map

```text
.
|-- _data/                  Structured assessment data for generated pages
|-- assets/                 Site styles and browser-side JavaScript
|-- careers/                Career preparation guides
|-- data/                   Schemas, taxonomies, and attributed resource inventory
|-- docs/                   Audits, content standards, deployment, and roadmap
|-- learning/               Lessons, courses, practice, guides, and projects
|-- offers/                 Student offer-verification guidance
|-- scripts/                Source, migration, coverage, and build validators
|-- tests/                  Python and JavaScript regression tests
|-- _includes/              Reusable Liquid partials
|-- _layouts/               Shared Jekyll page templates
|-- _config.yml             Site URL, base path, and Jekyll configuration
`-- .github/workflows/      Build and GitHub Pages deployment workflow
```

## Content quality and review

Tajkart aims for clear objectives, stated prerequisites, original explanations, worked examples, practice, hints, and next steps. Content and external-resource rules are in [content standards](docs/CONTENT_STANDARDS.md), the [content policy](docs/CONTENT_POLICY.md), and the [editorial review guide](docs/EDITORIAL_REVIEW.md). The open review and reliability tasks are tracked in the [quality and reliability backlog](docs/QUALITY_RELIABILITY_BACKLOG.md).

Automated checks cover structure and selected examples. The current audit records 30 questions with written answers and question-specific test evidence; all 30 still await human educational review. Sixteen static prompts do not have machine-readable answer formats and remain manual-comparison tasks. Tests of a reference implementation do not evaluate a learner's reasoning or replace a qualified review.

## Languages and accessibility

English is the main content language. Hindi and Urdu each have one draft Python translation awaiting fluent review. The site includes semantic landmarks, a skip link, visible keyboard focus, responsive and reduced-motion styles, and RTL-aware layout rules. Structural HTML checks have passed, but no manual keyboard-only, screen-reader, zoom/reflow, mobile, contrast, or rendered RTL review is recorded. Tajkart does not claim WCAG conformance.

## Deployment

The GitHub Actions workflow checks pull requests and deploys successful pushes to `main` through GitHub Pages. HTTPS enforcement for the project URL remains an unresolved release gate; a prior authorized setting update was rejected because GitHub did not yet report a certificate. The [master audit](docs/MASTER_AUDIT_REPORT.md) is the current consolidated evidence; the [deployment report](docs/DEPLOYMENT.md) preserves the recovery history. Do not treat a successful build or deployment as proof that HTTPS enforcement is enabled.

## Roadmap

### Available now

- Student goal-based discovery, original learning material, search, courses, practice, project briefs, and career guidance.
- A local-only study planner and portfolio draft tool.
- An opt-in, attributed directory of unverified reference-link candidates.

### Next content increment

The next bounded academic unit is **linear-equation word problems and modeling**, after an educator reviews the current arithmetic-to-algebra path. It should teach students to define an unknown, translate a scenario into an equation, check units and assumptions, solve, and substitute the result back into the context. Include prerequisites, worked examples, varied practice with hints, checked numeric examples, and a formative assessment mapped to existing algebra skills. Keep it pending review until an educator records a decision.

### Release and quality work

- Resolve the already-authorized GitHub Pages HTTPS enforcement blocker only when GitHub reports certificate readiness; do not alter DNS or domain settings as part of this content work. Follow [deployment recovery](docs/DEPLOYMENT.md) and the [P0 incident report](docs/P0_INCIDENT_REPORT.md).
- Arrange technical and mathematics review, fluent Hindi/Urdu review, and manual accessibility testing. Keep review states pending until a human review is recorded.
- Decide whether to maintain verified third-party catalogues. Do not promote candidate links without checking source, attribution, terms, rights, learner relevance, and last-checked date.

This is a prioritized work queue, not a release promise. The [master audit](docs/MASTER_AUDIT_REPORT.md) records current evidence and limitations.

## Contributing

1. Read [CONTRIBUTING.md](CONTRIBUTING.md), the [Code of Conduct](CODE_OF_CONDUCT.md), and the [content policy](docs/CONTENT_POLICY.md).
2. Find a specific learner need and check whether the repository already covers it.
3. Make a focused change with original material, useful examples, sources for claims that need verification, and truthful review metadata.
4. Run the checks relevant to your change and describe what passed in the pull request.

Contributions can improve explanations, worked examples, tests, project briefs, translations, accessibility, or documentation. Ask the maintainer about publication and reuse terms before preparing a substantial outside contribution; the current policy does not state a general contributor copyright grant. Do not add copied course text, books, answer keys, or unlicensed assets.

## License and acknowledgements

The root [LICENSE](LICENSE) reserves rights in original Tajkart-authored content, except where a file states otherwise. This repository does not grant a blanket open-source reuse license for Tajkart material. See [copyright and licensing](COPYRIGHT.md) and check any file-specific notice before reuse.

The reference-list metadata is separately attributed under its stated CC BY 4.0 terms. That attribution does not cover the works linked by the index. Tajkart does not claim affiliation with or endorsement by listed providers. The project acknowledges its external sources in the [master audit](docs/MASTER_AUDIT_REPORT.md); dependencies are recorded in [Gemfile](Gemfile) and [Gemfile.lock](Gemfile.lock).
