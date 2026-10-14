---
layout: lesson
title: "Algebra: two-step equations"
summary: Reverse addition or subtraction and then multiplication or division, showing each balanced step and checking the solution.
description: Reverse addition or subtraction and then multiplication or division, showing each balanced step and checking the solution.
permalink: /learning/lessons/math-algebra-two-step/
id: math-algebra-two-step-001
content_type: lesson
category: math-foundations
language: en
difficulty: beginner
tags: [mathematics, algebra, equations, linear-equations]
skills: [algebra-equations-two-step, algebra-substitution]
prerequisites: [math-algebra-one-step-001]
related_resources: [course-algebra-foundations, problem-algebra-foundations-check-011]
learning_objectives:
  - Solve equations of the form ax + b = c by reversing operations in a justified order.
  - Preserve equality at each step and verify a solution in the original equation.
  - Identify when a two-step equation has a negative or fractional solution without rounding it prematurely.
estimated_minutes: 40
content_status: drafted
review_status: pending
searchable: true
order: 7
topic: Mathematics foundations
---

## Audience and prerequisites

This beginner lesson follows [one-step equations]({{ '/learning/lessons/math-algebra-one-step/' | relative_url }}). You should be able to preserve equality with an inverse operation and check a solution by substitution. This first two-step unit covers equations in the form `ax + b = c`; it does not cover every algebraic equation.

## Reverse the operations in order

In `2x + 5 = 17`, the variable is first multiplied by 2 and then 5 is added. To isolate `x`, undo those operations in reverse order: subtract 5, then divide by 2. Apply each operation to both sides and retain each line so the reasoning can be checked.

## Worked examples

**Example 1:** Solve `2x + 5 = 17`.

1. Subtract 5 from each side: `2x = 12`.
2. Divide each side by 2: `x = 6`.
3. Substitute into the original: `2(6) + 5 = 12 + 5 = 17`.

**Example 2:** Solve `3y - 4 = 8`.

Add 4 to each side: `3y = 12`. Divide each side by 3: `y = 4`. Check: `3(4) - 4 = 8`.

**Example 3:** Solve `2z + 1 = 4`.

Subtract 1: `2z = 3`. Divide by 2: `z = 3/2`. Check: `2(3/2) + 1 = 3 + 1 = 4`. Keep the fraction exact; as a decimal it is 1.5.

**Example 4:** Solve `-2q + 3 = 8`.

Subtract 3: `-2q = 5`. Divide by -2: `q = -5/2`. Check: `-2(-5/2) + 3 = 5 + 3 = 8`.

```python
def solve_two_step(coefficient, constant, right_side):
    if coefficient == 0:
        raise ValueError("coefficient must be non-zero")
    return (right_side - constant) / coefficient

answer = solve_two_step(2, 5, 17)
print(answer)
print(2 * answer + 5 == 17)
```

Expected output:

```text
6.0
True
```

This small example uses numbers exactly representable here. For fractional work, use exact fraction arithmetic rather than relying on floating-point equality.

## Common mistakes and invalid steps

- Dividing before removing the added constant: that changes the intended order and often gives a wrong result.
- Subtracting a constant on one side only.
- Changing a negative coefficient to positive without dividing both sides by it.
- Rounding a fraction before substituting it back.
- Dividing by a zero coefficient. The function rejects this case instead of pretending a solution exists.

## Practice, hints, and worked answers

1. Solve `4a + 3 = 19`.
2. Solve `5b - 7 = 8`.
3. Solve `3c + 2 = -7`.
4. Solve `2d + 1 = 4`; give an exact fraction and check it.
5. Explain why `0x + 2 = 5` cannot be solved by dividing by the coefficient.

<details><summary>Hints</summary>
<ol><li>Undo addition before multiplication.</li><li>Add 7 first, then divide by 5.</li><li>Subtract 2 first; keep the negative sign when dividing by 3.</li><li>Subtract 1, then divide 3 by 2.</li><li>The coefficient is zero, so inspect the resulting statement instead of dividing.</li></ol>
</details>

<details><summary>Worked answers and substitution checks</summary>
<ol><li><code>4a = 16</code>, so <code>a = 4</code>; <code>4(4)+3=19</code>.</li><li><code>5b = 15</code>, so <code>b = 3</code>; <code>5(3)-7=8</code>.</li><li><code>3c=-9</code>, so <code>c=-3</code>; <code>3(-3)+2=-7</code>.</li><li><code>d=3/2</code>; <code>2(3/2)+1=4</code>.</li><li>The left side is always 2, so it never equals 5; the equation has no solution.</li></ol>
</details>

## Self-check and further learning

Before using your result, point to the first operation applied to the variable, show its inverse on both sides, and substitute into the original equation. Continue with the [algebra foundations self-check]({{ '/learning/problem-sets/algebra-foundations-check/' | relative_url }}). Khan Academy's [linear equations course](https://www.khanacademy.org/math/algebra-home/alg-basic-eq-ineq) was checked on 2026-10-15; its broader curriculum goes beyond this short Tajkart draft.
