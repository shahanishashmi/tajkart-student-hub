---
title: "Computer networks: follow a request across boundaries"
description: "Build a basic model of names, addresses, transport, and application protocols."
summary: Build a basic model of names, addresses, transport, and application protocols.
permalink: /learning/guides/computer-networks/
id: guide-computer-networks
content_type: guide
category: networking
language: en
difficulty: beginner
tags: [networking, dns, tcp, udp, http, tls]
prerequisites: [guide-programming-foundations]
learning_objectives:
  - Trace a web request from a hostname to an application response.
  - Distinguish transport delivery from application protocol meaning.
  - Use a layered model to narrow a connection problem.
estimated_minutes: 40
content_status: drafted
review_status: pending
searchable: true
order: 6
---

## What this guide covers

A network connects devices so software can exchange data. Layers are a reasoning aid: each layer has a job and communicates through defined interfaces. Real protocol stacks do not always fit a classroom diagram perfectly.

## Concept path

1. Addresses identify network interfaces; ports identify application endpoints on a host.
2. DNS resolves a name to address records that a client can use.
3. IP routes packets between networks. TCP provides an ordered byte stream; UDP sends independent datagrams without that stream guarantee.
4. TLS protects a connection when configured and validated correctly.
5. HTTP defines request methods, headers, status codes, and response bodies.
6. Troubleshoot from the nearest failing layer: local network, name resolution, connection, TLS, then application response.

## Worked trace

When a browser opens a page, it parses the URL, may resolve the host through DNS, establishes a transport connection, negotiates TLS for HTTPS, then sends an HTTP request. The server returns a status and content; the browser may request scripts, styles, and images separately. Caches and proxies can change which systems participate.

## Common mistakes

- Treating a domain name as the address itself.
- Saying TCP guarantees that an application successfully processed a message; it only concerns transport delivery.
- Treating HTTP status `200` as proof that the page's content is correct.
- Sharing real public IPs, credentials, or private request headers in a bug report.

## Practice and next steps

Draw the request path for a site that loads HTML but not its stylesheet. List one possible fault at DNS, connection, server routing, and browser cache. Use browser network tools on a site you are allowed to inspect, and avoid scanning systems without permission.
