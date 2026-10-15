---
layout: lesson
title: Define a reusable Python function
description: "Give a useful operation named inputs, a return value, and a testable contract."
summary: Give a useful operation named inputs, a return value, and a testable contract.
permalink: /learning/lessons/python-functions/
id: python-functions-001
content_type: lesson
category: programming-languages
language: en
difficulty: beginner
tags: [python, functions, parameters, return-values]
prerequisites: [python-variables-001, python-loops-001]
related_resources: [python-collections-001, problem-array-total-001, language-path-python]
learning_objectives:
  - Define and call a function with a parameter.
  - Distinguish displaying a value from returning it.
  - Test a function with ordinary and boundary inputs.
estimated_minutes: 25
content_status: drafted
review_status: pending
searchable: true
order: 5
topic: Python
level: Beginner
reading_time: 8
---

## Learning objectives

After this lesson, you can define a named operation, pass an input, receive a result, and test the rule independently of display code.

## Prerequisites

You should be able to assign variables and read a loop. Review [Python variables]({{ '/learning/lessons/python-variables/' | relative_url }}) and [loops]({{ '/learning/lessons/problem-solving-loops/' | relative_url }}) if needed.

## Define the operation

A function packages an operation behind a name. Its parameters describe the information it needs; `return` gives a result to the caller.

```python
def remaining_pages(total, read):
    if total < 0 or read < 0 or read > total:
        raise ValueError("page counts must be between zero and total")
    return total - read

print(remaining_pages(240, 35))
```

Expected output: `205`. The function does not print internally, so another caller can use the returned number in a report or a test.

## Common mistakes

- Printing inside a function when the caller needs a value to reuse.
- Naming parameters too vaguely to explain their roles.
- Ignoring invalid inputs instead of defining the function's contract.
- Repeating large blocks instead of extracting one operation that has a clear purpose.

## Practice

Write `study_total(minutes)` that returns the sum of a list. Decide whether negative durations should be rejected. Test an empty list, one value, and a negative value if your contract rejects it.

## Check your understanding

If `print(remaining_pages(10, 3))` displays `7`, what does the function return? Why is that different from a function that only calls `print`?

## Next steps

Use functions to make a small script easier to test. Continue to [data structures and algorithms]({{ '/learning/guides/data-structures-algorithms/' | relative_url }}) and the [Python path]({{ '/learning/languages/python/' | relative_url }}).
