---
layout: lesson
title: Compare algorithms by their growth
description: "Estimate how work changes as input grows, using simple examples."
summary: Estimate how work changes as input grows, using simple examples.
permalink: /learning/lessons/algorithm-efficiency/
id: algorithms-efficiency-001
content_type: lesson
category: algorithms-and-data-structures
language: en
difficulty: beginner
tags: [algorithms, complexity, measurement, loops]
prerequisites: [python-loops-001]
related_resources: [guide-data-structures-algorithms, problem-binary-search-004, course-data-structures-six-weeks]
learning_objectives:
  - Count repeated operations in a simple algorithm.
  - Compare linear and quadratic growth qualitatively.
estimated_minutes: 25
content_status: drafted
review_status: pending
searchable: true
order: 3
topic: Algorithms
level: Beginner
reading_time: 10
---

## Learning objectives

Describe input size, compare linear and quadratic growth, and use a rough estimate to choose a simple algorithm.

## Prerequisites

Be comfortable reading a loop and multiplying small numbers. You do not need advanced mathematics.

## Count work as input grows

An algorithm's running time depends partly on how much input it receives. If a loop visits each of `n` items once, the number of visits grows in proportion to `n`. Computer scientists call this linear growth and write `O(n)` as a broad description of how work scales.

```python
values = [4, 7, 2, 9]
for value in values:
    print(value)
```

With 4 items, the body runs 4 times; with 100 items, it runs 100 times. If one operation takes a millisecond, the rough operation time increases from about 4 to about 100 milliseconds. Real timing also depends on hardware and implementation.

A loop nested inside another loop can compare every pair:

```python
values = [4, 7, 2, 9]
for left in values:
    for right in values:
        print(left, right)
```

For `n` values, the inner body runs `n × n` times: `O(n²)`. Four values produce 16 pairs; doubling the input to eight produces 64.

## Use the estimate wisely

Growth descriptions help compare approaches on large inputs. They leave out constant factors and machine details, so they are not precise stopwatch predictions. Measure real programs when actual performance matters.

## Common mistakes

- Treating `O(n)` as an exact number of seconds. It describes a growth pattern.
- Assuming every nested loop is always quadratic. The inner loop may run a fixed number of times or stop early.
- Optimising tiny code before measuring. Correctness and clarity come first for beginner programs.

## Practice

1. A loop visits 12 items once. How many visits happen?
2. A nested loop compares every pair among 12 items. How many comparisons happen?
3. If a single loop processes 50 records and the input doubles, about how many iterations will it make?

Answers: 12, 144, and 100 iterations. For each answer, state what the loop body does once.

## Further learning within Tajkart

The [subject map]({{ '/learning/subjects/' | relative_url }}) connects algorithm analysis to data structures and problem solving.
