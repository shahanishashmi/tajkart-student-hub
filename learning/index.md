---
layout: page
title: Learning Library
description: Search original lessons, guides, courses, projects, career guidance, and practice by topic, language, type, and level.
permalink: /learning/
---

Start with a question you want to answer or a skill you want to practise. Search covers only Tajkart-authored resources and category indexes explicitly marked for discovery. It runs in your browser from a static JSON file; no search query is sent to a server.

## Search learning resources

<div class="resource-search" data-index-url="{{ '/search-index.json' | relative_url }}">
  <label for="resource-query"><strong>Search titles, descriptions, tags, and topics</strong></label>
  <input id="resource-query" class="search-box" type="search" placeholder="Try Python, databases, testing, or interviews" autocomplete="off">
  <div class="search-filters">
    <div><label for="filter-type">Resource type</label><select id="filter-type" class="search-box"><option value="">All types</option></select></div>
    <div><label for="filter-category">Topic</label><select id="filter-category" class="search-box"><option value="">All topics</option></select></div>
    <div><label for="filter-language">Content language</label><select id="filter-language" class="search-box"><option value="">All languages</option></select></div>
    <div><label for="filter-difficulty">Difficulty</label><select id="filter-difficulty" class="search-box"><option value="">All levels</option></select></div>
    <div><label for="filter-origin">Content source</label><select id="filter-origin" class="search-box"><option value="">All sources</option></select></div>
    <div><label for="sort-results">Sort results</label><select id="sort-results" class="search-box"><option value="relevance">Relevance</option><option value="title">Title</option><option value="type">Type</option><option value="difficulty">Difficulty</option></select></div>
  </div>
  <p id="search-status" class="search-status" role="status" aria-live="polite">Loading learning resources…</p>
  <ul id="search-results" class="search-results" aria-label="Learning resource results"></ul>
</div>

## Browse by format

- [Programming foundations lessons]({{ '/learning/lessons/python-variables/' | relative_url }})
- [Subject guides]({{ '/learning/subjects/' | relative_url }})
- [Programming language paths]({{ '/learning/languages/' | relative_url }})
- [Courses and study plans]({{ '/learning/courses/' | relative_url }})
- [Books and reading guides]({{ '/learning/books/' | relative_url }})
- [Cheatsheets]({{ '/learning/cheatsheets/' | relative_url }})
- [Interactive tutorials]({{ '/learning/interactive-tutorials/' | relative_url }})
- [Problem sets]({{ '/learning/problem-sets/' | relative_url }})
- [Projects and playgrounds]({{ '/learning/projects/' | relative_url }})
- [Podcasts and screencasts]({{ '/learning/podcasts-screencasts/' | relative_url }})

Search results describe published work, not a promise that every subject has a complete course. See the [content progress report]({{ '/docs/CONTENT_PROGRESS/' | relative_url }}) for honest coverage status.
