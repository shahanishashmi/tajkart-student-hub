---
title: "Object-oriented programming: model behavior with small objects"
summary: Use classes, methods, and composition when they clarify a program's responsibilities.
permalink: /learning/guides/object-oriented-programming/
id: guide-object-oriented-programming
content_type: guide
category: programming-paradigms
language: en
difficulty: beginner
tags: [oop, classes, methods, composition]
prerequisites: [guide-programming-foundations]
learning_objectives:
  - Distinguish a class from an instance.
  - Keep state changes behind methods with clear behavior.
  - Choose composition when one object uses another object's service.
estimated_minutes: 35
content_status: drafted
review_status: pending
searchable: true
order: 3
---

## What this guide covers

Object-oriented programming groups state and related operations. A class describes a kind of object; an instance is one concrete object created from that description. This is one way to organize code, not a requirement for every program.

## Who should study it

Use this guide after writing functions and working with collections. If a short script is already clear as a few functions, adding classes may make it harder to read rather than better.

## Concept path

1. Define a class for a concept with stable state and behavior.
2. Construct instances and pass required data explicitly.
3. Keep invariants in one place; a method should leave state valid.
4. Prefer composition when a type needs another service.
5. Test public behavior instead of relying on private implementation details.

## Worked example

```python
class StudyTimer:
    def __init__(self, minutes):
        if minutes < 0:
            raise ValueError("minutes cannot be negative")
        self.minutes = minutes

    def add_time(self, extra_minutes):
        if extra_minutes < 0:
            raise ValueError("extra time cannot be negative")
        self.minutes += extra_minutes

timer = StudyTimer(25)
timer.add_time(5)
print(timer.minutes)
```

Expected output: `30`. The constructor and method both protect the rule that stored time cannot be reduced by a negative input. In a larger app, prefer a property or a single operation that makes the intended state change obvious.

## Common mistakes

- Creating a class for every noun, even when a function is simpler.
- Storing duplicated values that can contradict each other.
- Making a “god object” responsible for unrelated tasks.
- Testing private fields while ignoring the behavior a learner actually uses.

## Practice and next steps

Sketch a `Book` object with a title and page count. Decide which invalid values to reject, then write two tests. Next compare this design with a dictionary plus functions and explain which is clearer for a one-time report.
