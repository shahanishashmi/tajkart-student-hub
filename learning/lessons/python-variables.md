---
layout: lesson
title: Variables and values in Python
summary: Name data clearly, inspect its type, and update a value.
permalink: /learning/lessons/python-variables/
id: python-variables-001
content_type: lesson
category: programming-languages
language: en
difficulty: beginner
tags: [python, variables, data-types, assignment]
skills: [python-values, python-assignment-tracing]
prerequisites: []
related_resources: [python-loops-001, python-functions-001, guide-programming-foundations]
learning_objectives:
  - Assign values to descriptive names.
  - Distinguish common types and update a value safely.
estimated_minutes: 20
content_status: drafted
review_status: pending
searchable: true
order: 1
topic: Python
level: Beginner
reading_time: 8
---

## Learning objectives

By the end, you can assign a value to a name, distinguish common value types, and update a variable without confusing assignment with comparison.

## Prerequisites

You need Python 3 and a way to run a short script. No prior programming experience is needed.

## Give a value a name

A variable is a name that refers to a value while a program runs. Assignment uses `=`: Python evaluates the right side, then binds its result to the name on the left.

```python
student = "Amina"
completed_lessons = 3
minutes_per_lesson = 20
study_minutes = completed_lessons * minutes_per_lesson
print(student, "studied", study_minutes, "minutes")
```

Expected output:

```text
Amina studied 60 minutes
```

Names should describe the information they hold. Use lowercase words separated by underscores, such as `study_minutes`. A later assignment can bind the name to a new value:

```python
completed_lessons = completed_lessons + 1
print(completed_lessons)
```

Output: `4`. The old value is read first, one is added, and the result is assigned back.

## Check the kind of a value

Text is a `str`, whole numbers are `int`, and decimal numbers are `float`. `type(value)` helps inspect them:

```python
course = "Python basics"
lesson_count = 4
print(type(course).__name__)
print(type(lesson_count).__name__)
```

Expected output is `str` followed by `int`. Text such as `"4"` and the number `4` look similar when printed, but they behave differently in calculations.

## Common mistakes

- `=` assigns a value; `==` asks whether two values are equal.
- `lesson-count` is read as subtraction. Use `lesson_count` for a name.
- Adding the string `"4"` to the integer `2` raises a `TypeError`. Convert deliberately with `int("4")` when the text represents a whole number.
- A name must be assigned before it is read, or Python raises `NameError`.

## Practice

1. Store a book title, its page count, and how many pages you read. Print the remaining pages.
2. Store a price and quantity. Print the total cost.
3. Start a variable at `0`, increase it twice, and print the final value.

Hints: subtract pages read from total pages; multiply price by quantity; use `count = count + 1` for each increase.

## Further learning within Tajkart

Continue with the [computer science subject map]({{ '/learning/subjects/' | relative_url }}) and the [four-week programming foundations plan]({{ '/learning/courses/' | relative_url }}).
