---
title: "System design: define boundaries before choosing tools"
description: "Turn a product need into components, data flow, and explicit trade-offs."
summary: Turn a product need into components, data flow, and explicit trade-offs.
permalink: /learning/guides/system-design/
id: guide-system-design
content_type: guide
category: software-architecture
language: en
difficulty: intermediate
tags: [system-design, architecture, reliability, trade-offs]
prerequisites: [guide-web-development, guide-databases-sql]
learning_objectives:
  - Clarify functional behavior and constraints before selecting components.
  - Draw a data flow and identify trust and failure boundaries.
  - Explain one trade-off with its operating cost and failure mode.
estimated_minutes: 45
content_status: drafted
review_status: pending
searchable: true
order: 10
---

## What this guide covers

System design is the work of choosing components and boundaries that meet a set of requirements. A diagram is useful only if it helps explain data, responsibilities, failure handling, and trade-offs. Start with the smallest system that can satisfy the need.

## Concept path

1. Write functional requirements and measurable constraints separately.
2. Estimate scale only when the use case provides a reason; label assumptions.
3. Sketch clients, services, data stores, and external dependencies.
4. Trace one request and identify authentication, validation, and error responses.
5. Consider failure, backup, observability, privacy, and recovery.
6. Compare alternatives by cost, complexity, latency, reliability, and team ability.

## Worked example: a study-session tracker

Requirements: create a session, list a learner's sessions, and calculate total minutes. A first design can store each session with an owner ID, start time, and duration. Validate duration and ownership at the boundary. If one database is sufficient, adding a queue and several services increases operational work without solving a stated problem.

## Common mistakes

- Starting with a fashionable database or cloud service before writing the requirements.
- Treating a diagram as complete without discussing permissions and failure.
- Quoting throughput or latency without assumptions and a measurement method.
- Ignoring backups, deletion, and who can access student information.

## Practice and next steps

Draw the smallest architecture for a local-only tracker and a hosted multi-user version. Mark what changes, what data is personal, and one failure case for each. Continue only when a requirement needs the additional component.
