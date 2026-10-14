---
title: "HTML and CSS learning path"
summary: Create semantic pages and responsive styles that remain usable with a keyboard and zoom.
permalink: /learning/languages/html-css/
id: language-path-html-css
content_type: guide
category: web-development
language: en
difficulty: beginner
tags: [html, css, responsive-design, accessibility]
prerequisites: []
learning_objectives:
  - Use HTML elements according to their meaning.
  - Apply CSS layout and responsive rules without hiding content.
  - Check labels, focus, zoom, and narrow viewport behavior.
estimated_minutes: 45
content_status: drafted
review_status: pending
searchable: true
---

HTML is a markup language for document structure; CSS describes how elements look and flow. Neither is a substitute for JavaScript when an interaction needs program logic.

## First page

Save a document with `<!doctype html>`, `<html lang="en">`, a `<head>` containing a character set and title, and a `<main>` containing one `<h1>` and a paragraph. Add a stylesheet with a readable font, content width, spacing, and a visible `:focus-visible` outline.

## Learning path

Use headings in order, paragraphs for text, lists for grouped items, and anchors for navigation. Label form controls explicitly. Learn CSS selectors, the box model, flex/grid layout, relative units, media queries, and custom properties. Test at narrow widths and 200% zoom rather than relying on one screenshot.

## Common mistakes

Do not use heading elements only to change font size. Do not create a button with a plain `div`. Avoid fixed widths that cause horizontal scrolling. Keep a focus indicator, sufficient text contrast, and alternative text for informative images.

## Practice project

Make a one-page study plan with three semantic sections and a labeled checkbox list. Check keyboard order, zoom, contrast, and a small viewport. Continue with the [web development guide]({{ '/learning/guides/web-development/' | relative_url }}).
