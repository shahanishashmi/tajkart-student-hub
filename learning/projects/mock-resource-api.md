---
layout: page
title: "Project: mock learning-resource API client"
description: "Practise requests and error states against a local fixture instead of an invented live service."
summary: Practise requests and error states against a local fixture instead of an invented live service.
permalink: /learning/projects/mock-resource-api/
id: project-mock-resource-api-client
content_type: project
category: web-development
language: en
difficulty: intermediate
tags: [api, json, http, testing, project]
prerequisites: [language-path-javascript-typescript, guide-computer-networks]
learning_objectives: ["Parse a documented JSON response and handle loading, empty, invalid, and error states."]
estimated_minutes: 180
content_status: drafted
review_status: pending
searchable: true
---

## Goal and requirements

Build a client that reads a local JSON fixture representing learning resources. Each record has an ID, title, language, topic, and level. This project does not point to a fabricated public API or require a server.

## Milestones

1. Write the fixture schema and include three clearly fictional sample records.
2. Parse the fixture and reject a record missing a required field.
3. Filter records by topic and display a clear empty state.
4. Simulate loading and failure states using local test data.
5. If you later connect a real service, first verify its official endpoint, terms, authentication, rate limits, and data-handling rules.

## Example and rubric

Filtering for `web-development` returns only matching sample entries. Test empty fixture, malformed JSON, missing ID, and no match. Score 0–2 for schema validation, safe display, error feedback, and repeatable tests. Do not send API keys to browser code or commit them to Git.
