---
layout: page
title: "Project: command-line reading tracker"
description: "Build a small local tool that validates a page count and reports reading progress."
summary: Build a small local tool that validates a page count and reports reading progress.
permalink: /learning/projects/reading-tracker/
id: project-reading-tracker
content_type: project
category: programming-fundamentals
language: en
difficulty: beginner
tags: [python, command-line, validation, project]
prerequisites: [python-functions-001, python-collections-001]
learning_objectives: ["Separate input, validation, calculation, and display in a small program."]
estimated_minutes: 120
content_status: drafted
review_status: pending
searchable: true
---

## Goal and prerequisites

Track a book title, total pages, and pages read. Use sample titles only. You should know variables, conditions, functions, and lists; see the [Python path]({{ '/learning/languages/python/' | relative_url }}).

## Requirements and example

Accept a title and two whole-number page counts. Reject negative values and a pages-read value greater than total pages. For total `240` and read `35`, report `205` pages remaining and `14.6%` complete (rounding policy: one decimal place).

## Milestones

1. Write a pure function for validation and remaining pages.
2. Add a command-line prompt and a helpful error message.
3. Store multiple entries in a list or local JSON file; explain what happens if the file is missing or malformed.
4. Add tests for zero pages, completed reading, invalid counts, and repeated titles.

## Evaluation and extensions

Check that output matches the example, invalid input does not crash with an unexplained traceback, and tests run from a clean checkout. Score 0–2 for behavior, tests, readability, and explanation. Extensions: add a daily goal or export a summary. Do not collect real users' reading histories without a privacy design.
