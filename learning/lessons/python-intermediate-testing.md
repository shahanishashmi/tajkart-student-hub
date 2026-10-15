---
layout: lesson
title: Test and organize a small Python application
description: "Keep reusable logic importable, test behavior with temporary data, and guard the command-line entry point."
summary: Keep reusable logic importable, test behavior with temporary data, and guard the command-line entry point.
permalink: /learning/lessons/python-intermediate-testing/
id: python-intermediate-testing-001
content_type: lesson
category: programming-languages
language: en
difficulty: intermediate
tags: [python, unittest, modules, command-line]
prerequisites: [python-intermediate-json-001, python-intermediate-validation-001]
related_resources: [language-path-python, course-python-intermediate-study-log]
learning_objectives:
  - Write a focused unit test for expected and boundary behavior.
  - Use a temporary directory for file-based tests.
  - Prevent command-line behavior from running when a module is imported.
estimated_minutes: 45
content_status: drafted
review_status: pending
searchable: true
order: 10
topic: Python
level: Intermediate
reading_time: 15
---

## Learning objectives

After this lesson, you can test a small function, test file behavior without leaving permanent artifacts, and organize a script so its functions can be imported safely.

## Prerequisites

You should know how to validate records and persist JSON. Review [input contracts]({{ '/learning/lessons/python-intermediate-validation/' | relative_url }}) and [JSON files]({{ '/learning/lessons/python-intermediate-json/' | relative_url }}).

## Test a behavior and a boundary

The standard-library `unittest` module discovers methods whose names start with `test_`. Test outcomes rather than copying the implementation into the test.

```python
import unittest


def remaining_minutes(goal, completed):
    if goal < 0 or completed < 0 or completed > goal:
        raise ValueError("completed minutes must be between zero and the goal")
    return goal - completed


class RemainingMinutesTests(unittest.TestCase):
    def test_goal_is_reached(self):
        self.assertEqual(remaining_minutes(60, 60), 0)

    def test_completed_cannot_exceed_goal(self):
        with self.assertRaises(ValueError):
            remaining_minutes(60, 61)
```

Expected result: both tests pass when run with `python -m unittest -v`. The first test covers the zero-result boundary; the second checks the stated invalid-input contract.

## Separate reusable logic from program startup

Put functions in an importable module. A `main` function describes the command-line action, and the guard runs it only when the file is executed directly.

```python
def main():
    print("Study log ready")


if __name__ == "__main__":
    main()
```

Expected output when executed directly: `Study log ready`. Importing this module defines `main` but does not print; that makes imports predictable for tests and other code.

## Common mistakes

- Testing only the example input and missing the empty or invalid boundary.
- Reusing one permanent test file and accidentally depending on yesterday's contents.
- Calling `main()` at module import time.
- Making tests depend on the current working directory or a network service.

## Practice

1. Test that an empty session list produces an empty summary. **Hint:** assert the returned value, not a printed representation.
2. Use `TemporaryDirectory` to test saving and loading JSON. **Hint:** create the path inside the temporary folder.
3. Move one calculation into a module and add the main guard. **Hint:** importing the calculation should have no visible side effect.

Run tests from the repository root and from a clean temporary-data state. A passing local test is evidence for the cases it covers, not a substitute for a technical review of the lesson.

## Next steps

Build the [Python study-log capstone]({{ '/learning/projects/python-study-log/' | relative_url }}), following the four-part [intermediate course]({{ '/learning/courses/python-intermediate/' | relative_url }}). Its small reference helpers are tested locally, while the full application remains your implementation exercise.
