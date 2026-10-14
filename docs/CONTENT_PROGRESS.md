---
layout: page
title: Content progress
description: Honest status of Tajkart's learning, discovery, translation, and quality work.
permalink: /docs/CONTENT_PROGRESS/
---

The counts below describe authored pages, not approved curriculum. Automated checks validate structure and selected examples; a human technical and language review is still required before these drafts should be presented as approved.

## Current authored material

| Area | Current material | Status | Remaining work |
|---|---|---|---|
| Programming lessons | Six original lessons: variables, loops, algorithm growth, Git commits, functions, and Python collections. | Drafted; Python snippets and local routes validate. | Technical review and broader language-specific lessons. |
| Subject reading guides | Twelve guides for foundations, algorithms, OOP, SQL, web, networks, operating systems, engineering/testing, architecture, system design, security, and DevOps/cloud. | Drafted; each has objectives, a concept path, practice, and next steps. | Add worked examples where thin; technical review; map remaining 46 subject headings honestly. |
| Programming language paths | Eleven introductory paths: C, C++, Java, Python, JavaScript/TypeScript, HTML/CSS, SQL, PHP, Go, Rust, and shell. | In progress; paths introduce use cases and a next-study sequence. | Add deeper language-specific lessons, tested examples, installation guidance, and intermediate sequences. |
| Courses | Three self-guided plans: programming foundations, data structures, and web foundations. | Drafted with objectives, modules, assignments, checks, projects, rubrics, and completion criteria. | Create intermediate/advanced progression and technical review. |
| Cheatsheets | Ten original references across Git/CLI, programming, SQL, web, algorithms, testing, networking/security, and containers/deployment. | Drafted; examples and local links validate. | Technical review and add missing focused CLI/REST/API references. |
| Interactive learning | A prediction routine and a four-question browser quiz with answer feedback and an answered-question counter. | Client-side behavior is implemented; no arbitrary code is executed. Browser interaction has not been exercised locally. | Add debugging and fill-in activities; review the quiz with keyboard and assistive technology. |
| Problem sets | Nine distinct tasks covering arrays, strings, hashing, search, sorting, recursion, trees, graphs, and SQL. | Specifications include examples and hints; eight Python solutions and one SQL query have tests. | Human review and additional difficulty tiers. |
| Projects and playgrounds | Six reproducible briefs for a tracker, quiz, portfolio, database, read-only file audit, and mock API client. | Drafted with milestones, expected behavior, tests, extensions, and rubrics. | Implement selected projects and add intermediate/advanced briefs. |
| Media learning | Active podcast/screencast study guidance and a metadata schema for future verified entries. | Guidance is original; no channels or episodes are listed. | Review a real resource before adding any listing. |
| Careers and offers | Five focused guides for resumes, interviews, internships, professional email, and entry-level learning paths; offer-verification guidance. | No jobs, discounts, scholarships, or internships are claimed live. | Human review and more role-specific, locally verified advice. |
| Multilingual content | Fifty-seven source locale records; one Hindi and one Urdu translation draft of the Python variables lesson. | Unicode and RTL layout support are present; both translations are pending fluent review. | Review Hindi and Urdu; add more lessons before claiming broader language support. |
| Accessibility | Semantic landmarks, skip link, responsive layouts, visible focus, reduced motion, and RTL-aware styles. | Generated HTML passes checks for language, landmarks, headings, labels, IDs, images, and local targets. | Perform manual keyboard, zoom/reflow, mobile, RTL, and screen-reader review. |

## Search and validation snapshot

- The static search index contains **70 searchable resources** in source metadata: 68 English originals and 2 draft translations. Search supports all-token text matching, relevance ranking, type, subject/category, language, difficulty, provenance, and title/type/difficulty sorting. Results identify original work and draft translation/review state; external entries have a separate provenance path and are required to show creator, source, attribution, and rights status.
- `python scripts/validate_site.py` passed locally: 112 Markdown files, 99 Jekyll routes, unique resource IDs/routes, required search metadata, known prerequisites, Python examples, and local Markdown links.
- `python -m unittest discover -s tests -v` passed locally: 8 solution tests, 7 resource-provenance/rights metadata tests, and 1 SQLite example test (16 total).
- `node --check assets/js/site.js` and `node tests/search_test.js` passed locally; the focused search test covers token matching, relevance, original/translation/external provenance, attribution, and no-results behavior.
- The verified external-resource inventory is empty: no third-party learning resource or opportunity is advertised as current. External link/rights record counts are therefore zero; future `external` pages are source-validated for HTTP(S) URL, creator, attribution, and a resolved rights state.
- YAML front matter in 99 Markdown files, five YAML configuration/inventory files, and both JSON schemas parsed locally with PyYAML/Python's JSON parser. CI is configured to run equivalent Ruby standard-library checks.
- Ruby 3.3.12 with Bundler resolves 100 gems from `Gemfile.lock`; `bundle exec jekyll build` passes in production mode and `python scripts/validate_html.py _site` validates 99 actual generated pages and all 70 search-index entries. The first generated-output check exposed unlabeled checklist checkboxes and an extensionless-file route check bug; both were fixed before the passing run.
- No full external-link crawl, human technical review, fluent translation review, or manual assistive-technology audit has been completed.

Commit `a83766c` passed GitHub Actions and the Pages deploy workflow; the deployed host still has an HTTPS/hostname blocker. The latest evidence is in the [deployment recovery report]({{ '/docs/DEPLOYMENT/' | relative_url }}). See the [reference coverage audit]({{ '/docs/REFERENCE_COVERAGE/' | relative_url }}), [implementation plan]({{ '/docs/IMPLEMENTATION_PLAN/' | relative_url }}), and [next steps]({{ '/docs/NEXT_STEPS/' | relative_url }}).
