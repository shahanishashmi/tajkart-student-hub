---
title: "Database concepts and SQL: store facts, ask precise questions"
summary: Model related records and query them with readable, bounded SQL.
permalink: /learning/guides/databases-and-sql/
id: guide-databases-sql
content_type: guide
category: databases
language: en
difficulty: beginner
tags: [database, sql, tables, joins, data-integrity]
prerequisites: [guide-programming-foundations]
learning_objectives:
  - Explain rows, columns, primary keys, and foreign keys.
  - Filter and aggregate rows with basic SQL.
  - Relate tables with a join and preserve data integrity.
estimated_minutes: 40
content_status: drafted
review_status: pending
searchable: true
order: 4
---

## What this guide covers

A relational database stores records in tables and relates them through keys. SQL describes operations on those records. A schema is a set of rules for which values can be stored and how records connect.

## Prerequisites and concept path

You should understand values, conditions, and lists. Learn in this order: tables and row identity; `SELECT` and `WHERE`; sorting and limiting; aggregation; joins; constraints and transactions. Learn how the database you use handles types and transactions before depending on vendor-specific behavior.

## Worked example

Suppose a `sessions` table has `student_id` and `minutes` columns. This query reports the total practice minutes per student:

```sql
SELECT student_id, SUM(minutes) AS total_minutes
FROM sessions
WHERE minutes > 0
GROUP BY student_id
ORDER BY total_minutes DESC;
```

The filter runs before grouping; `SUM` combines remaining rows; the order makes the largest total appear first. The result contains one row per student represented in qualifying records.

## Common mistakes

- Using a display name as a key when it may change or repeat.
- Joining tables without checking whether the join key is unique, which can multiply rows.
- Assuming row order without an explicit `ORDER BY`.
- Building SQL strings from untrusted input. Use parameterized queries in application code.

## Practice

Create a tiny table of three study sessions with student IDs and minute values. Write queries for sessions over 20 minutes, total minutes per student, and the student with the largest total. Include a zero-minute row and explain why your filter includes or excludes it.

## Revision and next steps

Draw the tables and keys before writing a join. Then revise the query by changing one condition and predicting how many rows remain. Continue with the [SQL quick reference]({{ '/learning/cheatsheets/sql/' | relative_url }}) and the [database project brief]({{ '/learning/projects/' | relative_url }}).
