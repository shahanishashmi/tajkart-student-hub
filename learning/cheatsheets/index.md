---
layout: page
title: Python starter reference
description: A compact original reminder of Python syntax introduced in the beginner lessons.
permalink: /learning/cheatsheets/
---

Use this as a reminder after practising each idea. It is not a substitute for reading error messages or checking the official documentation for details.

```python
# Assign values
name = "Amina"
minutes = 25

# Choose a branch
if minutes >= 20:
    print("Goal reached")
else:
    print("Keep going")

# Repeat for each item
topics = ["lists", "loops"]
for topic in topics:
    print(topic)

# Define and call a function
def double(number):
    return number * 2

print(double(4))  # 8
```

Remember: indentation defines blocks, `=` assigns, and `==` compares. See the [variables lesson]({{ '/learning/lessons/python-variables/' | relative_url }}) and [loop lesson]({{ '/learning/lessons/problem-solving-loops/' | relative_url }}) for explanations and exercises.
