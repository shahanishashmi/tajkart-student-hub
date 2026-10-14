---
layout: page
title: Interactive learning
description: A practice-first routine for turning a short lesson into an active coding session.
permalink: /learning/interactive-tutorials/
id: interactive-learning-guide
content_type: interactive
category: programming-fundamentals
language: en
difficulty: beginner
tags: [prediction, practice, feedback, programming]
learning_objectives:
  - Predict a program result before running it.
  - Compare a result with a prediction and explain the difference.
prerequisites: []
content_status: drafted
review_status: pending
searchable: true
---

An effective interactive lesson asks you to predict, act, observe, and explain. You can use this routine in any local editor or browser-based environment.

## A four-step practice loop

1. **Predict:** read a short code sample and write down what you expect it to do.
2. **Run:** execute it without changing the code.
3. **Observe:** compare the output with your prediction and note the first difference.
4. **Change:** edit one value or line, predict again, then run the new version.

Try this with the [Python loop lesson]({{ '/learning/lessons/problem-solving-loops/' | relative_url }}): predict how many times the body runs if you add one more topic to the list.

## Quick check

The list below contains three values. How many times will the loop body run?

```python
for day in ["Mon", "Tue", "Wed"]:
    print(day)
```

<label for="loop-answer"><strong>Your answer</strong></label>
<input id="loop-answer" class="search-box" type="number" min="0" inputmode="numeric" aria-describedby="loop-feedback">
<button id="check-loop-answer" class="button" type="button">Check answer</button>
<p id="loop-feedback" class="search-status" aria-live="polite">Count one loop pass for each list item.</p>

## Make a useful activity

Keep one idea per step. Give learners a way to check their result, a hint they can request, and a chance to retry. Avoid treating typing speed as understanding. When using a third-party playground, review its privacy and data-handling terms before entering personal information.

Try the [four-question code-reading quiz]({{ '/learning/interactive-tutorials/quiz/' | relative_url }}). It checks selected answers in your browser and does not execute submitted code.
