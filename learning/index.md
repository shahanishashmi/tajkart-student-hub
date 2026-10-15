---
layout: page
title: Learning Library
description: Search original lessons, guides, courses, projects, career guidance, and practice by topic, language, type, and level.
permalink: /learning/
---

Start with a question you want to answer or a skill you want to practise. Visit the [Explore resources directory]({{ '/explore/' | relative_url }}) to browse student-facing categories. By default, search covers Tajkart-authored resources and category indexes explicitly marked for discovery. You can optionally include unverified link candidates imported from the attributed Free Programming Books index. Those candidates have not been checked by Tajkart for availability, quality, access terms, or rights. Search runs in your browser; no query is sent to a server.

Not sure where to start? Use the [student learning route]({{ '/getting-started/' | relative_url }}) to connect a goal to existing courses, practice, projects, and career guides.

## Search learning resources

<div class="resource-search" data-index-url="{{ '/search-index.json' | relative_url }}" data-reference-index-url="{{ '/data/reference_resources.json' | relative_url }}">
  <label for="resource-query"><strong>Search titles, topics, and source notes where available</strong></label>
  <input id="resource-query" class="search-box" type="search" placeholder="Try Python, databases, testing, or interviews" autocomplete="off">
  <div class="search-filters">
    <div><label for="filter-type">Resource type</label><select id="filter-type" class="search-box"><option value="">All types</option></select></div>
    <div><label for="filter-category">Topic</label><select id="filter-category" class="search-box"><option value="">All topics</option></select></div>
    <div><label for="filter-source-category">Reference source list category</label><select id="filter-source-category" class="search-box"><option value="">All source categories</option></select></div>
    <div><label for="filter-source-topic">Reference source topic path</label><select id="filter-source-topic" class="search-box"><option value="">All reference topic paths</option></select></div>
    <div><label for="filter-tag">Skill or technology</label><select id="filter-tag" class="search-box"><option value="">All skills</option></select></div>
    <div><label for="filter-language">Content language</label><select id="filter-language" class="search-box"><option value="">All languages</option></select></div>
    <div><label for="filter-source-locale">Reference list locale</label><select id="filter-source-locale" class="search-box"><option value="">All reference list locales</option></select></div>
    <div><label for="filter-difficulty">Difficulty</label><select id="filter-difficulty" class="search-box"><option value="">All levels</option></select></div>
    <div><label for="filter-origin">Content source</label><select id="filter-origin" class="search-box"><option value="">All sources</option></select></div>
    <div><label for="sort-results">Sort results</label><select id="sort-results" class="search-box"><option value="relevance">Relevance</option><option value="title">Title</option><option value="type">Type</option><option value="difficulty">Difficulty</option></select></div>
  </div>
  <p><label><input id="include-reference-candidates" type="checkbox"> Include unverified reference-list candidates</label></p>
  <p class="search-notice">Candidate links are shown as unverified. Tajkart has not checked the linked work's current availability, provider, suitability, access conditions, or rights. Provider and source annotations are searchable only when present in the source row; difficulty, price, and the linked work's language are not reliably available. The source-list locale records the index language, not the destination language. Do not treat a listing as a recommendation or permission to copy the work. Imported listing metadata is attributed to the Free Ebook Foundation under CC BY 4.0; linked works have their own terms.</p>
  <p id="search-status" class="search-status" role="status" aria-live="polite">Loading learning resources…</p>
  <ul id="search-results" class="search-results" aria-label="Learning resource results"></ul>
</div>

## Browse by format

- [Study skills and assessment preparation]({{ '/learning/study-skills/' | relative_url }})
- [Mathematics foundations: six-part self-study path]({{ '/learning/courses/academic-foundations/' | relative_url }})
- [Mathematics lesson: ratios and unit rates]({{ '/learning/lessons/math-ratios-unit-rates/' | relative_url }})
- [Programming foundations lessons]({{ '/learning/lessons/python-variables/' | relative_url }})
- [Subject guides]({{ '/learning/subjects/' | relative_url }})
- [Programming language paths]({{ '/learning/languages/' | relative_url }})
- [Courses and study plans]({{ '/learning/courses/' | relative_url }})
- [Plan sessions from course prerequisites]({{ '/learning/planner/' | relative_url }})
- [Books and reading guides]({{ '/learning/books/' | relative_url }})
- [Cheatsheets]({{ '/learning/cheatsheets/' | relative_url }})
- [Interactive tutorials]({{ '/learning/interactive-tutorials/' | relative_url }})
- [Problem sets]({{ '/learning/problem-sets/' | relative_url }})
- [Projects and playgrounds]({{ '/learning/projects/' | relative_url }})
- [Podcasts and screencasts]({{ '/learning/podcasts-screencasts/' | relative_url }})
- [How reference-list candidates were imported]({{ '/docs/MASTER_AUDIT_REPORT/#reference-migration' | relative_url }})

Search results describe published work, not a promise that every subject has a complete course. See the [content progress report]({{ '/docs/CONTENT_PROGRESS/' | relative_url }}) for honest coverage status.
