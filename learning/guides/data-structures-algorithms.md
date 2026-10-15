---
title: "Data structures and algorithms: choose, explain, measure"
description: "Learn how representations and procedures affect the work a program performs."
summary: Learn how representations and procedures affect the work a program performs.
permalink: /learning/guides/data-structures-algorithms/
id: guide-data-structures-algorithms
content_type: guide
category: algorithms-and-data-structures
language: en
difficulty: beginner
tags: [algorithms, arrays, dictionaries, searching, complexity]
prerequisites: [guide-programming-foundations]
learning_objectives:
  - Describe a data structure by the operations it supports.
  - Compare linear search with binary search and state binary search's precondition.
  - Estimate how work changes as the input grows.
estimated_minutes: 45
content_status: drafted
review_status: pending
searchable: true
order: 2
---

## What this guide covers

A data structure represents information; an algorithm transforms or searches it. The useful question is not “Which structure is best?” but “Which operations must be fast, and what rules must the data obey?”

## Who should study it

Study this after you can use variables, conditions, loops, functions, and lists. You do not need advanced mathematics. The examples use small collections so you can trace each operation by hand.

## Concept path

1. Arrays/lists: ordered values, indexed access, and linear scans.
2. Sets and maps/dictionaries: membership and key-to-value lookup.
3. Stacks and queues: last-in-first-out and first-in-first-out workflows.
4. Searching and sorting: preconditions, output guarantees, and measured cost.
5. Trees and graphs: hierarchical and network-shaped relationships.
6. Complexity: count how the number of steps grows, then verify with measurements.

## Worked example: search an unsorted list

```python
def contains(items, target):
    for item in items:
        if item == target:
            return True
    return False

print(contains([8, 3, 6], 6))
```

Expected output: `True`. In the worst case the loop checks every item, so doubling a list can approximately double the comparisons. This is linear work, commonly written `O(n)`.

Binary search can use fewer comparisons, but only when the input is sorted and random indexed access is available. Skipping the sorted-input condition is a correctness bug, even if a demonstration happens to return the expected answer.

## Common mistakes

- Choosing a structure by name before listing the operations the program needs.
- Calling a method constant-time without considering the language or implementation.
- Measuring tiny inputs once and treating the result as a proof of complexity.
- Applying binary search to unsorted data.

## Practice and revision

Trace `contains([4, 7, 9, 2], 2)` and count comparisons. Then write a version that counts all matches and decide how it should behave for an empty list. Explain the invariant you keep while scanning.

## Next steps

Continue to the [practice set]({{ '/learning/problem-sets/' | relative_url }}) and the [algorithm efficiency lesson]({{ '/learning/lessons/algorithm-efficiency/' | relative_url }}). Add one measured test at a time; timing results depend on hardware and runtime, so use them as evidence rather than a universal promise.
