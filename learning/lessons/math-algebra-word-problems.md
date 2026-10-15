---
layout: lesson
title: "Algebra: model linear word problems"
description: Define an unknown, translate a fixed amount plus a repeated rate into a linear equation, solve it, and check the result in context.
summary: Practise moving from a real situation to a one-variable linear equation, with units, assumptions, worked steps, and a formative check.
permalink: /learning/lessons/math-algebra-word-problems/
id: math-algebra-word-problems-001
content_type: lesson
category: math-foundations
language: en
difficulty: beginner
tags: [mathematics, algebra, word-problems, equations, modeling]
skills: [algebra-word-problem-modeling, algebra-equations-two-step, algebra-substitution]
prerequisites: [math-algebra-expressions-001, math-algebra-two-step-001]
related_resources: [course-algebra-foundations, problem-algebra-foundations-check-011]
learning_objectives:
  - Define an unknown with a meaning and unit that match the situation.
  - Translate fixed and repeated quantities into a linear equation and state assumptions.
  - Solve the equation, interpret the value in context, and verify it in the original situation.
estimated_minutes: 35
content_status: drafted
review_status: pending
searchable: true
order: 4
topic: Mathematics foundations
---

## Prerequisites

Review [variables and expressions]({{ '/learning/lessons/math-algebra-expressions/' | relative_url }}) and [two-step equations]({{ '/learning/lessons/math-algebra-two-step/' | relative_url }}). You should be able to multiply a rate by a count, undo operations on both sides, and check a value by substitution. This draft is an introduction to one-variable linear models, not a complete word-problem curriculum.

## A modeling routine

1. **Name the unknown.** Say what it represents and attach a unit, such as `v = number of visits`.
2. **Separate fixed and repeated quantities.** A joining fee is paid once; a per-visit charge is multiplied by visits.
3. **Write an equation from the relationship.** Keep both sides in the same unit.
4. **State assumptions.** For example, every visit costs the same amount, there are no extra fees, and the total covers exactly those charges.
5. **Solve and interpret.** A number is only useful if its unit and allowed values fit the situation.
6. **Substitute back.** Check the result in the original statement, not only in a rearranged equation.

## Worked example: equal unit prices

Five identical notebooks cost 150 currency units in total. Let `p` be the cost of one notebook, measured in currency units per notebook. The five equal prices add to the total:

`5p = 150`

Divide both sides by 5: `p = 30` currency units per notebook. Check the model: `5 × 30 = 150` currency units. This assumes the notebooks have the same price and the stated total includes no other charge.

## Worked example: a fixed fee and a repeated rate

A club collects a 24-unit joining fee and 6 units for each visit. The bill is 60 units. Define `v` as the number of visits. The total relationship is:

`24 + 6v = 60`

Subtract 24 from both sides: `6v = 36`. Divide both sides by 6: `v = 6` visits. Check: the joining fee plus six visit charges is `24 + 6 × 6 = 60` units. The answer is a whole non-negative count, so it fits the stated context.

## Units and assumptions

In `fixed fee + (rate × count) = total`, the rate is measured in units per count and the count is measured in counts. Their product has the same unit as the fee and total. A mismatch such as adding currency directly to a number of visits signals that a unit or model term is missing. Some real settings allow fractional counts or have taxes, minimum charges, or changing rates; include those only when the prompt supports them.

## Common mistakes

- Choosing a variable without saying what it counts or measures.
- Multiplying the fixed fee by the unknown when the fee is paid once.
- Dividing the total by the repeated rate before accounting for the fixed amount.
- Reversing the order of inverse operations in a two-step equation.
- Accepting a negative or fractional count when the situation requires a whole non-negative count.
- Checking only the rearranged equation instead of substituting into the original story.

## Graduated practice

Try each prompt before opening its method. The first asks for a unit price; later items include a fixed amount or a starting balance. The interactive check scores only the requested number. It does not assess whether the variable definition, equation, assumptions, or units are explained correctly.

```python
from fractions import Fraction

def solve_additive_model(rate, fixed, total):
    if rate == 0:
        raise ValueError("rate must be non-zero")
    return Fraction(total - fixed, rate)

print(solve_additive_model(5, 0, 150))
print(solve_additive_model(6, 24, 60))
print(solve_additive_model(30, 140, 350))
```

Expected output:
```text
30
6
7
```

The code illustrates exact arithmetic for the three checked examples. It does not parse a story, choose assumptions, or validate a learner's model.

## Formative check

Define the variable and equation in your own work, then submit the requested value. A correct value gives limited feedback: compare the displayed variable definition, equation, steps, units, and substitution with your approach. Hints remain separate from the worked solutions until you submit.

<form data-quiz data-assessment-id="{{ site.data.algebra_modeling_assessment.id | escape }}">
  {% for question in site.data.algebra_modeling_assessment.questions %}
  {% assign mapped_lesson = site.pages | where: "id", question.lesson_id | first %}
  <fieldset class="quiz-question" data-question data-question-id="{{ question.id | escape }}" data-skill-ids="{{ question.skill_ids | join: ',' | escape }}" data-resource-id="{{ question.lesson_id | escape }}" data-resource-url="{{ mapped_lesson.url | relative_url }}" data-answer-format="{{ question.answer_format | escape }}" data-accepted-answers="{{ question.accepted_answers | join: '|' | escape }}">
    <legend><strong>{{ forloop.index }}.</strong> {{ question.question | escape }} <span class="difficulty-label">{{ question.difficulty | escape }}</span></legend>
    <label for="answer-{{ question.id | escape }}">Your numeric answer</label>
    <input id="answer-{{ question.id | escape }}" name="{{ question.id | escape }}" type="text" inputmode="decimal" autocomplete="off" aria-describedby="hint-{{ question.id | escape }} feedback-{{ question.id | escape }}">
    <details id="hint-{{ question.id | escape }}"><summary>Hint</summary><p>{{ question.hint | escape }}</p></details>
    {% for mistake in question.common_mistakes %}<details><summary>Common mistake to avoid</summary><p>{{ mistake | escape }}</p></details>{% endfor %}
    {% for prerequisite_id in question.prerequisite_ids %}{% assign prerequisite_page = site.pages | where: "id", prerequisite_id | first %}{% if prerequisite_page %}<p>Prerequisite: <a href="{{ prerequisite_page.url | relative_url }}">{{ prerequisite_page.title | escape }}</a></p>{% endif %}{% endfor %}
    {% if mapped_lesson %}<p><a href="{{ mapped_lesson.url | relative_url }}">Review the related lesson: {{ mapped_lesson.title | escape }}</a></p>{% endif %}
    <p id="feedback-{{ question.id | escape }}" data-feedback aria-live="polite"></p>
    <details data-solution hidden><summary>Worked solution and method</summary><p>{{ question.solution | escape }}</p><p>{{ question.explanation | escape }}</p></details>
  </fieldset>
  {% endfor %}
  <p data-quiz-progress role="status" aria-live="polite">0 of {{ site.data.algebra_modeling_assessment.questions.size }} questions answered.</p>
  <button class="button" type="submit">Check answers</button>
  <p data-quiz-status role="status" aria-live="polite">The numeric result is checked locally; equation setup and explanation are not scored.</p>
  <section class="mastery-summary" data-mastery-summary aria-live="polite" aria-atomic="true" aria-label="Practice evidence"></section>
</form>

## Next step

Use the [algebra foundations path]({{ '/learning/courses/algebra-foundations/' | relative_url }}) to see the lesson in sequence. Continue only when you can name the unknown, make an equation with consistent units, solve it, and check it against the original situation. This English draft remains pending a mathematics educator's review.
