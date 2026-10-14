---
title: "Containers and deployment quick reference"
summary: Distinguish images, containers, configuration, and a reproducible release.
permalink: /learning/cheatsheets/containers-deployment/
id: cheatsheet-containers-deployment
content_type: cheatsheet
category: devops-and-cloud
language: en
difficulty: beginner
tags: [containers, deployment, releases, secrets]
prerequisites: [guide-devops-cloud]
learning_objectives: ["Describe the difference between a container image and a running instance."]
content_status: drafted
review_status: pending
searchable: true
---

- An image is a packaged template; a container is a running instance created from it.
- A container does not automatically provide durable storage, backups, or monitoring.
- Pin and update dependencies deliberately; record the image/source used for a release.
- Keep credentials outside the image and repository; grant only required permissions.
- Build once, test that artifact, then deploy the same artifact.
- Define health checks, logs that avoid private values, rollback steps, and backup restoration.
- For static sites, a container may add complexity without helping; choose the simplest host that meets the need.
