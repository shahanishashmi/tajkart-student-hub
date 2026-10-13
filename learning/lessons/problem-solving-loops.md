---
title: Repeat a task with a Python loop
summary: Use for loops to process a sequence and keep a running total.
category: Python
level: Beginner
reading_time: 9
---

## Learning objectives

Use a `for` loop to repeat an action, explain what an accumulator stores, and predict a loop's output.

## Prerequisites

You should know how to assign [Python variables]({{ '/learning/lessons/python-variables/' | relative_url }}), call `print`, and read a list of values.

## Repeat once for each item

When the same operation applies to several values, a loop expresses that repetition directly. This example prints a short plan:

```python
topics = ["variables", "conditions", "loops"]
for topic in topics:
    print("Practise:", topic)
```

Expected output:

```text
Practise: variables
Practise: conditions
Practise: loops
```

The loop assigns each item in `topics` to `topic` in turn. The indented line is the loop body, so it runs once for every item.

## Keep a running total

An accumulator is a variable updated as a loop processes data. It often starts at a neutral value such as `0` for addition.

```python
minutes = [15, 20, 10]
total = 0
for session in minutes:
    total = total + session
print(total)
```

Output: `45`. After each pass, `total` contains the amount accumulated so far.

## Common mistakes

- Forgetting indentation changes which statements belong to the loop.
- Starting an addition total with an unrelated old value gives the wrong answer.
- A loop over an empty list runs zero times, so the initial accumulator remains unchanged.
- Printing the running total inside the loop shows intermediate values; move `print(total)` after the loop for one final result.

## Practice

1. Given `scores = [8, 6, 10]`, print each score on its own line.
2. Find the total number of pages in `[12, 18, 9]`.
3. Count how many study sessions are listed in `[25, 30, 15, 20]`.

Hints: loop over the list; add each page count to a total; increment a counter once per item. Check your outputs: total pages `39`, session count `4`.

## Further learning within Tajkart

Use the [practice set]({{ '/learning/problem-sets/' | relative_url }}) to plan a sequence of small programming challenges.
