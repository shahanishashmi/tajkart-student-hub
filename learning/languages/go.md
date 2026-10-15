---
title: "Go learning path"
description: "Learn Go through values, functions, slices, maps, errors, and small packages."
summary: Learn Go through values, functions, slices, maps, errors, and small packages.
permalink: /learning/languages/go/
id: language-path-go
content_type: guide
category: programming-languages
language: en
difficulty: beginner
tags: [go, packages, errors, concurrency]
prerequisites: []
learning_objectives:
  - Run a minimal Go program and explain its package entry point.
  - Use slices, maps, functions, and explicit error returns.
  - Add a test for a small function.
estimated_minutes: 50
content_status: drafted
review_status: pending
searchable: true
---

Go is a compiled language with built-in support for packages and concurrent tasks. Install the official toolchain for your platform and use the module and test commands documented for your project.

## First program

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, Go!")
}
```

Expected output: `Hello, Go!`.

## Learning path

Study declarations and types; conditions and loops; functions and multiple return values; arrays, slices, and maps; structs and methods; interfaces; packages; error values; tests; then goroutines and channels. Learn concurrency only after you can explain who owns shared state and how work stops.

## Common mistakes and practice

Appending to a slice can allocate a new backing array. A map lookup can return a zero value when a key is absent, so use the presence result when absence matters. Handle returned errors instead of discarding them. Avoid launching goroutines that have no cancellation or completion plan.

Write a function that totals non-negative session minutes and returns an error for a negative value. Test an empty slice and an invalid item. Then split input parsing from the calculation into separate functions.
