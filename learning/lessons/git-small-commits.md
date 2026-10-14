---
layout: lesson
title: Save project progress with Git commits
summary: Inspect changed files, stage selected work, and write a useful commit message.
permalink: /learning/lessons/git-small-commits/
id: git-small-commits-001
content_type: lesson
category: developer-tools
language: en
difficulty: beginner
tags: [git, version-control, code-review, command-line]
prerequisites: []
related_resources: [guide-software-engineering-testing, project-reading-tracker, course-programming-foundations-four-weeks]
learning_objectives:
  - Inspect unstaged and staged changes separately.
  - Create a focused commit with a descriptive summary.
estimated_minutes: 20
content_status: drafted
review_status: pending
searchable: true
order: 4
topic: Git
level: Beginner
reading_time: 9
---

## Learning objectives

Explain what a commit records, inspect a working tree, and save a focused change with a clear message.

## Prerequisites

Git must be installed. Open a terminal inside a project folder. If the folder is not already a Git repository, run `git init` once.

## A commit records a project snapshot

Git tracks changes over time. A commit records selected file changes together with a message; it does not automatically upload files to a website.

```sh
git status
git add README.md
git diff --staged
git commit -m "Document project setup"
```

`git status` shows changed and untracked files. `git add` stages one chosen file. `git diff --staged` lets you review what will be saved. The commit message says what the change accomplishes.

Expected result: Git creates a commit and reports the files and lines it recorded. Exact wording varies by Git version.

## Keep commits understandable

Prefer a small commit that describes one coherent change. For example, separate a new lesson from an unrelated visual redesign. A focused history makes it easier to review work and find when a change was introduced.

## Common mistakes

- Running Git from the wrong directory. Check `git status` before staging.
- Using `git add .` without reviewing the changed files. It can stage unrelated work or generated files.
- Writing messages such as `stuff` or `update`. Describe the outcome in a few words.
- Thinking `git commit` publishes to GitHub. Sharing changes usually requires a separate push to a configured remote.
- Staging passwords or API keys. Remove secrets and rotate them if they were already shared.

## Practice

1. Create a text file, inspect `git status`, and stage only that file.
2. Review staged changes before committing.
3. Edit the file again and explain why the second edit is not part of the earlier commit until staged and committed.

Hint: repeat `git status` after each step and observe how the file moves between untracked, staged, and modified states.

## Further learning within Tajkart

Follow the [study plans]({{ '/learning/courses/' | relative_url }}) to pair version control with a small portfolio project.
