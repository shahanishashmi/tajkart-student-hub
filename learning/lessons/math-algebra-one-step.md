---
layout: lesson
title: "Algebra: one-step equations"
summary: Solve one-step equations by preserving equality, using inverse operations, and checking by substitution.
description: Solve one-step equations by preserving equality, using inverse operations, and checking by substitution.
permalink: /learning/lessons/math-algebra-one-step/
id: math-algebra-one-step-001
content_type: lesson
category: math-foundations
language: en
difficulty: beginner
tags: [mathematics, algebra, equations, inverse-operations]
skills: [algebra-equations-one-step, algebra-substitution]
prerequisites: [math-algebra-expressions-001]
related_resources: [course-algebra-foundations, math-algebra-two-step-001, problem-algebra-foundations-check-011]
learning_objectives:
  - Solve one-step addition, subtraction, multiplication, and division equations while applying the same operation to both sides.
  - Check a proposed solution by substituting it into the original equation.
  - Distinguish an equation with one solution from simple identity and no-solution cases without dividing by zero.
estimated_minutes: 40
content_status: drafted
review_status: pending
searchable: true
order: 6
topic: Mathematics foundations
---

## Audience and prerequisites

This beginner lesson follows [variables and expressions]({{ '/learning/lessons/math-algebra-expressions/' | relative_url }}). You should recognize a variable and be able to substitute a value. A solution is a value that makes the original equation true.

## Equality as a balance

An equation states that its left and right sides have the same value. Imagine two equal piles: if you remove the same amount from both, they remain equal. Algebra uses this balance idea. An operation on only one side generally changes the equality; apply the same operation to both sides.

Inverse operations undo one another: addition and subtraction are inverses, as are multiplication and division by a non-zero number. Choose the inverse that isolates the variable, then check the result in the original statement.

## Worked examples

**Addition:** Solve `x + 8 = 13`.

1. Subtract 8 from both sides: `x + 8 - 8 = 13 - 8`.
2. Simplify: `x = 5`.
3. Check: `5 + 8 = 13`, so the statement is true.

**Subtraction with a negative result:** Solve `m - 9 = 4`.

Add 9 to both sides: `m = 13`. Check: `13 - 9 = 4`.

**Multiplication with zero as the answer:** Solve `7n = 0`.

Divide both sides by 7: `n = 0`. Check: `7(0) = 0`. Zero is allowed as a solution; the divisor, 7, is non-zero.

**Division and a negative value:** Solve `p / 4 = -3`.

Multiply each side by 4: `p = -12`. Check: `-12 / 4 = -3`.

```python
def solve_addition_equation(right_side, added_amount):
    return right_side - added_amount

solution = solve_addition_equation(13, 8)
print(solution)
print(solution + 8 == 13)
```

Expected output:

```text
5
True
```

The check evaluates the original equation after substituting the proposed value.

## Special cases and invalid operations

For `0w = 0`, every value of `w` makes the statement true, so there are infinitely many solutions. For `0w = 5`, no value works because the left side is always 0; there is no solution. Do not divide either equation by zero. If an inverse operation would require division by a zero coefficient, stop and compare both sides instead.

## Common mistakes

- Changing one side only, which breaks the equality.
- Saying “move it across and change the sign” without showing the same operation on both sides.
- Dividing by zero, which is undefined.
- Forgetting negative signs when multiplying or dividing.
- Checking only a transformed equation instead of substituting into the original.

## Practice, hints, and worked answers

1. Solve `a + 6 = 10` and check it.
2. Solve `b - 4 = -2` and check it.
3. Solve `4c = 0`. Explain why the answer is permitted.
4. Solve `4p = -48` and substitute your answer into the left side.
5. Classify `0r = 0` and `0r = 6` as having one, none, or infinitely many solutions.

<details><summary>Hints</summary>
<ol><li>Subtract 6 from each side.</li><li>Add 4 to each side; keep the negative value.</li><li>Divide by the non-zero coefficient 4.</li><li>Divide both sides by 4, then check the product.</li><li>Compare the left side, which is always zero, with each right side.</li></ol>
</details>

<details><summary>Worked answers and substitution checks</summary>
<ol><li><code>a = 4</code>; <code>4 + 6 = 10</code>.</li><li><code>b = 2</code>; <code>2 - 4 = -2</code>.</li><li><code>c = 0</code>; <code>4(0) = 0</code>, and division by 4 is valid.</li><li><code>p = -12</code>; <code>4(-12) = -48</code>.</li><li><code>0r=0</code> is true for every <code>r</code>; <code>0r=6</code> is never true.</li></ol>
</details>

## Self-check and further learning

Can you explain which operation preserves the balance, show it on both sides, and verify the result? Continue to [two-step equations]({{ '/learning/lessons/math-algebra-two-step/' | relative_url }}). Khan Academy's [one-step equations review](https://www.khanacademy.org/math/pre-algebra/pre-algebra-equations-expressions/pre-algebra-equation-word-problems/a/one-step-equation-review) was checked on 2026-10-15. It is an external learning option; its content and terms are separate from Tajkart.
