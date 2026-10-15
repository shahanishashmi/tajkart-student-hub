---
layout: page
title: Combined platform audit and execution report
description: One evidence-based report on Tajkart's student-first platform, reference coverage, content, implementation, validation, and release gates.
permalink: /docs/MASTER_AUDIT_REPORT/
---

**Audit date:** 2026-10-16<br>
**Repository:** shahanishashmi/tajkart-student-hub<br>
**Branch / baseline:** main at b4e19802d7dfd1c43b83bc1fd621e61b606b2a62<br>
**Scope:** Supplied archive and pinned current upstream, resource-list migration, student journey and content breadth, reusable question/solution contracts, local implementation/build/tests, publication, and release blockers.

The reference-directory campaign was already present in baseline `b4e1980`; this follow-up adds a shared structured question contract, a data-driven code-reading quiz, question-level coverage evidence, and independent answer tests. It does not claim complete curriculum parity, expert-approved teaching, validated mastery measurement, verified third-party recommendations, or secure release readiness. Automated checks establish structure and selected behavior; human review remains necessary.

## Executive result

Tajkart is a student-first static learning platform: a student can choose a goal, follow one of six metadata-backed course paths, practise, build project evidence, and optionally save checkmarks or portfolio notes in the current browser. The current content includes 18 original lessons, six courses, formative practice, a prerequisite-aware planner, local skill evidence, and a portfolio draft tool. The reference-directory campaign adds opt-in search over 10,583 source-attributed candidate destinations. This follow-up makes the algebra assessment and four-question code-reading quiz use a shared structured question contract, adds independent execution checks for the quiz examples, and generates a 30-question solution coverage report from repository content and tests.

The candidate passes source validation, 59 Python tests, Node checks, Ruby front-matter validation, a strict production Jekyll build, generated HTML checks, candidate-data integrity checks, generated quiz-choice/disclosure checks, and the existing focused headless Chrome interaction checks. After two early hosted failures exposed PyYAML imports absent from the runner, those imports were removed. GitHub Actions run [38800374330](https://github.com/shahanishashmi/tajkart-student-hub/actions/runs/38800374330) passed build and deploy for `53651211597f74f6d217cd4eab0d68ff850a6fbb`. The build produces 124 HTML routes and a Tajkart search index with 90 resources (88 English originals and two Hindi/Urdu draft translations). The separate reference index contains 10,583 unique, still-unverified link candidates. Of 30 discovered questions, all have a written answer and explanation, and each has question-specific automated test evidence; all 30 still await human educational review. Sixteen static prompts lack machine-readable answer formats and per-question skill/lesson mappings, so they remain manual-comparison tasks.

This is a useful student-first foundation, not a comprehensive all-subject curriculum. Mathematics and algebra are short English drafts; most school and college subjects are absent. The verified third-party catalogue remains empty: the separate imported directory is explicitly a candidate list, not an approved recommendation set. Progress is browser-local and not synced. No human content, translation, rights, or accessibility sign-off has been recorded. GitHub Pages HTTPS enforcement remains off. The campaign's hosted CI result is reported separately from local checks.

## Product journey

1. **Start:** [Getting started]({{ '/getting-started/' | relative_url }}) offers routes for programming, CS/IT, academic study, portfolio building, and career preparation.
2. **Discover:** the learning library, subject map, courses, practice, projects, study resources, careers, and language paths link to authored pages. Default search covers Tajkart's own resources; a separate opt-in loads unverified reference candidates by title/topic/type and source-list locale, with source links and the unverified/rights-not-assessed state visible.
3. **Study and plan:** the [study-skills guide]({{ '/learning/study-skills/' | relative_url }}) provides general study methods. The [planner]({{ '/learning/planner/' | relative_url }}) generates sessions and prerequisite prompts from six courses' resource metadata.
4. **Practice:** the code-reading quiz and algebra self-check accept explicit answer formats, show hints and worked explanations, and provide limited skill-linked feedback. Attempts are optional browser-local records.
5. **Build:** seven project briefs describe deliverables and rubrics. The student portfolio page can save a learner's own draft notes in local storage; it does not publish or certify work.
6. **Grow:** five career guides cover resumes, interviews, internships, professional email, and entry-level learning paths.

The product has no student accounts, cross-device sync, server-side progress storage, personalized AI tutor, hosted code runner, job feed, or learner tracking. Lesson checkmarks, quiz correctness, and skill evidence are stored and described separately.

## Reference comparison and capability matrix

The supplied `free-programming-books-main.zip` has 233 files and verified SHA-256 `a57382573afb96eed8623f41884e049b12b9fab54dcf43815629437906abd1e1` (the extra final `1` corrects a truncated hash in older reports). Its historical upstream identity is commit `2574d859ecf34dd8d1643cc5c7c9f11ae99f845c`. Read-only `git ls-remote` confirmed current upstream `main` at `4c301cce10db10026d632606b5167a9d1b8cd4ec`. The two trees each have 233 paths and no path additions/removals; 226 files differ in content overall, including 117 of the 120 Markdown list files in `books/`, `courses/`, `casts/`, and `more/`. No source scripts, Actions, workflows, designs, or lesson content were executed or copied. Unlike the earlier audit, this campaign deliberately imports source-attributed link-list metadata under the reference repository's CC BY 4.0 license; that license does not extend to the separately linked works.

| Reference/student capability | Tajkart evidence | Status and concrete gap |
|---|---|---|
| Books and external learning directories | 10,583 unique candidate destinations from books, courses, media, cheatsheets, interactive tutorials, problem sets, and playgrounds, with 10,796 source appearances retained. | **Directory implemented as unverified candidates.** Search is opt-in and shows provenance; provider, availability, learner suitability, terms, and rights for the linked works have not been checked. Zero candidates are approved as verified recommendations. |
| Original lessons and language indexes | 18 lessons: 10 programming and 8 mathematics/data/algebra; 11 introductory programming-language paths. | **Partial.** These are short units and introductions, not complete curricula. Expert review is pending. |
| Courses and learning paths | Six original plans: programming foundations, data structures, web foundations, intermediate Python, mathematics foundations, and algebra foundations. | **Implemented locally, partial in breadth.** Explicit resource mappings power the planner; intermediate/advanced study across subjects is missing. |
| Cheatsheets and study resources | Ten original cheatsheets, one study-skills guide, one reading guide. | **Partial.** Computing-focused; technical and education review and broader academic study support remain. |
| Interactive tutorials and quizzes | A prediction activity, four-question code-reading quiz and ten-question algebra check share the structured assessment contract for hints, choices, worked solutions, skills, prerequisites, verification and review status. | **Implemented locally.** Fixed questions and deterministic feedback; the 4-question quiz renders 11 choices and keeps worked answers hidden until requested. No arbitrary learner code execution. Educator, keyboard, and assistive-technology review remain. |
| Assessment and mastery | Stable question IDs, answer formats, skills, hints, explanations, testable answer derivations, and an explicit evidence threshold. | **Partial.** Threshold is a product heuristic, not a validated educational mastery model. No partial credit or reasoning evaluation. |
| Planner and learner progress | Six paths produce 33 sessions with prerequisites, local checkmarks, time estimates, and next-step recommendations. | **Implemented locally.** No account, sync, streaks, or adaptive difficulty. Self-reported completion is not mastery. |
| Problem sets and solutions | Eleven problem sets, including mixed math and algebra; eight Python solutions and SQL examples have tests. | **Partial.** More difficulty levels and human review remain; test success is not teaching approval. |
| Projects and playgrounds | Seven project briefs, including the Python study-log capstone; local portfolio draft fields. | **Partial.** Briefs are specifications, not finished apps. No hosted playground or external playground catalogue. |
| Podcasts and screencasts | Original guidance and metadata schema. | **Guide only.** No verified channel or episode directory. |
| Academic student support | Goal-based start guide, study-skills guide, eight English mathematics/data/algebra lessons, two short courses, and two formative assessments. | **Early coverage.** Drafts only; geometry, broader statistics, science, humanities, and most other academic subjects remain absent. The 46 mapped reference headings do not represent 46 complete Tajkart courses. |
| Careers and opportunities | Five career guides and verification advice. | **Guidance present.** No current job, scholarship, internship, or discount listings are claimed. |
| Translation and localization | One Hindi and one Urdu draft translation of the Python variables lesson; Unicode and RTL-aware styles. | **Partial.** Both drafts await fluent review. The 57 locale records belong to the reference snapshot, not Tajkart translations. |
| Search and discovery | Generated Tajkart index with 90 resources plus a separate 10,583-destination candidate index; opt-in source-locale and topic filters. | **Implemented locally.** The candidate file is lazy-loaded and not included in the default Tajkart search count. Browser, accessibility, and usability review remain open. |
| Contribution and editorial process | Contribution guide, schemas, review metadata, issue/PR templates, code of conduct, and editorial guidance. | **Partial.** Rights-holder still needs to decide explicit reuse permission for substantial outside contributions. |
| Validation and maintenance | SHA-pinned Pages workflow, source/schema checks, Python/Node/Ruby checks, Jekyll build, generated HTML validation. | **Local and hosted checks pass.** Two early hosted runs exposed PyYAML imports in the coverage script and test module; both now use the built-in parser. Run `38800374330` passed build and deploy. No full external-link crawl or scheduled freshness process was run. |
| Accessibility and responsive design | Semantic landmarks, skip link, visible focus, reduced-motion and RTL-aware CSS, structural HTML validation. | **Automated checks plus narrow browser smoke test.** Human keyboard, zoom/reflow, mobile, RTL, screen-reader, and contrast review remain open. |

The historical file-level reference mapping is in the [reference parity matrix]({{ '/docs/REFERENCE_PARITY_MATRIX/' | relative_url }}), which is explicitly marked as superseded for Tajkart's current counts. Source snapshot and taxonomy notes are in the [reference coverage audit]({{ '/docs/REFERENCE_COVERAGE/' | relative_url }}).

## Reference listing migration {#reference-migration}

The generated [candidate inventory]({{ '/data/reference_resources.json' | relative_url }}) is from current upstream commit `4c301cce10db10026d632606b5167a9d1b8cd4ec`. It is 8.6 MB, loaded only after the student opts in, and kept separate from the 90 Tajkart-authored/translated search resources.

| Reconciliation evidence | Supplied ZIP snapshot (`2574d859`) | Current upstream (`4c301cce`) | Disposition |
|---|---:|---:|---|
| Resource-list Markdown files | 120 | 120 | Same paths; 117 source files changed contents and three did not. |
| External resource list appearances | 10,792 | 10,796 | 10,791 row appearances match; one old row was removed and five current rows were added. |
| Unique primary destinations | 10,579 | 10,583 | 10,578 destinations are shared; one archive-only destination is retired from the current index and five destinations are current-only additions. |
| Repeated appearances | 213 | 213 | Deduplicated into one candidate record per normalized destination; every appearance and source location remains in the JSON. |
| Additional/alternate links | 131 | 131 | Kept on their source occurrence; includes alternate formats/links and the EPUB continuation attached to its preceding book row. |
| Parser exceptions | 0 | 0 | Every external URL line in the four source listing directories was parsed as a resource row or attached continuation. |

The sole archive-only URL is [Python Notes | Hindi](https://ehindistudy.com/2022/10/12/python-pdf-notes-hindi/); it no longer appears in the checked current source. The five current-only URLs are [BugBot Lab](https://app.bugbotlab.com), [Кодолимп](https://codolymp.ru/catalog), [nvim-edu](https://s3onghyun.github.io/nvim-edu/), [BugBot Lessons](https://www.bugbotlab.com/lessons/), and [Vibe Coding for Beginners](https://www.youtube.com/playlist?list=PLLRVNOCjAuec). These are migration dispositions only; none was opened or checked for rights, access, suitability, availability, or current content.

The current inventory classifies unique destinations from source paths and explicit media labels: 4,728 books, 4,513 courses, 320 cheatsheets, 245 interactive tutorials, 192 playgrounds, 128 problem-set links, 379 podcast links, 106 screencasts, and 29 media links without a source label. Category counts can overlap where one URL appears in multiple formats. Records retain source file, line, source section/topic path, raw source-list locale, title, URL, source annotations, alternate links, stable destination ID, and all duplicate appearances. The source-list locale codes are index provenance; they are not proof of each linked work's language. The extracted candidate index contains 52 distinct list-locale codes, not 52 Tajkart translations.

Every record has `verification_status: unverified`, `rights_status: not-assessed`, and `access_status: not-checked`. The source index's CC BY 4.0 applies to the migrated listing data with attribution; it does not grant rights in the listed books, courses, videos, or websites. The dataset includes its attribution, license link, source revision, source-file hashes, and a note describing extraction/deduplication. The root Tajkart `LICENSE` was not changed. No linked file, lesson, solution, transcript, or media was downloaded or republished. No candidate was promoted into the verified-resource schema or marked searchable in the default index.

Search adds a checkbox that is off by default. When enabled, it fetches the separate static JSON, offers type/topic and reference-list-locale filters, shows each destination as unverified with rights/access unreviewed, links to the source row at the pinned GitHub revision, and displays at most 100 matches while reporting the total. Candidate results are not described as free, approved, or safe. A failed automated request would not remove a candidate. `node tests/search_test.js` verifies that the 8.6 MB candidate index is not fetched until opt-in, that the candidate state and attribution link appear, that source locale filtering works, and that disabling opt-in removes candidates from the result set.

The import is deterministic and rerunnable. `scripts/import_reference_resources.py` checks the audited ZIP hash by default, accepts a pinned source revision and explicit input hash for another snapshot, groups duplicates by scheme/host case and fragment, and preserves malformed lines in an exception list instead of dropping them. Rebuild the current dataset from a checkout of the pinned upstream commit with:

```powershell
git archive --format=zip --prefix=free-programming-books-main/ --output=fpb-current.zip 4c301cce10db10026d632606b5167a9d1b8cd4ec books courses casts more
python scripts/import_reference_resources.py --archive fpb-current.zip --revision 4c301cce10db10026d632606b5167a9d1b8cd4ec --expected-sha256 41ef6a05d433fe59454d57d81ad6512e20857e926bc1a6273741c2352fecc410 --output data/reference_resources.json
python scripts/import_reference_resources.py --check --output data/reference_resources.json
```

The generated source archive hash above identifies the selected resource-list directories in that pinned checkout. Rebuilding the supplied historical ZIP with the default revision/hash validates its 10,792 appearances separately; it does not replace the current-upstream candidate dataset.

## Authored inventory and editorial state

Current source metadata counts **90 Tajkart search resources: 88 English originals and two draft translations**. Separately, the source validator sees 137 Markdown files, Jekyll generates 124 HTML pages, and the default generated Tajkart search index contains 90 entries. The separate reference index has 10,583 unique destinations and is not included in that count.

- **18 lessons:** 10 programming and 8 arithmetic/data/algebra mathematics lessons.
- **13 guides:** 12 computing subject guides plus one study-skills guide.
- **11 language paths:** introductory programming-language indexes, not full courses.
- **6 courses:** programming foundations, data structures, web foundations, intermediate Python, mathematics foundations, and algebra foundations.
- **10 cheatsheets; 11 problem sets; 7 project briefs; 2 interactive resources; 5 career guides; 1 student start guide.**
- **External directory:** 10,583 unverified link candidates with source attribution; zero verified book, course, media, playground, job, internship, scholarship, or discount records.

The eight mathematics/data/algebra lessons, two mathematics courses, two math problem sets, seven-question arithmetic/data check, and ten-question algebra assessment remain drafts with `review_status: pending`. The four structured code-reading questions also remain pending. The Python intermediate sequence and capstone, student start guide, and study-skills guide await their respective human reviews. The two translations await fluent Hindi and Urdu review. No automated pass changes an editorial status.

<!-- solution-coverage:begin -->

## Question and solution coverage

<!-- Generated from problem-set front matter, structured assessment JSON, and test references by `scripts/solution_coverage.py`. -->

Counts are repository-derived. ‘Automated verification evidence’ means a matching test is present; its pass/fail result is established by the validation table below. Static programming prompts are not scored by string-matching learner code.

| Measure | Count |
|---|---:|
| Questions discovered across problem sets and interactive assessments | 30 |
| Questions with an answer record and solution | 30 |
| Questions with a worked solution and explanation field/text | 30 |
| Questions with question-specific automated test evidence | 30 |
| Questions awaiting human educational review | 30 |
| Questions without a machine-readable accepted-answer format | 16 |
| Questions without a per-question skill and lesson mapping | 16 |
| Broken structured skill, lesson, prerequisite, or source mappings | 0 |
| Questions missing a worked-answer record | 0 |

The unstructured tasks inherit subject tags, objectives, and prerequisites from their problem-set page; they do not have per-question machine-scored answer contracts. Their written answers remain available for manual comparison. The interactive quiz and algebra check use the shared JSON question schema, accepted formats, prerequisite and lesson mappings, common-mistake guidance, provenance, and review status. Automated checks do not establish teaching quality.

No third-party answer keys or solution files were imported. The reference index contains outbound link candidates only; linked works were not copied. Open-ended solution code is reviewed by running the repository's canonical tests, not by executing learner submissions.

### Per-question status

| Question ID | Source | Answer format | Automated verification evidence | Human review |
|---|---|---|---|---|
| `python-assignment-tracing-001` | `/learning/interactive-tutorials/quiz/` | integer | `tests/test_interactive_quiz_answers.py` executes the stored example and derives its answer | pending |
| `python-condition-branch-001` | `/learning/interactive-tutorials/quiz/` | text | `tests/test_interactive_quiz_answers.py` executes the stored example and derives its answer | pending |
| `python-list-index-001` | `/learning/interactive-tutorials/quiz/` | integer | `tests/test_interactive_quiz_answers.py` executes the stored example and derives its answer | pending |
| `python-loop-count-001` | `/learning/interactive-tutorials/quiz/` | integer | `tests/test_interactive_quiz_answers.py` executes the stored example and derives its answer | pending |
| `algebra-combine-like-terms-001` | `/learning/problem-sets/algebra-foundations-check/` | integer | `tests/test_algebra_foundations.py` independently derives the answer from its equation contract | pending |
| `algebra-evaluate-study-hours-001` | `/learning/problem-sets/algebra-foundations-check/` | integer | `tests/test_algebra_foundations.py` independently derives the answer from its equation contract | pending |
| `algebra-one-step-addition-001` | `/learning/problem-sets/algebra-foundations-check/` | integer | `tests/test_algebra_foundations.py` independently derives the answer from its equation contract | pending |
| `algebra-one-step-negative-001` | `/learning/problem-sets/algebra-foundations-check/` | integer | `tests/test_algebra_foundations.py` independently derives the answer from its equation contract | pending |
| `algebra-one-step-subtraction-001` | `/learning/problem-sets/algebra-foundations-check/` | integer | `tests/test_algebra_foundations.py` independently derives the answer from its equation contract | pending |
| `algebra-one-step-zero-001` | `/learning/problem-sets/algebra-foundations-check/` | integer | `tests/test_algebra_foundations.py` independently derives the answer from its equation contract | pending |
| `algebra-two-step-fraction-001` | `/learning/problem-sets/algebra-foundations-check/` | fraction | `tests/test_algebra_foundations.py` independently derives the answer from its equation contract | pending |
| `algebra-two-step-integer-001` | `/learning/problem-sets/algebra-foundations-check/` | integer | `tests/test_algebra_foundations.py` independently derives the answer from its equation contract | pending |
| `algebra-two-step-negative-001` | `/learning/problem-sets/algebra-foundations-check/` | fraction | `tests/test_algebra_foundations.py` independently derives the answer from its equation contract | pending |
| `algebra-zero-coefficient-001` | `/learning/problem-sets/algebra-foundations-check/` | text | `tests/test_algebra_foundations.py` independently derives the answer from its equation contract | pending |
| `problem-array-total-001-q01` | `/learning/problem-sets/array-total/` | manual comparison | `tests/test_solutions.py` executes the canonical solution module | pending |
| `problem-binary-search-004-q01` | `/learning/problem-sets/binary-search/` | manual comparison | `tests/test_solutions.py` executes the canonical solution module | pending |
| `problem-factorial-recursion-006-q01` | `/learning/problem-sets/factorial-recursion/` | manual comparison | `tests/test_solutions.py` executes the canonical solution module | pending |
| `problem-first-duplicate-002-q01` | `/learning/problem-sets/first-duplicate/` | manual comparison | `tests/test_solutions.py` executes the canonical solution module | pending |
| `problem-graph-reachability-008-q01` | `/learning/problem-sets/graph-reachability/` | manual comparison | `tests/test_solutions.py` executes the canonical solution module | pending |
| `problem-insertion-sort-005-q01` | `/learning/problem-sets/insertion-sort/` | manual comparison | `tests/test_solutions.py` executes the canonical solution module | pending |
| `problem-math-foundations-check-010-q01` | `/learning/problem-sets/math-foundations-check/` | manual comparison | `tests/test_math_foundations.py` independently recalculates every listed answer | pending |
| `problem-math-foundations-check-010-q02` | `/learning/problem-sets/math-foundations-check/` | manual comparison | `tests/test_math_foundations.py` independently recalculates every listed answer | pending |
| `problem-math-foundations-check-010-q03` | `/learning/problem-sets/math-foundations-check/` | manual comparison | `tests/test_math_foundations.py` independently recalculates every listed answer | pending |
| `problem-math-foundations-check-010-q04` | `/learning/problem-sets/math-foundations-check/` | manual comparison | `tests/test_math_foundations.py` independently recalculates every listed answer | pending |
| `problem-math-foundations-check-010-q05` | `/learning/problem-sets/math-foundations-check/` | manual comparison | `tests/test_math_foundations.py` independently recalculates every listed answer | pending |
| `problem-math-foundations-check-010-q06` | `/learning/problem-sets/math-foundations-check/` | manual comparison | `tests/test_math_foundations.py` independently recalculates every listed answer | pending |
| `problem-math-foundations-check-010-q07` | `/learning/problem-sets/math-foundations-check/` | manual comparison | `tests/test_math_foundations.py` independently recalculates every listed answer | pending |
| `problem-sql-session-summary-009-q01` | `/learning/problem-sets/sql-session-summary/` | manual comparison | `tests/test_sql_examples.py` executes the exact SQL block from this page in SQLite | pending |
| `problem-string-vowel-count-003-q01` | `/learning/problem-sets/string-vowel-count/` | manual comparison | `tests/test_solutions.py` executes the canonical solution module | pending |
| `problem-tree-height-007-q01` | `/learning/problem-sets/tree-height/` | manual comparison | `tests/test_solutions.py` executes the canonical solution module | pending |

### Blocked or excluded solution records

No local problem-set question is missing a worked-answer record. Third-party linked works are excluded from solution content because their material and reuse rights were not reviewed.

<!-- solution-coverage:end -->

## Phase 3/4 implementation details

| Area | What was implemented | Limits and follow-up |
|---|---|---|
| Algebra sequence | Original lessons on variables/expressions, one-step equations, and introductory two-step equations; course mapping, prerequisites, worked transformations, mistakes, hints, practice, and next steps. | Pending mathematics educator review; not a complete algebra curriculum. |
| Data-interpretation unit | Original table/chart lesson covers totals, mean, median, shares, zero versus missing values, chart scales, and limits of causal claims; it is sequenced after percentages in the academic foundations path. | Runnable Python example and selected numeric answers pass tests; remains an English draft pending mathematics educator review. |
| Structured algebra assessment | Ten question records in _data/algebra_assessment.json plus data/assessment_question.schema.json. Each includes stable ID, skill/lesson mapping, level, accepted answer formats, hint, solution/explanation, derivation metadata, and pending review state. | Validates expected answers and metadata, not learner reasoning, partial credit, or psychometric quality. |
| Independent answer checks | Python Fraction-based derivations and substitution; coverage for negative and rational answers and zero-coefficient identity/contradiction cases. All lesson code examples were executed and matched the documented output. | A matching test result is not an independent human review. |
| Mastery evidence | Rules-based attempt records by skill and practice session; the interface explains the threshold: at least five attempts, two sessions, and 80% on the latest five. Repeated errors can recommend a linked lesson. | This is not adaptive learning, an AI tutor, or a validated mastery measure. A small number of attempts cannot establish skill. |
| Study planner | Catalog generated from six course pages and explicit related_resources; 33 sessions, lesson/prerequisite routes, time estimates, local checkmarks, and next-step recommendations. | Local storage is optional and not private from anyone with access to the browser profile; time is estimated; sequence quality needs educator review. |
| Portfolio drafts | Optional title, summary, skills, status, and project URL stored locally. URL validation requires HTTPS and no embedded credentials; safe DOM text rendering prevents entered markup from becoming elements. | Drafts are neither submitted nor published, synced, verified, or certified. Users should not save secrets or sensitive information. |
| Validator and regressions | Self-prerequisite and directed-cycle detection; assessment ID/schema/skill/route/answer-format/review consistency checks; SQL null/non-positive/tie/empty cases. | Graph integrity cannot prove prerequisite appropriateness; SQL execution was tested with SQLite only. |
| Cross-platform assessment tooling | Two early hosted runs exposed PyYAML imports in the coverage script and its test module; both now use the existing standard-library front-matter helpers. Source validation and all 59 Python tests pass locally. | Corrected commit `5365121` passed the hosted build and deployment workflow. |

The Phase 3 controls are local and deterministic; they do not create a student account, claim to assess a learner's complete ability, or execute learner-supplied code.

## Validation and browser evidence

All local checks below are run against the campaign worktree on 2026-10-15. The production build uses a unique temporary output directory; the repository `_site/` directory is preserved.

| Check | Result | Evidence/limit |
|---|---|---|
| `python scripts/validate_site.py` | **Pass:** 137 Markdown files, 124 routes, 90 Tajkart search resources. | Required metadata, unique IDs/routes, local links, known references, Python syntax, prerequisite self/cycle checks, and structured assessment contracts passed. |
| `python scripts/import_reference_resources.py --check` | **Pass:** 120 source files, 10,796 source appearances, 10,583 unique destinations, 213 repeated appearances, 131 additional links, zero exceptions. | Candidate IDs, URLs, provenance, source files, counts, attribution, and unverified/rights-not-assessed states validate. |
| `python scripts/solution_coverage.py --check` | **Pass:** 30 questions; 30 written answers/explanations and test evidence; zero broken structured mappings. | Finds 16 static prompts without a machine-readable answer format or per-question mapping; all 30 remain pending human review. |
| `python -m unittest discover -s tests -v` | **Pass: 59 tests.** | Includes algebra and math derivations, all four quiz examples executed with answers derived from their output, shared assessment-contract/choice checks, importer parsing and reconciliation, prerequisite graph, study-log helpers, solution modules, provenance, and SQLite edge cases. |
| Node syntax and tests | **Pass:** asset/test syntax checks plus search, navigation, and learning-tools tests. | Search candidate index loads only after opt-in; provenance, source attribution, source-list locale, local search, menu/routes, local storage, answer formats, recommendations, and portfolio checks pass. |
| Ruby front matter | **Pass:** Ruby 3.3.12 parsed 127 Markdown front-matter files and five YAML files. | Ruby was invoked from `C:\Ruby33-x64\bin` because it is not on this shell's PATH. |
| Strict production Jekyll build | **Pass:** 124 generated HTML pages and 90 default search records. | Production mode, strict front matter, unique temp destination. Known non-blocking notice: optional faraday-retry middleware is absent. |
| Generated HTML validation | **Pass:** 124 HTML pages, 90 Tajkart search resources, and 10,583 unverified candidates copied into the output. | Local routes/fragments, IDs, labels, language, landmarks, candidate-index presence, and provenance structure passed. The quiz page has four questions, 11 radio choices, mapped lesson/prerequisite links, and hidden solution disclosures. |
| Generated data integrity | **Pass:** six courses, 33 planner sessions, ten algebra questions and solution disclosures; all session and prerequisite routes resolve. | Parsed from generated output rather than inferred from Markdown source. |
| Headless Chrome 154 interaction check | **Pass for the earlier planner/quiz/portfolio sample** at 375 × 812 CSS pixels. | Planner recommendation, quiz feedback, local portfolio validation, and no horizontal overflow on those pages were checked. The new reference opt-in behavior has Node interaction tests, not a real-browser session. |
| git diff --check | **Pass:** no whitespace defects. | Git printed line-ending normalization notices on existing CRLF-configured files. |

The browser pass verifies selected DOM interactions at one narrow viewport, not visual quality across devices. No manual keyboard-only, screen-reader, color-contrast, zoom, RTL, or learner-usability review was completed. No human technical, mathematics, translation, or rights-holder review was completed. No full external URL crawl was run; all 10,583 candidates remain unverified. Hosted CI status is not inferred from these local checks.

## Selected outbound source checks

These optional links support further study; they are **not** verified catalogue records. Five earlier checks fetched the official pages with bounded requests and received HTTP 200 on 2026-10-15. Three Khan Academy algebra pages were opened on the official provider domain for topic relevance on 2026-10-15. None reviewed licensing/terms, captions/accessibility, region/device access, or long-term availability. No content was copied.

| Official page | Intended context | Check boundary |
|---|---|---|
| [Khan Academy: dividing fractions](https://www.khanacademy.org/math/arithmetic-home/arith-review-fractions/dividing-fractions) | Optional practice after fractions. | Earlier bounded GET: HTTP 200; rights/accessibility not reviewed. |
| [Khan Academy: fractions, decimals, and percents](https://www.khanacademy.org/math/algebra-basics/basic-alg-foundations/e/relate-fractions--decimals--and-percents) | Optional practice after conversions. | Earlier bounded GET: HTTP 200; dynamic page. |
| [Khan Academy: rates and percentages](https://www.khanacademy.org/math/cc-seventh-grade-math/cc-7th-fractions-decimals) | Optional practice after percentages. | Earlier bounded GET: HTTP 200; terms and learner access not audited. |
| [Python fractions docs](https://docs.python.org/3/library/fractions.html) and [Python decimal docs](https://docs.python.org/3/library/decimal.html) | Verify arithmetic APIs used in examples. | Earlier bounded GET: both HTTP 200; not catalogue entries. |
| [Khan Academy: variables and expressions](https://www.khanacademy.org/math/als-k-to-12-math/x54b4346ef80b5dcc%3Aperformance-standard-e/x54b4346ef80b5dcc%3Aalgebraic-numerical-expressions-and-equations/v/variables-expressions-and-equations) | Optional companion for expressions. | Official page opened for topic relevance; terms and accessibility not audited. |
| [Khan Academy: one-step equation review](https://www.khanacademy.org/math/pre-algebra/pre-algebra-equations-expressions/pre-algebra-equation-word-problems/a/one-step-equation-review) | Optional review. | Official page opened for topic relevance; terms and accessibility not audited. |
| [Khan Academy: algebra course](https://www.khanacademy.org/math/algebra-home/alg-basic-eq-ineq) | Optional next study resource. | Official page opened for topic relevance; terms and accessibility not audited. |

A full crawl was not run. A timeout, redirect, or automated block must enter a human review queue and must not alone cause removal. The reference ZIP's license does not grant rights to separately linked works.

## Deployment and release gates

These hosting facts are the latest recorded evidence in [deployment recovery]({{ '/docs/DEPLOYMENT/' | relative_url }}) and [the P0 incident report]({{ '/docs/P0_INCIDENT_REPORT/' | relative_url }}); they were **not re-probed during this content pass**:

- The project URL https://shahanishashmi.github.io/tajkart-student-hub/ serves with valid TLS, but HTTP also serves the site and the Pages API reports https_enforced: false.
- The owner authorized enabling **Enforce HTTPS** for that project URL. The API update was rejected with HTTP 404, “The certificate does not exist yet”; no setting changed. Retry only that setting after GitHub reports certificate readiness.
- Latest recorded probes show apex/www returning GitHub Pages 404 and learn.shahanishashmi.me unresolved. No DNS or _config.yml change is authorized by the current project-URL instruction; keep the known hostname issue visible.
- Baseline `b4e1980` is published on `main`; it contains the reference candidate directory and student learning tools. Actions runs [38799996735](https://github.com/shahanishashmi/tajkart-student-hub/actions/runs/38799996735) and [38800191889](https://github.com/shahanishashmi/tajkart-student-hub/actions/runs/38800191889) found PyYAML imports unavailable on the runner; those failures were fixed. The final run [38800374330](https://github.com/shahanishashmi/tajkart-student-hub/actions/runs/38800374330) passed both build and deploy for `5365121`. HTTPS enforcement remains a separate blocker: the project setting is off, HTTP still serves the site, and the earlier authorized API update reported that the certificate does not exist yet. Do not infer secure-release readiness from a successful Pages workflow.
- Human mathematics/programming review, fluent Hindi/Urdu review, manual accessibility review, contributor-rights decision, and any third-party catalog review remain outstanding.

Do not call this secure-release ready until HTTPS enforcement is confirmed, hosted Actions succeeds for the reviewed commit, the selected browser/release smoke checks pass, and the human review states are truthful.

## Worktree and change record

The pre-existing worktree was clean and synchronized at `b4e19802d7dfd1c43b83bc1fd621e61b606b2a62` before this follow-up. Commits `ec999ba4f02294f63df7b1e1a17115fabf83a008`, `cd720928e34fa8c67a04ef0c406c0d6a0d8b335d`, and `53651211597f74f6d217cd4eab0d68ff850a6fbb` were pushed to `main`. The two initial workflow failures identified unavailable PyYAML imports; the standard-library correction passed local tests and GitHub Actions build/deploy run `38800374330`. No DNS, Pages settings, or license was changed.

Core files added/used for this increment include _data/algebra_assessment.json, data/assessment_question.schema.json, assets/js/learning-tools.js, learning/planner/index.md, the algebra course/lessons/problem set, the student portfolio brief, tests/learning_tools_test.js, tests/test_algebra_foundations.py, and tests/test_assessment_contract.py. Core integration points include assets/js/site.js, assets/css/site.css, _layouts/default.html, scripts/validate_site.py, .github/workflows/pages.yml, and the content/progress/audit documents. The full accumulated path list remains available in git status --short.

No DNS/Pages mutation, license change, or deployment command was run directly. Any Pages deployment is initiated only by the repository's existing main-branch workflow. Generated builds were written to temporary directories; `_site/` was preserved.

## Recommended next content move

Next, convert appropriate existing static problem questions to the shared question model in a bounded batch. Start with the seven arithmetic/data questions: add stable question IDs, explicit skills/lesson mappings, answer formats where deterministic checking is sound, verification evidence, and keep any reasoning-heavy prompt as manual review. Do not force machine scoring on open-ended programming tasks. Once educators review the current arithmetic-to-algebra sequence, add an original **linear-equation word problems and modeling** unit with tested numeric examples and a formative assessment.

The immediate release task remains retrying the already authorized HTTPS enforcement control once GitHub makes a certificate available. The complete ordered queue is in [next steps]({{ '/docs/NEXT_STEPS/' | relative_url }}); this report is the single consolidated audit snapshot.
