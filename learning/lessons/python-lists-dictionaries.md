---
layout: lesson
title: Choose a Python list or dictionary
summary: Represent ordered items and keyed facts with the structure that matches the task.
permalink: /learning/lessons/python-lists-dictionaries/
id: python-collections-001
content_type: lesson
category: programming-languages
language: en
difficulty: beginner
tags: [python, lists, dictionaries, data-structures]
prerequisites: [python-variables-001, python-loops-001]
related_resources: [guide-data-structures-algorithms, problem-first-duplicate-002, course-data-structures-six-weeks]
learning_objectives:
  - Use a list for ordered values and a dictionary for named associations.
  - Check whether a key exists before relying on a lookup.
  - Choose a structure based on the operation the program needs.
estimated_minutes: 30
content_status: drafted
review_status: pending
searchable: true
order: 6
topic: Python
level: Beginner
reading_time: 9
---

## Learning objectives

After this lesson, you can store a sequence in a list, associate keys with values in a dictionary, and explain why you chose one representation.

## Prerequisites

Know variables, functions, and loops. Begin with [variables]({{ '/learning/lessons/python-variables/' | relative_url }}) and [loops]({{ '/learning/lessons/problem-solving-loops/' | relative_url }}).

## Work with an ordered list

A list preserves a sequence of values. Indexes start at zero, and a loop can process each value without manually naming each position.

```python
minutes = [15, 20, 10]
total = sum(minutes)
print(total)
```

Expected output: `45`.

## Associate a key with a value

A dictionary is useful when a key such as a learner ID should locate a fact. The lookup can be absent, so define what to do in that case.

```python
minutes_by_day = {"Mon": 25, "Tue": 30}
print(minutes_by_day.get("Wed", 0))
```

Expected output: `0`. `.get` provides a default for a missing key; use a different response if missing data should be an error.

## Common mistakes

- Reading an index that is outside the list's range.
- Assuming dictionary keys exist without checking.
- Using a list when the code repeatedly searches it by a stable key.
- Storing the same fact in two places and allowing them to disagree.

## Practice and next steps

Store three tasks in a list and print them in order. Then store each task's estimated minutes in a dictionary and calculate a total. Test an empty list and a missing key. Continue with the [data structures guide]({{ '/learning/guides/data-structures-algorithms/' | relative_url }}).
