---
layout: page
title: Next-phase audit and roadmap
description: Evidence-based baseline, release blockers, review gates, and prioritized roadmap for Tajkart Student Hub.
permalink: /docs/ROADMAP_NEXT_PHASE/
---

> **Superseded status note:** The implementation and reference inventory have advanced since this roadmap snapshot. See the [combined current audit]({{ '/docs/MASTER_AUDIT_REPORT/' | relative_url }}) for the candidate-directory migration, updated content counts, validation results, and the remaining HTTPS/human-review gates.

> **Current-state note (2026-10-15):** This roadmap preserves the earlier release sequence and Pages recovery analysis. Its product/content counts and next-content recommendation predate the algebra assessment, local study planner, mastery evidence, and portfolio draft tool. Use the [combined platform audit]({{ '/docs/MASTER_AUDIT_REPORT/' | relative_url }}) for the current implementation and validation snapshot, and [next steps]({{ '/docs/NEXT_STEPS/' | relative_url }}) for the current queue.

**Audit date:** 2026-10-15

**Repository:** `shahanishashmi/tajkart-student-hub`

**Reference:** [EbookFoundation/free-programming-books at audited commit `4c301cce`](https://github.com/EbookFoundation/free-programming-books/tree/4c301cce10db10026d632606b5167a9d1b8cd4ec)

This is the project execution plan and evidence record. It distinguishes original Tajkart content from third-party directories and selects one next task. No content was copied from the reference. This recheck made no DNS or Pages-setting changes and did not commit, push, or deploy.

## Executive decision

Tajkart is deployed from commit `d60d3c5`; its GitHub Actions build and Pages deployment both succeeded. The default project URL and its nested pages currently serve over HTTPS with valid certificate checks, but the same site also serves over HTTP without redirecting to HTTPS. The Pages API reports `https_enforced: false`. The prior redirect to the apex was not reproduced in this recheck. The personal-domain apex and `www` now return GitHub Pages 404 responses, direct HTTPS to the apex fails hostname validation, and `learn.shahanishashmi.me` has no DNS record. The site is therefore **not secure-release ready**, and the personal homepage's current state is unknown.

The reference is a multilingual directory of links to learning resources. Tajkart has built original guides, courses, practice, and career advice across similar categories; it has **not** built an equivalent external-resource directory. Search indexes Tajkart's own pages, and the verified external learning-resource inventory is empty. Category pages and taxonomy mappings do not establish complete course, book, or language coverage.

**Recommended immediate task — P0, authorized but blocked:** The owner authorized **Enforce HTTPS** for Tajkart's existing GitHub Pages project URL. GitHub rejected the settings API update with HTTP 404, `The certificate does not exist yet`; the setting remains off, and HTTP still serves the page without redirect. Resolve the Pages certificate/control mismatch, then retry only enforcement and verify the redirect. This requires no DNS or `_config.yml` change. Leave apex and `www` records untouched; their sites currently return 404, so do not claim the personal homepage is preserved or restored. If GitHub confirms enforcement is unavailable or the owner chooses a branded hostname, use the separately documented `learn` subdomain plan after domain/DNS ownership is confirmed. See [current deployment evidence and action package]({{ '/docs/DEPLOYMENT/' | relative_url }}).

## Verified baseline

### Git, workflow, and local checks

| Item | Verified state |
|---|---|
| Branch and commit | Branch `main`; `HEAD`, local `origin/main`, and live `origin/main` all resolve to `d60d3c55589b05b16415c812ff4eb06cc553eb97`. The worktree was clean at the start of this recheck. |
| Hosted Pages workflow | GitHub Actions run [38628224439](https://github.com/shahanishashmi/tajkart-student-hub/actions/runs/38628224439) completed successfully for exact SHA `d60d3c5`; both `build` and `deploy` passed. |
| Source validation | `python scripts/validate_site.py` passed with 114 Markdown files, 101 routes, and 70 searchable resources after adding the P0 incident report; no missing required fields, duplicate IDs/routes, invalid curated source URLs, unknown references, Python syntax errors, or broken local Markdown links. |
| Python and search tests | `python -m unittest discover -s tests -v`: 16 passed. `node --check assets/js/site.js` and `node tests/search_test.js`: passed. |
| Front matter and YAML | Ruby 3.3.12 / Bundler 2.5.22. Re-run `ruby scripts/validate_front_matter.rb` parsed 103 Markdown front-matter blocks and five YAML inventories/configuration files. |
| Production build and generated HTML | `JEKYLL_ENV=production bundle exec jekyll build --destination <temporary-directory>` passed outside the worktree. `python scripts/validate_html.py <build-output>` passed for 100 HTML pages and all 70 search resources, including local links/fragments, IDs, labels, language, landmarks, and provenance metadata. Jekyll emitted a non-blocking notice that optional Faraday retry middleware is not installed. |
| Review state | A front-matter scan of all 70 searchable Markdown resources found `review_status: pending` on all 70. No human technical, fluent Hindi/Urdu, accessibility, or licensing review was performed by this audit. |
| Current documentation edits | The original `d60d3c5` recheck began clean. Since then, eight tracked documentation files are modified and `docs/P0_INCIDENT_REPORT.md` is untracked; nothing is staged. Current edits remain local and uncommitted. |

The hosted run and local checks establish a healthy build for `d60d3c5`. They do not establish HTTPS enforcement, expert correctness of teaching content, or human accessibility approval. No external-link crawl, browser interaction session, vulnerability scan, or assistive-technology test was run for this recheck.

### Reference snapshot

The supplied ZIP is present at `D:\GITHUB PUBLIC HELP\free-programming-books-main.zip`; its SHA-256 matches the previous audit record: `a57382573afb96eed8623f41884e049b12b9fab54dcf43815629437906abd1e1`. The archive was treated as data, not executed. The live upstream `main` head checked for this comparison was `4c301cce10db10026d632606b5167a9d1b8cd4ec`, newer than the ZIP's recorded snapshot. Its README groups material into books, cheatsheets, courses, interactive programming, problem sets, podcasts/screencasts, and playgrounds, with many translated indexes. See the [upstream README at the audited commit](https://github.com/EbookFoundation/free-programming-books/blob/4c301cce10db10026d632606b5167a9d1b8cd4ec/README.md) and the [current reference coverage report]({{ '/docs/REFERENCE_COVERAGE/' | relative_url }}).

The upstream README's CC BY 4.0 statement covers eligible files in that repository. It does not grant rights to books, courses, or other works linked from its lists. Tajkart's existing all-rights-reserved license remains in force for original Tajkart material; no license was inferred for third-party works.

### Earlier endpoint observation (historical; superseded by the recheck below)

The following redirect and Pages API evidence was recorded before deployment of `d60d3c5`. It was reproducible at that time, but the redirect is no longer observed. Do not use this historical diagnosis as the current endpoint state.

Read-only probes on 2026-10-15 confirmed:

- `https://shahanishashmi.github.io/tajkart-student-hub/` returns `301` to `http://shahanishashmi.me/tajkart-student-hub/`.
- Direct HTTPS to `https://shahanishashmi.me/tajkart-student-hub/` fails certificate hostname validation (`curl` error 60 / Schannel `SEC_E_WRONG_PRINCIPAL`). Verification was not bypassed.
- The HTTP destination returns `200` and serves the Tajkart project route. This confirms reachability over HTTP, not secure release readiness.
- `learn.shahanishashmi.me` does not currently resolve. The existing apex and `www` hosts serve the founder's personal homepage; they must not be repointed for Tajkart.

The checked-in `_config.yml` is internally configured for the project path, `url: https://shahanishashmi.github.io` and `baseurl: /tajkart-student-hub`. Generated local assets, search index, canonical URLs, and routes validate for that configuration. The public redirect is a hosting/account behavior; a local build cannot repair it. More endpoint and Pages API evidence is in [deployment recovery]({{ '/docs/DEPLOYMENT/' | relative_url }}).

### Earlier Pages redirect diagnosis and Plan B proposal (historical)

This section describes the earlier API state and prior `learn`-host proposal. The current Pages settings and next action are recorded in **Current execution recheck and owner action** below.

Authenticated, read-only Pages API results on 2026-10-15:

| Pages repository | Build type | Custom domain | HTTPS enforced | API URL/status |
|---|---|---|---|---|
| `shahanishashmi/tajkart-student-hub` | `workflow` | none (`cname: null`) | `false` | `http://shahanishashmi.me/tajkart-student-hub/`; status null |
| `shahanishashmi/shahanishashmi.github.io` | `legacy` | `shahanishashmi.me` | `false` | `http://shahanishashmi.me/`; status `built` |

GitHub documents that a custom domain configured on a user site is used by default for that account's project sites unless an individual project repository sets its own custom domain. This matches the observed API settings and `301` location: Tajkart has no per-project override, so it inherits the personal site's apex domain at `/tajkart-student-hub/`. The redirect target uses HTTP, consistent with the API reporting HTTPS enforcement disabled. This is the confirmed redirect cause, not a DNS HTTP-forwarding rule. See GitHub's [custom-domain inheritance and override documentation](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/about-custom-domains-and-github-pages).

The TLS failure on direct `https://shahanishashmi.me/tajkart-student-hub/` is confirmed, but the exact certificate provisioning failure is not exposed by the current Pages API. The Pages health-check endpoint returned `404` during this run, so it supplied no certificate diagnostics. Do not treat the redirect explanation as proof that the apex TLS certificate is repaired.

**Proposed Plan B, pending owner approval:**

1. Confirm the owner controls the `shahanishashmi.me` DNS zone and verify the domain in GitHub for takeover protection. No DNS or Pages mutation has been made.
2. In `shahanishashmi/tajkart-student-hub` → **Settings → Pages**, keep the source as **GitHub Actions** and set that repository's **Custom domain** to `learn.shahanishashmi.me`. This per-repository value overrides the inherited apex domain. With a custom Actions workflow GitHub does not create a source-branch `CNAME` file; none is required.
3. At the DNS provider, add exactly this host record for Tajkart:

   | Type | Name/host | Target/value | Other records |
   |---|---|---|---|
   | `CNAME` | `learn` | `shahanishashmi.github.io.` | Do not add an `A`/`AAAA` record for `learn`; do not point it to the apex or include `/tajkart-student-hub`. Keep apex and `www` records unchanged. |

   GitHub's [subdomain setup guidance](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site#configuring-a-subdomain) requires the subdomain CNAME to point directly to the account's `github.io` host, not the apex or repository path. Follow the DNS provider's required target formatting/TTL; the owner has not identified the provider, so no TTL is assumed.
4. Prepare and review `_config.yml` as `url: "https://learn.shahanishashmi.me"` and `baseurl: ""`; build and inspect canonical links, asset URLs, search index, sitemap, and nested routes before deploying the config update.
5. Allow DNS and certificate provisioning time (GitHub notes each can take up to 24 hours). Verify `Resolve-DnsName learn.shahanishashmi.me -Type CNAME`, confirm the Pages custom domain shows a valid certificate, then enable **Enforce HTTPS** for the Tajkart repository.
6. Deploy the reviewed config and smoke-test the selected HTTPS host, certificate, redirects, home, nested course, CSS/JS, search and its 76-entry index, canonical URL, sitemap, `robots.txt`, nested-page refresh, and the personal homepage.

**Rollback limit:** Removing the `learn` per-repository override would make Tajkart inherit `shahanishashmi.me` again and restore the known HTTP redirect; that is a reachability rollback only, not a secure state. If rollback is necessary, coordinate removal of only the `learn` CNAME and Tajkart repository's domain association, restore the reviewed project-path `_config.yml`, and redeploy. Do not remove the custom domain or records from `shahanishashmi.github.io`. Expect DNS caches to retain the old answer for up to the provider's TTL/propagation period. No secure fallback to the current `github.io` URL has been demonstrated while the personal user-site domain remains configured.

At the time of that earlier proposal, no GitHub Support request was needed to try the documented per-project override. Its assumptions must be rechecked before use.

### Current execution recheck and owner action

Read-only checks run after commit `d60d3c5` on 2026-10-15:

| Probe | Current result |
|---|---|
| Tajkart Pages API | `build_type: workflow`, `cname: null`, `https_enforced: false`, `html_url: http://shahanishashmi.github.io/tajkart-student-hub/`, `status: null`. |
| Authorized enforcement update | Owner authorized the setting change. GitHub's documented Pages update endpoint returned HTTP 404, `The certificate does not exist yet`, when sent only `https_enforced: true`; the follow-up GET still reports `false`. No setting was changed. |
| `https://shahanishashmi.github.io/tajkart-student-hub/` | HTTP 200, zero redirects; normal TLS certificate verification succeeds. |
| HTTP project URL | HTTP 200, zero redirects. The same site is still served without encryption; HTTPS is therefore not enforced. |
| Nested course and learning/search pages | HTTP 200 over HTTPS; canonical host is the project `github.io` URL and search points to `/tajkart-student-hub/search-index.json`. |
| Search index, sitemap, robots, CSS, JavaScript, new roadmap page | All returned HTTP 200 over HTTPS. The search index is JSON. |
| `learn.shahanishashmi.me` | DNS name does not exist; no HTTPS request is possible. |
| Apex and `www` HTTP sites | Both return GitHub Pages 404 `Site not found`. Their DNS still points to GitHub Pages (apex A records; `www` CNAME to apex). |
| Apex HTTPS | Normal TLS validation fails with `SEC_E_WRONG_PRINCIPAL`. |
| Personal user-site repository/API | Current `gh` access returned 404 / GraphQL could not resolve the repository. This does not establish whether it was removed, renamed, made private, or is inaccessible to this credential. Do not infer its settings. |
| Hosted workflow | [Run 38628224439](https://github.com/shahanishashmi/tajkart-student-hub/actions/runs/38628224439) completed successfully for exact SHA `d60d3c55589b05b16415c812ff4eb06cc553eb97`, including build and Pages deploy. |

The earlier `github.io` → apex HTTP redirect is not current. The current blocker is narrower: GitHub Pages serves the project over both HTTP and HTTPS, and the Pages API reports HTTPS enforcement disabled. The owner-authorized update was rejected because the API says the certificate does not exist yet, although normal public HTTPS validation succeeds. The personal apex and `www` 404s are a separate, unresolved site-availability issue. No DNS or Pages setting changed.

**Single next task — P0 remains blocked:** Inspect `shahanishashmi/tajkart-student-hub` → **Settings → Pages** for certificate/control status and resolve why GitHub's API reports no certificate for an HTTPS-serving project host. The owner has authorized enabling **Enforce HTTPS**; retry that one setting only after GitHub allows it. Do not change DNS, the custom domain, or `_config.yml`. Keep apex and `www` records untouched.

After GitHub accepts the setting, verify with normal certificate checking that:

1. `http://shahanishashmi.github.io/tajkart-student-hub/` redirects to the HTTPS URL (not an HTTP 200).
2. Home, learning library, nested course, CSS, JavaScript, search page/index, sitemap, robots, and direct nested refresh still return the expected 200 responses over HTTPS.
3. Canonical URLs and the search-index path remain under `/tajkart-student-hub/`.

The checked-in `_config.yml` already matches this host (`url: https://shahanishashmi.github.io`, `baseurl: /tajkart-student-hub`). If the enforcement option is unavailable or HTTP still serves content after the setting change, stop and ask the owner whether to proceed with the dedicated `learn.shahanishashmi.me` custom-domain proposal. That alternative requires domain verification, Tajkart Pages admin access, a direct `learn` CNAME to `shahanishashmi.github.io`, the custom Pages domain setting, and a reviewed config change to `url: https://learn.shahanishashmi.me` with empty `baseurl`; wait for valid TLS before enforcing HTTPS.

**Rollback:** If enabling enforcement causes an unexpected failure, an admin can turn that one setting back off; that restores the current behavior where HTTP remains available, so it is a diagnostic rollback and not a secure release state. Do not change or remove apex/`www` DNS or the separate user-site Pages association. Do not change `_config.yml` for the first enforcement attempt.

GitHub's [HTTPS guide](https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https) documents enforcement; its [Pages REST API](https://docs.github.com/en/rest/pages/pages#update-information-about-a-github-pages-site) documents the update endpoint. The owner has authorized this enforcement setting only; the failed API request did not change it.

## Category-by-category coverage

Statuses follow the requested vocabulary. “Verified” below means the automated implementation/check named in the evidence passed; it never implies human content approval.

| Area | Status | Actual Tajkart coverage | Gap / qualification |
|---|---|---|---|
| 1. Books and reading directories | **Partially implemented** | A reading-method page, 12 original subject guides, and 11 language paths. | No third-party book catalogue by title, language, or subject. Reading guides are not book listings. |
| 2. Subject taxonomy and curriculum depth | **Partially implemented** | The 46 subjects from the earlier reference snapshot are mapped into seven strands; 12 original subject guides exist. | A map is not a set of complete courses. Many subjects lack lessons, worked examples, or assessed practice. |
| 3. Programming-language paths | **Implemented but not human-reviewed** | Eleven introductory paths: C, C++, Java, Python, JavaScript/TypeScript, HTML/CSS, SQL, PHP, Go, Rust, and shell. | Paths are introductions, not complete language courses; `review_status` is pending. |
| 4. Courses and study plans | **Implemented but not human-reviewed** | Four original plans: programming foundations, data structures, web foundations, and the four-part Python intermediate sequence, with assignments, rubrics, and completion criteria. | Expert accuracy review remains. No external course directory exists. |
| 5. Cheatsheets and quick references | **Implemented but not human-reviewed** | Ten Tajkart-authored references. | Technical accuracy and broader CLI/API coverage need review. These are not an index of upstream-linked cheat sheets. |
| 6. Interactive tutorials and quizzes | **Implemented but not human-reviewed** | An interactive practice routine and a four-question browser quiz. It runs fixed choices locally; no server code execution. | Browser keyboard, assistive-technology, and learner-quality review remain; there are no external interactive-resource listings. |
| 7. Problem sets and competitive programming | **Implemented but not human-reviewed** | Nine authored tasks; eight Python solutions and one SQL example are covered by tests. | Automated tests do not validate every explanation or intended difficulty. No contest/ranking catalogue. |
| 8. Podcasts and screencasts | **Partially implemented** | Original listening/viewing and note-taking guidance plus a metadata schema. | No channels, episodes, or external directory. |
| 9. Programming playgrounds and projects | **Partially implemented** | Playground safety guide and seven reproducible project briefs, including the Python study-log capstone. | No hosted runner or external playground catalogue; briefs are specifications, not completed applications. |
| 10. Multilingual content and translations | **Partially implemented** | One Hindi and one Urdu draft of the Python variables lesson; Unicode and RTL-aware styles exist. | Both translations await fluent review. The 57 source-locale records describe the reference snapshot, not 57 Tajkart translations. |
| 11. Search and resource discovery | **Implemented and verified locally** | Source metadata contains 76 Tajkart resources. Matching, title relevance, provenance, and no-result behavior pass Node tests; this continuation adds a tested skill/technology facet. Generated-output validation passed only for an earlier candidate. | No external-resource catalogue. Real-browser search/filter behavior has not been manually reviewed on a valid HTTPS deployment. |
| 12. Career preparation and student opportunities | **Partially implemented** | Five career guides and an offer-verification policy; no live job, scholarship, discount, or internship claims. | Human review and individually verified provider listings are absent. This is a Tajkart addition, not reference parity. |
| 13. Contribution guidelines and editorial workflow | **Partially implemented** | Contribution guide, code of conduct, issue forms, PR template, content schema, editorial checklist, and review-status fields. | No explicit contributor grant or formal reuse policy for accepted work; owner decision required before accepting substantial outside contributions. |
| 14. Validation, URL checking, accessibility, and maintenance automation | **Partially implemented** | One SHA-pinned Pages workflow, source validators, 16 Python tests, Node search tests, Ruby front-matter validation, Jekyll build, and structural generated-HTML checks. Hosted build/deploy passed on `a83766c`. | External URL review was a bounded one-time check in the previous audit, not a live guarantee. Manual keyboard, screen reader, zoom/reflow, RTL, and mobile checks remain. Secure HTTPS is blocked by hosting configuration. |

The complete resource counts, source mappings, and rights discussion are in [content progress]({{ '/docs/CONTENT_PROGRESS/' | relative_url }}), [reference coverage]({{ '/docs/REFERENCE_COVERAGE/' | relative_url }}), and [licensing review]({{ '/docs/LICENSING_REVIEW/' | relative_url }}).

## Priority model and highest-impact gaps

Priority reflects learner impact, correctness and trust risk, deployment/security impact, dependencies, and effort. P0 blocks safe release. P1 closes trust/review gates. P2 improves learning depth and maintainability. P3 expands discovery only after product direction and rights are settled. Estimates include review coordination; actual calendar time depends on reviewer availability.

| Candidate | Priority | Why now / current evidence | Likely files and components | Effort | Owner decision? |
|---|---|---|---|---|---|
| A. Enforce HTTPS for the current Pages hostname | **P0** | The project `github.io` URL serves valid HTTPS, but also serves HTTP without redirect; Pages API reports `https_enforced: false` and `https_certificate: null`. The previously authorized update failed; apex/`www` return 404 and `learn` has no DNS. | Tajkart repository Pages certificate/control state; verify generated routes/search/sitemap after enforcement. Custom-domain/DNS/config work only if the current host cannot meet the gate or the owner chooses it. | S for settings/support; M for custom-host fallback | **Authorization received for the same-host toggle.** No authorization for a custom-domain fallback or personal-domain changes. |
| B. Expert technical review | **P1** | All searchable resources have pending human review; automated checks cover structure and selected examples, not teaching correctness. | `learning/` content, solution tests, front matter review fields, `docs/EDITORIAL_REVIEW.md`. | XL | **Yes.** Assign qualified reviewers and accept/reject findings. |
| C. Fluent Hindi/Urdu and RTL review | **P1** | Only two translation drafts exist and both are pending; machine or structural checks cannot certify meaning or tone. | Two translation pages, layouts, CSS RTL rules, `docs/EDITORIAL_REVIEW.md`. | M | **Yes.** Recruit fluent reviewers and decide whether reviewed drafts are ready to publish. |
| D. Manual accessibility and mobile review | **P1** | Automated structural checks pass and focus/reduced-motion/RTL styles exist, but no human device or assistive-technology review is recorded. | Layouts, `assets/css/site.css`, `assets/js/site.js`, quiz/search markup. | M | **Yes.** Select reviewer and supported test/browser matrix. |
| E. Expert-review the Python intermediate path | **P1** | The four-unit sequence, course plan, capstone brief and tested study-log helpers now exist locally; all six searchable additions remain draft/pending. | `learning/lessons/python-intermediate-*.md`, `learning/courses/python-intermediate.md`, `learning/projects/python-study-log.md`, `_includes/solutions/study_log.py`, `tests/test_python_study_log.py`. | M | Assign a qualified Python reviewer; do not update review status before sign-off. |
| F. Deepen mapped CS subjects | **P2** | Forty-six subject headings are mapped but only 12 original subject guides exist; maps can overstate depth if presented as curriculum. | `learning/guides/`, `learning/subjects/`, `data/reference_coverage.yml`, tests and review metadata. | XL | **Yes.** Choose learner priority among the mapped topics after the pilot/review evidence. |
| G. Add verified external directories | **P3** | External resource count is zero. Existing schema already requires source, creator, date, attribution, and rights; upstream directory entries are individual third-party works. | `data/verified_resource.schema.json`, `learning/books/`, course/media indexes, source validator. | M for a small pilot; L for a maintained catalogue | **Yes.** Decide whether Tajkart should be an original curriculum, a directory, or a mix. |
| H. Improve practice and assessment | **P2** | The quiz has four questions and problem sets have tested canonical solutions; no debugging sequence or staged formative assessment exists. | `learning/interactive-tutorials/`, `learning/problem-sets/`, `assets/js/site.js`, `tests/search_test.js` or a focused test. | M | No, if limited to static, privacy-preserving activities; content reviewer required. |
| I. Set contributor permission terms | **P1** | Contribution docs request original work, but the all-rights-reserved license has no explicit grant for modifying, translating, or maintaining accepted external contributions. | `LICENSE` only if the owner approves a change; `COPYRIGHT.md`, `CONTRIBUTING.md`, `docs/LICENSING_REVIEW.md`. | M | **Yes.** This is a rights-holder decision; obtain qualified advice if formal terms are needed. |
| J. Strengthen maintenance checks selectively | **P2** | Core CI is green and Actions are SHA-pinned. Prior bounded URL checks are dated; adding flaky checks without an external catalogue creates maintenance cost. | `.github/workflows/pages.yml`, validators, schemas, `docs/DEPLOYMENT.md`, Dependabot settings. | S–M | No for an investigation/proposal; owner review before adding workflow or dependency changes. |

### Task definitions and acceptance criteria

#### A. Resolve secure hosting — P0, effort M

- **Deliver:** One confirmed public HTTPS hostname, correct Jekyll `url`/`baseurl`, matching GitHub Pages domain configuration, and a repeatable smoke-test record.
- **Dependencies:** The owner has authorized the same-host enforcement toggle. A repository admin must inspect the Settings → Pages certificate/control state or GitHub Support must explain the API/UI mismatch before retry. DNS-zone control and separate custom-domain approval are required only if the dedicated `learn` fallback is selected.
- **Acceptance:** The existing HTTPS project URL remains valid; HTTP redirects to HTTPS; home, nested course, CSS/JS, search page, 76-entry search index, canonical tags, sitemap, `robots.txt`, and nested refresh pass. Do not alter apex/`www` DNS; record their pre-existing 404 status separately rather than claiming the personal homepage is preserved or restored. The GitHub Actions build/deploy for the reviewed SHA passes.
- **Human review:** Owner confirms domain ownership and personal-site preservation; a human runs the browser smoke tests.
- **Decision:** Authorization for **Enforce HTTPS** on the current Tajkart project URL has been received, but the API rejected the attempt with `The certificate does not exist yet`. Do not retry until the Pages UI or GitHub Support confirms readiness. The `learn` custom-domain fallback requires a separate decision. Never change apex or `www` records for this task.

#### B. Review existing technical content — P1, effort XL

- **Deliver:** Expert review notes tied to page IDs, corrections merged with provenance, and truthful review statuses.
- **Dependencies:** Reviewers with relevant programming/CS experience; stable content freeze per batch.
- **Acceptance:** Complete the first core batch of 6 lessons, 3 study plans, 9 problem sets/solutions, and 10 cheatsheets. Then review the 12 subject guides, 11 language paths, and 6 project briefs before declaring the existing library reviewed. Every item has a recorded decision and review date; all code snippets have expected output and edge-case notes; executable examples continue to pass tests; no item is marked approved without a human sign-off.
- **Human review:** Required for each content unit; automated test pass is supplementary evidence only.
- **Decision:** Owner assigns reviewers and decides which factual corrections to accept.

#### C. Review Hindi/Urdu drafts — P1, effort M

- **Deliver:** Two fluent-reviewed translations with terminology and rendering notes, or explicit continued-draft status if reviewers identify unresolved issues.
- **Dependencies:** One fluent reviewer per language or qualified bilingual reviewers; technical source lesson remains stable.
- **Acceptance:** Each draft is compared sentence-by-sentence with the English source for meaning, naturalness, technical vocabulary, punctuation, and mixed-script code examples; `lang`/`dir`, wrapping, keyboard focus, and screen-reader reading order are checked in the rendered page. No machine-only approval.
- **Human review:** Fluent language review and one rendered RTL review are mandatory.
- **Decision:** Owner recruits reviewers and approves publication status; translators do not rewrite source without authorization.

#### D. Manual accessibility and mobile review — P1, effort M

- **Deliver:** A reproducible issue log with browser/device/assistive-technology versions, severity, and retest outcome.
- **Dependencies:** A built candidate at a working HTTPS URL; selected browser and device matrix.
- **Acceptance:** Human checks include keyboard-only navigation and focus visibility, skip link, navigation expansion, search and quiz controls/status updates, at least 200% zoom and narrow-screen reflow, RTL content, reduced-motion preference, labels/landmarks, and one screen-reader/browser pairing. Resolve all critical/blocking findings; retest significant findings; document any accepted limitations. Do not claim conformance solely from this sample.
- **Human review:** Required from a keyboard/screen-reader user or accessibility reviewer.
- **Decision:** Owner approves target support matrix and remediation tradeoffs.

#### E. Complete human review of the intermediate learning path — P1, effort M

- **Deliver:** Page-level review notes, accepted corrections and a decision for the four Python intermediate lessons, course sequence, study-log helpers and capstone rubric.
- **Dependencies:** A qualified Python reviewer; the current candidate must pass CI before release.
- **Acceptance:** The reviewer checks objectives, prerequisites, examples and expected output, edge cases, practice hints, helper behavior, project milestones and rubric. Retest accepted code corrections. Keep all six new searchable pages `review_status: pending` until the reviewer records a decision; automated checks do not count as approval.
- **Human review:** Required for instructional correctness and project fit.
- **Decision:** Owner assigns the reviewer and decides whether to accept requested changes.

#### F. Deepen subject coverage — P2, effort XL

- **Deliver:** A learner-prioritized sequence of complete learning units in subjects already mapped by the reference audit.
- **Dependencies:** Pilot path and technical review reveal where current guides are too thin; choose topics based on learner demand or founder direction.
- **Acceptance:** Select three subjects from the 46 mapped headings. For each, publish at least one original lesson with measurable objectives, prerequisites, worked example, practice with hints, one assessment item, and links to next steps. Update the taxonomy matrix with content depth and review status; do not count a topic index as a completed course.
- **Human review:** Subject-matter review per selected subject.
- **Decision:** Required to choose the three topics.

#### G. Decide on external resource catalogues — P3, effort M for a pilot

- **Deliver:** A written product decision. If approved, a small pilot in one user-requested category; no minimum number of entries.
- **Dependencies:** Rights policy and contribution permission decisions; maintainers who can recheck sources over time.
- **Acceptance:** For every published item, store official source URL, author/provider, language/topic/type, last-checked date, clear attribution, and resolved rights state. Manually verify current destination and access terms. Never copy descriptions or linked works. A 404, timeout, or bot block enters review and does not alone trigger deletion. Zero entries is the correct outcome when provenance or rights cannot be established.
- **Human review:** Rights/provenance and learning relevance reviewed by a named maintainer.
- **Decision:** Required; choose directory-first, original-curriculum-first, or a limited mix.

#### H. Add staged interactive practice — P2, effort M

- **Deliver:** One debugging or code-reading activity that gives useful feedback without server execution, accounts, or learner tracking.
- **Dependencies:** Use a reviewed lesson objective and existing static JavaScript pattern; avoid a new dependency.
- **Acceptance:** At least three staged prompts, progressive hints, clear answer feedback, keyboard-operable controls, announced status, no arbitrary code execution, no personal data collection, and focused tests for correct/incorrect/no-answer states. The activity has a written objective and is linked to the corresponding lesson.
- **Human review:** Educator checks feedback and difficulty; accessibility reviewer checks the rendered interaction.
- **Decision:** Not required if kept to this small static activity.

#### I. Finalize contributor rights — P1, effort M

- **Deliver:** A clear statement of what permission contributors grant and how their work may be published, maintained, translated, or adapted under Tajkart's chosen policy.
- **Dependencies:** Rights-holder decision; qualified rights advice if the project wants a formal agreement.
- **Acceptance:** Policy is consistent with the root license and copyright page; contribution form/guide says what contributors affirm; third-party exceptions and attribution are documented; no license is broadened by implication. Update contributor templates and the licensing review only after owner approval.
- **Human review:** Rights-holder review; legal professional if a formal contributor agreement is adopted.
- **Decision:** Required. Do not change `LICENSE` or claim a contributor grant without approval.

#### J. Improve maintenance automation only where justified — P2, effort S–M

- **Deliver:** A decision and a small CI improvement tied to an observed failure mode, not a copy of upstream workflows.
- **Dependencies:** Current CI remains green; a concrete recurring problem or growing verified-resource catalogue.
- **Acceptance:** Any URL check has a timeout, bounded retries, rate limiting, redirect cap, status classification for 4xx/5xx/timeouts/blocks, and a manual-review queue; it never deletes or rejects a resource solely because automation cannot access it. New dependencies require a documented benefit and pinned version. Any new workflow has least-privilege permissions and a successful PR run.
- **Human review:** Maintainer reviews crawler exceptions and false positives before decisions about content.
- **Decision:** Owner review before adopting a new dependency or hosted workflow.

## Four-phase roadmap

### Phase 0 — Protect and verify

1. Preserve the eight existing documentation edits, inspect the full diff, and keep all evidence updates uncommitted until a separate publication decision.
2. The owner has authorized enabling **Enforce HTTPS** for the current project `github.io` URL. Inspect its Pages certificate/control state; the API currently says no certificate exists although public HTTPS works.
3. Do not retry until GitHub confirms readiness or explains a supported recovery. Then change only that Pages setting and run task A's HTTP-to-HTTPS and route smoke tests. Consider the `learn` subdomain only after a separate owner decision.

**Milestone 0:** The chosen hostname serves over valid HTTPS, HTTP redirects to HTTPS, and routes/assets/search pass. Apex/`www` records are unchanged; their current 404 status is separately reported. Record workflow and browser smoke evidence. Until this passes, do not call deployment ready.

### Phase 1 — Trust and quality

1. Run task B's expert review in reviewable batches, starting with lessons, study plans, and tested problems.
2. Complete task C with fluent Hindi and Urdu reviewers; keep draft status when unresolved.
3. Complete task D's manual accessibility/mobile matrix and retest blocking issues.
4. Decide task I's contributor permission terms before substantial outside contributions.

**Milestone 1:** Every currently published searchable resource has an honest review state; the core lessons/plans/problems have recorded expert review; translation/accessibility findings are resolved or documented; contributor terms are explicit. Automated tests remain green, but human approval is separately recorded.

### Phase 2 — Educational depth

1. Complete task E's expert review of the four-unit Python intermediate sequence and capstone; apply accepted corrections and keep review status pending until sign-off.
2. Select three mapped subjects for task F using learner demand or founder direction; author one complete lesson unit per selected subject.
3. Add task H's staged debugging/code-reading exercise only after a reviewed lesson supplies its learning objective.

**Milestone 2:** The four-unit Python path and capstone have expert review and tested accepted corrections; three additional subject units have outcomes, practice, and review status; the interactive task is keyboard-operable and privacy-preserving. No new page is counted as complete solely because it exists.

### Phase 3 — Discovery and scale

1. Make the product decision for task G. If a catalogue is justified, pilot one category with per-item provenance and rights review. Do not bulk import the reference ZIP.
2. Expand translations only when fluent reviewers and a chosen source curriculum are available; report actual translated lesson counts by language.
3. Evaluate task J after the catalogue or contributor workload grows; add bounded checks only for recurring maintenance risks.

**Milestone 3:** The directory-vs-curriculum decision is documented; any pilot entries pass source, attribution, rights, and freshness review (or the catalogue remains intentionally empty); locale and workflow coverage reflect actual maintained content.

## Risks and unresolved owner decisions

| Risk or decision | Current evidence | Required resolution |
|---|---|---|
| Hostname and HTTPS | Project URL serves over HTTPS but HTTP is not redirected; Pages API reports enforcement false. Apex/`www` HTTP return 404, apex TLS validation fails, and `learn` has no DNS record. | Authorize one Pages enforcement setting for Tajkart; keep apex and `www` DNS untouched. |
| Personal homepage availability | Apex and `www` currently return GitHub Pages 404; the prior audit had observed a homepage, but current user-site repository/API access returns 404. | Owner must determine whether the separate personal site should be restored and provide access; do not alter it as part of Tajkart's Pages task. |
| Human review availability | Searchable content remains drafted/pending; no expert review is recorded. | Name technical, fluent-language, and accessibility reviewers; agree scope and record decisions. |
| Third-party rights | Current external learning-resource inventory is empty; Tajkart reserves rights in original work. | Keep it empty unless each item and its rights are individually verified; decide contribution terms separately. |
| Scope inflation | Taxonomy has 46 mapped subjects and source locale inventory has 57 records. | Do not interpret maps as 46 completed subjects or 57 translations. Prioritize a small number of learning outcomes. |
| Automation noise | Prior external URL crawl was a dated bounded check; websites may block bots or change links. | Keep automation bounded and advisory for ambiguous failures; require human decision before removal. |
| Privacy and security | Static site; no server-side learner-code execution or student account tracking is designed. | Preserve this constraint. Any future code runner/account system requires separate privacy and isolation review. |
| Worktree publication | At the latest report snapshot, eight tracked documentation files are modified and `docs/P0_INCIDENT_REPORT.md` is untracked; none is staged. | Review all local changes together. The owner separately decides whether to stage, commit, push, or deploy; never discard existing edits. |

## Single recommended next task

**P0: Complete HTTPS enforcement on Tajkart's current project Pages URL.** The owner authorized this one setting, but GitHub rejected the update with `The certificate does not exist yet`. HTTPS serves the site with valid TLS; HTTP still serves it without a redirect. Inspect the Pages UI or get GitHub's explanation, then retry only if readiness is confirmed. No DNS or Jekyll config change is authorized or needed for this step; leave apex/`www` untouched. See the [P0 incident report]({{ '/docs/P0_INCIDENT_REPORT/' | relative_url }}) for the support draft and separate personal-domain findings.

- **Deliver:** HTTP requests redirect to the valid HTTPS project URL, with a passing smoke-test record for routes, assets, search index, sitemap, and direct nested-page refresh.
- **Out of scope for this task:** Changing DNS, changing `_config.yml`, restoring or changing the personal homepage, switching to a custom domain, adding learning features, importing resource lists, changing licenses, or claiming human content review.
- **How to verify:** Normal certificate validation succeeds; HTTP redirects to the selected HTTPS URL; canonical and base paths remain correct; all required routes/assets/index return 200; hosted Pages run succeeds for the reviewed SHA. The personal-domain 404 is separately reported, not represented as fixed or preserved.
- **Immediately afterward:** Start Phase 1's expert review of the existing core lessons, courses, problems, and solutions. Keep their approval state pending until reviewers complete it.

The owner has authorized the HTTPS enforcement setting only. The `learn` custom-domain fallback additionally requires DNS-zone control and a separate hostname decision. The attempted API update was rejected and made no Pages setting change; DNS was not changed.

## Out of scope

- Copying books, course descriptions, curated rows, translations, code, templates, or workflow implementations from the reference repository.
- Bulk importing the supplied ZIP or adding external entries to increase counts.
- Generating placeholder lessons or machine-translating content and marking it approved.
- Changing `LICENSE`, applying upstream CC BY 4.0 to Tajkart, or inventing contributor permission.
- Repointing the active personal homepage's apex/`www` DNS or removing its Pages domain association.
- Adding server accounts, learner tracking, or arbitrary server-side code execution.
- Claiming secure production readiness before hostname/TLS, human content, translation, and manual accessibility gates are complete.
- Committing, pushing, deploying, or editing DNS/Pages settings as part of this planning task.

## Complete ecosystem mission continuation (2026-10-15)

The latest bounded implementation improves search discovery: the learning library now generates a **Skill or technology** filter from existing resource tags. It composes with the current type, category, language, difficulty and origin filters. No resources, dependencies, third-party links or publication state were added. The parity matrix now gives source paths, Tajkart file evidence, current gaps, priority, closure criteria and verification for each reference category.

The supplied ZIP's SHA-256 was rechecked as `a57382573afb96eed8623f41884e049b12b9fab54dcf43815629437906abd1e1`. It was extracted to a new temporary folder and inspected without running its scripts/actions or importing entries. Current upstream `main` was `4c301cce10db10026d632606b5167a9d1b8cd4ec`; a local read-only comparison found 233 common paths, no path changes, and 226 files whose contents differ. This confirms the ZIP is not a current content snapshot. Current README and list-lint workflow were read at the same commit; the [parity matrix]({{ '/docs/REFERENCE_PARITY_MATRIX/' | relative_url }}) and [repository audit]({{ '/docs/REFERENCE_AUDIT/' | relative_url }}) provide the category-level evidence.

### Verification for this local candidate

| Check | Result |
|---|---|
| `python scripts/validate_site.py` | **Pass:** 121 Markdown files, 108 routes, 76 searchable resources; zero reported metadata, ID/route, curated-URL, reference, Python syntax or local Markdown-link errors. |
| `python -m unittest discover -s tests -v` | **Pass:** 21 tests. |
| `node --check assets/js/site.js` and `node tests/search_test.js` | **Pass:** tag option generation/filter composition, token matching, relevance, provenance, attribution and no-results checks. |
| PyYAML / Python JSON parsing | **Pass:** 111 Markdown front-matter blocks, `_config.yml`, two data YAML inventories, Pages workflow YAML and two JSON schemas parsed. |
| `git diff --check` | **Pass:** no whitespace errors; Git emitted line-ending conversion notices for existing CRLF-normalized worktree files. |
| Ruby front matter / Jekyll / generated HTML | **Not run:** Ruby, Bundler and Jekyll executables are unavailable in this shell. |
| Hosted CI / browser / external URL crawl / human reviews | **Not run for this candidate.** Hosted success for `d60d3c5` predates these local edits; technical, fluent translation, accessibility and rights reviews remain human gates. |

The local branch remains at `d60d3c55589b05b16415c812ff4eb06cc553eb97`; 17 tracked files are modified and 10 paths are untracked, with nothing staged. Existing user changes were preserved. The Pages HTTPS enforcement issue and personal-domain `404` remain open. No commit, push, deployment, DNS/Pages mutation, license change or third-party resource entry was made.

## Student-first continuation (2026-10-15)

The product's primary audience is students across learning and career-development needs. The student start guide links existing subject, course, practice, project, career, and opportunity-guidance routes into five goal-based paths. New academic content comprises a general study-skills guide and one mathematics lesson on ratios and unit rates, surfaced in the subject map and learning library. Primary navigation exposes eight authored sections; the branded wordmark remains the home route. Details and file-level gaps are in the [student-first parity matrix]({{ '/docs/REFERENCE_PARITY_MATRIX/' | relative_url }}).

This implementation is a bounded student-orientation and academic-study increment, not a claim of comprehensive student coverage. The library still centers on computing/programming; broad non-CS subject sequences, persisted learner progress, verified third-party directories, fluent Hindi/Urdu course coverage, and human content/accessibility reviews remain incomplete. All three new student/academic resources are pending human review. No dependencies, copied reference content, DNS/Pages changes, or deployment were introduced.

The final local candidate passes source validation (125 Markdown files, 112 routes, 79 searchable resources), 21 Python tests, Node search/navigation tests, JavaScript syntax checks, Ruby front-matter checks, strict production Jekyll build, generated-HTML validation, and `git diff --check`. The production build generated 112 HTML pages. Local route checks resolve authored targets, and the menu test covers click/close/Escape/focus behavior. Ruby 3.3.12 was found under `C:\Ruby33-x64\bin`; no browser is available for rendered mobile/accessibility checks. Hosted Actions have not run on this worktree. Existing worktree changes remain uncommitted and unstaged. The [combined platform audit]({{ '/docs/MASTER_AUDIT_REPORT/' | relative_url }}) consolidates the current evidence and next content task.
