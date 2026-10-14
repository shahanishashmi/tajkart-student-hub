---
layout: lesson
title: "Problem PS-007: find a binary tree's height"
summary: Recursively count the longest path from a node to an empty child.
permalink: /learning/problem-sets/tree-height/
id: problem-tree-height-007
content_type: problem-set
category: trees
language: en
difficulty: intermediate
tags: [trees, recursion, data-structures]
prerequisites: [problem-factorial-recursion-006]
learning_objectives: ["Use a tree definition recursively and define the empty-tree result."]
content_status: drafted
review_status: pending
searchable: true
---

## Problem

**PS-007.** A node is represented as `(value, left, right)`; an empty child is `None`. Return the number of nodes on the longest path from the root to an empty child. The height of an empty tree is 0.

## Example

`("a", ("b", None, None), ("c", None, ("d", None, None)))` has height `3`.

## Hint and reference solution

The root adds one level to the greater height of its two children.

```python
{% include solutions/tree_height.py %}
```

Time is `O(n)` for `n` nodes; recursion space is `O(h)` for tree height `h`. A very deep unbalanced tree may exceed a runtime's recursion limit. Tests cover an empty tree and a tree with unequal branch depths.
