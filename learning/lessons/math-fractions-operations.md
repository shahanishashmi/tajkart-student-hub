---
layout: lesson
title: "Fractions: equivalent values and the four operations"
description: Simplify fractions, add and subtract with common denominators, multiply, divide, and check exact results.
permalink: /learning/lessons/math-fractions-operations/
id: math-fractions-operations-001
content_type: lesson
category: math-foundations
language: en
difficulty: beginner
tags: [mathematics, fractions, arithmetic, number-sense]
prerequisites: []
related_resources: [course-academic-math-foundations, math-decimals-conversions-001]
learning_objectives:
  - Explain what a numerator and denominator count in a fraction.
  - Produce an equivalent fraction and simplify by a common factor.
  - Add, subtract, multiply, and divide fractions and check the result.
estimated_minutes: 35
content_status: drafted
review_status: pending
searchable: true
order: 1
topic: Mathematics foundations
---

A fraction represents a number of equal parts. In `a/b`, the numerator `a` counts parts and the non-zero denominator `b` names the size of each part. A fraction can also represent division: `a/b` means `a ÷ b`. This lesson is an original first pass; follow your teacher's notation and simplify answers when requested.

## Prerequisites

Be comfortable with whole-number multiplication, division, and multiplication facts. If common factors are unfamiliar, use a factor list to find a number that divides both numerator and denominator.

## 1. Equivalent fractions and simplifying

Multiplying or dividing both terms by the same non-zero number preserves the value. For example, `3/4 = (3 × 5)/(4 × 5) = 15/20`. To simplify, divide top and bottom by a common factor: `18/24 = 3/4` after dividing both by 6. Do not cancel terms that are being added; `1/2 + 1/3` is not `2/5`.

## 2. Add and subtract

The parts must have the same size before they can be combined. Use a common denominator, then add or subtract numerators:

- `2/3 + 1/4 = 8/12 + 3/12 = 11/12`.
- `7/8 - 1/3 = 21/24 - 8/24 = 13/24`.

The denominator names the part size; it does not get added or subtracted.

## 3. Multiply and divide

For multiplication, multiply numerators and denominators, then simplify: `(2/3) × (9/10) = 18/30 = 3/5`. To divide by a non-zero fraction, multiply by its reciprocal: `(5/6) ÷ (10/9) = (5/6) × (9/10) = 45/60 = 3/4`. Division by zero is undefined, including when the divisor is `0`.

Python's `Fraction` keeps these examples exact instead of storing an approximate decimal:

```python
from fractions import Fraction

sum_result = Fraction(2, 3) + Fraction(1, 4)
division_result = Fraction(5, 6) / Fraction(10, 9)
print(sum_result)
print(division_result)
```

Expected output:

```text
11/12
3/4
```

## Common mistakes

- Adding denominators when adding fractions. Find a common denominator first.
- Changing only the numerator or only the denominator while making an equivalent fraction.
- Cancelling across addition, such as treating `1/2 + 1/3` like a product.
- Forgetting to multiply by the reciprocal when dividing, or allowing a zero divisor.
- Rounding an exact fraction too early when an exact answer is possible.

## Practice

Try first, and keep each step visible.

1. Simplify `21/28`.
2. Calculate `3/5 + 1/4`.
3. Calculate `7/9 - 1/6`.
4. Calculate `4/7 × 14/15`.
5. Calculate `3/8 ÷ 9/16`. Why would the same operation with a zero divisor be invalid?

### Hints

1. Divide both terms by their greatest common factor.
2. Use denominator 20.
3. Use denominator 18.
4. Multiply across, then simplify by a common factor.
5. Multiply by the reciprocal of `9/16`; compare the divisor with zero.

### Worked answers

1. `21/28 = 3/4`, dividing both terms by 7.
2. `12/20 + 5/20 = 17/20`.
3. `14/18 - 3/18 = 11/18`.
4. `56/105 = 8/15`.
5. `(3/8) × (16/9) = 48/72 = 2/3`. Division by zero has no defined result.

## Further learning

Use [Khan Academy's fractions lessons](https://www.khanacademy.org/math/arithmetic-home/arith-review-fractions/dividing-fractions) for another explanation and practice. This is an outbound link to the provider; Tajkart does not reproduce its exercises or claim its terms. Continue with the [decimal and conversion lesson]({{ '/learning/lessons/math-decimals-conversions/' | relative_url }}) in the [mathematics foundations path]({{ '/learning/courses/academic-foundations/' | relative_url }}).
