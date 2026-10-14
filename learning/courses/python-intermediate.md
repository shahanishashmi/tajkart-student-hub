---
layout: page
title: "Python beyond the basics: a four-part study plan"
description: An intermediate sequence for structured data, validation, JSON persistence, testing, and a local study-log project.
permalink: /learning/courses/python-intermediate/
id: course-python-intermediate-study-log
content_type: course
category: programming-languages
language: en
difficulty: intermediate
tags: [python, intermediate, json, testing, study-plan]
prerequisites: [language-path-python]
related_resources: [python-intermediate-collections-001, python-intermediate-validation-001, python-intermediate-json-001, python-intermediate-testing-001]
learning_objectives:
  - Transform structured records into useful summaries.
  - Validate input and handle expected file errors.
  - Persist local JSON and test behavior with temporary files.
  - Build a small importable command-line study log.
estimated_minutes: 240
content_status: drafted
review_status: pending
searchable: true
---

This four-part plan extends Tajkart's introductory Python path. It is a self-study sequence, not a credential. Plan for about four hours of reading and practice; implementation and review time vary by learner.

## Prerequisites and materials

You should be able to use Python variables, loops, functions, lists, and dictionaries. Review the [Python learning path]({{ '/learning/languages/python/' | relative_url }}) and [programming foundations course]({{ '/learning/courses/' | relative_url }}) if those ideas are still new. You need a local Python interpreter, editor, and temporary sample data. No third-party package is required.

## Sequence and assignments

| Part | Study | Assignment and check |
|---|---|---|
| 1. Transform records | [Comprehensions and aggregation]({{ '/learning/lessons/python-intermediate-collections/' | relative_url }}) | Filter sample sessions and total minutes by topic; test an empty list and a repeated topic. |
| 2. Define contracts | [Input validation and exceptions]({{ '/learning/lessons/python-intermediate-validation/' | relative_url }}) | Normalize topic names and reject blank names, non-integer durations, and invalid boundaries. |
| 3. Persist data | [Read and write JSON]({{ '/learning/lessons/python-intermediate-json/' | relative_url }}) | Save and reload sample records; distinguish a missing file from malformed JSON. |
| 4. Test and organize | [Modules and unit tests]({{ '/learning/lessons/python-intermediate-testing/' | relative_url }}) | Add tests with temporary files and make importing a module side-effect free. |

## Project and rubric

Complete the [local Python study-log project]({{ '/learning/projects/python-study-log/' | relative_url }}). Score 0–2 for each area: behavior and validation; clear function boundaries; tests for ordinary, empty, and invalid cases; explanation of file and privacy limits. A zero identifies the next revision; this is a formative self-check, not a grade or certification.

## Completion criteria and next steps

You can explain how a session moves from input to validated record, saved JSON, and a tested summary. Demonstrate the project from a clean temporary folder and show its test output. Keep the files local and use fictional data. Before expanding to web APIs or databases, review the [data structures course]({{ '/learning/courses/data-structures/' | relative_url }}) and relevant [security guide]({{ '/learning/guides/cybersecurity-basics/' | relative_url }}).
