---
layout: page
title: "Capstone: local Python study log"
description: "Build a small command-line program that validates, stores, and summarizes fictional study sessions."
summary: Build a small command-line program that validates, stores, and summarizes fictional study sessions.
permalink: /learning/projects/python-study-log/
id: project-python-study-log
content_type: project
category: programming-languages
language: en
difficulty: intermediate
tags: [python, capstone, json, testing, command-line]
prerequisites: [course-python-intermediate-study-log, python-intermediate-testing-001]
related_resources: [python-intermediate-collections-001, python-intermediate-validation-001, python-intermediate-json-001]
learning_objectives:
  - Build a small program from validated, reusable functions.
  - Persist fictional study-session records in local JSON.
  - Test normal, empty, invalid, and missing-file behavior.
estimated_minutes: 180
content_status: drafted
review_status: pending
searchable: true
---

## Goal and prerequisites

Build a command-line study log that records a topic and positive whole-number minutes, saves entries in a local JSON file, and prints totals per topic. Work through the [four-part Python intermediate course]({{ '/learning/courses/python-intermediate/' | relative_url }}) first. The full application is a learner-built project; this repository includes small tested reference helpers, not a finished command-line product.

## Required behavior

- Accept a topic and number of minutes for one study session.
- Strip surrounding whitespace from the topic; reject an empty topic, non-integer duration, zero, and negative duration with a clear message.
- Load previous records from a local JSON file. Start with an empty list if the file does not exist, and report malformed JSON without silently overwriting it.
- Summarize total minutes by topic in a stable order.
- Keep the calculation and validation functions independent from prompts and printing.
- Use fictional records only. Do not add user accounts, telemetry, private learning histories, or network services.

## Milestones

1. Implement and test the record validator and topic summary using in-memory lists.
2. Add JSON load/save functions; test them in a temporary directory with a missing file, valid file, and malformed file.
3. Add a small command-line entry point guarded by `if __name__ == "__main__"`.
4. Write a short README for the project describing how to run it, the JSON shape, and the limits of local storage.

## Acceptance checks

Try a new empty log, one valid session, repeated topics, whitespace around a topic, invalid text for minutes, zero, a negative number, malformed JSON, and an empty summary. Tests should not depend on a learner's real files or a network connection. The reference functions in `_includes/solutions/study_log.py` are covered by `tests/test_python_study_log.py`; these tests do not validate every learner's final application.

## Evaluation and extensions

Score 0–2 for correct behavior and boundaries, separation of concerns, meaningful tests, and clear setup/data documentation. Revise any zero before adding features. Optional extensions: filter a summary by topic or export a separate CSV copy. Keep the original JSON unchanged if an export fails.

## Further learning

After review, extend the design only when a concrete need appears. The [data structures course]({{ '/learning/courses/data-structures/' | relative_url }}) helps compare representations; the [content progress report]({{ '/docs/CONTENT_PROGRESS/' | relative_url }}) records what still needs human technical review.
