---
layout: page
title: "Predict the output: a beginner code-reading quiz"
description: Four small questions with browser-side feedback and hints; no learner code is executed.
permalink: /learning/interactive-tutorials/quiz/
id: interactive-output-quiz-001
content_type: interactive
category: programming-fundamentals
language: en
difficulty: beginner
tags: [quiz, code-reading, python, output-prediction]
prerequisites: [python-variables-001, python-loops-001]
learning_objectives:
  - Trace assignments, conditions, indexes, and loop passes.
  - Predict an output before checking an answer.
estimated_minutes: 10
content_status: drafted
review_status: pending
searchable: true
---

Read each snippet and choose the output before selecting **Check answers**. A wrong answer is a prompt to trace the values one step at a time. The page compares a choice in your browser; it does not run learner-submitted code.

<form data-quiz data-assessment-id="{{ site.data.code_reading_assessment.id | escape }}">
  {% for question in site.data.code_reading_assessment.questions %}
  {% assign mapped_lesson = site.pages | where: "id", question.lesson_id | first %}
  <fieldset class="quiz-question" data-question data-question-id="{{ question.id | escape }}" data-skill-ids="{{ question.skill_ids | join: ',' | escape }}" data-resource-id="{{ question.lesson_id | escape }}" data-resource-url="{{ mapped_lesson.url | relative_url }}" data-answer-format="{{ question.answer_format | escape }}" data-accepted-answers="{{ question.accepted_answers | join: '|' | escape }}" data-answer="{{ question.accepted_answers | first | escape }}">
    <legend><strong>{{ forloop.index }}.</strong> {{ question.question | escape }} <span class="difficulty-label">{{ question.difficulty | escape }}</span></legend>
    <pre><code>{{ question.verification.code | escape }}</code></pre>
    {% for answer in question.choices %}
    <label><input type="radio" name="{{ question.id | escape }}" value="{{ answer | escape }}"> {{ answer | escape }}</label>
    {% endfor %}
    <details><summary>Hint</summary><p>{{ question.hint | escape }}</p></details>
    {% for mistake in question.common_mistakes %}
    <details><summary>Common mistake to avoid</summary><p>{{ mistake | escape }}</p></details>
    {% endfor %}
    {% if mapped_lesson %}<p><a href="{{ mapped_lesson.url | relative_url }}">Review the related lesson: {{ mapped_lesson.title | escape }}</a></p>{% endif %}
    {% for prerequisite_id in question.prerequisite_ids %}
      {% assign prerequisite_page = site.pages | where: "id", prerequisite_id | first %}
      {% if prerequisite_page %}<p>Prerequisite: <a href="{{ prerequisite_page.url | relative_url }}">{{ prerequisite_page.title | escape }}</a></p>{% endif %}
    {% endfor %}
    <details data-solution hidden><summary>Worked answer and method</summary><p>{{ question.solution | escape }}</p><p>{{ question.explanation | escape }}</p></details>
    <p data-feedback aria-live="polite"></p>
  </fieldset>
  {% endfor %}

  <p data-quiz-progress role="status" aria-live="polite">0 of {{ site.data.code_reading_assessment.questions.size }} questions answered.</p>
  <button class="button" type="submit">Check answers</button>
  <p data-quiz-status role="status" aria-live="polite">Choose one answer in each question.</p>
  <section class="mastery-summary" data-mastery-summary aria-live="polite" aria-atomic="true" aria-label="Practice evidence"></section>
</form>

## Next practice

Write down why each answer is correct, then solve the [original practice set]({{ '/learning/problem-sets/' | relative_url }}). If this page's script is unavailable, use the hints and work the snippets out by hand.
