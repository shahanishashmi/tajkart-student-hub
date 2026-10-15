---
title: "Web development: connect structure, style, behavior, and HTTP"
description: "Understand the browser-facing pieces of a small accessible website."
summary: Understand the browser-facing pieces of a small accessible website.
permalink: /learning/guides/web-development/
id: guide-web-development
content_type: guide
category: web-development
language: en
difficulty: beginner
tags: [html, css, javascript, http, accessibility]
prerequisites: [guide-programming-foundations]
learning_objectives:
  - Use semantic HTML for page structure and controls.
  - Explain how CSS styles elements and JavaScript changes behavior.
  - Describe a browser request and server response at a basic level.
estimated_minutes: 40
content_status: drafted
review_status: pending
searchable: true
order: 5
---

## What this guide covers

A browser renders a document, applies styles, runs permitted scripts, and exchanges requests with servers. A useful beginner model separates three jobs: HTML describes meaning, CSS controls presentation, and JavaScript handles interaction.

## Who should study it

Start after you can read basic code and use a text editor. You can make a static page before learning a framework or server. Build the smallest page that answers a real question.

## Concept path

1. HTML headings, paragraphs, lists, links, landmarks, forms, and labels.
2. CSS selectors, box model, typography, layout, responsive rules, and focus states.
3. JavaScript values, functions, events, DOM selection, and state updates.
4. HTTP request/response, status codes, URLs, and browser developer tools.
5. Accessibility checks: keyboard operation, labels, contrast, zoom, and semantic structure.

## Worked example

```html
<label for="minutes">Study minutes</label>
<input id="minutes" type="number" min="0">
<button type="button" id="show">Show value</button>
<p id="result" aria-live="polite"></p>
```

The label names the field; the button has an explicit type; the live region can announce an updated result. JavaScript should read the input, handle an empty value, and update `#result` without moving keyboard focus unexpectedly.

## Common mistakes

- Choosing elements for appearance instead of meaning.
- Removing the keyboard focus outline without providing a visible replacement.
- Treating client-side validation as a security boundary for data sent to a server.
- Adding a framework before understanding the document and browser tools.

## Practice and next steps

Build a two-section personal learning page with one labeled form control. Test it with only the keyboard, zoom to 200%, and make the viewport narrow. Study the [web quick reference]({{ '/learning/cheatsheets/web/' | relative_url }}) after you can explain what each element contributes.
