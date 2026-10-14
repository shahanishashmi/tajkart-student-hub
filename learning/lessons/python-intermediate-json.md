---
layout: lesson
title: Read and write local JSON data in Python
summary: Persist structured records while handling missing files and malformed content explicitly.
permalink: /learning/lessons/python-intermediate-json/
id: python-intermediate-json-001
content_type: lesson
category: programming-languages
language: en
difficulty: intermediate
tags: [python, json, files, exceptions]
prerequisites: [python-intermediate-validation-001]
related_resources: [language-path-python, course-python-intermediate-study-log]
learning_objectives:
  - Read and write UTF-8 JSON using the standard library.
  - Treat a missing first-run file differently from malformed JSON.
  - Validate decoded values before using them as application records.
estimated_minutes: 40
content_status: drafted
review_status: pending
searchable: true
order: 9
topic: Python
level: Intermediate
reading_time: 14
---

## Learning objectives

After this lesson, you can save a list of records as JSON, load it again, and explain how the program responds when the file is missing or invalid.

## Prerequisites

You should know how to validate function inputs and handle an expected exception. Review [function contracts]({{ '/learning/lessons/python-intermediate-validation/' | relative_url }}) first. Use sample data only; do not place private student information in a practice file.

## Read a file that may not exist yet

`json.loads` parses text, while `Path.read_text` reads the file. A missing file is a normal first-run condition; malformed JSON is a different problem and should remain visible.

```python
import json
from pathlib import Path

path = Path("sessions.json")
try:
    records = json.loads(path.read_text(encoding="utf-8"))
except FileNotFoundError:
    records = []
print(len(records))
```

Expected output: `0` when `sessions.json` does not exist. If the file exists but contains invalid JSON, `json.JSONDecodeError` is raised; do not silently replace that data with an empty list.

## Save a structured value

`json.dumps` converts supported Python values to text. The newline and indentation make a small practice file easier to inspect by hand.

```python
import json
from pathlib import Path

path = Path("sessions.json")
records = [{"topic": "Python", "minutes": 25}]
path.write_text(json.dumps(records, indent=2) + "\n", encoding="utf-8")
loaded = json.loads(path.read_text(encoding="utf-8"))
print(loaded[0]["topic"])
```

Expected output: `Python`. This simple example overwrites the named file. For tests, use a temporary directory; do not experiment on a file containing information you need to keep.

## Common mistakes

- Treating malformed JSON as an empty file and losing the chance to recover the original.
- Assuming decoded JSON has the expected shape or value types.
- Omitting an explicit encoding and getting different text behavior across systems.
- Saving credentials, private records, or real learner histories in a public project.

## Practice

1. Load a missing file as an empty list. **Hint:** catch only `FileNotFoundError` around the read.
2. Write and read two sample records. **Hint:** compare the decoded Python value with the original list.
3. Reject a top-level JSON object when the application requires a list of sessions. **Hint:** validate the decoded value before looping over it.

Test the missing-file case, valid empty data, valid records, malformed JSON, and an unexpected record shape in a temporary directory.

## Next steps

Add tests and separate the command-line entry point from reusable functions in [organizing and testing a Python program]({{ '/learning/lessons/python-intermediate-testing/' | relative_url }}). Then complete the [local study-log project]({{ '/learning/projects/python-study-log/' | relative_url }}).
