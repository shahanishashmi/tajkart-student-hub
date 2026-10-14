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

<form data-quiz>
  <fieldset class="quiz-question" data-question data-answer="6">
    <legend><strong>1. Assignment</strong>: what does `print(score)` display?</legend>
    <pre><code>score = 4
score = score + 2
print(score)</code></pre>
    <label><input type="radio" name="quiz-1" value="4"> 4</label>
    <label><input type="radio" name="quiz-1" value="6"> 6</label>
    <label><input type="radio" name="quiz-1" value="42"> 42</label>
    <details><summary>Hint</summary><p>The old value is read before the new value is assigned.</p></details>
    <p data-feedback aria-live="polite"></p>
  </fieldset>

  <fieldset class="quiz-question" data-question data-answer="3">
    <legend><strong>2. Loop passes</strong>: how many times does the body run?</legend>
    <pre><code>for day in ["Mon", "Tue", "Wed"]:
    print(day)</code></pre>
    <label><input type="radio" name="quiz-2" value="2"> 2</label>
    <label><input type="radio" name="quiz-2" value="3"> 3</label>
    <label><input type="radio" name="quiz-2" value="4"> 4</label>
    <details><summary>Hint</summary><p>Count the items in the sequence.</p></details>
    <p data-feedback aria-live="polite"></p>
  </fieldset>

  <fieldset class="quiz-question" data-question data-answer="true">
    <legend><strong>3. Condition</strong>: which branch runs?</legend>
    <pre><code>if 5 &gt; 3:
    result = "true"
else:
    result = "false"
print(result)</code></pre>
    <label><input type="radio" name="quiz-3" value="true"> true</label>
    <label><input type="radio" name="quiz-3" value="false"> false</label>
    <details><summary>Hint</summary><p>Compare the two numbers before reading the branch.</p></details>
    <p data-feedback aria-live="polite"></p>
  </fieldset>

  <fieldset class="quiz-question" data-question data-answer="7">
    <legend><strong>4. List index</strong>: what does `print(values[0])` display?</legend>
    <pre><code>values = [7, 9]
print(values[0])</code></pre>
    <label><input type="radio" name="quiz-4" value="0"> 0</label>
    <label><input type="radio" name="quiz-4" value="7"> 7</label>
    <label><input type="radio" name="quiz-4" value="9"> 9</label>
    <details><summary>Hint</summary><p>Python list indexes begin at zero.</p></details>
    <p data-feedback aria-live="polite"></p>
  </fieldset>

  <p data-quiz-progress role="status" aria-live="polite">0 of 4 questions answered.</p>
  <button class="button" type="submit">Check answers</button>
  <p data-quiz-status role="status" aria-live="polite">Choose one answer in each question.</p>
</form>

## Next practice

Write down why each answer is correct, then solve the [original practice set]({{ '/learning/problem-sets/' | relative_url }}). If this page's script is unavailable, use the hints and work the snippets out by hand.
