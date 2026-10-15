---
title: "Debugging and testing quick reference"
description: "A compact checklist for reproducing defects and testing behavior."
summary: A compact checklist for reproducing defects and testing behavior.
permalink: /learning/cheatsheets/debugging-testing/
id: cheatsheet-debugging-testing
content_type: cheatsheet
category: software-engineering
language: en
difficulty: beginner
tags: [debugging, testing, edge-cases, reproducibility]
prerequisites: [guide-software-engineering-testing]
learning_objectives: ["Turn a report into a reproducible case and choose an informative test."]
content_status: drafted
review_status: pending
searchable: true
---

1. Reproduce the problem with the smallest input you can keep.
2. Write the expected and actual behavior separately.
3. Inspect the first point where they differ; do not change several things at once.
4. Add a regression test before or immediately after the fix.
5. Test a typical case, an edge case, and an invalid case defined by the program's contract.
6. Re-run the relevant checks and record what the checks do not cover.

Tests may be unit, integration, or end-to-end checks. Use the narrowest test that can expose the defect, then a broader check for interactions. A passing test suite is evidence for tested cases, not proof of complete correctness.
