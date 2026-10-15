---
title: "SQL quick reference"
description: "Remember common read queries, joins, grouping, and safe parameter use."
summary: Remember common read queries, joins, grouping, and safe parameter use.
permalink: /learning/cheatsheets/sql/
id: cheatsheet-sql
content_type: cheatsheet
category: databases
language: en
difficulty: beginner
tags: [sql, select, joins, aggregation]
prerequisites: [language-path-sql]
learning_objectives: ["Compose a bounded query and identify where duplicates can arise."]
content_status: drafted
review_status: pending
searchable: true
---

```sql
SELECT student_id, SUM(minutes) AS total
FROM sessions
WHERE minutes > 0
GROUP BY student_id
HAVING SUM(minutes) >= 30
ORDER BY total DESC;
```

- `WHERE` filters rows before grouping; `HAVING` filters groups.
- `INNER JOIN` keeps matching rows; `LEFT JOIN` keeps every row from the left input.
- Add `ORDER BY` when the output order matters. A database does not promise an implicit order.
- `NULL` is checked with `IS NULL`, not `= NULL`.
- Use primary/foreign keys and constraints to preserve relationships.
- In application code, pass values as parameters; never concatenate untrusted input into SQL text.

SQL dialects differ. Check the database engine's documentation before using date functions, generated IDs, or transaction-specific features.
