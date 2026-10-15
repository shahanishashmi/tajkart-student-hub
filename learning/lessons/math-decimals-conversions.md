---
layout: lesson
title: Decimals, fraction conversions, and rounding
description: Read decimal place value, convert common fractions exactly, recognize repeating expansions, and round only as needed.
permalink: /learning/lessons/math-decimals-conversions/
id: math-decimals-conversions-001
content_type: lesson
category: math-foundations
language: en
difficulty: beginner
tags: [mathematics, decimals, fractions, place-value, rounding]
skills: [math-decimal-conversion]
prerequisites: [math-fractions-operations-001]
related_resources: [course-academic-math-foundations, math-percentages-001]
learning_objectives:
  - Explain the value of a decimal digit using its place.
  - Convert a fraction to a decimal and recognize terminating and repeating cases.
  - Round a decimal to a stated place using an explicit rule.
estimated_minutes: 35
content_status: drafted
review_status: pending
searchable: true
order: 2
topic: Mathematics foundations
---

Decimals use place value to write parts of one: tenths, hundredths, thousandths, and so on. In `4.36`, the 3 means 3 tenths and the 6 means 6 hundredths. A decimal point is a place marker, so aligning points matters when adding or subtracting.

## Prerequisites

Review [fraction operations]({{ '/learning/lessons/math-fractions-operations/' | relative_url }}) if numerator, denominator, or equivalent fractions are not familiar. This lesson uses division and place value.

## 1. Convert between common forms

To write a fraction as a decimal, divide its numerator by its denominator. `3/8 = 0.375`, which terminates. `1/3 = 0.333…`, which repeats; a finite rounded decimal such as `0.333` is an approximation, not the exact value. To convert a terminating decimal such as `0.625` to a fraction, write `625/1000` and simplify to `5/8`.

To change a decimal to a percentage, multiply by 100 and attach `%`: `0.375 = 37.5%`. To change a percentage to a decimal, divide by 100: `12% = 0.12`. These are different labels for the same proportional value.

```python
from decimal import Decimal, ROUND_HALF_UP

decimal_value = Decimal(3) / Decimal(8)
percentage_value = decimal_value * 100
rounded = Decimal("2.675").quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
print(f"{decimal_value:.3f} = {percentage_value:.1f}%")
print(rounded)
```

Expected output:

```text
0.375 = 37.5%
2.68
```

`Decimal("2.675")` constructs the decimal from text so the stated decimal is represented directly. `ROUND_HALF_UP` is one common rule; a class, currency system, or assignment may require another rule. Confirm it before rounding.

## 2. Estimate and align

Before computing `18.7 + 2.36`, estimate about `19 + 2 = 21`. Then align decimal points: `18.70 + 2.36 = 21.06`, which is close to the estimate. An answer such as `20.106` would be a signal to check the place-value alignment.

## Common mistakes

- Reading `0.4` as smaller than `0.35`; compare `0.40` with `0.35`.
- Moving the decimal point without applying the same scale to the fraction or percentage.
- Claiming `1/3 = 0.333` exactly; the decimal repeats and `0.333` is rounded.
- Rounding each intermediate step, which can change the final result.
- Assuming a universal tie-breaking rule; state the rule supplied for the task.

## Practice

1. Write `7/20` as a decimal and percentage.
2. Write `0.45` as a simplified fraction and a percentage.
3. Is the decimal form of `1/6` terminating or repeating? Give its first four decimal digits.
4. Add `12.8 + 0.37`, then compare the result with an estimate.
5. Round `6.245` to two decimal places using half-up rounding. How could another specified rule differ?

### Hints

1. Convert the denominator to 100.
2. `0.45` is 45 hundredths before simplification.
3. Divide 1 by 6 and look for a repeated digit pattern.
4. Write `12.80` before adding.
5. Inspect the third decimal digit and name the rule.

### Worked answers

1. `7/20 = 35/100 = 0.35 = 35%`.
2. `0.45 = 45/100 = 9/20 = 45%`.
3. `1/6 = 0.1666…`; the decimal repeats, and its first four digits are `1666`.
4. `12.80 + 0.37 = 13.17`; an estimate of about 13 is reasonable.
5. Half-up gives `6.25`. A different tie rule may treat an exact halfway case differently, so follow the rule named in the task.

## Further learning

Practise fraction, decimal, and percentage connections with [Khan Academy's conversion practice](https://www.khanacademy.org/math/algebra-basics/basic-alg-foundations/e/relate-fractions--decimals--and-percents). The link is a separately hosted learning activity; Tajkart does not copy its questions or claim its license. Next, study [ratios and unit rates]({{ '/learning/lessons/math-ratios-unit-rates/' | relative_url }}) and then [percentages in context]({{ '/learning/lessons/math-percentages/' | relative_url }}).
