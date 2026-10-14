---
layout: page
title: Content schema
description: Stable fields and statuses used to catalogue Tajkart learning resources.
permalink: /docs/CONTENT_SCHEMA/
---

Searchable learning resources use YAML front matter. The schema keeps page identity, discovery, review, and progress separate. Category landing pages can omit resource fields; every item marked `searchable: true` must provide them.

```yaml
id: python-variables-001
title: "Names and values in Python"
permalink: /learning/lessons/python-variables/
content_type: lesson
category: programming-languages
language: en
content_origin: original
difficulty: beginner
tags: [python, variables, data-types]
prerequisites: []
learning_objectives:
  - Explain the difference between a name and a value
estimated_minutes: 20
content_status: drafted
review_status: pending
searchable: true
```

## Field rules

| Field | Rule |
|---|---|
| `id` | Required for searchable resources; lowercase ASCII words separated by hyphens; globally unique; do not change after publication. |
| `title` | Required and specific. Avoid using the subject name alone when the page teaches a narrower skill. |
| `permalink` | Required, site-root-relative, stable, and unique. Use the trailing slash convention for pages. |
| `content_type` | One of `lesson`, `guide`, `course`, `cheatsheet`, `problem-set`, `project`, `interactive`, `career`, or `opportunity-guide`. |
| `category` | A stable discovery label such as `programming-languages`, `computer-science`, `web-development`, or `career-skills`. |
| `language` | BCP 47 language tag in lowercase/standard region form, for example `en`, `hi`, `ur`, `pt-BR`. Keep source archive filename spellings in the reference inventory separately. |
| `content_origin` | `original` is the site-wide default. Use `translation` for a Tajkart translation draft and `external` for a third-party resource entry. |
| `translation_of` | Required for translations; must reference the ID of an original Tajkart resource. |
| `translation_status` | Required for translations: `draft`, `review-required`, or `approved`. A draft cannot be marked approved. |
| `difficulty` | One of `beginner`, `intermediate`, `advanced`, or `all-levels`; describe prerequisites honestly. |
| `tags` | Short, lowercase discovery terms; do not use prose sentences as tags. |
| `prerequisites` | IDs of resources or a short, explicit skill statement; never an unexplained acronym. |
| `related_resources` | Optional list of other Tajkart resource IDs; every ID must resolve to a page. |
| `learning_objectives` | Observable learner actions, not promises about employment or mastery. |
| `estimated_minutes` | Optional estimate; state that actual time varies where relevant. |
| `content_status` | `not-started`, `in-progress`, `drafted`, `review-required`, `validated`, or `complete`. |
| `review_status` | `not-reviewed`, `pending`, `technical-reviewed`, `language-reviewed`, `accessibility-reviewed`, or `approved`. |
| `searchable` | Set to `true` only for substantive content with a stable destination. |

`complete` is reserved for content that meets [the editorial review gate]({{ '/docs/EDITORIAL_REVIEW/' | relative_url }}), has working links and examples, and has no known blocker. A file's existence or route is not enough.

## External resource and opportunity records

There are currently **no third-party books, courses, media, websites, or opportunities listed as verified**. An `external` searchable page must have `verification_status: verified`, a creator, an HTTP(S) `source_url`, `source_checked` date, a clear attribution statement, a `rights_note`, and a resolved `rights_status` (`link-only`, `license-identified`, `permission-granted`, or `public-domain`). `license-identified` entries must name the terms in `terms_or_license`. Unclear rights must be resolved before publication; the source validator rejects unverified entries, missing attribution, invalid source URLs/dates, and unresolved rights states. Search labels external entries as external, shows creator/rights/verification details, and links directly to their source.

Future external learning-resource records must match the [verified resource schema]({{ '/data/verified_resource.schema.json' | relative_url }}) and include title, creator, language, URL, topic, format, attribution, rights status/note, and the date the official source was checked. Future opportunity entries must match the [opportunity schema]({{ '/data/opportunity.schema.json' | relative_url }}) and state provider, eligibility, official source, deadline when known, verification status, last-verified date, and terms. An unverified record must not be published as live.
