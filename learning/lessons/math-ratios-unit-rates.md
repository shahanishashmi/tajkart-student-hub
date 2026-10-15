---
layout: lesson
title: Ratios, unit rates, and proportional reasoning
description: Compare quantities in the correct order, calculate a unit rate, and scale a proportional relationship.
permalink: /learning/lessons/math-ratios-unit-rates/
id: lesson-math-ratios-unit-rates-001
content_type: lesson
category: math-foundations
language: en
difficulty: beginner
tags: [mathematics, ratios, unit-rates, proportions, problem-solving]
skills: [math-unit-rates]
prerequisites: [math-fractions-operations-001, math-decimals-conversions-001]
related_resources: [course-academic-math-foundations, math-percentages-001]
learning_objectives:
  - Write and simplify a ratio while preserving the order and meaning of its quantities.
  - Calculate and label a unit rate from two quantities with different units.
  - Scale a proportional relationship using a common multiplier.
estimated_minutes: 30
content_status: drafted
review_status: pending
searchable: true
order: 3
topic: Mathematics foundations
---

Ratios, rates, and proportions help compare quantities. They appear in recipes, prices, maps, measurements, science, and everyday planning. This lesson introduces a few foundational cases; follow your course's notation and rounding rules when they differ.

## Prerequisites

Be comfortable with whole-number multiplication, division, and fractions. If those are new, practise them first with your class material or ask your teacher for a suitable starting example.

## 1. Read the order of a ratio

A ratio compares quantities in a stated order. If a bowl has 8 red beads and 12 blue beads, then the ratio of red beads to blue beads is `8:12`. Divide both terms by their greatest common divisor, 4, to simplify it to `2:3`.

The reverse comparison is blue to red: `12:8`, or `3:2` after simplifying. Keep the labels with the numbers until you are sure which quantity comes first. A ratio can compare two parts, such as red to blue, or one part with the whole, such as red to all beads (`8:20`, simplified to `2:5`). Those statements answer different questions.

## 2. Find and label a unit rate

A rate compares quantities with different units. A unit rate gives the amount for one unit of the second quantity.

**Example:** Four notebooks cost 120 currency units. The price per notebook is:

```text
120 currency units ÷ 4 notebooks = 30 currency units per notebook
```

You can check the division with a short Python calculation if you are already using Python:

```python
def unit_rate(total, quantity):
    if quantity <= 0:
        raise ValueError("quantity must be positive")
    return total / quantity

print(f"{unit_rate(120, 4):g}")
```

Expected output: `30`. The function rejects zero or negative quantities because a unit rate cannot be calculated by dividing by them in this example.

Keep the unit in the answer. If the same price per notebook continues, seven notebooks cost `7 × 30 = 210 currency units`. This assumes there is no discount, tax, or other fee changing the price.

### Compare package prices

One pack has 6 notebooks for 54 currency units; another has 10 for 85. Their unit prices are `54 ÷ 6 = 9` and `85 ÷ 10 = 8.5` currency units per notebook. The second pack has the lower price per notebook if the products are comparable. Its total price is still higher, so choose based on both the unit price and the amount you can afford or use.

## 3. Scale a proportional relationship

Two quantities are proportional in a situation when multiplying one by a factor also multiplies the other by the same factor, under the stated conditions.

**Example:** A recipe uses 2 cups of rice for 3 people. To plan for 6 people, the number of people is multiplied by 2. Multiply the rice by the same factor: `2 cups × 2 = 4 cups`. This calculation assumes the recipe scales directly and the serving size stays the same.

You can check the relationship with a table:

| People | 3 | 6 |
|---|---:|---:|
| Rice (cups) | 2 | 4 |

The pairs have the same ratio, `2:3` and `4:6`. Dividing each pair's terms by the same non-zero number preserves the ratio.

## Worked check: travel rate

A trip covers 180 kilometres in 2.5 hours at a steady rate. Divide distance by time:

```text
180 kilometres ÷ 2.5 hours = 72 kilometres per hour
```

The units are distance per time. At that constant rate, 1.5 hours corresponds to `72 × 1.5 = 108 kilometres`. Real journeys include stops and changing speeds, so use this as a constant-rate model rather than a promise about an actual trip.

## Common mistakes

- **Reversing the order:** “red to blue” and “blue to red” are different comparisons. Write labels before simplifying.
- **Comparing a part with the whole as if it were another part:** `red:blue` is not the same as `red:all beads`.
- **Dropping units:** currency units per item and items per currency unit describe different rates.
- **Adding instead of scaling:** if a recipe doubles the people, multiply each proportional ingredient by 2; do not add the same number to every quantity.
- **Assuming every situation is proportional:** check whether the context says or supports a constant ratio. Fees, discounts, and fixed starting amounts can change it.
- **Rounding too soon:** keep exact fractions or enough precision through intermediate steps, then round only as the assignment requires.

## Practice

Try each problem before reading the worked answers. Include labels and units in your work.

1. A group has 15 red counters and 25 blue counters. Simplify the ratio red to blue.
2. Five metres of fabric cost 450 currency units. Find the cost per metre.
3. A steady trip covers 180 kilometres in 2.5 hours. Find the unit rate in kilometres per hour.
4. A recipe uses 4 cups of flour for 6 servings. How much flour would the same direct proportion use for 9 servings?
5. A class compares 6 notebooks at 54 currency units with 10 at 85. Which pack has the lower unit price, and what assumption does that comparison make?

### Worked answers

1. `15:25` simplifies by dividing both terms by 5, so red to blue is `3:5`.
2. `450 ÷ 5 = 90` currency units per metre.
3. `180 ÷ 2.5 = 72` kilometres per hour.
4. The scale factor is `9 ÷ 6 = 1.5`; `4 × 1.5 = 6` cups.
5. The first is `54 ÷ 6 = 9` units per notebook; the second is `85 ÷ 10 = 8.5`. The 10-notebook pack is cheaper per notebook if the items are comparable and there are no additional fees. It still costs more in total.

## Assessment mini-task

Choose two comparable package sizes, recipe quantities, or travel examples from a class problem. Record the source quantities, the order of the comparison, the calculation, units, assumptions, and one check. Your work is complete when another student can follow the calculation and see whether the comparison is fair.

## Further learning

Explain why `2:3` and `4:6` represent the same ratio, then create a different example where the order matters. Use the [study-planning guide]({{ '/learning/study-skills/' | relative_url }}) to practise one problem, check it, and record a next step. Continue with [percentages in context]({{ '/learning/lessons/math-percentages/' | relative_url }}) in the [mathematics foundations path]({{ '/learning/courses/academic-foundations/' | relative_url }}). The broader subject map lists computing topics too; this is still an introductory unit.
