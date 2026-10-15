---
layout: page
title: Explore resources
description: Browse Tajkart learning by student goal and subject, with original content separated from unverified external link candidates.
permalink: /explore/
---

Choose a topic or format below. Tajkart's original pages are linked separately from the optional reference-list candidates. The candidate index is lazy-loaded only after you choose one of those search links; each destination remains unverified, and its access conditions and rights have not been assessed.

Search can match titles, topics, and source-list annotations where those notes exist. The imported data does not reliably identify provider, difficulty, price, or the linked work's language. A source-list locale is not the same as a resource language.

## Browse categories

<nav class="directory-navigation" aria-label="Explore resource categories">
  {% for category in site.data.resource_categories.categories %}
  <a href="#resource-category-{{ category.id }}">{{ category.title }}</a>
  {% endfor %}
</nav>

<div class="directory-grid">
  {% for category in site.data.resource_categories.categories %}
  <section class="directory-card" id="resource-category-{{ category.id }}" aria-labelledby="heading-{{ category.id }}">
    <p class="directory-status directory-status-{{ category.status }}">{{ category.status | replace: "-", " " | capitalize }}</p>
    <h2 id="heading-{{ category.id }}">{{ category.title }}</h2>
    <p>{{ category.status_label }}</p>
    <p>{{ category.summary }}</p>
    {% if category.links.size > 0 %}
    <h3>Tajkart content</h3>
    <ul>
      {% for link in category.links %}
      <li><a href="{{ link.route | relative_url }}">{{ link.label }}</a></li>
      {% endfor %}
    </ul>
    {% endif %}
    {% if category.candidate_links.size > 0 %}
    <h3>External link candidates</h3>
    <ul>
      {% for link in category.candidate_links %}
      <li><a href="{{ link.route | relative_url }}">{{ link.label }} (unverified)</a></li>
      {% endfor %}
    </ul>
    {% endif %}
    {% if category.status == "awaiting-content" %}<p class="directory-empty">This category is awaiting a complete original learning unit or reviewed resource records.</p>{% endif %}
  </section>
  {% endfor %}
</div>

## Complete imported source index

This index is generated from the imported snapshot's actual list files and candidate records. It includes **{{ site.data.reference_resource_facets.candidate_count }} unique unverified destinations**, **{{ site.data.reference_resource_facets.source_entry_appearances }} source-list appearances**, **{{ site.data.reference_resource_facets.duplicate_appearances }} repeated appearances**, and **{{ site.data.reference_resource_facets.alternate_link_count }} alternate links**. The parser recorded {{ site.data.reference_resource_facets.parser_exception_count }} exceptions. A zero exception count means each URL row in the selected lists was parsed; it does not verify destination pages or their rights.

The source snapshot is [Free Programming Books at commit `{{ site.data.reference_resource_facets.source_revision }}`]({{ site.data.reference_resource_facets.source_repository }}/tree/{{ site.data.reference_resource_facets.source_revision }}). Imported listing metadata is attributed to the Free Ebook Foundation under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). That license does not grant rights to the linked works. Every candidate remains unverified, access not checked, and rights not assessed. Source-list locale is provenance for the index file, not a claim about the linked work's language.

### Browse by source category and resource type

{% for source_category in site.data.reference_resource_facets.source_categories %}
<details class="reference-facet" id="reference-source-category-{{ forloop.index }}">
  <summary><a href="{{ source_category.search_url | relative_url }}">{{ source_category.id }}: {{ source_category.unique_destinations }} unique destinations</a> ({{ source_category.source_files }} source lists, {{ source_category.source_entry_appearances }} appearances)</summary>
  <ul>
    {% for source_list in source_category.lists %}
    <li id="{{ source_list.dom_id }}"><a href="{{ source_list.source_url }}">{{ source_list.path }}</a> — {{ source_list.source_list_locale | default: "no locale label" }}; {{ source_list.source_entry_appearances }} source appearances.</li>
    {% endfor %}
  </ul>
</details>
{% endfor %}

<ul>
  {% for resource_type in site.data.reference_resource_facets.resource_types %}
  <li>
    {% if resource_type.source_entry_appearances > 0 %}<a href="{{ resource_type.search_url | relative_url }}">{{ resource_type.id | replace: "-", " " | capitalize }} candidates</a>{% else %}{{ resource_type.id | replace: "-", " " | capitalize }} candidates{% endif %}: {{ resource_type.unique_destinations }} unique destinations across {{ resource_type.source_entry_appearances }} source appearances.
    {% if resource_type.source_entry_appearances == 0 %}No rows of this type were parsed in the selected source files.{% endif %}
  </li>
  {% endfor %}
</ul>

### Browse by source-list locale

{% for source_locale in site.data.reference_resource_facets.source_locales %}
<details class="reference-facet" id="reference-list-locale-{{ forloop.index }}">
  <summary>
    {% if source_locale.source_entry_appearances > 0 %}<a href="{{ source_locale.search_url | relative_url }}">{{ source_locale.label }}</a>{% else %}{{ source_locale.label }}{% endif %}
    — {{ source_locale.source_files }} source lists, {{ source_locale.source_entry_appearances }} appearances, {{ source_locale.unique_destinations }} unique destinations.
    {% if source_locale.source_entry_appearances == 0 %}No resource rows were parsed from these list files.{% endif %}
  </summary>
  <ul>
    {% for source_list_path in source_locale.lists %}
      {% assign matching_list = site.data.reference_resource_facets.source_list_files | where: "path", source_list_path | first %}
      <li><a href="{{ matching_list.source_url }}">{{ source_list_path }}</a> ({{ matching_list.source_category }})</li>
    {% endfor %}
  </ul>
</details>
{% endfor %}

### Browse all source topic paths

<details class="reference-facet" id="reference-topic-paths">
  <summary>Show {{ site.data.reference_resource_facets.topic_paths.size }} topic paths taken from the source headings</summary>
  <ul>
    {% for source_topic in site.data.reference_resource_facets.topic_paths %}
    <li id="reference-topic-path-{{ forloop.index }}"><a href="{{ source_topic.search_url | relative_url }}">{{ source_topic.label }}</a> — {{ source_topic.unique_destinations }} unique destinations, {{ source_topic.source_entry_appearances }} appearances.</li>
    {% endfor %}
  </ul>
</details>

## Choose a student goal

- [I want to learn a subject]({{ '/learning/subjects/' | relative_url }})
- [I want to practise and compare worked solutions]({{ '/learning/problem-sets/' | relative_url }})
- [I want to build a project]({{ '/learning/projects/' | relative_url }})
- [I want to prepare for an exam]({{ '/learning/study-skills/' | relative_url }})
- [I want to improve career skills]({{ '/careers/' | relative_url }})
- [I want to learn in another language]({{ '/learning/languages/' | relative_url }})

See [content progress]({{ '/docs/CONTENT_PROGRESS/' | relative_url }}) for authored coverage and review status. Search external candidate links only when you want to inspect the source-listed destinations; Tajkart does not call them approved, free, safe, or legally reusable.
