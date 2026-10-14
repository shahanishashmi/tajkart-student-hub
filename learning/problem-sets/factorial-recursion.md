---
layout: lesson
title: "Problem PS-006: compute a factorial recursively"
summary: Use a base case and a smaller subproblem to calculate a factorial.
permalink: /learning/problem-sets/factorial-recursion/
id: problem-factorial-recursion-006
content_type: problem-set
category: recursion
language: en
difficulty: beginner
tags: [recursion, functions, base-case]
prerequisites: [python-functions-001]
learning_objectives: ["Define a terminating recursive rule and reject values outside its contract."]
content_status: drafted
review_status: pending
searchable: true
---

## Problem

**PS-006.** For an integer `n` from 0 through 12, return `n!`, the product of the positive integers from 1 through `n`. Define `0!` as 1. Negative input must raise `ValueError`.

## Examples

| Input | Expected output |
|---:|---:|
| `0` | `1` |
| `5` | `120` |
| `-1` | `ValueError` |

## Hint and reference solution

The base case is `0` or `1`. Otherwise multiply `n` by the result for `n - 1`.

```python
{% include solutions/factorial.py %}
```

Time and call-stack space are `O(n)`. The stated input limit keeps the teaching example small; production code should consider iterative alternatives and language recursion limits. Tests cover base, ordinary, and invalid inputs.
