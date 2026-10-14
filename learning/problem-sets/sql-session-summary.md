---
layout: lesson
title: "Problem PS-009: summarize study sessions with SQL"
summary: Filter rows and aggregate session minutes by learner.
permalink: /learning/problem-sets/sql-session-summary/
id: problem-sql-session-summary-009
content_type: problem-set
category: databases
language: en
difficulty: beginner
tags: [sql, aggregation, group-by, databases]
prerequisites: [language-path-sql]
learning_objectives: ["Filter rows, aggregate grouped values, and state an ordering explicitly."]
content_status: drafted
review_status: pending
searchable: true
---

## Problem

**PS-009.** Given a `sessions(student_id, minutes)` table, return each student with the total of positive session minutes, ordered from largest total to smallest. Ignore zero-minute rows.

## Sample rows and expected result

Rows: `('L1',20)`, `('L1',15)`, `('L2',0)`, `('L2',45)`.

| student_id | total_minutes |
|---|---:|
| L2 | 45 |
| L1 | 35 |

## Hint and reference solution

Filter rows before grouping; group on the student key, then order by the aggregate.

```sql
SELECT student_id, SUM(minutes) AS total_minutes
FROM sessions
WHERE minutes > 0
GROUP BY student_id
ORDER BY total_minutes DESC;
```

The expected output is checked against SQLite in `tests/test_sql_examples.py`. SQL syntax and type behavior can vary by database, so verify the target dialect before relying on extensions.
