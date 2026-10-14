---
layout: page
title: Implementation plan
description: A reviewable plan for growing Tajkart Student Hub from its first release into a multilingual learning library.
permalink: /docs/IMPLEMENTATION_PLAN/
---

This plan adapts the reference archive's breadth to Tajkart's original-content policy and static GitHub Pages stack. It does not copy the archive's entries, prose, translations, scripts, templates, workflows, or branding. Progress belongs in [the content progress report]({{ '/docs/CONTENT_PROGRESS/' | relative_url }}); category-by-category traceability belongs in [the reference inventory]({{ '/docs/REFERENCE_COVERAGE/' | relative_url }}).

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
| 3. Discovery and practice | Index authored resources by text, type, category, language, tags, difficulty, provenance, and review state; add exercises and tested solutions. | 70 source resources identified; source checks, 16 Python unit tests, and the Node search behavior check pass locally; relevance ranking and provenance filters are implemented. | Production index and all 70 rendered search entries pass local build/output validation. |
| 4. Projects and careers | Add project briefs and career guides; keep opportunity advice separate from live listings. | Six project specs and five focused career guides; no fabricated opportunities. | Authored; human review and project implementations remain. |
| 5. Multilingual and accessibility | Add Hindi/Urdu drafts, RTL support, source locale inventory, keyboard, and screen-reader checks. | Two translations have explicit draft/pending status; automated output checks are configured. | Translation review and manual accessibility checks remain. |
| 6. Release quality | Build, route/link/schema checks, code tests, generated-HTML checks, external URL crawl, accessibility review, and deployment verification. | Local source checks, code tests, Jekyll production build, and generated-HTML checks pass on Ruby 3.3.12. A bounded crawl checked 18 repository/reference/tooling URLs; all returned HTTP 200 after redirect handling. | GitHub-hosted CI has not run on this uncommitted batch. The published Pages URL redirects to an HTTP custom domain whose HTTPS certificate fails hostname validation; the Pages API returned 404. Human technical, translation, and accessibility reviews remain. See the dated release-gate evidence in [the audit]({{ '/docs/REFERENCE_AUDIT/' | relative_url }}). |

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

The hosted Pages workflow and deployment succeeded for `a83766c26c97e13767f307176c0883df7cd2023b`. Read-only endpoint checks still show a redirect from the GitHub project URL to HTTP on the custom domain and a certificate hostname failure on direct HTTPS. Local source, test, production-build, and generated-HTML checks pass; uncommitted documentation changes have not run through hosted CI. The immediate recommended task is to resolve the HTTPS hostname without changing the active personal homepage; see the [next-phase audit and roadmap]({{ '/docs/ROADMAP_NEXT_PHASE/' | relative_url }}) and [deployment recovery evidence]({{ '/docs/DEPLOYMENT/' | relative_url }}).
