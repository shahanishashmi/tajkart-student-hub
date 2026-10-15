---
layout: lesson
title: Give Python functions clear input contracts
description: "Validate boundary values, use helpful exceptions, and keep transformations testable."
summary: Validate boundary values, use helpful exceptions, and keep transformations testable.
permalink: /learning/lessons/python-intermediate-validation/
id: python-intermediate-validation-001
content_type: lesson
category: programming-languages
language: en
difficulty: intermediate
tags: [python, functions, validation, exceptions]
prerequisites: [python-functions-001, python-intermediate-collections-001]
related_resources: [language-path-python, course-python-intermediate-study-log]
learning_objectives:
  - State accepted input types and boundary rules for a function.
  - Raise a useful exception when an input violates its contract.
  - Separate validation from display and file operations.
estimated_minutes: 35
content_status: drafted
review_status: pending
searchable: true
order: 8
topic: Python
level: Intermediate
reading_time: 12
---

## Learning objectives

After this lesson, you can describe what a function accepts, reject invalid values with a useful error, and call the function independently from a user interface.

## Prerequisites

You should know how to define a function and build summaries from dictionaries. Review [functions]({{ '/learning/lessons/python-functions/' | relative_url }}) and [record aggregation]({{ '/learning/lessons/python-intermediate-collections/' | relative_url }}).

## Write down the contract

Type hints communicate expected inputs to people and editor tools, but Python does not enforce them at runtime. Validate values that can arrive from a prompt, file, or other untrusted source.

```python
def validate_session(topic: object, minutes: object) -> tuple[str, int]:
    if not isinstance(topic, str) or not topic.strip():
        raise ValueError("topic must be non-empty text")
    if isinstance(minutes, bool) or not isinstance(minutes, int) or minutes <= 0:
        raise ValueError("minutes must be a positive whole number")
    return topic.strip(), minutes

print(validate_session("  Python  ", 25))
```

Expected output: `('Python', 25)`. Whitespace around a valid topic is removed. `True` is rejected even though `bool` is a subclass of `int`; accepting it would incorrectly treat a yes/no value as one minute.

## Return a value callers can reuse

Keep the contract separate from display. A caller can format the result for a terminal, a test, or a report without changing the calculation.

```python
def remaining_minutes(goal: int, completed: int) -> int:
    if goal < 0 or completed < 0 or completed > goal:
        raise ValueError("completed minutes must be between zero and the goal")
    return goal - completed

print(remaining_minutes(120, 45))
```

Expected output: `75`. The boundary `completed == goal` returns `0`; a negative value or an amount above the goal raises `ValueError` instead of returning a misleading result.

## Common mistakes

- Assuming a type hint converts or validates an input.
- Catching every exception and hiding the original problem.
- Returning an error string where callers expect an integer result.
- Mixing `input()` and `print()` into a function that should be easy to test.

## Practice

1. Write a function that accepts a title and page count and returns normalized values. **Hint:** strip the title and reject an empty result.
2. Define whether a session may have zero minutes, then implement and test that rule. **Hint:** state the allowed range before writing the condition.
3. Add a function that totals validated session records. **Hint:** validate each record before reading its numeric field.

Test ordinary input, each boundary, the wrong type, and a boolean where an integer is expected.

## Next steps

Use these contracts when reading [JSON files]({{ '/learning/lessons/python-intermediate-json/' | relative_url }}). The complete sequence and project rubric are in the [intermediate Python course]({{ '/learning/courses/python-intermediate/' | relative_url }}).
