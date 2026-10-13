---
layout: page
title: Learning Library
description: Original lessons and practice for programming, computer science, and independent study.
permalink: /learning/
---

Start with a question you want to answer or a skill you want to practise. Lessons are written to be read, tried, and revisited.

## Find a lesson

<label for="lesson-search"><strong>Search lessons</strong></label>
<input id="lesson-search" class="search-box" type="search" placeholder="Try “variables”, “Git”, or “algorithms”" autocomplete="off">
<label for="lesson-category"><strong>Filter by topic</strong></label>
<select id="lesson-category" class="search-box">
<option value="">All topics</option>
{% assign categories = site.lessons | map: "category" | uniq | sort %}
{% for category in categories %}<option value="{{ category | escape }}">{{ category | escape }}</option>{% endfor %}
</select>
<p id="search-status" class="search-status" aria-live="polite"></p>
<div id="search-results" class="search-results">
{% assign lessons = site.lessons | sort: "title" %}
{% for lesson in lessons %}
<a class="search-result" data-category="{{ lesson.category | escape }}" href="{{ lesson.url | relative_url }}"><strong>{{ lesson.title }}</strong><span>{{ lesson.summary }}{% if lesson.category %} · {{ lesson.category }}{% endif %}</span></a>
{% endfor %}
</div>

## Explore the map

- [Computer science subjects]({{ '/learning/subjects/' | relative_url }})
- [Programming languages]({{ '/learning/languages/' | relative_url }})
- [Courses and study plans]({{ '/learning/courses/' | relative_url }})
- [Books and reading guides]({{ '/learning/books/' | relative_url }})
- [Interactive tutorials]({{ '/learning/interactive-tutorials/' | relative_url }})
- [Playgrounds]({{ '/learning/playgrounds/' | relative_url }})
- [Cheatsheets]({{ '/learning/cheatsheets/' | relative_url }})
- [Problem sets]({{ '/learning/problem-sets/' | relative_url }})
- [Podcasts and screencasts]({{ '/learning/podcasts-screencasts/' | relative_url }})
