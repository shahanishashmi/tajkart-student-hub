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
node tests/search_test.js
bundle exec jekyll build
python scripts/validate_html.py _site
```

Ruby 3.3.x is the required compatibility line; CI currently selects Ruby `3.3`. The cross-platform `Gemfile.lock` pins the `github-pages` dependency tree for Windows and Linux, so `bundle install` uses the same resolved gems locally and in CI.

Run the checks before opening a pull request:

```sh
python scripts/validate_site.py
python -m unittest discover -s tests -v
node --check assets/js/site.js
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
