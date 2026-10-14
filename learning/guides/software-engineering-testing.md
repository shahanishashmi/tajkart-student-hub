---
title: "Software engineering and testing: make change safer"
summary: Plan small changes, define observable behavior, and use tests as feedback.
permalink: /learning/guides/software-engineering-testing/
id: guide-software-engineering-testing
content_type: guide
category: software-engineering
language: en
difficulty: beginner
tags: [software-engineering, testing, git, maintenance]
prerequisites: [guide-programming-foundations]
learning_objectives:
  - Convert a requirement into observable behavior and examples.
  - Choose tests that cover typical and boundary cases.
  - Make a small change that can be reviewed and reverted.
estimated_minutes: 40
content_status: drafted
review_status: pending
searchable: true
order: 8
---

## What this guide covers

Software engineering includes the decisions that let software stay understandable as it changes: requirements, design, testing, version control, review, and maintenance. Testing provides evidence about selected behavior; it does not prove that every possible situation is correct.

## Concept path

1. Write a user-visible requirement as an example input and expected outcome.
2. Separate a behavior from its implementation so it can be tested.
3. Test a typical case, an edge case, and an invalid case where the contract defines one.
4. Keep a change small enough to understand in one review.
5. Use Git history to show what changed and why; keep secrets and generated files out of commits.
6. Re-run checks after the change and record limitations.

## Worked example

Requirement: “A page counter never reports a negative number.” Cases: total 10/read 3 -> 7; total 10/read 10 -> 0; total 10/read 11 -> reject the invalid input or explain the chosen rule. The third case forces the product to define behavior before implementation.

## Common mistakes

- Writing tests that repeat the implementation's assumption instead of checking the requirement.
- Testing only a happy path.
- Treating a green suite as proof of security, usability, or complete correctness.
- Making a large unrelated change that is difficult to review.

## Practice and next steps

Choose one function you have written. State its input, output, and invalid cases; add three tests; then change its implementation without changing the expected behavior. Read the [Git small-commits lesson]({{ '/learning/lessons/git-small-commits/' | relative_url }}) before sharing the change.
