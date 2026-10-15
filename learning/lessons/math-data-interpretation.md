---
layout: lesson
title: Read data tables, averages, and charts
description: Compare small data sets with units, distinguish zero from missing data, and avoid misleading chart conclusions.
summary: Learn to read a table, calculate a total, mean, median, and share, and check what a chart does and does not show.
permalink: /learning/lessons/math-data-interpretation/
id: math-data-interpretation-001
content_type: lesson
category: math-foundations
language: en
difficulty: beginner
tags: [mathematics, data-interpretation, mean, median, charts, statistics]
skills: [math-data-summaries]
prerequisites: [math-percentages-001]
related_resources: [course-academic-math-foundations, problem-math-foundations-check-010]
learning_objectives:
  - Read a small table and keep its units and time period clear.
  - Calculate and interpret a total, mean, median, and share of a total.
  - Distinguish a measured zero from a missing value and identify misleading chart choices.
estimated_minutes: 35
content_status: drafted
review_status: pending
searchable: true
order: 5
topic: Mathematics foundations
---

Data is a set of recorded observations. Before calculating, ask what each value measures, which group it describes, when it was collected, and whether a missing value means zero or simply “not recorded.” A correct calculation can still answer the wrong question if those labels are ignored.

## Prerequisites

Review [percentages and baselines]({{ '/learning/lessons/math-percentages/' | relative_url }}). You should be able to add whole numbers and find a percentage of a total. If the table's values have a different unit, keep that unit attached to every result.

## 1. Read the table before calculating

Suppose a learner records focused study minutes on five weekdays:

| Day | Minutes |
|---|---:|
| Monday | 30 |
| Tuesday | 45 |
| Wednesday | 0 |
| Thursday | 60 |
| Friday | 45 |

The table says the recorded time for Wednesday was zero minutes. If Wednesday had not been recorded, the cell should be marked missing instead. Replacing an unknown value with zero would change totals and averages and could create a false conclusion.

## 2. Choose a summary that fits the question

The total is `30 + 45 + 0 + 60 + 45 = 180 minutes`. There are five recorded days, so the mean is `180 ÷ 5 = 36 minutes per recorded weekday`. The sorted observations are `0, 30, 45, 45, 60`; the middle value, or median, is 45 minutes.

The mean uses every value and is useful for a total spread across equally counted observations. The median is the middle observation after sorting and is less affected by a very large or small value. Neither summary is automatically “the right average”; state which one you use and why.

Thursday accounts for `60 ÷ 180 × 100% = 33.3%` of the recorded total, rounded to one decimal place. This share is about the total in this five-day table. It does not say that Thursday is a typical day or that the same pattern will continue.

```python
from decimal import Decimal
from statistics import median

minutes = [30, 45, 0, 60, 45]
total = sum(minutes)
mean_minutes = total / len(minutes)
median_minutes = median(minutes)
thursday_share = Decimal(60) / Decimal(total) * 100
print(total)
print(mean_minutes)
print(median_minutes)
print(f"{thursday_share.quantize(Decimal('0.1'))}%")
```

Expected output:

```text
180
36.0
45
33.3%
```

## 3. Check a chart's scales and labels

A bar chart for these observations should label the horizontal axis with the days, label the vertical axis “focused study (minutes),” and use a consistent scale. Starting a bar chart at 50 instead of zero can make a change from 55 to 60 minutes look much larger than it is. A line chart can show order over time, but joining separate categories with a line may imply a continuous sequence that the data does not contain.

When you compare two groups, check that both use the same units, time period, and collection method. A larger count may reflect a larger group rather than a higher individual rate. For rates, divide by the relevant group size and state the denominator.

## Common mistakes

- Treating an unrecorded observation as zero without evidence.
- Calculating the mean with the number of non-missing rows when the question defines a different group.
- Reporting “36” without saying it is minutes per recorded weekday.
- Choosing the mean or median without considering the data shape and question.
- Comparing counts across groups with different sizes instead of comparing a suitable rate.
- Inferring that one event caused another from a small table or a chart that only shows an association.
- Ignoring a truncated axis, inconsistent intervals, or missing units.

## Practice

Use the values `12, 15, 0, 9` unless a question gives a different set.

1. Find the total, mean, and median. Include the unit “minutes.”
2. What share of the total is the observation 15? Round to the nearest whole percent.
3. A second group has values `10, 10, 12, 14`. Compare the two means, and state one reason the means alone do not prove that one group studied more overall.
4. A chart's vertical axis starts at 50 and shows bars of 55 and 60. What should a reader check before judging the difference?
5. Explain why a blank cell and a recorded zero must not automatically be treated as the same value.
6. A table shows that people who studied longer also received higher scores. Name one reason this association alone does not prove that study time caused the score difference.

### Hints

1. Add all four observations and divide by four; sort them before choosing the middle pair.
2. Divide 15 by the total before converting the fraction to a percentage.
3. A mean describes a per-observation average; group size and collection conditions matter too.
4. Check the baseline and interval sizes. A bar chart normally needs a zero baseline to compare bar lengths fairly.
5. A zero is an observed quantity; a blank may be unknown or not collected.
6. Other differences between people or groups may explain some or all of the pattern.

### Worked answers

1. Total: `12 + 15 + 0 + 9 = 36 minutes`. Mean: `36 ÷ 4 = 9 minutes`. Sorted values are `0, 9, 12, 15`; median: `(9 + 12) ÷ 2 = 10.5 minutes`.
2. `15 ÷ 36 × 100% = 41.7%`, which rounds to `42%`.
3. The first mean is 9 minutes. The second total is 46 minutes and its mean is `46 ÷ 4 = 11.5 minutes`. The means describe these observations only; group sizes, timing, or collection methods may differ.
4. Check whether both bars share the same zero baseline and evenly spaced intervals. A truncated axis can exaggerate the visual difference.
5. A recorded zero contributes an observed quantity of none. A blank has no measured value, so filling it with zero requires an explicit rule and evidence.
6. Prior knowledge, available time, task difficulty, or another factor could affect both study time and scores. The table alone shows association, not cause.

## Further learning

Return to the [mathematics foundations path]({{ '/learning/courses/academic-foundations/' | relative_url }}) for the sequence and mixed practice, or open the [student subject map]({{ '/learning/subjects/' | relative_url }}) to see which other academic areas still need original lessons. This is an introductory English draft; a mathematics educator has not reviewed it.
