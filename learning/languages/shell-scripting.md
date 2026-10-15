---
title: "Shell scripting learning path"
description: "Automate repeatable file and command-line tasks with careful quoting and checks."
summary: Automate repeatable file and command-line tasks with careful quoting and checks.
permalink: /learning/languages/shell-scripting/
id: language-path-shell
content_type: guide
category: programming-languages
language: en
difficulty: beginner
tags: [shell, bash, command-line, automation]
prerequisites: []
learning_objectives:
  - Run a script with a clear interpreter and predictable inputs.
  - Quote paths and check command failures.
  - Avoid destructive operations on unverified paths.
estimated_minutes: 40
content_status: drafted
review_status: pending
searchable: true
---

Shells connect commands and manage files and processes. Bash and PowerShell have different syntax; first identify the shell your environment actually uses. A shell script is executable automation, so review every command before running it.

## First Bash example

```bash
#!/usr/bin/env bash
set -eu
name="Amina"
printf 'Hello, %s!\\n' "$name"
```

Expected output: `Hello, Amina!`. `set -e` changes how failures stop a script; it is useful but not a substitute for checking critical commands and their inputs.

## Learning path

Learn navigation and quoting; variables and arguments; exit codes; pipes and redirection; conditions and loops; functions; file tests; and safe cleanup. Then add logging and tests using temporary directories. Prefer commands that explain their target before changing or deleting data.

## Common mistakes

Unquoted variables can split paths containing spaces. `rm -rf` with a computed path can delete unintended files. A pipeline may hide a failure unless the shell and commands are configured to propagate it. Never paste an unfamiliar network script into a privileged shell.

## Practice project

Write a script that lists Markdown files under a chosen study folder and counts them without modifying any file. Test a path with spaces and a missing folder. Add a dry-run mode before any future script that would change files.
