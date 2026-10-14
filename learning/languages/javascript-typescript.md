---
title: "JavaScript and TypeScript learning path"
summary: Learn browser behavior in JavaScript, then add TypeScript's static checks where useful.
permalink: /learning/languages/javascript-typescript/
id: language-path-javascript-typescript
content_type: guide
category: programming-languages
language: en
difficulty: beginner
tags: [javascript, typescript, browser, web-development]
prerequisites: []
learning_objectives:
  - Run JavaScript in a browser and use values, functions, and arrays.
  - Handle a browser event without losing keyboard access.
  - Explain what TypeScript checks before JavaScript runs.
estimated_minutes: 60
content_status: drafted
review_status: pending
searchable: true
---

JavaScript is the browser's built-in programming language and is also used in server and tooling environments. TypeScript adds type analysis and compiles to JavaScript; browsers do not execute TypeScript syntax directly. Learn JavaScript fundamentals before adding a framework.

## First programs

In a browser script, `console.log("Hello, JavaScript!");` prints a message in developer tools. A TypeScript equivalent can declare `const greeting: string = "Hello, TypeScript!";` and log it after a TypeScript toolchain compiles it.

## Learning path

Learn `const` and `let`, primitive values, arrays and objects, conditions, loops, functions, modules, errors, and asynchronous work. Then learn DOM selection, events, forms, accessible updates, and browser debugging. Add TypeScript types for function inputs, returned values, and data crossing a boundary.

## Common mistakes and checks

`===` avoids many implicit-conversion surprises. A DOM selector can return no element; handle that case. An event handler should not rely only on color or pointer input. TypeScript can catch some mistakes before execution, but it does not validate untrusted runtime data on its own.

## Practice project

Build a small page that filters a local list of learning topics. Provide a labeled search field, an empty state, and a status announcement. First test with plain JavaScript; add TypeScript only if the project benefits from its extra checks. Continue with the [web development guide]({{ '/learning/guides/web-development/' | relative_url }}).
