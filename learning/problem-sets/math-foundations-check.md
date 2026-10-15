---
layout: lesson
title: "Mixed self-check: arithmetic, percentages, and data"
description: "A seven-question formative set to practise exact values, conversions, unit rates, percentages, and basic data interpretation."
summary: A seven-question formative set to practise exact values, conversions, unit rates, percentages, and basic data interpretation.
permalink: /learning/problem-sets/math-foundations-check/
id: problem-math-foundations-check-010
content_type: problem-set
category: math-foundations
language: en
difficulty: beginner
tags: [mathematics, assessment, fractions, decimals, ratios, percentages, data-interpretation]
prerequisites: [math-fractions-operations-001, math-decimals-conversions-001, lesson-math-ratios-unit-rates-001, math-percentages-001, math-data-interpretation-001]
related_resources: [course-academic-math-foundations]
learning_objectives:
  - Select a suitable fraction, decimal, ratio, or percentage calculation for a question.
  - Show steps, units, rounding assumptions, and a reasonableness check.
content_status: drafted
review_status: pending
searchable: true
---

## Problem

Try each question before opening its hint or worked solution. Show your steps. Five final numeric values use deterministic checking; the fraction-conversion explanation and data-interpretation response use manual comparison because each combines multiple values with a written explanation. For real coursework, follow your instructor's methods and rounding rules. This is formative practice, not an official test or a substitute for a teacher's assessment.

## Example questions

The prompt, answer format, hint, skill route, derivation record, and solution below are generated from the shared assessment data. Manual responses are not scored or saved as correctness attempts.

<form data-quiz data-assessment-id="{{ site.data.math_foundations_assessment.id | escape }}">
  {% for question in site.data.math_foundations_assessment.questions %}
  {% assign mapped_lesson = site.pages | where: "id", question.lesson_id | first %}
  <fieldset class="quiz-question" data-question data-question-id="{{ question.id | escape }}" data-skill-ids="{{ question.skill_ids | join: ',' | escape }}" data-resource-id="{{ question.lesson_id | escape }}" data-resource-url="{{ mapped_lesson.url | relative_url }}" data-answer-format="{{ question.answer_format | escape }}" data-accepted-answers="{{ question.accepted_answers | join: '|' | escape }}">
    <legend><strong>{{ forloop.index }}.</strong> {{ question.question | escape }} <span class="difficulty-label">{{ question.difficulty | escape }}</span></legend>
    {% if question.answer_format == "manual" %}
    <label for="answer-{{ question.id | escape }}">Your written response for manual comparison</label>
    <textarea id="answer-{{ question.id | escape }}" name="{{ question.id | escape }}" rows="4" aria-describedby="hint-{{ question.id | escape }} feedback-{{ question.id | escape }}"></textarea>
    {% else %}
    <label for="answer-{{ question.id | escape }}">Your numeric answer</label>
    <input id="answer-{{ question.id | escape }}" name="{{ question.id | escape }}" type="text" inputmode="decimal" autocomplete="off" aria-describedby="hint-{{ question.id | escape }} feedback-{{ question.id | escape }}">
    {% endif %}
    <details id="hint-{{ question.id | escape }}"><summary>Hint</summary><p>{{ question.hint | escape }}</p></details>
    {% for mistake in question.common_mistakes %}<details><summary>Common mistake to avoid</summary><p>{{ mistake | escape }}</p></details>{% endfor %}
    {% for prerequisite_id in question.prerequisite_ids %}{% assign prerequisite_page = site.pages | where: "id", prerequisite_id | first %}{% if prerequisite_page %}<p>Prerequisite: <a href="{{ prerequisite_page.url | relative_url }}">{{ prerequisite_page.title | escape }}</a></p>{% endif %}{% endfor %}
    {% if mapped_lesson %}<p><a href="{{ mapped_lesson.url | relative_url }}">Review the related lesson: {{ mapped_lesson.title | escape }}</a></p>{% endif %}
    <p id="feedback-{{ question.id | escape }}" data-feedback aria-live="polite"></p>
    <details data-solution hidden><summary>Worked solution and method</summary><p>{{ question.solution | escape }}</p><p>{{ question.explanation | escape }}</p></details>
  </fieldset>
  {% endfor %}
  <p data-quiz-progress role="status" aria-live="polite">0 of {{ site.data.math_foundations_assessment.questions.size }} questions answered.</p>
  <button class="button" type="submit">Check answers and reveal methods</button>
  <p data-quiz-status role="status" aria-live="polite">Your numeric results stay in this browser if local storage is available. Written comparisons are never counted as correct or incorrect.</p>
  <section class="mastery-summary" data-mastery-summary aria-live="polite" aria-atomic="true" aria-label="Practice evidence"></section>
</form>

## Hints

Every question keeps its hint separate and collapsed until you request it.

## Reference solutions

Worked solutions open after submission. Compare the transformations and units with your own steps; numeric feedback alone does not assess the method.

## Self-review rubric

For each manual response, check that the conversion values agree and the denominator reasoning supports whether it terminates; for the data question, check the total, mean, sorted median, units, and zero-versus-missing explanation. Numeric feedback checks only the submitted value, not the reasoning or unit notation. Ask a teacher to review methods that differ from your class conventions.

## Next step

Review the lesson that matches any missed item in the [mathematics foundations course]({{ '/learning/courses/academic-foundations/' | relative_url }}). Then continue to the [linear-equation word-problems and modeling lesson]({{ '/learning/lessons/math-algebra-word-problems/' | relative_url }}) after completing the algebra foundations path.
