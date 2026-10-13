---
layout: page
title: Programming practice set
description: Small original exercises for practising variables, loops, and clear reasoning.
permalink: /learning/problem-sets/
---

Try each task before looking at the hint. Write one example input and expected output first; it makes it easier to tell whether your program works.

## 1. Remaining pages

Given `total_pages = 240` and `pages_read = 35`, calculate how many pages remain.

Hint: subtract the pages read from the total.

## 2. Count completed sessions

Given `sessions = [20, 0, 30, 25]`, count sessions whose duration is greater than zero.

Hint: start a count at zero, then add one when a session is positive. Expected count: `3`.

## 3. Study-time total

Given `minutes = [15, 20, 10]`, calculate total study time using a loop.

Hint: use an accumulator. Expected total: `45`.

## 4. Find the longest title

Given `titles = ["Loops", "Variables", "Functions"]`, find and print the longest title.

Hint: keep a current best title. Compare lengths with `len(title)`. Expected answer: `"Functions"`.

## 5. Explain the method

Write a short explanation of one exercise as if a classmate will implement it in another language. Include the input, the steps, and how you know the output is correct.

See the [loop lesson]({{ '/learning/lessons/problem-solving-loops/' | relative_url }}) for an example of processing a list.
