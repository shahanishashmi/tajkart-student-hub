---
layout: lesson
title: "Problem PS-008: check graph reachability with BFS"
description: "Use a queue and a visited set to determine whether one node can reach another."
summary: Use a queue and a visited set to determine whether one node can reach another.
permalink: /learning/problem-sets/graph-reachability/
id: problem-graph-reachability-008
content_type: problem-set
category: graphs
language: en
difficulty: intermediate
tags: [graphs, breadth-first-search, queues, sets]
prerequisites: [problem-first-duplicate-002]
learning_objectives: ["Traverse a graph without revisiting nodes and handle unknown endpoints."]
content_status: drafted
review_status: pending
searchable: true
---

## Problem

**PS-008.** The graph is a dictionary from each node to its neighbor list. Return `True` if a directed path leads from `start` to `target`; return `False` if either endpoint is absent or there is no path.

## Example and constraints

For `{"A": ["B", "C"], "B": ["D"], "C": [], "D": []}`, `A` reaches `D`; `C` does not. Neighbor values should have entries in the graph, including nodes with no outgoing edges.

## Hint and reference solution

Use breadth-first search: enqueue the start, mark it visited, then add each unvisited neighbor once.

```python
{% include solutions/graph_reachable.py %}
```

Time and extra space are `O(V + E)` for vertices `V` and edges `E`. Tests cover a path, a disconnected node, and an absent endpoint. The visited set prevents an infinite loop in a cyclic graph.
