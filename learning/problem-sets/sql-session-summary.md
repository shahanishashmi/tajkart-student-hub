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

**PS-009.** Given a `sessions(student_id, minutes)` table, return each identified student who has at least one positive, non-null session, with the total positive minutes. Order by total from largest to smallest, then by student ID alphabetically to make ties reproducible. Ignore zero, negative, and `NULL` minute values. Students with no positive session are omitted. The input is expected to use a non-null `student_id` for each real student.

## Sample rows and expected result

Rows: `('L1',20)`, `('L1',15)`, `('L2',0)`, `('L2',45)`.

| student_id | total_minutes |
|---|---:|
| L2 | 45 |
| L1 | 35 |

## Hint and reference solution

Filter invalid/non-positive durations before grouping; group on the student key, then order by the aggregate and a stable tie-breaker. SQL `WHERE minutes > 0` also excludes `NULL`, because that comparison is unknown rather than true.

```sql
SELECT student_id, SUM(minutes) AS total_minutes
FROM sessions
WHERE minutes > 0
GROUP BY student_id
ORDER BY total_minutes DESC, student_id ASC;
```

The query is tested against SQLite with duplicate sessions, non-positive and `NULL` durations, tied totals, and an empty input. It relies on standard grouping and ordering; still check the target database's type and identifier rules before using it on real tables. The sample has no privacy-sensitive records.
