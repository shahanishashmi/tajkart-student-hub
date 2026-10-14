---
title: "Operating systems: processes, memory, files, and permissions"
summary: Study the services an operating system provides to programs.
permalink: /learning/guides/operating-systems/
id: guide-operating-systems
content_type: guide
category: operating-systems
language: en
difficulty: beginner
tags: [operating-systems, processes, memory, files, permissions]
prerequisites: [guide-programming-foundations]
learning_objectives:
  - Distinguish a program file from a running process.
  - Explain why a process has an address space and resource handles.
  - Use least privilege when running tools and scripts.
estimated_minutes: 40
content_status: drafted
review_status: pending
searchable: true
order: 7
---

## What this guide covers

An operating system coordinates hardware and gives applications controlled services for running code, storing files, communicating, and sharing resources. Interfaces and details vary by operating system; this guide teaches a portable mental model.

## Concept path

1. A program is stored instructions; a process is one running instance with state.
2. The scheduler shares CPU time among runnable work.
3. Virtual memory gives a process an address space and helps isolate it from other processes.
4. File systems organize named data; permissions govern who can read or change it.
5. System calls cross from an application into operating-system services.
6. Processes communicate through pipes, sockets, files, or other OS facilities.

## Worked example

If two terminal windows run the same script, there are usually two process instances. They may read the same source file but have separate local variables and execution state. If both write to one output file, they can interfere unless the program coordinates writes.

## Common mistakes

- Assuming a process has unlimited memory or CPU time.
- Running a downloaded script with administrator privileges without understanding what it does.
- Treating a file path as portable across Windows, Linux, and macOS.
- Confusing a process ID with a permanent identity; IDs can be reused.

## Practice and revision

Run a harmless command that prints its process ID, start two copies, and compare them. Then list which data they share (the executable file) and which data they normally do not (their private process state). Use the documentation for your own operating system when you need exact commands.
