---
layout: page
title: "Project: browser flashcard quiz"
summary: Make a keyboard-friendly flashcard activity with predictable feedback.
permalink: /learning/projects/flashcard-quiz/
id: project-browser-flashcard-quiz
content_type: project
category: web-development
language: en
difficulty: beginner
tags: [javascript, html, accessibility, quiz, project]
prerequisites: [language-path-html-css, language-path-javascript-typescript]
learning_objectives: ["Build a local quiz interaction with labels, feedback, and edge-case handling."]
estimated_minutes: 150
content_status: drafted
review_status: pending
searchable: true
---

## Goal and prerequisites

Create a small page of original question/answer cards. Use only a local sample list; do not copy test-bank questions or course answer keys. Review the [web course]({{ '/learning/courses/web-development/' | relative_url }}).

## Requirements and sample behavior

Show one question, accept an answer, give a useful retry message, and allow the learner to move on. Empty input should not be marked correct. For a card asking “What does `=` do in Python?”, a correct answer explains assignment rather than comparison.

## Milestones

1. Write cards as local data with stable IDs.
2. Render one card and label the answer field.
3. Add checking and feedback with `textContent`; do not interpret learner text as HTML.
4. Add next-card and completion states; handle an empty card set.
5. Test keyboard use, reload behavior, and a narrow viewport.

## Testing and rubric

Test correct, incorrect, empty, and last-card behavior. Check that screen-reader users can find the question and hear feedback. Score 0–2 for correctness, keyboard flow, feedback, and maintainability. Extensions: shuffle cards with a reproducible seed or save anonymous progress locally with a clear reset control.
