---
title: "Programming foundations: from a task to a tested program"
description: "Turn a small goal into inputs, steps, code, and checks."
summary: Turn a small goal into inputs, steps, code, and checks.
permalink: /learning/guides/programming-foundations/
id: guide-programming-foundations
content_type: guide
category: programming-fundamentals
language: en
difficulty: beginner
tags: [problem-solving, variables, control-flow, debugging]
skills: [python-condition-tracing]
prerequisites: []
learning_objectives:
  - Break a task into input, transformation, and output.
  - Use names, conditions, loops, and functions to express a solution.
  - Check a program with a normal case and an edge case.
estimated_minutes: 35
content_status: drafted
review_status: pending
searchable: true
order: 1
---

## What this guide covers

Programming is a way to describe precise steps a computer can repeat. Start with a task that has a visible result, such as calculating the minutes left in a study session. This guide gives you a path through the ideas; it is not a claim that one page replaces practice.

## Who should study it

Start here if you are new to programming or if code feels like a collection of symbols rather than a sequence of decisions. No prior language is required. Examples use Python because the current Tajkart beginner lessons use it.

## Prerequisites and objectives

You need a text editor and a way to run a short program. After studying, you should be able to describe a task with input, a rule, and output; read simple variables and branches; and test at least two cases.

## Concept path

1. Values and names: store data, distinguish text from numbers, and choose descriptive names.
2. Decisions: choose a branch with a condition that evaluates to true or false.
3. Repetition: process a sequence with a loop and track a running total.
4. Functions: give a reusable operation a name, inputs, and a returned result.
5. Collections: group related values in a list or dictionary.
6. Debugging: reproduce a wrong result, inspect the smallest failing example, and change one cause at a time.

## Worked example

For a 50-minute study block with a 5-minute break, the remaining focus time is `50 - 5 = 45`. In code, name each quantity so a reader can check the rule:

```python
block_minutes = 50
break_minutes = 5
focus_minutes = block_minutes - break_minutes
print(focus_minutes)
```

Expected output: `45`. Try a zero-minute break and a break equal to the full block. Those are useful boundaries because the result should be `50` and `0`.

## Common mistakes

- Coding before agreeing on what counts as a valid input.
- Using a name such as `x` when `break_minutes` would explain the calculation.
- Testing only one example, which can hide a boundary error.
- Changing several lines at once and losing track of which change fixed the result.

## Practice

Write a small program that takes a total number of pages and pages read, then prints pages remaining. Check a typical case, reading zero pages, and reading all pages. For each case, write the expected output before running the code.

## Revision and next steps

Close the editor and explain the program's input, rule, and output from memory. Then study [variables]({{ '/learning/lessons/python-variables/' | relative_url }}), [loops]({{ '/learning/lessons/problem-solving-loops/' | relative_url }}), and [algorithm efficiency]({{ '/learning/lessons/algorithm-efficiency/' | relative_url }}). Use the [foundations plan]({{ '/learning/courses/' | relative_url }}) to schedule practice.
