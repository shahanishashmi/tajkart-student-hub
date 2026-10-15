---
title: "Data structures and algorithms: a six-week course"
description: "A self-study course in choosing representations, searching, sorting, and explaining complexity."
summary: A self-study course in choosing representations, searching, sorting, and explaining complexity.
permalink: /learning/courses/data-structures/
id: course-data-structures-six-weeks
content_type: course
category: algorithms-and-data-structures
language: en
difficulty: beginner
tags: [algorithms, data-structures, complexity, problem-solving]
prerequisites: [guide-programming-foundations]
related_resources: [python-collections-001, algorithms-efficiency-001, problem-array-total-001, problem-first-duplicate-002, problem-binary-search-004, problem-insertion-sort-005, problem-tree-height-007, problem-graph-reachability-008]
learning_objectives:
  - Implement and test searches and simple sorts.
  - Select a list, set, map, stack, or queue for a stated operation.
  - Explain correctness, boundary cases, and approximate growth in work.
estimated_minutes: 1200
content_status: drafted
review_status: pending
searchable: true
---

This is an estimate of about 20 hours over six weeks, not a deadline or credential. Use Python or another language you can already read. Keep a notebook with a problem statement, a hand trace, a test, and a short complexity explanation for each implementation.

## Prerequisites

You should be comfortable with variables, conditions, loops, functions, and lists. Review the [programming foundations guide]({{ '/learning/guides/programming-foundations/' | relative_url }}) if you need a refresher.

## Modules and assignments

| Week | Module | Assignment and check |
|---|---|---|
| 1 | Lists, indexing, and linear scans | Implement a count and a maximum; test an empty and single-item list. |
| 2 | Sets and maps | Count repeated words; explain when key lookup is useful. |
| 3 | Binary search and preconditions | Search a sorted list; prove the range shrinks and test absent values. |
| 4 | Sorting and comparison | Implement insertion sort; compare output with a trusted built-in sort on test inputs. |
| 5 | Stacks, queues, trees, and graph models | Choose a representation for a path or task queue; draw one example. |
| 6 | Complexity and final project | Build a duplicate detector or route finder; document trade-offs and limits. |

## Knowledge checks

Before each implementation, answer: What are valid inputs? What result should an empty input produce? What invariant remains true after one step? What is the worst-case number of comparisons? If you cannot answer, make a smaller example before coding.

## Project and rubric

Choose either a duplicate detector for a list of identifiers or a breadth-first path finder in a small graph. Submit source, at least five tests, and a one-page explanation. Score each item 0–2: correctness and edge cases; understandable names and structure; tests that can fail for a real defect; accurate complexity explanation. A total of 6/8 is a useful self-check, not an accredited grade. Revise any area scored 0.

## Completion and next steps

Complete the project, explain every data structure choice, and make one change after the tests pass. Then apply the ideas in the [problem set]({{ '/learning/problem-sets/' | relative_url }}) and [systems-design guide]({{ '/learning/guides/system-design/' | relative_url }}).
