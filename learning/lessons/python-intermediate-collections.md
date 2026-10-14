---
layout: lesson
title: Aggregate records with Python comprehensions and dictionaries
summary: Filter records and build stable summaries from structured data.
permalink: /learning/lessons/python-intermediate-collections/
id: python-intermediate-collections-001
content_type: lesson
category: programming-languages
language: en
difficulty: intermediate
tags: [python, dictionaries, comprehensions, aggregation]
prerequisites: [python-collections-001, python-loops-001]
related_resources: [language-path-python, course-python-intermediate-study-log]
learning_objectives:
  - Filter a sequence of records with a clear condition.
  - Aggregate repeated keys without losing earlier totals.
  - Choose a useful result for empty input.
estimated_minutes: 35
content_status: drafted
review_status: pending
searchable: true
order: 7
topic: Python
level: Intermediate
reading_time: 12
---

## Learning objectives

After this lesson, you can transform a list of records into a smaller list or a keyed summary, and explain what your code returns when there is no data.

## Prerequisites

You should be comfortable with Python lists, dictionaries, loops, and functions. Review [lists and dictionaries]({{ '/learning/lessons/python-lists-dictionaries/' | relative_url }}) and [loops]({{ '/learning/lessons/problem-solving-loops/' | relative_url }}). This begins the [intermediate Python study-log path]({{ '/learning/courses/python-intermediate/' | relative_url }}).

## Filter records with a comprehension

A comprehension creates a new list from an iterable. Keep its condition readable; a longer multi-step transformation is often clearer as a loop or a named function.

```python
sessions = [
    {"topic": "Python", "minutes": 25},
    {"topic": "SQL", "minutes": 0},
    {"topic": "Python", "minutes": 15},
]
positive_sessions = [session for session in sessions if session["minutes"] > 0]
print([session["topic"] for session in positive_sessions])
```

Expected output: `['Python', 'Python']`. The zero-minute entry is not included. If `sessions` is empty, the result is an empty list; it does not need a special case.

## Aggregate repeated keys

A dictionary can hold one running total per topic. `.get(key, 0)` defines the initial total for a topic that has not appeared yet.

```python
sessions = [
    {"topic": "Python", "minutes": 25},
    {"topic": "SQL", "minutes": 0},
    {"topic": "Python", "minutes": 15},
]
totals = {}
for session in sessions:
    topic = session["topic"]
    totals[topic] = totals.get(topic, 0) + session["minutes"]
print(totals)
```

Expected output: `{'Python': 40, 'SQL': 0}`. An empty input produces `{}`. If input records can be malformed, validate them before aggregating; this loop assumes every record has a text `topic` and a numeric `minutes` value.

## Common mistakes

- Replacing a previous total with the latest value instead of adding to it.
- Forgetting to decide whether zero or negative durations are valid.
- Treating input data as trusted just because it came from a local file.
- Writing a nested comprehension that hides more than one operation.

## Practice

1. Filter completed tasks from a list of dictionaries. **Hint:** choose one boolean field and make the condition explicit.
2. Count minutes per topic from three sample sessions. **Hint:** use `totals.get(topic, 0)` for a topic's first record.
3. Write a function that returns the longest topic name, or `None` when there are no sessions. **Hint:** check the empty case before calling `max`.

Try each task with an empty list, one record, and repeated topics. Keep the input unchanged unless mutation is part of the function's stated contract.

## Next steps

Continue to [validate function inputs]({{ '/learning/lessons/python-intermediate-validation/' | relative_url }}), then use these transformations in the [intermediate Python course]({{ '/learning/courses/python-intermediate/' | relative_url }}).
