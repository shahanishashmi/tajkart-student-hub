---
title: "Computer architecture: how instructions use hardware"
description: "Connect machine instructions, registers, memory, and input/output devices."
summary: Connect machine instructions, registers, memory, and input/output devices.
permalink: /learning/guides/computer-architecture/
id: guide-computer-architecture
content_type: guide
category: computer-architecture
language: en
difficulty: beginner
tags: [architecture, cpu, memory, instruction-cycle]
prerequisites: [guide-programming-foundations]
learning_objectives:
  - Identify the roles of a processor, registers, memory, and input/output.
  - Describe a simplified fetch-decode-execute cycle.
  - Explain why caches and locality affect performance.
estimated_minutes: 35
content_status: drafted
review_status: pending
searchable: true
order: 9
---

## What this guide covers

Computer architecture describes how a computer's parts work together to execute instructions. A useful beginner view starts with a processor, main memory, storage, and devices, then asks how data moves among them.

## Concept path

1. Instructions and data are represented as bits.
2. Registers hold small values close to the processor while an instruction runs.
3. The simplified instruction cycle fetches an instruction, decodes it, and performs an operation.
4. Main memory is larger than registers but typically farther away; caches keep recently used data closer.
5. Storage keeps data when power is off; input/output controllers connect other devices.
6. Performance depends on work, memory access patterns, parallelism, and the hardware implementation.

## Worked analogy

Suppose a processor repeatedly sums values in a sequence. Reading adjacent elements may let a cache reuse nearby data. Looking up scattered values can cause more memory waits. The exact speed depends on hardware, language runtime, and workload, so measure the real program before optimizing.

## Common mistakes

- Saying that one architecture detail applies to every processor.
- Treating cache size as a direct promise of application speed.
- Assuming more cores automatically make a sequential task faster.
- Confusing persistent storage with the memory a running process uses.

## Practice and next steps

Draw a data path for a program that reads a file, adds two numbers, and prints the result. Label storage, memory, processor, and output. Then explain one reason the program might wait even when it performs very few arithmetic operations.
