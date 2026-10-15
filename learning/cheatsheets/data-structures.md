---
title: "Data structures and algorithms quick reference"
description: "Compare common structures by the operations they support."
summary: Compare common structures by the operations they support.
permalink: /learning/cheatsheets/data-structures/
id: cheatsheet-data-structures
content_type: cheatsheet
category: algorithms-and-data-structures
language: en
difficulty: beginner
tags: [arrays, sets, maps, stacks, queues, searching, sorting]
prerequisites: [guide-data-structures-algorithms]
learning_objectives: ["Choose a structure from required operations and state its assumptions."]
content_status: drafted
review_status: pending
searchable: true
---

| Structure | Useful when | Check before choosing |
|---|---|---|
| List/array | Order and indexed access matter | Inserting near the beginning may shift items. |
| Set | Membership and uniqueness matter | Order and iteration guarantees depend on implementation. |
| Map/dictionary | Keys should locate values | Keys need stable equality/hash behavior. |
| Stack | Most recent item is handled first | Define empty-pop behavior. |
| Queue | Oldest item is handled first | Choose an implementation with efficient front removal. |
| Tree | Data has hierarchy or ordered search | Keep balance/invariants if performance relies on them. |
| Graph | Objects have arbitrary relationships | Choose directed/undirected and weighted/unweighted semantics. |

Linear scan is `O(n)`. Binary search is `O(log n)` comparisons on sorted, indexable data. Always state the precondition and test empty, one-item, duplicate, and missing-target cases.
