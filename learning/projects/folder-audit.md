---
layout: page
title: "Project: read-only folder audit"
description: "Write a report that counts and classifies files without modifying them."
summary: Write a report that counts and classifies files without modifying them.
permalink: /learning/projects/folder-audit/
id: project-read-only-folder-audit
content_type: project
category: developer-tools
language: en
difficulty: beginner
tags: [automation, shell, python, file-safety]
prerequisites: [language-path-shell]
learning_objectives: ["Inspect files under an explicit root and report findings without destructive side effects."]
estimated_minutes: 120
content_status: drafted
review_status: pending
searchable: true
---

## Goal

Create a local command-line report of file counts by extension under a folder you own. The first version is read-only: it must not rename, delete, upload, or modify files.

## Requirements and example

Given three `.md` files and one `.py` file, report totals `md: 3` and `py: 1`. If the folder does not exist, print an error and exit with a non-zero status. Skip symbolic links unless you explicitly decide how to handle them.

## Milestones

1. Accept one root directory and verify it exists.
2. Walk files and count extensions case-insensitively.
3. Sort output so two runs on the same tree are easy to compare.
4. Test an empty directory, a path with spaces, a file with no extension, and a missing path.
5. Review the code to confirm that it only reads metadata.

## Evaluation

Score 0–2 for correct counts, safe behavior, useful error handling, and tests. Do not add a cleanup mode. If you later add any modifying action, require a dry run, explicit destination checks, and a separate review.
