---
layout: page
title: P0 incident report
description: Verified diagnosis and safe recovery plan for Tajkart HTTPS enforcement and separate personal-domain availability incidents.
permalink: /docs/P0_INCIDENT_REPORT/
---

**Audit date:** 2026-10-15 (Asia/Kolkata)

**Repository:** `shahanishashmi/tajkart-student-hub`

**Current deployed SHA:** `d60d3c55589b05b16415c812ff4eb06cc553eb97`

This report records new evidence and a support draft. Earlier deployment history and broader site coverage remain in the [deployment record]({{ '/docs/DEPLOYMENT/' | relative_url }}) and [next-phase roadmap]({{ '/docs/ROADMAP_NEXT_PHASE/' | relative_url }}).

## Resolution status

**Incident A, Tajkart HTTPS enforcement: unresolved P0.** The project host serves normally over HTTPS with certificate verification, but its HTTP URL also serves the site without redirecting. The Pages API reports `https_enforced: false` and `https_certificate: null`. A previously owner-authorized update attempt returned HTTP 404, `The certificate does not exist yet`; a subsequent read left enforcement disabled. Do not repeat the request until GitHub Pages certificate/control readiness is confirmed.

**Incident B, personal-domain availability: unresolved and separate.** Apex and `www` DNS resolve to GitHub Pages, but both HTTP hosts return `404 Site not found`; HTTPS hostname validation fails before an HTTP response. The `learn` subdomain has no DNS answer. Do not change personal-domain DNS or Pages settings as part of Incident A.

The site is **not secure-release ready**. No DNS, Pages setting, Jekyll configuration, commit, push, or deployment was changed for this report. The Pages Settings UI was not available through the current CLI-only inspection, so its certificate/control display is **unknown**.

## Timeline

| Date/time | Evidence or action |
|---|---|
| 2026-10-14 19:59–20:00 UTC (2026-10-15 01:29–01:30 IST) | GitHub Actions run [38628224439](https://github.com/shahanishashmi/tajkart-student-hub/actions/runs/38628224439) built and deployed exact SHA `d60d3c55589b05b16415c812ff4eb06cc553eb97`; both jobs succeeded. |
| 2026-10-15, earlier in this session | Owner authorized **Enforce HTTPS** for the current Tajkart project URL. `PUT /repos/shahanishashmi/tajkart-student-hub/pages` with only `https_enforced: true` returned HTTP 404, `The certificate does not exist yet`. A follow-up GET reported enforcement still false. No setting changed. |
| 2026-10-15, approximately 01:59 IST | Read-only recheck confirmed the public project host still works on both protocols without redirect; current Pages API has `https_certificate: null`; apex/`www` still fail as detailed below. No second update attempt was made. |

## Current verified evidence

### Git and deployed workflow

At the start of this recheck, branch `main`, `HEAD`, `origin/main`, and live `origin/main` all resolved to `d60d3c55589b05b16415c812ff4eb06cc553eb97`. Eight tracked documentation files were already modified and unstaged; there were no staged files or untracked files. The existing edits were inspected and preserved. This report task also updated links/status wording in `ARCHITECTURE.md`, `DEPLOYMENT.md`, `IMPLEMENTATION_PLAN.md`, `NEXT_STEPS.md`, and `ROADMAP_NEXT_PHASE.md`; the report itself is the only new file. `_config.yml` and `.github/workflows/pages.yml` have no diff. Nothing has been staged, committed, pushed, or deployed.

Run [38628224439](https://github.com/shahanishashmi/tajkart-student-hub/actions/runs/38628224439) is `success` for the exact current deployed SHA. Its `build` and `deploy` jobs both succeeded. This proves hosted build/deployment for that SHA, not HTTPS enforcement or personal-domain availability.

### Incident A: Tajkart host

The current read-only Pages API result is:

```json
{
  "build_type": "workflow",
  "cname": null,
  "https_enforced": false,
  "html_url": "http://shahanishashmi.github.io/tajkart-student-hub/",
  "status": null,
  "protected_domain_state": null,
  "pending_domain_unverified_at": null,
  "https_certificate": null
}
```

Public probes used `curl.exe` with ordinary certificate verification, an eight-redirect cap, a 10-second connect timeout, and a 20-second total timeout. No TLS verification bypass was used.

| Request | Result |
|---|---|
| `https://shahanishashmi.github.io/tajkart-student-hub/` | HTTP 200, zero redirects; TLS verification succeeds. |
| `http://shahanishashmi.github.io/tajkart-student-hub/` | HTTP 200, zero redirects. |
| HTTPS learning library and nested data-structures course | Both HTTP 200, zero redirects. |
| HTTPS `search-index.json` | HTTP 200, `application/json`. |
| HTTPS `sitemap.xml` and `robots.txt` | Both HTTP 200. |
| HTTPS CSS and JavaScript assets | Both HTTP 200. |

Previously authorized setting attempt (not repeated during this report task):

```powershell
gh api --method PUT repos/shahanishashmi/tajkart-student-hub/pages -F https_enforced=true
```

GitHub returned HTTP 404 with `The certificate does not exist yet`. The current Pages GET still reports `https_enforced: false`. The API's certificate/control fields are null even though public HTTPS succeeds. **The internal cause is unknown.** A mismatch between edge TLS service and Pages enforcement readiness is an observation, not a confirmed explanation. The Settings UI has not been inspected, so it is unknown whether it shows a disabled control, a validation message, or another status.

GitHub documents HTTPS enforcement in its [Pages HTTPS guide](https://docs.github.com/en/pages/getting-started-with-github-pages/securing-your-github-pages-site-with-https) and the settings operation in the [Pages REST API](https://docs.github.com/en/rest/pages/pages#update-information-about-a-github-pages-site).

### Incident B: apex, `www`, and `learn`

| Host/probe | Result |
|---|---|
| `shahanishashmi.me` DNS A | `185.199.108.153`, `.109.153`, `.110.153`, `.111.153` (TTL about 1,088 seconds at the probe). |
| `www.shahanishashmi.me` DNS | CNAME to `shahanishashmi.me`. |
| `http://shahanishashmi.me/` and `http://www.shahanishashmi.me/` | Both HTTP 404, zero redirects. |
| `https://shahanishashmi.me/` and `https://www.shahanishashmi.me/` | TLS validation fails with `SEC_E_WRONG_PRINCIPAL` (curl exit 60); no HTTP status is available. |
| `learn.shahanishashmi.me` | DNS name does not resolve; HTTPS request fails with curl exit 6. |

The current CLI cannot resolve/read the separate `shahanishashmi/shahanishashmi.github.io` user-site repository/Pages resource (404). This does not prove whether that repo is deleted, renamed, private, or merely inaccessible to these credentials. DNS reaches GitHub Pages, but the root cause of the personal-domain 404 and certificate mismatch is **unknown**. Do not infer a repository or DNS fix from these probes.

## Root-cause assessment and control boundary

| Incident | Confirmed | Probable or unknown |
|---|---|---|
| A — HTTPS enforcement | Project HTTPS succeeds; HTTP also serves content; API says enforcement false and certificate null; the authorized update was rejected with the exact certificate error. | Why GitHub's enforcement endpoint reports no certificate while its public `github.io` endpoint serves valid TLS is unknown. No evidence establishes that waiting alone will fix it. |
| B — personal domain | Apex A records and `www` CNAME point to GitHub Pages; both HTTP hosts return 404; HTTPS host checks fail; `learn` is absent from DNS. | Which repository/account configuration caused the apex/`www` state is unknown because the separate user-site repo/settings are not accessible through current CLI credentials. |

Repository-controlled evidence includes source/config files, build workflow, local validation, and read-only API/probe records. GitHub Pages certificate issuance/enforcement internals, repository settings UI, and DNS-provider state are outside this worktree. DNS and hosting mutations require their respective owner/admin access and a separately scoped decision.

## GitHub Support draft — not submitted

**Subject:** Pages HTTPS enforcement reports missing certificate for a project site that serves valid HTTPS

> Repository: `shahanishashmi/tajkart-student-hub` (Pages build type `workflow`; custom domain `null`).
>
> On 2026-10-15, the owner-authorized Pages update request `PUT /repos/shahanishashmi/tajkart-student-hub/pages` with body `{"https_enforced":true}` returned HTTP 404: `The certificate does not exist yet`. A subsequent Pages GET reports `https_enforced: false`, `https_certificate: null`, `status: null`, and `html_url: http://shahanishashmi.github.io/tajkart-student-hub/`.
>
> At approximately 01:59 Asia/Kolkata on 2026-10-15, normal TLS-verified requests to `https://shahanishashmi.github.io/tajkart-student-hub/` and nested routes returned HTTP 200 with zero redirects, while `http://shahanishashmi.github.io/tajkart-student-hub/` also returned HTTP 200 with zero redirects. Search index, sitemap, robots, CSS, and JavaScript returned HTTP 200 over HTTPS. The latest successful Pages workflow is run [38628224439](https://github.com/shahanishashmi/tajkart-student-hub/actions/runs/38628224439) for SHA `d60d3c55589b05b16415c812ff4eb06cc553eb97`; its build and deploy jobs succeeded.
>
> Please explain why the Pages API reports no certificate and refuses HTTPS enforcement while the public default project hostname passes ordinary TLS validation. Is certificate/control provisioning pending or in an error state, and what supported action will make HTTPS enforcement available for this project URL? Please confirm whether repository-side action is required or GitHub must repair/reconcile its Pages certificate state.

This draft contains repository names and public endpoint evidence only. It contains no token, cookie, credential, or DNS-account data. **No GitHub Support request has been sent.** Submit it only through an owner-authorized support channel if the repository Settings → Pages view confirms the same mismatch or cannot explain the API response.

## Recovery options and rollback

### Option A — Resolve enforcement on the existing project hostname (recommended first)

1. A repository admin inspects **Settings → Pages** and records exactly what the certificate status and **Enforce HTTPS** control show. This UI inspection has not been done in this session.
2. If the UI says the certificate/control is not ready or gives no actionable explanation, submit the support draft above. Do not retry the API solely because time passed.
3. After GitHub confirms readiness, retry only `https_enforced: true` under the existing owner authorization. Verify HTTP redirects to HTTPS, with TLS verification on, and repeat the route/asset/index/sitemap/robots smoke checks.
4. If enforcement causes a problem, an admin may turn off only that same setting as a diagnostic rollback. This returns to a state where HTTP is available and **does not** satisfy the secure-release gate.

Risks: until enforcement succeeds, content remains available over plaintext HTTP. Changing project-domain or account Pages settings as a shortcut could affect unrelated Pages sites; do not do so.

### Option B — Dedicated `learn` hostname (separate owner decision; not applied)

Use only if the owner chooses a branded hostname or GitHub confirms the project host cannot be enforced. Prerequisites: verified control of the `shahanishashmi.me` DNS zone, repository Pages admin access, and a domain-verification check. Proposed DNS record: `CNAME` host/name `learn` → `shahanishashmi.github.io.` (directly; not to the apex and without a repository path). Tajkart Pages would need custom domain `learn.shahanishashmi.me`; Jekyll would need `url: "https://learn.shahanishashmi.me"` and `baseurl: ""`. Rebuild and validate canonical URLs, assets, search index, sitemap, and nested routes; wait for a valid matching certificate before enabling HTTPS.

Risks: DNS/TLS propagation can delay release; incorrect custom-domain setup can take the `learn` hostname offline or create ownership/confusion risk. Leave apex A records and `www` CNAME untouched. Rollback would remove only the `learn` CNAME and Tajkart's per-repository custom-domain association, restore the last reviewed `url`/`baseurl`, then rebuild/deploy. That rollback returns to the present non-enforced project host, not a secure state.

### Personal-domain recovery — separate incident

The owner/admin of the personal site must inspect the `shahanishashmi.github.io` repository, its Pages configuration, deployment status, and custom-domain ownership. Current evidence does not establish which setting or repository state caused the apex/`www` 404s. Do not remove a custom-domain association, alter apex/`www` DNS, or change the personal-site repo as part of Tajkart recovery. Any restoration needs its own approved plan and live HTTPS verification.

## Secure-release acceptance criteria

- The project hostname presents a valid certificate under normal TLS verification.
- Every tested HTTP project request redirects to the same HTTPS route; no HTTP content response remains.
- Home, learning library, nested lesson/course, CSS/JS, search index and interaction, canonical URLs, sitemap, robots, and direct nested refresh pass on HTTPS.
- The GitHub Pages workflow's build and deploy succeed for the reviewed SHA.
- Personal-domain apex/`www` status is reported separately and truthfully; it is not assumed fixed by the Tajkart change.
- Human browser smoke review is recorded. Until these criteria pass, keep P0 open and do not call the deployment secure-release ready.

## Checks performed for this report

Read-only commands included:

```powershell
git status --short --branch
git rev-parse HEAD
git ls-remote origin refs/heads/main
git diff --stat
git diff --cached --stat
git ls-files --others --exclude-standard
gh api repos/shahanishashmi/tajkart-student-hub/pages
gh run view 38628224439 --repo shahanishashmi/tajkart-student-hub
gh repo view shahanishashmi/shahanishashmi.github.io --json nameWithOwner,isPrivate,url
gh api repos/shahanishashmi/shahanishashmi.github.io/pages
curl.exe -sS -o NUL -w "%{http_code} redirects=%{num_redirects} effective=%{url_effective}`n" --max-redirs 8 --connect-timeout 10 --max-time 20 <URL>
Resolve-DnsName shahanishashmi.me -Type A
Resolve-DnsName www.shahanishashmi.me -Type CNAME
Resolve-DnsName learn.shahanishashmi.me -Type CNAME
```

After the report was added, `python scripts/validate_site.py` passed with 114 Markdown files, 101 routes, and 70 searchable resources. No support message, setting update, DNS edit, config edit, commit, push, or deployment was made. Ruby/Bundler were unavailable for a fresh Jekyll/generated-HTML run after these documentation edits. The worktree remains uncommitted; see `git status` before any later publication.

## Later local build evidence (2026-10-15)

The Ruby installation was subsequently found outside PATH at `C:\Ruby33-x64\bin`; Bundler dependencies were satisfied from the lockfile. The later student-first candidate passed Ruby front-matter validation, a strict production Jekyll build to a temporary destination, and generated-HTML validation for 110 pages and 78 search records. This does not change the incident state: the Pages API's last observed `https_enforced` value remains `false`, and no retry or Pages/DNS mutation occurred. Exact local results are in [deployment recheck]({{ '/docs/DEPLOYMENT/' | relative_url }}).
