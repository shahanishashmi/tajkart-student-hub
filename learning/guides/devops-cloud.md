---
title: "DevOps and cloud fundamentals: build, release, observe, recover"
description: "Understand the path from source code to a maintained service."
summary: Understand the path from source code to a maintained service.
permalink: /learning/guides/devops-cloud/
id: guide-devops-cloud
content_type: guide
category: devops-and-cloud
language: en
difficulty: beginner
tags: [devops, cloud, deployment, monitoring, containers]
prerequisites: [guide-software-engineering-testing, guide-web-development]
learning_objectives:
  - Describe a repeatable build and deployment pipeline.
  - Distinguish a container image from a running container.
  - Plan a basic health check, backup, and rollback.
estimated_minutes: 40
content_status: drafted
review_status: pending
searchable: true
order: 12
---

## What this guide covers

DevOps practice connects software changes to the work of running and maintaining a service. Cloud providers offer managed computing and storage, but the application still needs safe configuration, monitoring, and recovery.

## Concept path

1. Version source and dependencies so a build can be repeated.
2. Run validation before packaging a release.
3. Separate configuration and secrets from source code.
4. Deploy a known artifact and keep a rollback path.
5. Observe service health with useful logs, metrics, and alerts that avoid private data.
6. Back up important state and test restoration rather than assuming a backup works.

## Worked example

For a static site, a pipeline can check Markdown routes, build Jekyll, upload the generated files, and deploy only from the protected main branch. The deployed artifact should be the same artifact that passed the build. A static site has no application server to scale, but still needs dependency updates and a recovery plan.

## Common mistakes

- Putting tokens in a repository file or printing them in workflow logs.
- Treating a successful build as proof the deployed page is reachable.
- Using a container as a substitute for backups or monitoring.
- Adding a cloud service without accounting for cost, permissions, and maintenance.

## Practice and next steps

Draw your project pipeline from a pull request to production. Mark each check, credential boundary, and rollback step. Continue with the [deployment guide]({{ '/docs/DEPLOYMENT/' | relative_url }}) and [container quick reference]({{ '/learning/cheatsheets/containers-deployment/' | relative_url }}).
