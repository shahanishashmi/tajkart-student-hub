---
title: "HTML, CSS, and HTTP quick reference"
summary: Short reminders for semantic pages, responsive styles, and request/response basics.
permalink: /learning/cheatsheets/web/
id: cheatsheet-html-css-http
content_type: cheatsheet
category: web-development
language: en
difficulty: beginner
tags: [html, css, http, accessibility]
prerequisites: [language-path-html-css]
learning_objectives: ["Select semantic markup and distinguish common HTTP request/response fields."]
content_status: drafted
review_status: pending
searchable: true
---

## HTML and CSS

```html
<label for="topic">Topic</label>
<input id="topic" name="topic">
```

```css
.content { max-width: 70ch; margin-inline: auto; }
:focus-visible { outline: 3px solid currentColor; outline-offset: 3px; }
```

Use elements for their meaning; keep a visible keyboard focus; test reflow and text enlargement. Prefer logical CSS properties such as `margin-inline` for right-to-left layouts.

## HTTP

- A request has a method, target URL, headers, and sometimes a body.
- A response has a status code, headers, and sometimes a body.
- `GET` is for retrieval; `POST` often submits or creates data; exact behavior depends on the API contract.
- `404` means a requested resource was not found; it does not explain why by itself.
- HTTPS protects data in transit only when the certificate and hostname are correctly validated.
