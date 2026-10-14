---
layout: lesson
title: "Problem PS-002: find the first repeated value"
summary: Use a set to detect when a value has already appeared.
permalink: /learning/problem-sets/first-duplicate/
id: problem-first-duplicate-002
content_type: problem-set
category: hashing
language: en
difficulty: beginner
tags: [arrays, lists, hashing, sets]
prerequisites: [python-collections-001]
learning_objectives: ["Track previously seen values and define a no-match result."]
content_status: drafted
review_status: pending
searchable: true
---

## Problem

**PS-002.** Return the first value whose second occurrence is encountered while scanning left to right. Return `None` if no value repeats. Values are hashable integers or strings.

## Examples

| Input | Expected output |
|---|---|
| `[3, 1, 3, 1]` | `3` |
| `[2, 4, 6]` | `None` |
| `[]` | `None` |

## Hint and reference solution

Keep a set of values already seen. Check membership before adding the current value.

```python
{% include solutions/first_duplicate.py %}
```

Expected average time is `O(n)` and additional space is `O(n)` for `n` values, assuming expected constant-time set membership. Tests cover the earliest repeated value and no-repeat cases in `tests/test_solutions.py`.
