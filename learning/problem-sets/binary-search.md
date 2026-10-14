---
layout: lesson
title: "Problem PS-004: binary search a sorted list"
summary: Find a target index while maintaining a shrinking search interval.
permalink: /learning/problem-sets/binary-search/
id: problem-binary-search-004
content_type: problem-set
category: searching
language: en
difficulty: beginner
tags: [binary-search, sorted-arrays, algorithms]
prerequisites: [guide-data-structures-algorithms]
learning_objectives: ["Implement binary search and keep the sorted-input precondition visible."]
content_status: drafted
review_status: pending
searchable: true
---

## Problem

**PS-004.** Given a non-decreasing list of distinct integers and a target, return its index or `-1` when absent. The list is sorted ascending; this precondition is required.

## Examples and constraints

| Numbers | Target | Expected index |
|---|---:|---:|
| `[1, 4, 7, 9]` | `7` | `2` |
| `[1, 4, 7, 9]` | `5` | `-1` |
| `[]` | `5` | `-1` |

Values are integers. Do not apply this solution to unsorted input.

## Hint and reference solution

Use inclusive `low` and `high` indexes. Each comparison discards the half that cannot contain the target.

```python
{% include solutions/binary_search.py %}
```

Time is `O(log n)` comparisons for `n` elements; extra space is `O(1)`. Tests cover a found value, a missing value, and an empty list.
