---
layout: page
title: Editorial review
description: A practical review gate for accuracy, usability, accessibility, and translations.
permalink: /docs/EDITORIAL_REVIEW/
---

Review a lesson as a learner would use it. Automated checks catch structural mistakes; they do not certify teaching quality or factual accuracy.

## Before publication

- The title describes the skill and the opening states what the page teaches.
- The audience, prerequisites, objectives, and difficulty agree with the examples.
- Explanations are original. Quotes, facts that can change, and third-party assets have traceable sources and rights notes.
- Code has expected output, handles a normal case, and mentions a useful edge case. Reference solutions have tests where feasible.
- Exercises have a clear prompt and useful hint or answer; difficulty is not inflated by wording.
- Links are relevant, local destinations resolve, and third-party links have a checked date when currency matters.
- Headings follow a logical order; links are descriptive; controls have labels; keyboard focus is visible.
- The resource has a unique ID, stable permalink, accurate tags, and honest content/review statuses.

## Translation review

1. Record the source resource ID and target language tag.
2. Translate the idea in natural language; do not copy a third-party translation.
3. Keep code identifiers, outputs, and technical terms consistent. Explain a retained English term on first use when it helps.
4. Have a fluent reviewer check meaning, tone, punctuation, and mixed-script code examples.
5. Check `lang`, `dir`, line wrapping, screen-reader pronunciation, and keyboard behavior in the rendered page.
6. Mark editorial review complete only after a human review; machine translation alone is not review.

## Status meanings

See [the schema]({{ '/docs/CONTENT_SCHEMA/' | relative_url }}) for allowed values. `validated` means automated structure and link checks passed. `approved` means a human editorial review was recorded. `complete` requires both and no known missing learning section. Review dates and reviewer names should be recorded in the resource or change history without publishing private contact details.
