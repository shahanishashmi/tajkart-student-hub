---
layout: lesson
title: "Problem PS-003: count vowels in a string"
description: "Count the five English vowels without changing the original text."
summary: Count the five English vowels without changing the original text.
permalink: /learning/problem-sets/string-vowel-count/
id: problem-string-vowel-count-003
content_type: problem-set
category: strings
language: en
difficulty: beginner
tags: [strings, loops, text]
prerequisites: [python-loops-001]
learning_objectives: ["Normalize character case and count selected characters in one pass."]
content_status: drafted
review_status: pending
searchable: true
---

## Problem

**PS-003.** Count occurrences of `a`, `e`, `i`, `o`, and `u`, case-insensitively. Treat `y` as a consonant for this exercise. Spaces and punctuation do not count.

## Examples and constraints

| Input | Expected output |
|---|---:|
| `"Tajkart"` | `2` |
| `"rhythm"` | `0` |
| `""` | `0` |

Input may contain Unicode characters, but only the five listed English letters count.

## Hint and reference solution

Normalize one character at a time and test membership in a small set.

```python
{% include solutions/count_vowels.py %}
```

Time is `O(n)` and the vowel set uses constant extra space. Tests cover uppercase/lowercase, no vowels, and empty text.
