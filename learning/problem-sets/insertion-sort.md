---
layout: lesson
title: "Problem PS-005: sort a list with insertion sort"
description: "Build a sorted prefix by inserting each next value in its correct position."
summary: Build a sorted prefix by inserting each next value in its correct position.
permalink: /learning/problem-sets/insertion-sort/
id: problem-insertion-sort-005
content_type: problem-set
category: sorting
language: en
difficulty: beginner
tags: [sorting, arrays, loops, invariants]
prerequisites: [python-loops-001, guide-data-structures-algorithms]
learning_objectives: ["Maintain a sorted prefix and preserve repeated values."]
content_status: drafted
review_status: pending
searchable: true
---

## Problem

**PS-005.** Return a new list sorted in ascending order using insertion sort. Do not mutate the input. Repeated values must remain present.

## Examples and constraints

| Input | Expected output |
|---|---|
| `[4, 1, 3, 1]` | `[1, 1, 3, 4]` |
| `[]` | `[]` |
| `[5]` | `[5]` |

Input is a list of comparable integers.

## Hint and reference solution

The prefix before the current position is sorted. Move larger prefix values one place right, then write the current value in the gap.

```python
{% include solutions/insertion_sort.py %}
```

Worst-case time is `O(n²)`; extra space is `O(n)` here because the function returns a copy. Tests verify duplicates and that the original input stays unchanged.
