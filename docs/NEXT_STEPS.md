---
layout: page
title: Next steps
description: Ordered continuation tasks for Tajkart Student Hub's student-first learning platform.
permalink: /docs/NEXT_STEPS/
---

This is an open work queue, not an approval record. The [master audit]({{ '/docs/MASTER_AUDIT_REPORT/' | relative_url }}) summarizes the platform and current evidence. The [quality and reliability backlog]({{ '/docs/QUALITY_RELIABILITY_BACKLOG/' | relative_url }}) tracks specific issues, checks, and human-review gates.

## Phase 1: quality and reliability

1. Preserve the new local edge-case tests for the eight canonical Python solutions. The Phase 1-only suite passed 66 tests; the current Phase 2 suite passes 80. GitHub Actions run [38800723889](https://github.com/shahanishashmi/tajkart-student-hub/actions/runs/38800723889) is green for committed SHA `3913f88`, but does not include these uncommitted changes; repeat hosted CI after a separately authorized publication.
   - The Explore Resources page has 18 category sections and deep links into candidate search. Headless Chrome 155 confirmed one-column/zero-overflow layout at 390×844 and two-column layout at 1440×1000, then loaded a real 525-result candidate query. A human keyboard, screen-reader, contrast, zoom/reflow, and usability review is still needed.
2. Arrange a qualified mathematics and programming review for the 33 questions, their solutions, and the new modeling unit. Keep every `review_status` pending until a reviewer records an item-level decision.
3. Inspect the current GitHub Pages certificate/control state. The owner-authorized HTTPS enforcement request was rejected with “The certificate does not exist yet”; retry only when GitHub reports readiness. Do not change DNS, `_config.yml`, or Pages domain settings as part of this retry. See the [P0 incident report]({{ '/docs/P0_INCIDENT_REPORT/' | relative_url }}).
4. Arrange fluent Hindi and Urdu review of the existing translations, and human accessibility review for keyboard, screen reader, contrast, mobile, zoom/reflow, reduced motion, and RTL rendering.

## Phase 2 local content increment (completed 2026-10-16)

1. Converted the seven arithmetic/data prompts to the shared question model with stable IDs, explicit skill/lesson/prerequisite mappings, hints, explanations, derivations, tests, and pending review states. Five final numeric answers are checked automatically; two compound responses use manual comparison and are not scored.
2. Added the original linear-equation word-problems and modeling lesson, three formative numeric questions, independent equation/substitution tests, algebra-course ordering, search metadata, and generated-page checks. All content remains pending educator review.
3. Updated solution coverage and the master audit from the repository data. The current report counts 33 questions, 33 answer/explanation records, 33 matching test references, 33 pending human reviews, 11 without machine-checkable accepted answers, 9 without per-question mappings, and zero broken mappings.
4. Local validation passed: 80 Python tests, source validation (140 Markdown files/127 routes/91 searchable records), solution-coverage check, Node checks, Ruby front matter/YAML validation, strict production build, generated HTML validation, and a headless Chrome interaction check. The exact results and limits are in the [master audit]({{ '/docs/MASTER_AUDIT_REPORT/' | relative_url }}).

## Next content and review action

Arrange item-level review by a qualified mathematics educator for the arithmetic-to-algebra sequence and all 33 questions. Keep every `review_status` pending until a real reviewer decision is recorded. After review, choose the next academic unit with learner or educator input. The worktree remains local/uncommitted; no hosted CI result is inferred.

## Remaining quality and release work

- Keep all 10,583 external-reference destinations marked unverified until their source, relevance, access, attribution, rights, and check date are reviewed individually. No full link crawl or rights review has been completed.
- Ask the rights-holder to decide contributor reuse terms before accepting substantial outside contributions; preserve the current root license unless that decision is explicit.
- Record mobile, keyboard-only, screen-reader, zoom/reflow, contrast, reduced-motion, and RTL findings with browser/device details and retest outcomes.
- Treat HTTPS enforcement as an independent release gate. A successful Actions deployment does not prove HTTPS enforcement or personal-domain availability.
- Review the entire accumulated diff before any separate commit, push, or deployment decision. Current local changes remain uncommitted; no DNS or Pages setting was changed.
