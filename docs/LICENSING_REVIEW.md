---
layout: page
title: Licensing and attribution review
description: The rights notices inspected for Tajkart and the reference archive, plus practical boundaries for future resources.
permalink: /docs/LICENSING_REVIEW/
---

## Tajkart files inspected

The existing root `LICENSE` is a short, project-specific all-rights-reserved notice. It reserves rights in original Tajkart-authored content in this repository, allows exceptions where a file says otherwise, and states that later third-party materials may have separate terms. It does not grant a general permissive license to reuse Tajkart lessons, code, documentation, or visual work. The file was inspected and preserved unchanged during this work.

`COPYRIGHT.md` and `docs/CONTENT_POLICY.md` distinguish Tajkart-authored work from linked third-party material and say that rights and attribution must be checked before adding external text, images, code, or data. No separate file-level third-party license notice was found in the current learning-content inventory. The site favicon and design assets are Tajkart-created in the project; third-party work should not be added to them without recording its terms.

## Reference archive inspected

At the pinned upstream commit, the reference README says that each file included in its repository is under its CC BY License and links to the repository's `LICENSE`, whose legal text is Creative Commons Attribution 4.0 International. The read-only archive scan found license labels in some curated entries and contributor examples as well as the repository-wide notice. Those individual labels are indications about particular linked works, not permission to reproduce the works themselves.

The repository's blanket notice does not turn every listed book, course, website, podcast, image, or other linked work into CC BY material. A third-party work can have its own license or access conditions. This review did not inspect the rights of every resource URL in the source archive and makes no claim that the links are current or reusable. The source's scripts, workflows, templates, prose, and lists were not copied into Tajkart.

## Current boundaries

- Keep Tajkart's existing `LICENSE` and per-file notices authoritative for this project; do not silently apply the reference archive's CC BY license to Tajkart.
- Write original explanations, examples, exercises, translations, and project briefs. A fact or programming idea may be taught independently, but source wording, examples, illustrations, and solutions should not be copied without a valid basis.
- For an external record, store the provider/author, official URL, content type, language/topic, source-check date, verification state, clear attribution, a rights note, and a resolved license or reuse status. `license-identified` entries must name the terms. The [verified resource schema]({{ '/data/verified_resource.schema.json' | relative_url }}) and source validator enforce those fields.
- There are currently no verified third-party learning-resource or opportunity entries in the published content set. Future external entries must include creator attribution and one of the explicit link/license/permission/public-domain rights states; unknown rights remain blocked for review.
- Link to external resources instead of republishing their files. Identify authorship and rights at the item level; do not imply Tajkart authorship, endorsement, or affiliation.
- Remove or correct a resource promptly if its permission, attribution, URL, or availability cannot be established.

## Open contributor-rights decision

The current contribution guide asks for original work and prohibits unlicensed assets, but the repository has no formal Contributor License Agreement and no explicit contributor grant that explains how accepted contributions may be published, modified, translated, or maintained under the all-rights-reserved notice. This audit does not invent that legal term. Before accepting substantial material from outside the project, the maintainers should publish a clear contributor permission policy and record any exception or third-party license alongside the file.

This is a repository rights inventory, not legal advice. Consult a qualified rights professional if Tajkart needs a formal contributor agreement or plans to distribute substantial third-party content.

## Sources

- [Reference README at the audited commit](https://github.com/EbookFoundation/free-programming-books/blob/2574d859ecf34dd8d1643cc5c7c9f11ae99f845c/README.md)
- [Reference LICENSE at the audited commit](https://github.com/EbookFoundation/free-programming-books/blob/2574d859ecf34dd8d1643cc5c7c9f11ae99f845c/LICENSE)
- Tajkart's local [LICENSE]({{ '/LICENSE' | relative_url }}), [copyright page]({{ '/copyright/' | relative_url }}), and [content policy]({{ '/docs/CONTENT_POLICY/' | relative_url }})
