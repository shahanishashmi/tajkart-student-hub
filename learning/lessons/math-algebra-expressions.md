---
layout: lesson
title: "Algebra: variables and expressions"
summary: Translate everyday quantities into expressions, identify their parts, and evaluate them by substitution.
description: Translate everyday quantities into expressions, identify their parts, and evaluate them by substitution.
permalink: /learning/lessons/math-algebra-expressions/
id: math-algebra-expressions-001
content_type: lesson
category: math-foundations
language: en
difficulty: beginner
tags: [mathematics, algebra, variables, expressions, substitution]
skills: [algebra-expressions, algebra-substitution]
prerequisites: [math-percentages-001]
related_resources: [course-algebra-foundations, math-algebra-one-step-001]
learning_objectives:
  - Distinguish a variable, coefficient, constant, term, expression, and equation.
  - Translate a simple quantity situation into an algebraic expression.
  - Evaluate a linear expression by substituting a given value and checking the order of operations.
estimated_minutes: 35
content_status: drafted
review_status: pending
searchable: true
order: 5
topic: Mathematics foundations
---

## Audience and prerequisites

This beginner lesson is for learners who can work with fractions, decimals, ratios, and percentages. Algebra gives names to quantities that may vary or are not yet known. It is an introductory unit, not a complete algebra course.

## What the symbols mean

A **variable** is a letter standing for a quantity. In a context, it may represent an unknown value or a value that changes. A **coefficient** multiplies a variable: in `4h`, the coefficient is 4. A **constant** has no variable, such as `3` in `4h + 3`. A **term** is a part separated by addition or subtraction, so `4h` and `3` are the terms in `4h + 3`.

An **expression** combines values and operations but does not state that two sides are equal: `4h + 3`. An **equation** makes an equality claim: `4h + 3 = 19`. An expression can be evaluated after a value is supplied; an equation can be solved to find values that make it true.

## Translate a situation

If one notebook costs 35 currency units and you buy `n` notebooks, the cost is `35n`. If delivery adds a fixed 20 units, the total is `35n + 20`. The coefficient `35` is the per-notebook cost, while `20` is the fixed amount. The expression assumes each notebook has the same price and no other fee applies.

If a student studies `h` hours on each of three evenings, the total is `3h` hours. If there is also one extra half-hour review, a model is `3h + 0.5`. Write the units and assumptions beside a real-world model so another person can tell what the letters mean.

## Substitute and evaluate

**Example 1:** Evaluate `4h + 3` for `h = 4`.

1. Replace every `h` with 4: `4(4) + 3`.
2. Multiply first: `16 + 3`.
3. Add: `19`.

The result is 19 points if the expression modeled points. To check, substitute `h = 4` into the original expression again and repeat the operations.

**Example 2:** A club has `p` members and adds 6 guests. For `p = 18`, `p + 6 = 18 + 6 = 24` people.

**Example 3:** Combine `3t + 2t`. Both terms count the same variable, so add only the coefficients: `(3 + 2)t = 5t`. By contrast, `3t + 2` has unlike terms and cannot be combined into `5t`.

```python
def notebook_total(quantity, price=35, delivery=20):
    if quantity < 0:
        raise ValueError("quantity cannot be negative")
    return quantity * price + delivery

print(notebook_total(4))
```

Expected output: `160`. This is a direct arithmetic model of `35n + 20` at `n = 4`; it does not decide whether delivery is actually charged in a particular shop.

## Common mistakes

- Treating `4h` as the two separate numbers 4 and h; it means multiplication.
- Calling `4h + 3` an equation; it is an expression until an equality is stated.
- Combining unlike terms such as `3h + 2`; the constant has no `h` factor.
- Substituting into only the first appearance of a variable; replace every instance.
- Forgetting context or units. `35n + 20` means little until `n` and the currency unit are defined.

## Practice, hints, and worked answers

Try the problems before opening the hints. Keep variable meanings beside your work.

1. A print shop charges 4 units per page plus a fixed 12-unit setup fee. Write an expression for `p` pages.
2. Evaluate `2s + 5` for `s = 7`.
3. In `8m - 3`, identify the coefficient, variable, constant, and terms.
4. Simplify `6x + 2x - 4`.
5. A student has `m` marks and earns 5 more. Write an expression, then state why it is not yet an equation.

<details><summary>Hints</summary>
<ol><li>Multiply the per-page cost by the page count, then add the fixed fee.</li><li>Replace <code>s</code> with 7 and multiply before adding.</li><li>Separate the variable term from the constant term, including the negative sign.</li><li>Combine the two <code>x</code> coefficients and retain the constant.</li><li>Name the unknown total, or add an equality only if a total value is supplied.</li></ol>
</details>

<details><summary>Worked answers and checks</summary>
<ol><li><code>4p + 12</code> units. For 2 pages, the expression gives <code>4(2) + 12 = 20</code>.</li><li><code>2(7) + 5 = 14 + 5 = 19</code>.</li><li>Coefficient 8; variable <code>m</code>; constant <code>-3</code>; terms <code>8m</code> and <code>-3</code>.</li><li><code>(6 + 2)x - 4 = 8x - 4</code>.</li><li><code>m + 5</code>; no equality statement or specified value has been given.</li></ol>
</details>

## Self-check and next step

Explain aloud what the variable, coefficient, and constant mean in one expression you wrote. If you can substitute a value and check it, continue to [one-step equations]({{ '/learning/lessons/math-algebra-one-step/' | relative_url }}). For another explanation, see Khan Academy's [variables, expressions, and equations lesson](https://www.khanacademy.org/math/als-k-to-12-math/x54b4346ef80b5dcc%3Aperformance-standard-e/x54b4346ef80b5dcc%3Aalgebraic-numerical-expressions-and-equations/v/variables-expressions-and-equations), checked on 2026-10-15. Tajkart does not reproduce the provider's lesson or claim its reuse terms.
