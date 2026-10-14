---
layout: page
title: Next-phase audit and roadmap
description: Evidence-based baseline, release blockers, review gates, and prioritized roadmap for Tajkart Student Hub.
permalink: /docs/ROADMAP_NEXT_PHASE/
---

**Audit date:** 2026-10-15

**Repository:** `shahanishashmi/tajkart-student-hub`

**Reference:** [EbookFoundation/free-programming-books at audited commit `4c301cce`](https://github.com/EbookFoundation/free-programming-books/tree/4c301cce10db10026d632606b5167a9d1b8cd4ec)

This is a planning document, not an implementation authorization. It records verified repository and deployment evidence, distinguishes original Tajkart content from third-party directories, and recommends one next task. No content was copied from the reference. No DNS, Pages setting, commit, push, or deployment was changed for this audit.

## Executive decision

Tajkart has a working static learning site, an original first library, searchable metadata, tests, generated-page validation, and a successful Pages workflow for the deployed commit. The current repository checks pass. The public host is **not secure-release ready**: the GitHub project URL redirects to an HTTP custom-domain path, direct HTTPS on that custom domain fails certificate hostname validation, and the proposed `learn` subdomain has no DNS record.

The reference is a multilingual directory of links to learning resources. Tajkart has built original guides, courses, practice, and career advice across similar categories; it has **not** built an equivalent external-resource directory. Search indexes Tajkart's own pages, and the verified external learning-resource inventory is empty. Category pages and taxonomy mappings do not establish complete course, book, or language coverage.

**Recommended immediate next task — P0:** Resolve secure hosting at a dedicated `learn.shahanishashmi.me` hostname, after the owner confirms control of that DNS zone and repository Pages settings. This is the lower-collision option in the existing deployment diagnosis because it leaves the active personal homepage on the apex and `www` hosts untouched. Do not change DNS or Pages settings until the owner authorizes that exact target. See [deployment evidence and recovery options]({{ '/docs/DEPLOYMENT/' | relative_url }}).

## Verified baseline

### Git, workflow, and local checks

| Item | Verified state |
|---|---|
| Branch and commit | Branch `main`; `HEAD`, local `origin/main`, and live `origin/main` all resolve to `a83766c26c97e13767f307176c0883df7cd2023b`. The remote SHA was read with `git ls-remote`. |
| Worktree at this report snapshot | Seven tracked documentation files are modified: `docs/ARCHITECTURE.md`, `docs/CONTENT_PROGRESS.md`, `docs/DEPLOYMENT.md`, `docs/IMPLEMENTATION_PLAN.md`, `docs/NEXT_STEPS.md`, `docs/REFERENCE_AUDIT.md`, and `docs/REFERENCE_COVERAGE.md`. `docs/ROADMAP_NEXT_PHASE.md` is new and untracked. Nothing is staged. Existing edits were preserved; this audit's only content update is the roadmap. |
| Hosted Pages workflow | GitHub Actions run [38585940306](https://github.com/shahanishashmi/tajkart-student-hub/actions/runs/38585940306) completed successfully for the exact `a83766c` SHA. Both `build` and `deploy` jobs passed. Later Dependabot runs also passed; they are not Pages build evidence. |
| Source validation | Re-run for this report: `python scripts/validate_site.py` passed with 113 Markdown files, 100 routes, and 70 searchable resources; no missing required fields, duplicate IDs/routes, invalid curated source URLs, unknown references, Python syntax errors, or broken local Markdown links. |
| Python and search tests | `python -m unittest discover -s tests -v`: 16 passed. `node --check assets/js/site.js` and `node tests/search_test.js`: passed. |
| Front matter and YAML | Ruby 3.3.12 / Bundler 2.5.22. Re-run `ruby scripts/validate_front_matter.rb` parsed 103 Markdown front-matter blocks and five YAML inventories/configuration files. |
| Production build and generated HTML | `JEKYLL_ENV=production bundle exec jekyll build --destination <temporary-directory>` passed outside the worktree. `python scripts/validate_html.py <build-output>` passed for 100 HTML pages and all 70 search resources, including local links/fragments, IDs, labels, language, landmarks, and provenance metadata. Jekyll emitted a non-blocking notice that optional Faraday retry middleware is not installed. |
| Review state | A front-matter scan of all 70 searchable Markdown resources found `review_status: pending` on all 70. No human technical, fluent Hindi/Urdu, accessibility, or licensing review was performed by this audit. |
| Current documentation edits | The seven modified tracked documentation files listed above remain unstaged and uncommitted; this roadmap is untracked. The audit changed only this roadmap. GitHub Actions has not tested these uncommitted changes; the successful hosted run applies to `a83766c` only. |

The matching local checks and hosted run establish a healthy build for the committed baseline and a locally valid uncommitted candidate. They do not establish expert correctness of teaching content, secure live hosting, or human accessibility approval. No new external-link crawl, browser session, vulnerability scan, or assistive-technology test was run for this roadmap.

### Reference snapshot

The supplied ZIP is present at `D:\GITHUB PUBLIC HELP\free-programming-books-main.zip`; its SHA-256 matches the previous audit record: `a57382573afb96eed8623f41884e049b12b9fab54dcf43815629437906abd1e`. The archive was treated as data, not executed. The live upstream `main` head checked for this comparison was `4c301cce10db10026d632606b5167a9d1b8cd4ec`, newer than the ZIP's recorded snapshot. Its README groups material into books, cheatsheets, courses, interactive programming, problem sets, podcasts/screencasts, and playgrounds, with many translated indexes. See the [upstream README at the audited commit](https://github.com/EbookFoundation/free-programming-books/blob/4c301cce10db10026d632606b5167a9d1b8cd4ec/README.md) and the [current reference coverage report]({{ '/docs/REFERENCE_COVERAGE/' | relative_url }}).

The upstream README's CC BY 4.0 statement covers eligible files in that repository. It does not grant rights to books, courses, or other works linked from its lists. Tajkart's existing all-rights-reserved license remains in force for original Tajkart material; no license was inferred for third-party works.

### Current published endpoint

Read-only probes on 2026-10-15 confirmed:

- `https://shahanishashmi.github.io/tajkart-student-hub/` returns `301` to `http://shahanishashmi.me/tajkart-student-hub/`.
- Direct HTTPS to `https://shahanishashmi.me/tajkart-student-hub/` fails certificate hostname validation (`curl` error 60 / Schannel `SEC_E_WRONG_PRINCIPAL`). Verification was not bypassed.
- The HTTP destination returns `200` and serves the Tajkart project route. This confirms reachability over HTTP, not secure release readiness.
- `learn.shahanishashmi.me` does not currently resolve. The existing apex and `www` hosts serve the founder's personal homepage; they must not be repointed for Tajkart.

The checked-in `_config.yml` is internally configured for the project path, `url: https://shahanishashmi.github.io` and `baseurl: /tajkart-student-hub`. Generated local assets, search index, canonical URLs, and routes validate for that configuration. The public redirect is a hosting/account behavior; a local build cannot repair it. More endpoint and Pages API evidence is in [deployment recovery]({{ '/docs/DEPLOYMENT/' | relative_url }}).

### Confirmed Pages redirect cause and proposed recovery

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
6. Deploy the reviewed config and smoke-test the selected HTTPS host, certificate, redirects, home, nested course, CSS/JS, search and its 70-entry index, canonical URL, sitemap, `robots.txt`, nested-page refresh, and the personal homepage.

**Rollback limit:** Removing the `learn` per-repository override would make Tajkart inherit `shahanishashmi.me` again and restore the known HTTP redirect; that is a reachability rollback only, not a secure state. If rollback is necessary, coordinate removal of only the `learn` CNAME and Tajkart repository's domain association, restore the reviewed project-path `_config.yml`, and redeploy. Do not remove the custom domain or records from `shahanishashmi.github.io`. Expect DNS caches to retain the old answer for up to the provider's TTL/propagation period. No secure fallback to the current `github.io` URL has been demonstrated while the personal user-site domain remains configured.

No GitHub Support request is needed to try the documented per-project override. If the verified CNAME and repository override still produce an apex/HTTP redirect or no valid TLS certificate after the documented propagation window, stop; prepare a sanitized support request containing the repository names, Pages API fields above, CNAME result, UTC timestamps, HTTP `Location`, TLS error, and successful Actions run ID `38585940306`. Do not include credentials, DNS-account data, or unrelated personal details.

## Category-by-category coverage

Statuses follow the requested vocabulary. “Verified” below means the automated implementation/check named in the evidence passed; it never implies human content approval.

| Area | Status | Actual Tajkart coverage | Gap / qualification |
|---|---|---|---|
| 1. Books and reading directories | **Partially implemented** | A reading-method page, 12 original subject guides, and 11 language paths. | No third-party book catalogue by title, language, or subject. Reading guides are not book listings. |
| 2. Subject taxonomy and curriculum depth | **Partially implemented** | The 46 subjects from the earlier reference snapshot are mapped into seven strands; 12 original subject guides exist. | A map is not a set of complete courses. Many subjects lack lessons, worked examples, or assessed practice. |
| 3. Programming-language paths | **Implemented but not human-reviewed** | Eleven introductory paths: C, C++, Java, Python, JavaScript/TypeScript, HTML/CSS, SQL, PHP, Go, Rust, and shell. | Paths are introductions, not complete language courses; `review_status` is pending. |
| 4. Courses and study plans | **Implemented but not human-reviewed** | Three original plans: programming foundations, data structures, and web foundations, with modules, assignments, rubrics, and completion criteria. | Intermediate/advanced progression and expert accuracy review remain. No external course directory exists. |
| 5. Cheatsheets and quick references | **Implemented but not human-reviewed** | Ten Tajkart-authored references. | Technical accuracy and broader CLI/API coverage need review. These are not an index of upstream-linked cheat sheets. |
| 6. Interactive tutorials and quizzes | **Implemented but not human-reviewed** | An interactive practice routine and a four-question browser quiz. It runs fixed choices locally; no server code execution. | Browser keyboard, assistive-technology, and learner-quality review remain; there are no external interactive-resource listings. |
| 7. Problem sets and competitive programming | **Implemented but not human-reviewed** | Nine authored tasks; eight Python solutions and one SQL example are covered by tests. | Automated tests do not validate every explanation or intended difficulty. No contest/ranking catalogue. |
| 8. Podcasts and screencasts | **Partially implemented** | Original listening/viewing and note-taking guidance plus a metadata schema. | No channels, episodes, or external directory. |
| 9. Programming playgrounds and projects | **Partially implemented** | Playground safety guide and six reproducible project briefs. | No hosted runner or external playground catalogue; briefs are specifications, not completed applications. |
| 10. Multilingual content and translations | **Partially implemented** | One Hindi and one Urdu draft of the Python variables lesson; Unicode and RTL-aware styles exist. | Both translations await fluent review. The 57 source-locale records describe the reference snapshot, not 57 Tajkart translations. |
| 11. Search and resource discovery | **Implemented and verified** | Liquid-generated local index contains 70 Tajkart resources. Matching, title relevance, provenance, and no-result behavior pass Node tests; generated index passes HTML validation. | No external-resource catalogue. Real-browser search/filter behavior has not been manually reviewed on a valid HTTPS deployment. |
| 12. Career preparation and student opportunities | **Partially implemented** | Five career guides and an offer-verification policy; no live job, scholarship, discount, or internship claims. | Human review and individually verified provider listings are absent. This is a Tajkart addition, not reference parity. |
| 13. Contribution guidelines and editorial workflow | **Partially implemented** | Contribution guide, code of conduct, issue forms, PR template, content schema, editorial checklist, and review-status fields. | No explicit contributor grant or formal reuse policy for accepted work; owner decision required before accepting substantial outside contributions. |
| 14. Validation, URL checking, accessibility, and maintenance automation | **Partially implemented** | One SHA-pinned Pages workflow, source validators, 16 Python tests, Node search tests, Ruby front-matter validation, Jekyll build, and structural generated-HTML checks. Hosted build/deploy passed on `a83766c`. | External URL review was a bounded one-time check in the previous audit, not a live guarantee. Manual keyboard, screen reader, zoom/reflow, RTL, and mobile checks remain. Secure HTTPS is blocked by hosting configuration. |

The complete resource counts, source mappings, and rights discussion are in [content progress]({{ '/docs/CONTENT_PROGRESS/' | relative_url }}), [reference coverage]({{ '/docs/REFERENCE_COVERAGE/' | relative_url }}), and [licensing review]({{ '/docs/LICENSING_REVIEW/' | relative_url }}).

## Priority model and highest-impact gaps

Priority reflects learner impact, correctness and trust risk, deployment/security impact, dependencies, and effort. P0 blocks safe release. P1 closes trust/review gates. P2 improves learning depth and maintainability. P3 expands discovery only after product direction and rights are settled. Estimates include review coordination; actual calendar time depends on reviewer availability.

| Candidate | Priority | Why now / current evidence | Likely files and components | Effort | Owner decision? |
|---|---|---|---|---|---|
| A. Secure the chosen Pages hostname | **P0** | Public HTTPS currently downgrades to HTTP; apex TLS name check fails; a personal homepage owns apex/`www`; `learn` has no DNS. | DNS zone, repository Pages settings, `_config.yml`, `docs/DEPLOYMENT.md`; generated routes/search/sitemap. | M | **Yes.** Confirm hostname and access before any setting change. |
| B. Expert technical review | **P1** | All searchable resources have pending human review; automated checks cover structure and selected examples, not teaching correctness. | `learning/` content, solution tests, front matter review fields, `docs/EDITORIAL_REVIEW.md`. | XL | **Yes.** Assign qualified reviewers and accept/reject findings. |
| C. Fluent Hindi/Urdu and RTL review | **P1** | Only two translation drafts exist and both are pending; machine or structural checks cannot certify meaning or tone. | Two translation pages, layouts, CSS RTL rules, `docs/EDITORIAL_REVIEW.md`. | M | **Yes.** Recruit fluent reviewers and decide whether reviewed drafts are ready to publish. |
| D. Manual accessibility and mobile review | **P1** | Automated structural checks pass and focus/reduced-motion/RTL styles exist, but no human device or assistive-technology review is recorded. | Layouts, `assets/css/site.css`, `assets/js/site.js`, quiz/search markup. | M | **Yes.** Select reviewer and supported test/browser matrix. |
| E. Build a reviewed beginner-to-intermediate path | **P2** | Tajkart has six lessons, three plans, and tested examples, but most learning paths remain introductory. Python is the best evidenced pilot: existing lessons and eight tested Python solutions already support a sequence. | New/extended `learning/lessons/`, `learning/courses/`, one project brief, `tests/`, search metadata. | L | No product-direction decision needed for a bounded Python pilot; an expert reviewer is required. |
| F. Deepen mapped CS subjects | **P2** | Forty-six subject headings are mapped but only 12 original subject guides exist; maps can overstate depth if presented as curriculum. | `learning/guides/`, `learning/subjects/`, `data/reference_coverage.yml`, tests and review metadata. | XL | **Yes.** Choose learner priority among the mapped topics after the pilot/review evidence. |
| G. Add verified external directories | **P3** | External resource count is zero. Existing schema already requires source, creator, date, attribution, and rights; upstream directory entries are individual third-party works. | `data/verified_resource.schema.json`, `learning/books/`, course/media indexes, source validator. | M for a small pilot; L for a maintained catalogue | **Yes.** Decide whether Tajkart should be an original curriculum, a directory, or a mix. |
| H. Improve practice and assessment | **P2** | The quiz has four questions and problem sets have tested canonical solutions; no debugging sequence or staged formative assessment exists. | `learning/interactive-tutorials/`, `learning/problem-sets/`, `assets/js/site.js`, `tests/search_test.js` or a focused test. | M | No, if limited to static, privacy-preserving activities; content reviewer required. |
| I. Set contributor permission terms | **P1** | Contribution docs request original work, but the all-rights-reserved license has no explicit grant for modifying, translating, or maintaining accepted external contributions. | `LICENSE` only if the owner approves a change; `COPYRIGHT.md`, `CONTRIBUTING.md`, `docs/LICENSING_REVIEW.md`. | M | **Yes.** This is a rights-holder decision; obtain qualified advice if formal terms are needed. |
| J. Strengthen maintenance checks selectively | **P2** | Core CI is green and Actions are SHA-pinned. Prior bounded URL checks are dated; adding flaky checks without an external catalogue creates maintenance cost. | `.github/workflows/pages.yml`, validators, schemas, `docs/DEPLOYMENT.md`, Dependabot settings. | S–M | No for an investigation/proposal; owner review before adding workflow or dependency changes. |

### Task definitions and acceptance criteria

#### A. Resolve secure hosting — P0, effort M

- **Deliver:** One confirmed public HTTPS hostname, correct Jekyll `url`/`baseurl`, matching GitHub Pages domain configuration, and a repeatable smoke-test record.
- **Dependencies:** Owner approval of Plan B; DNS-zone control; repository Pages admin access; verification of the custom domain; DNS/TLS propagation time.
- **Acceptance:** DNS resolves to the intended Pages target; valid TLS certificate matches the selected hostname; HTTPS enforcement is on; the selected HTTPS URL does not redirect to HTTP; personal homepage and apex/`www` routing remain unchanged; home, nested course, CSS/JS, search page, 70-entry search index, canonical tags, sitemap, `robots.txt`, and nested refresh pass at the selected host. The GitHub Actions build/deploy for the reviewed SHA passes.
- **Human review:** Owner confirms domain ownership and personal-site preservation; a human runs the browser smoke tests.
- **Decision:** Required. Set Tajkart's Pages custom domain to `learn.shahanishashmi.me`; create `CNAME learn → shahanishashmi.github.io` directly; align Jekyll to `url: https://learn.shahanishashmi.me`, empty `baseurl`; enforce HTTPS only after valid certificate issuance. Do not alter the apex or `www` records as a shortcut. See the exact owner-gated sequence above.

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

#### E. Ship one intermediate learning path — P2, effort L

- **Deliver:** A bounded, original Python foundations-to-intermediate sequence that extends existing learning rather than generating placeholder pages.
- **Dependencies:** Core technical review should identify gaps in the current Python sequence; tests and content schema remain stable.
- **Acceptance:** Four sequenced lesson units; each has observable objectives, explicit prerequisites, two worked examples with expected output and at least one edge case, three practice prompts with hints, and tested canonical solutions where executable. Add one capstone project brief with milestones, rubric, and one integration task. Search metadata and prerequisite IDs validate. Keep status drafted/pending until expert review is complete.
- **Human review:** Technical review of all lessons, examples, solutions, and project rubric.
- **Decision:** No owner decision for a limited Python pilot; owner review before expanding to another track.

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

1. Preserve the seven existing tracked documentation edits plus this roadmap, and review the complete diff before publication.
2. Ask the owner to select the permanent host and confirm access. Preferred proposal: dedicated `learn` subdomain; leave the current apex and `www` records alone.
3. After explicit authorization, apply only the selected Pages/DNS configuration, rebuild for its `url`/`baseurl`, and complete task A's HTTPS smoke tests.

**Milestone 0:** The selected hostname serves the intended site over valid HTTPS; there is no downgrade redirect; personal-site routes are unchanged; workflow and browser smoke evidence are recorded. Until this passes, do not call deployment ready.

### Phase 1 — Trust and quality

1. Run task B's expert review in reviewable batches, starting with lessons, study plans, and tested problems.
2. Complete task C with fluent Hindi and Urdu reviewers; keep draft status when unresolved.
3. Complete task D's manual accessibility/mobile matrix and retest blocking issues.
4. Decide task I's contributor permission terms before substantial outside contributions.

**Milestone 1:** Every currently published searchable resource has an honest review state; the core lessons/plans/problems have recorded expert review; translation/accessibility findings are resolved or documented; contributor terms are explicit. Automated tests remain green, but human approval is separately recorded.

### Phase 2 — Educational depth

1. Use technical review findings to complete task E's four-unit Python intermediate sequence and one capstone project brief.
2. Select three mapped subjects for task F using learner demand or founder direction; author one complete lesson unit per selected subject.
3. Add task H's staged debugging/code-reading exercise only after a reviewed lesson supplies its learning objective.

**Milestone 2:** The Python path has four sequenced, tested units and one assessed project; three additional subject units have outcomes, practice, and review status; the interactive task is keyboard-operable and privacy-preserving. No new page is counted as complete solely because it exists.

### Phase 3 — Discovery and scale

1. Make the product decision for task G. If a catalogue is justified, pilot one category with per-item provenance and rights review. Do not bulk import the reference ZIP.
2. Expand translations only when fluent reviewers and a chosen source curriculum are available; report actual translated lesson counts by language.
3. Evaluate task J after the catalogue or contributor workload grows; add bounded checks only for recurring maintenance risks.

**Milestone 3:** The directory-vs-curriculum decision is documented; any pilot entries pass source, attribution, rights, and freshness review (or the catalogue remains intentionally empty); locale and workflow coverage reflect actual maintained content.

## Risks and unresolved owner decisions

| Risk or decision | Current evidence | Required resolution |
|---|---|---|
| Hostname and HTTPS | GitHub project URL redirects to HTTP apex path; direct apex HTTPS certificate validation fails; `learn` has no DNS record. | Choose the host and confirm DNS/Pages access. Keep apex and `www` untouched. |
| Personal homepage disruption | Apex and `www` serve the founder's existing personal site. | Do not remove or repoint its Pages custom domain during Tajkart setup. |
| Human review availability | Searchable content remains drafted/pending; no expert review is recorded. | Name technical, fluent-language, and accessibility reviewers; agree scope and record decisions. |
| Third-party rights | Current external learning-resource inventory is empty; Tajkart reserves rights in original work. | Keep it empty unless each item and its rights are individually verified; decide contribution terms separately. |
| Scope inflation | Taxonomy has 46 mapped subjects and source locale inventory has 57 records. | Do not interpret maps as 46 completed subjects or 57 translations. Prioritize a small number of learning outcomes. |
| Automation noise | Prior external URL crawl was a dated bounded check; websites may block bots or change links. | Keep automation bounded and advisory for ambiguous failures; require human decision before removal. |
| Privacy and security | Static site; no server-side learner-code execution or student account tracking is designed. | Preserve this constraint. Any future code runner/account system requires separate privacy and isolation review. |
| Worktree publication | At this report snapshot, seven tracked documentation files were modified and this roadmap was untracked; none was staged or committed. | Review all local changes together. The owner separately decides whether to stage, commit, push, or deploy; never discard existing edits. |

## Single recommended next task

**P0: Restore secure delivery on the dedicated `learn.shahanishashmi.me` hostname, subject to the owner's confirmation of DNS control and repository Pages access.** The failure is observable on the deployed site and blocks safe release, while changing the apex domain could disrupt the personal homepage. The dedicated host offers a path to fix Tajkart without repointing apex or `www`.

- **Deliver:** Valid HTTPS, enforced HTTPS, correct canonical/base paths, and a passing smoke-test record for routes, assets, search index, sitemap, and direct nested-page refresh.
- **Out of scope for this task:** Changing the personal homepage, replacing its custom domain, adding learning features, importing resource lists, changing licenses, or claiming human content review.
- **How to verify:** Normal certificate validation succeeds; the selected HTTPS URL does not downgrade; apex homepage still serves; Pages run succeeds for the reviewed SHA; human smoke tests pass on the same hostname.
- **Immediately afterward:** Start Phase 1's expert review of the existing core lessons, courses, problems, and solutions. Keep their approval state pending until reviewers complete it.

This task requires the owner's explicit hostname decision and authorization before any DNS or GitHub Pages setting changes. This document makes the recommendation only; no such changes were performed.

## Out of scope

- Copying books, course descriptions, curated rows, translations, code, templates, or workflow implementations from the reference repository.
- Bulk importing the supplied ZIP or adding external entries to increase counts.
- Generating placeholder lessons or machine-translating content and marking it approved.
- Changing `LICENSE`, applying upstream CC BY 4.0 to Tajkart, or inventing contributor permission.
- Repointing the active personal homepage's apex/`www` DNS or removing its Pages domain association.
- Adding server accounts, learner tracking, or arbitrary server-side code execution.
- Claiming secure production readiness before hostname/TLS, human content, translation, and manual accessibility gates are complete.
- Committing, pushing, deploying, or editing DNS/Pages settings as part of this planning task.
