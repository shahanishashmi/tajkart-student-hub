---
layout: page
title: Next steps
description: Ordered continuation tasks for Tajkart Student Hub's student-first learning platform.
permalink: /docs/NEXT_STEPS/
---

This list is a continuation queue, not a claim that drafts are approved. The single evidence record for current product coverage, implementation, checks, reference comparison, worktree state, and release gates is the [combined platform audit]({{ '/docs/MASTER_AUDIT_REPORT/' | relative_url }}). The dependency order and earlier recovery evidence remain in the [next-phase roadmap]({{ '/docs/ROADMAP_NEXT_PHASE/' | relative_url }}).

1. Retry the already authorized **Enforce HTTPS** setting for `https://shahanishashmi.github.io/tajkart-student-hub/` only after GitHub Pages reports that a certificate is available. The previous API attempt returned HTTP 404, `The certificate does not exist yet`; enforcement remains off. Do not alter DNS, `_config.yml`, CNAME, build source, or personal-domain settings as part of that retry. See the [P0 incident report]({{ '/docs/P0_INCIDENT_REPORT/' | relative_url }}).
2. Arrange a mathematics educator review of the seven draft arithmetic/algebra lessons, two courses, both formative assessments, and all ten algebra answer derivations. Separately review the ten programming lessons, intermediate Python path, other courses, guides, solutions, projects, and cheatsheets. Keep `review_status: pending` until a human records a decision.
3. Have fluent Hindi and Urdu reviewers check the existing translation drafts, terminology, `lang`/`dir`, and rendered reading order before approval.
4. Run a human browser review of navigation, search, planner, quiz feedback, local data clearing, and portfolio drafts on mobile and desktop. Include keyboard-only use, zoom/reflow, reduced motion, RTL, and a screen-reader pairing. Headless Chrome passed a narrow interaction/overflow check; that is not human accessibility or usability approval.
5. For the next content increment, draft an original **linear-equation word problems and modeling** unit that connects algebra to practical student scenarios. Include objectives, prerequisites, worked translations, unit checks, hints, substitution checks, and tested examples; map it into the algebra course and keep it pending educator review. Use learner/teacher feedback before choosing another subject.
6. Decide whether Tajkart should maintain third-party book/course/media/playground directories. Add no item without checking its official source, attribution, terms, rights state, and last-checked date; keep catalogues empty where those checks are unresolved.
7. Have the rights-holder decide contributor reuse terms before accepting substantial outside contributions. Preserve Tajkart's current license unless that decision is explicit.
8. Consider a bounded external-link crawl only if maintenance needs justify it. Use timeouts, retry limits, rate limits, redirect caps, and a manual queue for blocked or uncertain results; never remove a resource only because a crawler cannot access it.
9. Review the complete accumulated diff before a separate commit/push decision. The current worktree remains uncommitted on `main` at `d60d3c5`; no hosted Actions run covers this candidate. Do not commit, push, or deploy until the owner chooses that step.