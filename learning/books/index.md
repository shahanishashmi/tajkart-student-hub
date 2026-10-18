---
layout: page
title: Books and subject reading guides
description: Learn to select, read, practise, and revise from lawful technical material.
permalink: /learning/books/
id: guide-books-reading-method
content_type: guide
category: study-skills
language: en
difficulty: beginner
tags: [reading, books, revision]
prerequisites: []
learning_objectives:
  - Use active reading to turn a chapter into recall and practice.
  - Choose material using its audience, edition, and lawful access terms.
content_status: drafted
review_status: pending
searchable: true

---

Tajkart does not host third-party books or reproduce a catalogue of external titles. The guides below help you study a subject with material you lawfully obtain from an author, publisher, library, or course provider.

## Browse the copied book indexes

The links below open the 48 Markdown index files copied from the pinned Free Programming Books snapshot into the Tajkart repository. They are reference lists of external links, not reviewed or approved book recommendations. A source-list locale describes the index file and does not verify the language of every linked work. Use [Tajkart's unverified book-candidate search]({{ '/learning/?reference=1&source_category=books' | relative_url }}) to search the extracted destinations.

{% assign book_source_category = site.data.reference_resource_facets.source_categories | where: "id", "books" | first %}
{% if book_source_category %}
<ul class="book-index-list">
  {% for source_list in book_source_category.lists %}
  <li><a href="{{ site.data.books_mirror.repository }}/blob/{{ site.data.books_mirror.revision }}/{{ source_list.path }}">{{ source_list.source_list_locale | default: "No locale label" }} — {{ source_list.path }}</a> ({{ source_list.source_entry_appearances }} listed links)</li>
  {% endfor %}
</ul>
{% endif %}

## Reading method

Set one question before a chapter. Skim headings and examples, then write a short explanation from memory after reading. Run code examples where appropriate, change one input, and solve a related task without looking. Record a book's title, edition, and page if you need to cite a fact.

## Original subject guides

- [Programming foundations]({{ '/learning/guides/programming-foundations/' | relative_url }})
- [Data structures and algorithms]({{ '/learning/guides/data-structures-algorithms/' | relative_url }})
- [Object-oriented programming]({{ '/learning/guides/object-oriented-programming/' | relative_url }})
- [Databases and SQL]({{ '/learning/guides/databases-and-sql/' | relative_url }})
- [Web development]({{ '/learning/guides/web-development/' | relative_url }})
- [Computer networks]({{ '/learning/guides/computer-networks/' | relative_url }})
- [Operating systems]({{ '/learning/guides/operating-systems/' | relative_url }})
- [Software engineering and testing]({{ '/learning/guides/software-engineering-testing/' | relative_url }})
- [Computer architecture]({{ '/learning/guides/computer-architecture/' | relative_url }})
- [System design]({{ '/learning/guides/system-design/' | relative_url }})
- [Cybersecurity fundamentals]({{ '/learning/guides/cybersecurity-basics/' | relative_url }})
- [DevOps and cloud]({{ '/learning/guides/devops-cloud/' | relative_url }})

## Choose material responsibly

Check the author's or publisher's own page for the edition, intended audience, format, and terms. Prefer a source that explains prerequisites and includes exercises you can attempt. A reference repository's licence does not automatically apply to any work linked from it. See [Tajkart's content policy]({{ '/docs/CONTENT_POLICY/' | relative_url }}) before contributing external material.
