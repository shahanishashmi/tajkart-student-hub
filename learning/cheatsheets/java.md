---
title: "Java quick reference"
description: "Quick Java reminders for methods, collections, equality, and exceptions, with small code examples."
summary: Compact reminders for Java methods, collections, equality, and exceptions.
permalink: /learning/cheatsheets/java/
id: cheatsheet-java
content_type: cheatsheet
category: programming-languages
language: en
difficulty: beginner
tags: [java, methods, collections, exceptions]
prerequisites: [language-path-java]
learning_objectives: ["Read a small Java method and choose equality and collection operations deliberately."]
content_status: drafted
review_status: pending
searchable: true
---

```java
import java.util.List;

class Example {
    static int total(List<Integer> values) {
        int sum = 0;
        for (int value : values) sum += value;
        return sum;
    }
}
```

- Use `.equals` to compare string values; `==` compares object identity for references.
- Choose a collection based on required ordering and lookup operations.
- Handle exceptions at a boundary where the program can give a useful response.
- Keep methods small enough to explain and test.
- Add tests for empty, typical, and boundary inputs; check the project's configured Java version before using newer syntax.
