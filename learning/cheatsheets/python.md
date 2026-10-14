---
title: "Python quick reference"
summary: Compact reminders for Python values, decisions, loops, and functions.
permalink: /learning/cheatsheets/python/
id: cheatsheet-python-basics
content_type: cheatsheet
category: programming-languages
language: en
difficulty: beginner
tags: [python, syntax, variables, loops, functions]
prerequisites: [language-path-python]
learning_objectives: ["Look up beginner Python syntax without a long explanation."]
content_status: drafted
review_status: pending
searchable: true
---

## Values and decisions

```python
name = "Amina"          # str
minutes = 25             # int
if minutes >= 20:
    print("Goal reached")
else:
    print("Keep going")
```

`=` assigns; `==` compares. Indentation defines a block. Text and numbers are different types, even when the text contains digits.

## Repetition and functions

```python
topics = ["lists", "loops"]
for topic in topics:
    print(topic)

def double(number):
    return number * 2
```

Use `return` to pass a result back to the caller. Test empty collections and values at the boundary. See the [Python path]({{ '/learning/languages/python/' | relative_url }}) for explanations and practice.
