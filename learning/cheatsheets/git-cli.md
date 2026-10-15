---
title: "Git and command-line quick reference"
description: "Safe starter commands for inspecting, saving, and reviewing project changes."
summary: Safe starter commands for inspecting, saving, and reviewing project changes.
permalink: /learning/cheatsheets/git-cli/
id: cheatsheet-git-cli
content_type: cheatsheet
category: developer-tools
language: en
difficulty: beginner
tags: [git, command-line, version-control]
prerequisites: []
learning_objectives: ["Inspect a working tree and save a focused Git change safely."]
content_status: drafted
review_status: pending
searchable: true
---

## Inspect before changing

```text
git status --short --branch
git diff
git diff --check
```

These commands show branch/worktree state, content edits, and common whitespace errors. Review untracked files separately; ordinary `git diff` does not show their contents.

## Save a focused change

```text
git add path/to/file
git diff --cached
git commit -m "Describe the change"
```

Stage named files when possible, then inspect the staged diff before committing. A commit is local history; pushing publishes it to a remote. Do not use force-push or destructive cleanup as a routine fix.

## Shell safety

Quote paths that contain spaces. Check the current directory and resolved target before scripts modify files. Commands differ between Bash, PowerShell, and other shells; do not paste shell syntax into a different interpreter without checking it.
