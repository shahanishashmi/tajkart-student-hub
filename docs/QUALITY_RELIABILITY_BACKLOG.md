---
layout: page
title: Quality and reliability backlog
description: Evidence, regression coverage, and tracked human-review and release gates for Tajkart Student Hub.
permalink: /docs/QUALITY_RELIABILITY_BACKLOG/
---

**Audit date:** 2026-10-16  
**Repository:** `shahanishashmi/tajkart-student-hub`  
**Reviewed commit:** `3913f88b66c172f68eff36fecd2e857405ea1a48`

This is the Phase 1 quality and reliability tracker. It separates automated evidence from human decisions. “Passed” means the named local check ran successfully; it does not mean content has been approved.

## Current verification snapshot

The branch was `main` at `3913f88`, matching `origin/main`, before this Phase 1 change. A read-only GitHub Actions lookup found run [38800723889](https://github.com/shahanishashmi/tajkart-student-hub/actions/runs/38800723889) successful for that exact committed SHA. That hosted run does **not** include the uncommitted Phase 1 test additions.

The Phase 1 local test run passed **66 Python tests**. This pass added edge cases to the eight canonical Python solutions: negative/zero totals, repeated strings, binary-search boundaries and singleton inputs, sorted/reverse/single-item sorting, factorial boundary values, uppercase and accented vowel cases, one-sided trees, and cyclic graph traversal. No implementation defect was exposed by these cases. The documented SQL query already has tests for duplicate sessions, `NULL`, zero and negative values, tied totals, and empty input; it was executed in SQLite only.

### Phase 2 current local update (2026-10-16)

The follow-up now passes 80 Python tests and generated-page checks for seven migrated arithmetic/data questions and a new three-question linear-equation modeling check. Five of the seven arithmetic/data responses are deterministic numeric checks; two remain manual comparison. All new items remain pending human review. The current full details and command evidence are in the [master audit]({{ '/docs/MASTER_AUDIT_REPORT/' | relative_url }}).

## Tracked issues

| ID | Priority | Status | Evidence and next action |
|---|---|---|---|
| `REL-HTTPS` | P0 release gate | Open; external Pages state | HTTPS enforcement is off. The previously authorized update returned HTTP 404, “The certificate does not exist yet.” A repository administrator must inspect the Pages certificate/control state; retry only the authorized enforcement setting when GitHub reports it is ready. Do not alter DNS or `_config.yml` as part of this retry. See the [P0 incident report]({{ '/docs/P0_INCIDENT_REPORT/' | relative_url }}). |
| `EDU-QUESTIONS` | P1 | Open; reviewer not recorded | All 33 discovered questions have a written answer, explanation, and matching automated test evidence; all 33 remain pending human educational review. Arrange qualified mathematics and programming review, record the decision for each item, and keep `review_status: pending` until then. |
| `EDU-CONTENT` | P1 | Open; reviewer not recorded | The arithmetic/algebra sequence, Python lessons, courses, guides, and project briefs are drafts. Tests do not evaluate teaching clarity, difficulty, or suitability. Review a bounded batch and record findings before approval. |
| `A11Y-MANUAL` | P1 | Open; no manual sign-off | Structural generated-HTML checks pass. A human review still needs keyboard-only navigation, screen reader, contrast, mobile, zoom/reflow, reduced motion, and RTL rendering checks with browser/device and retest notes. |
| `L10N-HI-UR` | P1 | Open; fluent reviewers not recorded | The one Hindi and one Urdu Python translation are drafts. Review meaning, terminology, code context, `lang`/`dir`, and rendered reading order with fluent reviewers. Do not infer review from Unicode or layout checks. |
| `QUESTION-MAPPING` | P2 | Open; bounded content task | Eleven items lack machine-checkable accepted-answer formats: two compound arithmetic/data responses intentionally use manual comparison, and nine remaining static programming/SQL prompts lack answer contracts. Nine static prompts also lack per-question skill/lesson mappings. The seven math questions and three modeling questions now use structured records where sound; keep open-ended responses manual unless a defensible contract is established. |
| `EXT-RESOURCES` | P2 | Open; all candidates unverified | The attributed index contains 10,583 destinations from 10,796 source appearances. Verification, access, and linked-work rights remain unassessed; no candidate is an approved recommendation. Review items individually before promotion. No full link crawl was run. |
| `CONTRIBUTOR-RIGHTS` | P1 decision gate | Open; rights-holder decision needed | The contribution guide does not state a general contributor copyright grant. The rights-holder must decide publication/reuse terms before substantial outside contributions are accepted. Preserve the root license unless that decision is explicit. |
| `SQL-DIALECT` | P2 | Partially covered | The exact lesson query passes SQLite tests for the documented cases. Confirm behavior against a second database only if Tajkart chooses to support that dialect; current material does not claim cross-database execution. |

No reviewer names, approval dates, rights permissions, or accessibility results have been inferred or invented.

## Local commands and current results

| Command | Result |
|---|---|
| `python scripts/validate_site.py` | Pass: 140 Markdown files, 127 routes, 91 searchable resources. |
| `python scripts/import_reference_resources.py --check` | Pass: 120 source files, 10,796 appearances, 10,583 unique destinations, zero parser exceptions. |
| `python scripts/solution_coverage.py --check` | Pass: 33 questions, all with answers/explanations and test evidence; zero broken mappings. |
| `python -m unittest discover -s tests -v` | Pass: 80 tests, including the Phase 2 math/modeling regressions. |
| Node syntax and tests | Pass: `site.js`, `learning-tools.js`, search, navigation, and learning-tools checks. |
| `ruby scripts/validate_front_matter.rb` | Pass: 130 Markdown front-matter files and five YAML files. |
| Strict production Jekyll build and `python scripts/validate_html.py <temporary-output>` | Pass: 127 generated pages, 91 Tajkart search resources, and 10,583 candidate destinations. The build used a temporary output path and preserved `_site/`. |

The generated-site checks ran after this tracker was integrated. The successful hosted run covers the committed SHA only; hosted CI should be rerun after the owner chooses a separate commit/push. This tracker does not authorize publication.
