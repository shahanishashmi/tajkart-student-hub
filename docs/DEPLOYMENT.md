---
layout: page
title: Build and deploy
description: Local preview, validation, and GitHub Pages deployment instructions for Tajkart Student Hub.
permalink: /docs/DEPLOYMENT/
---

## Preview and validate locally

Install Ruby and Bundler, Python 3, and Node.js. From the repository root:

```sh
bundle install
bundle exec jekyll serve
```

### Windows setup

The production site is built with Jekyll through the `github-pages` Ruby gem. There is no npm/package.json build. On Windows, install the same Ruby 3.3 release line used by CI with RubyInstaller's MSYS2 development kit:

```powershell
winget install --id RubyInstallerTeam.RubyWithDevKit.3.3 --exact --accept-package-agreements --accept-source-agreements
```

Complete the RubyInstaller setup, including MSYS2/Devkit if prompted, then open a new PowerShell terminal so the Ruby path is refreshed. If the Devkit toolchain was not initialized during installation, run `ridk install` and select the MSYS2/MINGW development toolchain. From the repository root, verify and build with:

RubyInstaller publishes the Windows builds on its [downloads page](https://rubyinstaller.org/downloads/) and documents the MSYS2/Devkit setup [here](https://rubyinstaller.org/add-ons/devkit.html).

```powershell
ruby --version
bundle --version
bundle install --jobs 4 --retry 3
python scripts/validate_site.py
python -m unittest discover -s tests -v
node --check assets/js/site.js
node --check assets/js/learning-tools.js
node tests/search_test.js
node tests/learning_tools_test.js
node tests/navigation_test.js
bundle exec jekyll build
python scripts/validate_html.py _site
```

Ruby 3.3.x is the required compatibility line; CI currently selects Ruby `3.3`. The cross-platform `Gemfile.lock` pins the `github-pages` dependency tree for Windows and Linux, so `bundle install` uses the same resolved gems locally and in CI.

Run the checks before opening a pull request:

```sh
python scripts/validate_site.py
python -m unittest discover -s tests -v
node --check assets/js/site.js
node --check assets/js/learning-tools.js
node tests/learning_tools_test.js
bundle exec jekyll build
python scripts/validate_html.py _site
```

The source validator checks metadata, IDs, routes, prerequisites, Python examples, and local Markdown links. The generated-site validator checks rendered HTML, local links, basic accessibility structure, and search-index consistency.

## Publish with GitHub Pages

1. Review and push the branch to the GitHub repository.
2. In repository **Settings → Pages**, choose **GitHub Actions** under **Build and deployment → Source**.
3. Merge reviewed changes to `main`. The workflow runs source checks and tests, builds Jekyll, validates generated HTML, then deploys successful `main` updates.
4. In **Settings → Environments**, restrict the `github-pages` environment to `main`.
5. Use the URL shown in **Settings → Pages** or the deployment environment link in the Actions run.

The deploy job receives `pages: write` and `id-token: write`; the build job has read-only repository access. If the repository path or custom domain changes, update `url` and `baseurl` in `_config.yml`. A root custom domain uses an empty base URL; a project site normally uses the repository path. See [GitHub's custom Pages workflow guide](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages) for repository-side setup.

## Deployment recovery diagnosis (2026-10-14)

This section records read-only checks of the current local candidate and public endpoints. The configured deployment target still needs an owner decision; `_config.yml`, DNS, repository Pages settings, and the published site were not changed during this diagnosis.

### Repository state and local candidate

At inspection, `main` and `origin/main` both pointed to `7b63a7dae16dbac8282fa621cda0ca7387040840`. The worktree contained 47 modified tracked files and 61 untracked status paths (93 untracked files), with no staged changes. The untracked files include source content, schemas, workflows, tests, `Gemfile.lock`, and the Liquid source template `search-index.json`; they are project inputs, not expendable build output. `_site/` is ignored generated output and was preserved. The empty local-only `tajkart-student-hub/` directory was also preserved. No reset, clean, deletion, staging, commit, push, or deployment was run.

The current `_config.yml` is configured for the default project site:

```yaml
url: "https://shahanishashmi.github.io"
baseurl: "/tajkart-student-hub"
```

The production build generated 99 HTML routes and a 70-entry search index. The search page points to `/tajkart-student-hub/search-index.json`; local assets and routes include the same base path. A read-only scan resolved all 1,780 generated local `href` and `src` targets. The sitemap and canonical URLs use the `github.io` project path. This candidate is internally consistent with the default project URL.

The Pages Actions workflow publishes the artifact using GitHub's custom workflow. No `CNAME` exists in the local candidate or at the inspected `main` commit. For this workflow type, GitHub documents that a CNAME file is not created automatically and is not required; its absence alone does not identify the configured domain. See [GitHub's custom-domain guide](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site?platform=mac) and [Jekyll URL and base-path guidance](https://docs.github.com/en/pages/setting-up-a-github-pages-site-with-jekyll/creating-a-github-pages-site-with-jekyll).

### Confirmed published and DNS symptoms

Read-only DNS and HTTPS checks on 2026-10-14 found:

| Probe | Result |
|---|---|
| `shahanishashmi.me` A records | `185.199.108.153`, `.109.153`, `.110.153`, `.111.153`, the GitHub Pages apex address set. |
| `www.shahanishashmi.me` | CNAME to `shahanishashmi.me`. |
| `learn.shahanishashmi.me` | NXDOMAIN; no A, AAAA, or CNAME answer. |
| `http://shahanishashmi.me/` | HTTP 200, serving the existing Shah Anis Hashmi homepage. |
| `https://shahanishashmi.me/` | TLS hostname validation failed (`curl` error 60 / Schannel wrong principal); no certificate-verification bypass was used. |
| Default project URL | `https://shahanishashmi.github.io/tajkart-student-hub/` returned 200 after redirecting to `http://shahanishashmi.me/tajkart-student-hub/`. The served page's canonical still names the `github.io` project URL. |
| Published project search index | `/tajkart-student-hub/search-index.json` returned 404 on the previously published revision. The current local template is uncommitted, so this does not establish what a future deployment will publish. |

The apex and `www` DNS are active for the existing homepage; changing or repointing them could disrupt that site. The `github.io` to HTTP custom-domain redirect is confirmed, but its source is not: repository Pages settings were unavailable through the anonymous Pages API probe (404), and the GitHub settings page was not inspected. DNS and HTTP responses do not reveal which account or repository setting created the redirect. The API 404 alone does not prove Pages is disabled. Direct HTTPS to the apex currently fails hostname validation, so do not mark either URL production-ready until the intended host serves a valid certificate and redirects to HTTPS.

### Two target plans; decision pending

| | A. Default project URL | B. Dedicated `learn` subdomain |
|---|---|---|
| Jekyll config | Keep `url: "https://shahanishashmi.github.io"` and `baseurl: "/tajkart-student-hub"`. | Set `url: "https://learn.shahanishashmi.me"` and `baseurl: ""` after the target is selected. |
| DNS and hostname | Use `shahanishashmi.github.io/tajkart-student-hub/`; do not change apex or `www` DNS. First identify and resolve the confirmed redirect to the apex HTTP URL in Pages/account configuration. | Add a `learn` CNAME pointing directly to `shahanishashmi.github.io`; leave apex and `www` records unchanged. `learn` currently has no DNS record. |
| Pages settings | Confirm this repository publishes with GitHub Actions and has no custom-domain association that redirects the project URL. Do not change settings until the redirect owner and effect on the existing homepage are understood. | In this repository's **Settings → Pages**, set the custom domain to `learn.shahanishashmi.me` and confirm the GitHub Actions source. Wait for GitHub to issue a valid certificate, then enable **Enforce HTTPS**. |
| Generated paths | The existing local candidate already builds search, assets, canonical links, and sitemap under `/tajkart-student-hub/`. | Jekyll's `relative_url` should generate site-root paths with an empty base path; rebuild and inspect index fetch, assets, canonical links, and sitemap after changing config. |
| Dependencies | GitHub repository admin access to inspect/resolve Pages settings; no DNS change expected. | Repository admin access, control of the `shahanishashmi.me` DNS zone, and time for DNS/TLS issuance. |
| Validation and rollback | Verify the project URL no longer redirects to insecure HTTP; smoke-test home, a nested lesson, search index, CSS/JS, canonical, sitemap, and robots. Roll back only the reviewed Pages-setting change if needed; leave apex DNS untouched. | Verify CNAME resolution and GitHub's HTTPS status before release; run the same smoke tests at `https://learn.shahanishashmi.me/`. Roll back by removing only the `learn` CNAME and this repository's custom-domain setting, then restore the previous reviewed Jekyll config. Leave apex and `www` untouched. |

**Recommendation: Plan B is the safer fit for preserving the existing homepage**, because it gives Tajkart a dedicated hostname while leaving the active apex and `www` routing alone. It depends on DNS-zone and repository-admin access, neither of which was exercised here. Plan A requires fewer site-code changes and matches the current local build, but the confirmed redirect and HTTP-only destination need investigation first. The owner must choose A or B before `_config.yml` is changed.

GitHub's [custom-domain instructions](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site?platform=mac) and [HTTPS guidance](https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https) cover DNS, certificate readiness, and repository settings. This diagnosis did not make those settings or DNS changes.

### Local evidence and release sequence

The current local candidate passed `python scripts/validate_site.py` (112 Markdown files, 99 routes, 70 searchable resources), 16 Python tests, Node syntax and search tests, Ruby front-matter validation, the production Jekyll build, and generated HTML validation. GitHub-hosted Actions have not run on this uncommitted worktree. The local build and generated link scan validate Plan A's paths only; Plan B must be rebuilt after its config is selected. Full results and outstanding human reviews are in [the repository audit]({{ '/docs/REFERENCE_AUDIT/' | relative_url }}).

After the target is selected and the owner has reviewed the complete diff:

1. Apply only the corresponding Jekyll configuration and approved Pages/DNS steps; for Plan B, keep the apex and `www` records unchanged.
2. Build locally and verify the generated canonical URLs, sitemap, search index URL, stylesheet, scripts, and nested routes against the selected hostname and base path.
3. Have the owner approve a commit and push when ready. Confirm the Pages workflow and all required checks pass on the intended branch; do not infer hosted success from local tests.
4. Confirm the selected host has a valid TLS certificate and HTTPS enforcement before release.
5. Smoke-test the home page, a nested lesson, search index and query, CSS/JS, canonical URL, sitemap, and a direct refresh of a nested route.

No commit, push, Pages-setting change, DNS update, or deployment was performed. The current working tree remains uncommitted.

## Post-push recovery verification (2026-10-15)

This section supersedes the earlier pending CI/deployment status with read-only evidence collected after commit `a83766c`. The earlier statement that no push had occurred describes the pre-push diagnosis on 2026-10-14. No DNS or Pages setting was changed during this follow-up.

### Source and hosted workflow

At the start of this follow-up, `main`, `origin/main`, and the worktree were clean at `a83766c26c97e13767f307176c0883df7cd2023b` (`Build out Tajkart Student Hub learning platform`). GitHub Actions run [38585940306](https://github.com/shahanishashmi/tajkart-student-hub/actions/runs/38585940306) completed with `success` for that exact SHA. Its `build` and `deploy` jobs both completed successfully. GitHub's deployment record `7069065011` also reports `success`, with environment URL `http://shahanishashmi.me/tajkart-student-hub/`.

The workflow and Pages artifact deployment therefore succeeded. The deployment record's HTTP URL and the live HTTPS failure below mean that hosted workflow success does not establish secure release acceptance.

### Authenticated Pages settings and domain evidence

Read-only authenticated GitHub API inspection returned:

| Pages site | Build type | Configured custom domain | HTTPS enforced | GitHub-reported URL/status |
|---|---|---|---|---|
| `shahanishashmi/tajkart-student-hub` | `workflow` | none (`cname: null`) | `false` | `http://shahanishashmi.me/tajkart-student-hub/`; API `status` was null. |
| `shahanishashmi/shahanishashmi.github.io` | `legacy` | `shahanishashmi.me` | `false` | `http://shahanishashmi.me/`; API status `built`. |

GitHub's Pages API reports the project URL as the apex-domain path even though the project repo has no custom CNAME, while the user-site Pages configuration owns `shahanishashmi.me`. A first-hop header check for the public `github.io` URL returned `301 Moved Permanently`, `Server: GitHub.com`, and `Location: http://shahanishashmi.me/tajkart-student-hub/`. This confirms GitHub's edge is issuing the HTTP redirect; DNS is not doing HTTP forwarding. The authenticated Pages health endpoint returned no warnings (`{}`) for the user-site domain; the project-site health endpoint returned 422 because that repo has no CNAME. The direct apex TLS error is confirmed, but the Pages API does not expose certificate-provisioning state, so its certificate issuance history remains unknown.

Read-only DNS still shows the apex A records `185.199.108.153`, `.109.153`, `.110.153`, and `.111.153`, `www` CNAME to the apex, and NXDOMAIN for `learn.shahanishashmi.me`. The apex HTTP page is the existing personal homepage (`shahanishashmi.github.io | Shah Anis Hashmi`). The apex is actively used and must not be repointed as part of Tajkart's recovery.

### Live smoke-test matrix

Requests used normal certificate verification and followed at most eight redirects. No TLS-verification bypass was used.

| Check | Observed result | Assessment |
|---|---|---|
| `https://shahanishashmi.github.io/tajkart-student-hub/` | HTTP 200 after one redirect to `http://shahanishashmi.me/tajkart-student-hub/`. | Fails HTTPS acceptance: the final destination is HTTP. |
| Direct `https://shahanishashmi.me/tajkart-student-hub/` | TLS hostname validation failed (`curl` 60 / Schannel `SEC_E_WRONG_PRINCIPAL`). | Fail; do not suppress certificate validation. |
| Home and nested course page | Both returned HTTP 200 after the same redirect. | Routes publish and refresh; transport remains insecure. |
| CSS and JavaScript | Both returned HTTP 200 from `/tajkart-student-hub/assets/...`. | Asset paths work on the current HTTP route. |
| Search page | `/learning/` returned 200; HTML has canonical `https://shahanishashmi.github.io/tajkart-student-hub/learning/` and `data-index-url="/tajkart-student-hub/search-index.json"`. | Paths are consistent with the checked-in project `baseurl`; canonical host disagrees with the effective HTTP destination. |
| Search index | HTTP 200, `application/json`, valid JSON with 70 entries. | Index is deployed and fetchable through the HTTP redirect target. |
| Sitemap and robots | Sitemap returned 200 with 98 locations, all on the `github.io` project URL; `robots.txt` returned 200. | Generated URLs still describe the default project host. |
| Dedicated `learn` host | DNS lookup returned NXDOMAIN; HTTPS request could not resolve. | Not configured; no live test is possible yet. |
| Search interaction and resource links | Deployed search JavaScript returned 200; local Node search tests pass. No remote browser interaction was run. | Matching/filter behavior still needs browser or human verification on the selected HTTPS host. |

The release checklist included in the supplied plan must not be marked 9/9: HTTPS and hostname checks fail, and technical, Hindi/Urdu, accessibility, and licensing reviews remain human tasks. The search index and route delivery are confirmed; interactive browser behavior is not.

### Hosting options and recommendation

The current `_config.yml` already matches Plan A's candidate values:

```yaml
url: "https://shahanishashmi.github.io"
baseurl: "/tajkart-student-hub"
```

Jekyll generates the expected project-path asset, search-index, canonical, and sitemap URLs. GitHub's live Pages behavior currently redirects the default project URL to the user-site apex path, so Plan A cannot be independently verified at its HTTPS URL while the current user-site domain configuration remains in effect. Removing that user-site domain setting could break the existing personal homepage; no such change should be made without the owner's explicit decision.

Plan B would give Tajkart `https://learn.shahanishashmi.me/` with `url: "https://learn.shahanishashmi.me"` and `baseurl: ""`. It requires a `learn` CNAME directly to `shahanishashmi.github.io`, setting that custom domain on the Tajkart Pages site, waiting for certificate provisioning, and enabling HTTPS after the certificate is valid. Keep the apex A records and `www` CNAME unchanged. Rollback would remove only the `learn` CNAME and Tajkart's subdomain setting, then restore `_config.yml` to the reviewed commit version.

**Recommendation:** For a permanent Tajkart hostname that preserves the existing personal homepage, Plan B has the lower domain-collision risk. Plan A remains the simplest Jekyll configuration and should only be used if the owner confirms how to test the default host without disrupting the user-site domain. The permanent hostname is still the owner's choice; no configuration or hosting change was applied.

### Required manual actions and current Git state

1. Choose the permanent URL. If choosing Plan B, confirm DNS-zone and repository-admin access.
2. In GitHub Pages settings, have the owner configure only the selected target and verify HTTPS after GitHub issues a valid certificate. Do not alter the user-site apex domain as a shortcut.
3. Rebuild for the selected `url`/`baseurl`; verify canonical links, sitemap, robots, CSS/JS/icon paths, nested refreshes, and search-index URL before release.
4. Run browser checks for search, filters, empty results, resource links, keyboard behavior, and mobile layout on the valid HTTPS hostname; finish the documented human content and rights reviews.

This diagnosis changed only `docs/DEPLOYMENT.md` locally. It is uncommitted; no new commit, push, DNS update, Pages-setting change, or deployment was performed. The pre-edit worktree was clean at `a83766c26c97e13767f307176c0883df7cd2023b`.

## Current execution recheck (2026-10-15, after `d60d3c5`)

This is the latest read-only release snapshot and supersedes earlier statements in this file about the current URL, redirect, and homepage state. Earlier sections remain as dated evidence of what was observed at those times.

### Git and hosted deployment

- Branch `main`, `HEAD`, `origin/main`, and live `origin/main` all resolve to `d60d3c55589b05b16415c812ff4eb06cc553eb97`. The worktree was clean at the start of this recheck.
- GitHub Actions [run 38628224439](https://github.com/shahanishashmi/tajkart-student-hub/actions/runs/38628224439) completed successfully for that exact SHA. Both the build and Pages deploy jobs passed.
- The Pages deployment serves the new `/docs/ROADMAP_NEXT_PHASE/` page.

### Current DNS, Pages API, and HTTPS results

| Probe | Result |
|---|---|
| Tajkart Pages API | `build_type: workflow`, `cname: null`, `https_enforced: false`, `html_url: http://shahanishashmi.github.io/tajkart-student-hub/`, `status: null`. |
| Default project HTTPS URL | `https://shahanishashmi.github.io/tajkart-student-hub/` returns HTTP 200 with zero redirects and normal TLS validation. |
| Default project HTTP URL | `http://shahanishashmi.github.io/tajkart-student-hub/` returns HTTP 200 with zero redirects. HTTPS is not enforced. |
| Project smoke routes/assets | Home, learning library, nested data-structures course, roadmap page, search index, sitemap, robots, CSS, and JavaScript all return HTTP 200 over HTTPS. The learning-page canonical URL and search-index path match the checked-in project `url`/`baseurl`. |
| Apex DNS | `shahanishashmi.me` resolves to GitHub Pages A records `.108.153`, `.109.153`, `.110.153`, and `.111.153`. HTTP currently returns GitHub Pages 404 `Site not found`; normal HTTPS validation fails with `SEC_E_WRONG_PRINCIPAL`. |
| `www` DNS and response | `www.shahanishashmi.me` is a CNAME to the apex; HTTP currently returns GitHub Pages 404 `Site not found`. |
| `learn` hostname | `learn.shahanishashmi.me` does not resolve; no HTTPS test is possible. |
| Separate user-site repo | `gh repo view shahanishashmi/shahanishashmi.github.io` and its Pages API return 404 to the current GitHub CLI credential; `https://shahanishashmi.github.io/` also returns 404. This does not prove the repository was deleted or establish its current settings. |

The earlier reported project-URL redirect to the apex was **not reproduced** after `d60d3c5`; current HTTPS project routes return directly from `github.io`. The current Tajkart transport blocker is that HTTP also returns the page and the Pages API reports `https_enforced: false`. The apex/`www` site is currently unavailable by these probes, so do not claim the previous personal homepage is live, preserved, or restored. No DNS or Pages setting was changed.

### Owner-authorized HTTPS enforcement attempt (2026-10-15)

The owner explicitly authorized enabling **Enforce HTTPS** for Tajkart's current `github.io` project URL. The documented GitHub REST **Update information about a GitHub Pages site** endpoint was called with only `https_enforced: true`; GitHub returned HTTP 404 with `The certificate does not exist yet`. A follow-up GET still reports `https_enforced: false`, `cname: null`, and the same project URL. No Pages setting changed. The checked-in config remains `url: "https://shahanishashmi.github.io"` and `baseurl: "/tajkart-student-hub"`.

After the rejected request, normal `curl.exe` checks again returned HTTP 200 with zero redirects for both the HTTP and HTTPS home and learning routes. HTTPS certificate validation still succeeds for the project host; HTTP enforcement remains off. The apex A records, `www` CNAME, missing `learn` DNS record, and `_config.yml` were not changed.

**Current blocker:** GitHub refuses the enforcement update because its Pages settings API says the certificate does not exist yet; the latest read also reports `https_certificate: null`, despite the public project URL passing normal HTTPS validation. The next step is to inspect the Tajkart repository's **Settings → Pages** certificate/control state or obtain GitHub's explanation for this mismatch. Retry only the same `https_enforced` setting after GitHub reports it can be enforced. Do not change DNS, `cname`, `build_type`, or `_config.yml` as part of that retry. If GitHub confirms this host cannot enable enforcement, the separate `learn.shahanishashmi.me` option and support draft are in the [P0 incident report]({{ '/docs/P0_INCIDENT_REPORT/' | relative_url }}). Keep apex and `www` records untouched.

No setting change, DNS update, commit, push, or deployment occurred during this recheck. The current worktree has eight modified tracked documentation files and the new untracked `docs/P0_INCIDENT_REPORT.md`; nothing is staged. After adding the report, `python scripts/validate_site.py` passed with 114 Markdown files, 101 routes, and 70 searchable resources. The 16 Python tests and Node syntax/search checks passed during the preceding documentation follow-up; they were not rerun after this report-only update. Ruby and Bundler are not available in the current PowerShell PATH, so front-matter validation, a fresh production Jekyll build, and generated-HTML validation could not be rerun after the latest documentation edits; the earlier baseline results above apply to the earlier snapshot. No external-link crawl or human technical, language, rights, browser, or accessibility review was performed.

## Local student-first candidate validation (2026-10-15)

The local PowerShell PATH did not include Ruby, but Ruby 3.3.12 was found at `C:\Ruby33-x64\bin`; Bundler 2.5.22 and the `Gemfile.lock` dependencies were already available. No installation or lockfile change was needed. The current student-first candidate passed:

| Check | Result |
|---|---|
| `python scripts/validate_site.py` | **Pass:** 125 Markdown files, 112 routes, 79 searchable resources; no reported metadata, duplicate ID/route, curated URL, reference, Python syntax, or local Markdown-link errors. |
| `python -m unittest discover -s tests -v` | **Pass:** 21 tests. |
| JavaScript syntax, `node tests/search_test.js`, `node tests/navigation_test.js` | **Pass:** search token/tag/provenance cases; eight navigation destinations, five student routes, menu state, Escape/focus return, and source-level responsive CSS checks. |
| `ruby scripts/validate_front_matter.rb` | **Pass:** 115 Markdown front-matter files and five YAML files. |
| `JEKYLL_ENV=production bundle exec jekyll build --strict_front_matter --destination <temporary-directory>` | **Pass:** generated the candidate without touching the existing `_site/`; final output contains 112 HTML pages and 79 search records. Jekyll printed a non-blocking notice that optional `faraday-retry` middleware is not installed. |
| `python scripts/validate_html.py <temporary-directory>` | **Pass:** 112 generated HTML pages, 79 search records, local links/fragments, IDs, labels, language, landmarks, and provenance metadata. |
| `git diff --check` | **Pass:** no whitespace errors; Git reports expected LF-to-CRLF normalization notices for existing files. |

The table above records an earlier student-first candidate and its counts; later local implementation supersedes those numbers. The current algebra/mastery/planner/portfolio candidate validates 136 Markdown files, 123 routes, 89 searchable resources, 47 Python tests, six generated course paths, and 32 planner sessions. Headless Chrome 154 checked planner, quiz, and portfolio interactions at 375×812 CSS pixels with no horizontal overflow on those pages. This is not human visual, accessibility, technical, or language approval. No GitHub Actions run covers the current worktree; the Pages HTTPS enforcement state remains off, and no DNS/Pages mutation, commit, push, or deployment occurred. See the [combined platform audit]({{ '/docs/MASTER_AUDIT_REPORT/' | relative_url }}) for the single current evidence record and remaining release gates.
