---
title: "JavaScript and TypeScript quick reference"
description: "Common syntax for values, arrays, functions, and safe DOM updates."
summary: Common syntax for values, arrays, functions, and safe DOM updates.
permalink: /learning/cheatsheets/javascript-typescript/
id: cheatsheet-javascript-typescript
content_type: cheatsheet
category: web-development
language: en
difficulty: beginner
tags: [javascript, typescript, arrays, dom]
prerequisites: [language-path-javascript-typescript]
learning_objectives: ["Use a function and a type annotation while keeping runtime input checks explicit."]
content_status: drafted
review_status: pending
searchable: true
---

```javascript
const topics = ["HTML", "CSS", "JavaScript"];
const matching = topics.filter((topic) => topic.startsWith("J"));
console.log(matching);
```

Expected output: `["JavaScript"]`. `const` prevents rebinding the name; it does not make an array's contents immutable.

```typescript
function remaining(total: number, read: number): number {
  return total - read;
}
```

Types help detect some mistakes during development. Validate data at runtime when it comes from a form, file, network, or other untrusted boundary. Use `textContent` for plain text updates; do not treat user text as trusted HTML.
