---
layout: page
title: Implementation plan
description: A reviewable plan for growing Tajkart Student Hub from its first release into a multilingual learning library.
permalink: /docs/IMPLEMENTATION_PLAN/
---

This plan adapts the reference archive's breadth to Tajkart's original-content policy and static GitHub Pages stack. It does not copy the archive's entries, prose, translations, scripts, templates, workflows, or branding. Progress belongs in [the content progress report]({{ '/docs/CONTENT_PROGRESS/' | relative_url }}); category-by-category traceability belongs in [the reference inventory]({{ '/docs/REFERENCE_COVERAGE/' | relative_url }}) and the [file-level parity matrix]({{ '/docs/REFERENCE_PARITY_MATRIX/' | relative_url }}). The current evidence and results are consolidated in the [combined platform audit]({{ '/docs/MASTER_AUDIT_REPORT/' | relative_url }}).

## Principles

1. Publish a small, tested learning unit before expanding a category.
2. Treat each resource index as a navigation page, not evidence that its topic is taught.
3. Use stable IDs and shared front matter so search, review, and validation can grow together.
4. Start with original English content, then translate selected lessons into Hindi and Urdu with editorial review.
5. Keep the site static. Do not execute learner-submitted code on a server.
6. Preserve the existing `LICENSE`; document Tajkart's rights boundary separately.

## Delivery sequence

| Batch | Work | Exit evidence | Status |
|---|---|---|---|
| 1. Foundation | Audit repository and reference; define taxonomy, site shell, contribution standards, and first lessons. | Source hash, archive counts, all 46 subjects, 57 locale records, repository state, architecture, rights boundaries, and destination maps recorded in the audit documents. | Audit documents complete; review branch and human rights/contributor-term decisions remain. |
| 2. Content system | Publish schema, editorial gates, progress matrix, subject guides, language paths, and cheatsheets. | Searchable resources carry IDs, metadata, routes, objectives, and honest draft/review status. | Authored; human technical review remains. |
| 3. Discovery and practice | Index authored resources by text, type, category, language, tags, difficulty, provenance, and review state; add exercises and tested solutions. | 76 source resources identified; source checks, 21 Python unit tests, and the Node search behavior check pass locally; relevance ranking and provenance filters are implemented. | The previous 70-entry rendered index passed an earlier local build. The latest six resources await a Jekyll build and generated-output check. |
| 4. Projects and careers | Add project briefs and career guides; keep opportunity advice separate from live listings. | Seven project specifications and five focused career guides; no fabricated opportunities. | Authored; human review and learner-built project implementations remain. |
| 5. Multilingual and accessibility | Add Hindi/Urdu drafts, RTL support, source locale inventory, keyboard, and screen-reader checks. | Two translations have explicit draft/pending status; automated output checks are configured. | Translation review and manual accessibility checks remain. |
| 6. Release quality | Build, route/link/schema checks, code tests, generated-HTML checks, external URL crawl, accessibility review, and deployment verification. | Current Python source checks, 21 unit tests, and Node checks pass. Earlier Jekyll and generated-HTML checks passed for an older candidate; hosted run `38628224439` passed for `d60d3c5`. | Current Jekyll/generated-HTML checks and hosted CI are pending. HTTPS works on the project URL but HTTP is not redirected (`https_enforced: false`). Apex/`www` currently return 404; human technical, translation, and accessibility reviews remain. See the [deployment recheck]({{ '/docs/DEPLOYMENT/' | relative_url }}). |

## Out of scope until separately justified

- A server-side account system, learner tracking, or arbitrary code execution.
- Automated claims that an external offer, course, or link is current without checking its official source.
- Mass machine translation or a large third-party resource catalogue.
- Replacing or broadening the current repository licence without a separate rights review.

## Change control

Each batch updates the progress matrix and reference inventory. Work remains local until the owner explicitly approves a push. Never discard existing edits or use destructive Git commands to force the project into this plan.

## Release gate status (2026-10-14)

- **Passed locally:** source metadata/routes/link validation, Python tests, Node search checks, Ruby front matter/YAML parsing, production Jekyll build, generated HTML/search-index validation, and bounded external URL crawl.
- **Pending hosted evidence:** GitHub Actions must run on the reviewed commit; it cannot test these local uncommitted changes without publishing a branch or otherwise triggering GitHub.
- **Deployment blocker:** verify Pages/custom-domain settings and restore valid HTTPS on the published target before calling deployment ready. The current local `url` and `baseurl` build a project path, but the published URL redirects to a custom-domain HTTP address.
- **Pending human review:** technical correctness of examples and lessons, fluent Hindi/Urdu translations, attribution/originality and reuse terms, keyboard/screen-reader/contrast/zoom/mobile accessibility.
- **Worktree:** all prior work is preserved and remains uncommitted; no commit, push, or deployment was made. Exact status counts are recorded in the audit.

## Current baseline (2026-10-15)

The hosted Pages workflow and deployment succeeded for `d60d3c55589b05b16415c812ff4eb06cc553eb97`. The default project URL serves directly over HTTPS, but it also serves over HTTP without redirect; the Pages API reports `https_enforced: false` and `https_certificate: null`. The owner-authorized enforcement update failed with `The certificate does not exist yet`. Apex and `www` return GitHub Pages 404 responses, and direct apex HTTPS has a certificate hostname failure. The current support draft and separate recovery findings are in the [P0 incident report]({{ '/docs/P0_INCIDENT_REPORT/' | relative_url }}).
