---
layout: page
title: "Project: study-session database"
summary: Model sample study sessions and query totals while preserving relationships.
permalink: /learning/projects/study-session-database/
id: project-study-session-database
content_type: project
category: databases
language: en
difficulty: beginner
tags: [sql, database, schema, project]
prerequisites: [language-path-sql, guide-databases-sql]
learning_objectives: ["Create related tables and test basic filters, joins, and aggregates."]
estimated_minutes: 180
content_status: drafted
review_status: pending
searchable: true
---

## Goal and sample data

Model learners and study sessions using invented IDs only. A session stores an ID, learner ID, date, topic, and non-negative minutes. Example rows: learner `L1` has two sessions of 20 and 15 minutes; a total query should report 35.

## Milestones

1. Draw tables and identify primary and foreign keys.
2. Add a constraint for non-negative minutes.
3. Query sessions by learner and summarize totals.
4. Test an unknown learner, no sessions, repeated topics, and a zero-minute row.
5. Document how a real application would parameterize queries and control access.

## Tests, rubric, and extensions

Check that deleting or renaming a learner has an explicit relationship rule and that joins do not multiply rows unexpectedly. Score 0–2 for schema clarity, query correctness, edge cases, and safety explanation. Extensions: add a weekly summary or export CSV. Do not store actual student records in a public repository.
