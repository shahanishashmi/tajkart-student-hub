# Tajkart Student Hub

**Learn. Build. Grow.**

Tajkart Student Hub is an original learning and career-development platform built primarily for students. It also welcomes self-learners and early-career learners. It brings together subject guides, study support, language paths, self-guided courses, interactive exercises, problem sets, project briefs, career guidance, and student-opportunity safety advice.

The project is led by **Shah Anis Hashmi, Founder & Educator**. This repository makes no unverified claims about qualifications, employment outcomes, partnerships, or live opportunities.

## Explore

- [Start with a student learning goal](getting-started.md)
- [Study planning and assessment preparation](learning/study-skills/index.md)
- [Mathematics foundations: data interpretation](learning/lessons/math-data-interpretation.md)
- [Learning Library](learning/index.md)
- [Books and reading guides](learning/books/index.md)
- [Courses and study plans](learning/courses/index.md)
- [Programming languages](learning/languages/index.md)
- [Computer science subjects](learning/subjects/index.md)
- [Cheatsheets](learning/cheatsheets/index.md)
- [Interactive learning](learning/interactive-tutorials/index.md)
- [Problem sets](learning/problem-sets/index.md)
- [Projects and playground guidance](learning/projects/index.md)
- [Podcasts and screencasts](learning/podcasts-screencasts/index.md)
- [Career Hub](careers/index.md)
- [Student Offers guidance](offers/index.md)

## Reference and content policy

The supplied `free-programming-books-main.zip` archive and the pinned upstream source were audited for breadth, organization, and resource discovery. Tajkart now includes a source-attributed, CC BY 4.0 link index generated from the upstream snapshot; these 10,583 unique destinations are unverified candidates, not approved or rights-checked recommendations. Search loads them only when a learner opts in. No linked book/course/media content, reference prose beyond listing annotations, translations, code, branding, templates, or workflows are republished as Tajkart originals. See the [combined audit](docs/MASTER_AUDIT_REPORT.md), [repository and source audit](docs/REFERENCE_AUDIT.md), [architecture](docs/ARCHITECTURE.md), [coverage map](docs/REFERENCE_COVERAGE.md), [file-level parity matrix](docs/REFERENCE_PARITY_MATRIX.md), [licensing review](docs/LICENSING_REVIEW.md), [machine-readable category map](data/reference_coverage.yml), and [57-locale inventory](data/language_coverage.yml). Hindi and Urdu content is clearly marked as draft pending fluent review.

The existing `LICENSE` was inspected and preserved. It reserves rights in original Tajkart work; it does not grant rights to third-party works linked or mentioned here. Read [copyright and licensing](COPYRIGHT.md) and the [content policy](docs/CONTENT_POLICY.md) before contributing external material.

## Work locally

Install Ruby, Bundler, Python 3, and Node.js. From the repository root:

```sh
bundle install
bundle exec jekyll serve
```

Run the content and code checks:

```sh
python scripts/validate_site.py
python scripts/import_reference_resources.py --check
python -m unittest discover -s tests -v
node --check assets/js/site.js
node tests/search_test.js
node tests/navigation_test.js
bundle exec jekyll build
python scripts/validate_html.py _site
```

The search index and quiz work on static hosting. Tajkart does not execute submitted code on a server.

## Publish with GitHub Pages

The repository workflow builds pull requests and deploys successful updates to `main`. In repository **Settings → Pages**, choose **GitHub Actions** as the deployment source. The exact published address appears in the Pages settings and the `github-pages` deployment environment. Keep `url` and `baseurl` in [_config.yml](_config.yml) aligned with the repository or custom domain.

See [deployment instructions](docs/DEPLOYMENT.md), [content progress](docs/CONTENT_PROGRESS.md), and [contribution guide](CONTRIBUTING.md). No build/deploy claim applies to the current local changes until CI runs on them.
