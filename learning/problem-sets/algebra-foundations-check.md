---
layout: lesson
title: "Algebra foundations: formative self-check"
description: "A ten-question practice set for expressions, substitution, one-step equations, and introductory two-step equations."
summary: A ten-question practice set for expressions, substitution, one-step equations, and introductory two-step equations.
permalink: /learning/problem-sets/algebra-foundations-check/
id: problem-algebra-foundations-check-011
content_type: problem-set
category: math-foundations
language: en
difficulty: beginner
tags: [mathematics, algebra, practice, assessment, equations]
prerequisites: [math-algebra-expressions-001, math-algebra-one-step-001, math-algebra-two-step-001]
related_resources: [course-algebra-foundations]
learning_objectives:
  - Combine like terms and evaluate a linear expression by substitution.
  - Solve one-step and introductory two-step equations and verify their solutions.
  - Use an explanation and a linked skill to decide what to review after an error.
estimated_minutes: 25
content_status: drafted
review_status: pending
searchable: true
---

This is a formative self-check, not an official exam, grade, or credential. It compares answers using the format and accepted-answer set specified for each question; it does not interpret algebraic work or award partial credit. Show your steps on paper, then use the explanations to check the reasoning.

## Problem statement

Work through each question in the generated form. Questions cover combining like terms, substitution, one-step equations, two-step equations, negative and fractional values, and a zero-coefficient special case.

## Example questions

For example, solve `2y + 1 = 4` by subtracting 1 from each side and then dividing by 2. The exact result is `3/2`; this question explicitly permits `1.5` as an alternative.

## Hints

Each question keeps its hint collapsed until you choose to open it. Try a method first, then use the prompt to locate the next step.

## Worked solutions

After checking a non-empty answer, open that question's worked solution and compare the transformations with your own. A matching final value does not replace a valid method.

<form data-quiz data-assessment-id="{{ site.data.algebra_assessment.id | escape }}">
  {% for question in site.data.algebra_assessment.questions %}
  <fieldset class="quiz-question" data-question data-question-id="{{ question.id | escape }}" data-skill-ids="{{ question.skill_ids | join: ',' | escape }}" data-lesson-id="{{ question.lesson_id | escape }}" data-answer-format="{{ question.answer_format | escape }}" data-accepted-answers="{{ question.accepted_answers | join: '|' | escape }}">
    <legend><strong>{{ forloop.index }}.</strong> {{ question.question | escape }} <span class="difficulty-label">{{ question.difficulty | escape }}</span></legend>
    <label for="answer-{{ question.id | escape }}">Your answer</label>
    <input id="answer-{{ question.id | escape }}" name="{{ question.id | escape }}" type="text" inputmode="text" autocomplete="off" aria-describedby="hint-{{ question.id | escape }} feedback-{{ question.id | escape }}">
    <details id="hint-{{ question.id | escape }}"><summary>Hint</summary><p>{{ question.hint | escape }}</p></details>
    <p id="feedback-{{ question.id | escape }}" data-feedback aria-live="polite"></p>
    <details data-solution hidden><summary>Worked solution and method</summary><p>{{ question.solution | escape }}</p><p>{{ question.explanation | escape }}</p></details>
  </fieldset>
  {% endfor %}
  <p data-quiz-progress role="status" aria-live="polite">0 of {{ site.data.algebra_assessment.questions.size }} questions answered.</p>
  <button class="button" type="submit">Check answers</button>
  <p data-quiz-status role="status" aria-live="polite">Your results stay in this browser if local storage is available.</p>
  <section class="mastery-summary" data-mastery-summary aria-live="polite" aria-atomic="true" aria-label="Practice evidence"></section>
</form>

## How to use the result

Try each question before opening its hint. After checking, compare the steps and use the lesson link suggested for any missed skill. Each attempt is counted only when an answer is present. The optional browser-local record is not synced to another device; a small number of attempts is not enough evidence to call a skill mastered.

## Further learning

Return to the [algebra foundations path]({{ '/learning/courses/algebra-foundations/' | relative_url }}) or the [broader mathematics foundations route]({{ '/learning/courses/academic-foundations/' | relative_url }}). These Tajkart materials remain drafts pending a mathematics educator's review.
