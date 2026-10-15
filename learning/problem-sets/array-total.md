---
layout: lesson
title: "Problem PS-001: total a list of numbers"
description: "Add values in a list and define the result for an empty input."
summary: Add values in a list and define the result for an empty input.
permalink: /learning/problem-sets/array-total/
id: problem-array-total-001
content_type: problem-set
category: arrays-and-loops
language: en
difficulty: beginner
tags: [arrays, lists, loops, accumulator]
prerequisites: [python-loops-001]
learning_objectives: ["Traverse a list and return its total, including for an empty list."]
content_status: drafted
review_status: pending
searchable: true
---

## Problem

**PS-001.** Write `array_total(numbers)` that returns the sum of a list of integers. The function must not print. An empty list returns `0`.

## Input, constraints, and output

Input is a list of zero or more integers. For this exercise, the values fit in the language's ordinary integer type. Output one integer equal to their total.

| Input | Expected output |
|---|---:|
| `[4, 2, 8]` | `14` |
| `[]` | `0` |
| `[-3, 3]` | `0` |

## Hint

Start with a neutral total of zero and add each item once.

## Reference solution

```python
{% include solutions/array_total.py %}
```

Time is `O(n)` for `n` values; additional space is `O(1)`. Tests cover an empty list and a mixed list. The canonical snippet is imported by `tests/test_solutions.py`.
