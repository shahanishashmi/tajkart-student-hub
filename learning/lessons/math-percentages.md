---
layout: lesson
title: "Percentages: parts, discounts, and change"
description: Calculate a percentage of an amount, apply a discount and example tax rate, and compare changes with the correct baseline.
permalink: /learning/lessons/math-percentages/
id: math-percentages-001
content_type: lesson
category: math-foundations
language: en
difficulty: beginner
tags: [mathematics, percentages, discounts, percent-change, decimals]
prerequisites: [math-decimals-conversions-001, lesson-math-ratios-unit-rates-001]
related_resources: [course-academic-math-foundations, math-fractions-operations-001]
learning_objectives:
  - Interpret a percentage as a rate per 100 and find a percentage of a quantity.
  - Calculate a discount and a separately stated tax example with a clear order and rounding rule.
  - Calculate percent increase or decrease relative to a non-zero original amount.
estimated_minutes: 35
content_status: drafted
review_status: pending
searchable: true
order: 4
topic: Mathematics foundations
---

Percent means “per hundred.” Thus `25% = 25/100 = 0.25`, and 25% of 64 is `0.25 × 64 = 16`. A percentage compares an amount with a stated base. Increases, discounts, and percentages of a quantity can use different bases, so name the original amount before calculating.

## Prerequisites

Review [decimal and fraction conversions]({{ '/learning/lessons/math-decimals-conversions/' | relative_url }}) and [ratios and unit rates]({{ '/learning/lessons/math-ratios-unit-rates/' | relative_url }}). You should be able to multiply a decimal by a whole number and explain what the comparison's base represents.

## 1. Find a percentage of an amount

Change the percentage to a decimal and multiply by the amount. For 15% of 80, `0.15 × 80 = 12`. Check the scale: 15% is less than one fifth, and one fifth of 80 is 16, so 12 is plausible.

## 2. Apply a discount and a stated tax rate

Suppose an item costs 80.00 currency units, a 15% discount applies first, and an illustrative 8% tax is applied to the discounted amount. The discount is `80.00 × 0.15 = 12.00`; the reduced price is `80.00 − 12.00 = 68.00`. The example tax is `68.00 × 0.08 = 5.44`, so the example total is `73.44`.

This is arithmetic practice, not tax advice: actual tax bases, rates, and rounding rules depend on the place and transaction. Here we round the final currency values to two places using decimal half-up rounding.

```python
from decimal import Decimal, ROUND_HALF_UP

cent = Decimal("0.01")
price = Decimal("80.00")
discounted = (price * (Decimal("1") - Decimal("0.15"))).quantize(cent, rounding=ROUND_HALF_UP)
total = (discounted * (Decimal("1") + Decimal("0.08"))).quantize(cent, rounding=ROUND_HALF_UP)
percent_change = ((Decimal("50") - Decimal("40")) / Decimal("40") * 100).quantize(Decimal("0.1"))
print(discounted)
print(total)
print(f"{percent_change}% increase")
```

Expected output:

```text
68.00
73.44
25.0% increase
```

## 3. Describe percent change

For a non-zero starting amount, calculate `(new − original) ÷ original × 100%`. If a value changes from 40 to 50, the change is 10 and the original base is 40, so the increase is `10/40 × 100% = 25%`. The reverse change from 50 to 40 is `−10/50 × 100% = −20%`: reversing the direction changes the base, so the percentages need not match. Percent change from an original value of zero is undefined because the formula divides by zero.

Two changes of 10 percentage points are not always the same as a 10% change. A percentage point is the arithmetic difference between percentage values; a percent change uses the original percentage as its base.

## Common mistakes

- Multiplying by 15 instead of `0.15` when calculating 15% of an amount.
- Applying a tax to the original price when the question explicitly says it follows a discount.
- Reporting a percent increase without stating the original baseline.
- Treating a change from 40 to 50 as 10%; the absolute change is 10, while the percent change is 25% of the original 40.
- Computing percent change from zero or rounding intermediate currency amounts without a stated rule.

## Practice

1. Find 18% of 250.
2. A 120-unit item has a 20% discount. Find the reduced price.
3. Using a separate illustrative 5% tax after that discount, find the final total, rounded half-up to two places.
4. A score rises from 60 to 75. Find the absolute change and percent increase.
5. A count changes from 80 to 60. Find the percent change and identify its direction.
6. Why is a percent change from an original amount of zero undefined?

### Hints

1. Use `0.18 × 250`.
2. First find the discount amount, then subtract it from 120.
3. Multiply the discounted price by `1.05`.
4. Divide the increase by the original score, not the new score.
5. Use `(new − original) ÷ original × 100%`.
6. Identify the denominator in the percent-change formula.

### Worked answers

1. `0.18 × 250 = 45`.
2. Discount is 24, so the reduced price is 96 units.
3. `96 × 1.05 = 100.80` units.
4. Absolute change is 15 points; percent increase is `15/60 × 100% = 25%`.
5. `−20/80 × 100% = −25%`, a 25% decrease.
6. The formula divides by the original amount, and division by zero is undefined.

## Further learning

Use [Khan Academy's rate and percentage lessons](https://www.khanacademy.org/math/cc-seventh-grade-math/cc-7th-fractions-decimals) for separately hosted examples and practice. Tajkart has not copied that material or assessed its terms. Continue with [reading tables and charts]({{ '/learning/lessons/math-data-interpretation/' | relative_url }}), then use the [mixed mathematics self-check]({{ '/learning/problem-sets/math-foundations-check/' | relative_url }}) and the [complete foundations sequence]({{ '/learning/courses/academic-foundations/' | relative_url }}).
