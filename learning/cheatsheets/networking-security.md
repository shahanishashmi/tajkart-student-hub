---
title: "Networking and security quick reference"
description: "Remember request layers and practical defensive defaults."
summary: Remember request layers and practical defensive defaults.
permalink: /learning/cheatsheets/networking-security/
id: cheatsheet-networking-security
content_type: cheatsheet
category: networking-and-security
language: en
difficulty: beginner
tags: [dns, tcp, http, tls, privacy, least-privilege]
prerequisites: [guide-computer-networks, guide-cybersecurity-basics]
learning_objectives: ["Trace a request and identify a basic trust boundary."]
content_status: drafted
review_status: pending
searchable: true
---

## Request path

URL → name resolution → network route → transport connection → TLS for HTTPS → application request/response. Troubleshoot the nearest failing step rather than assuming every page error is a network fault.

## Defensive defaults

- Use unique passwords stored in a trusted password manager; enable multi-factor authentication where available.
- Keep secrets out of source code, screenshots, and logs.
- Validate permissions on the server; hiding a user interface control is not access control.
- Validate input and encode output for its context.
- Use least privilege and update dependencies from trusted sources.
- Test only systems you own or have explicit permission to assess.

HTTPS requires both encryption and correct certificate/hostname validation. Do not disable certificate checks to make a connection appear to work.
