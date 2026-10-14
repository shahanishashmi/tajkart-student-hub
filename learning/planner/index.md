---
layout: page
title: Study planner
description: Choose an authored Tajkart learning path, review its prerequisites, and keep optional progress in this browser.
permalink: /learning/planner/
---

Choose a course with explicit lesson metadata. The planner divides its listed materials into one-resource study sessions and reads the prerequisites already attached to each resource. Time values are estimates for planning, not promises about pace or mastery.

<section data-study-planner aria-labelledby="study-planner-title">
  <h2 id="study-planner-title">Plan a study path</h2>
  <label for="study-goal">Learning goal</label>
  <select id="study-goal">
    <option value="">Choose a course path</option>
  </select>
  <p id="study-plan-summary" role="status" aria-live="polite">Choose a course to see its sessions.</p>
  <ol id="study-plan-sessions"></ol>
  <div id="study-plan-recommendation" role="status" aria-live="polite" aria-atomic="true">Choose a course to see its next step.</div>
  <p id="study-plan-storage-message" role="status" aria-live="polite">Progress is optional and stays in this browser only.</p>
  <button type="button" data-reset-plan>Reset checkmarks for this path</button>
  <button type="button" data-clear-local-data>Clear all saved Tajkart learning data in this browser</button>
  <p data-clear-local-status role="status" aria-live="polite"></p>
  <p>You can pause and continue whenever you are ready. There are no streaks, penalties, account, or cross-device sync. Lesson checkmarks are self-reported completion, not evidence of mastery.</p>
<script id="study-plan-catalogue" type="application/json">
[
{% assign courses = site.pages | where: "content_type", "course" | sort: "title" %}
{% assign first_course = true %}
{% for course in courses %}
  {% if course.related_resources and course.related_resources.size > 0 %}
    {% unless first_course %},{% endunless %}
    {
      "id": {{ course.id | jsonify }},
      "title": {{ course.title | jsonify }},
      "url": {{ course.url | relative_url | jsonify }},
      "steps": [
        {% assign first_step = true %}
        {% for resource_id in course.related_resources %}
          {% assign resource = site.pages | where: "id", resource_id | first %}
          {% if resource %}
            {% unless first_step %},{% endunless %}
            {
              "id": {{ resource.id | jsonify }},
              "title": {{ resource.title | jsonify }},
              "url": {{ resource.url | relative_url | jsonify }},
              "kind": {{ resource.content_type | jsonify }},
              "minutes": {{ resource.estimated_minutes | default: 30 | jsonify }},
              "skills": {{ resource.skills | default: empty | jsonify }},
              "prerequisites": [
                {% assign first_prerequisite = true %}
                {% for prerequisite_id in resource.prerequisites %}
                  {% assign prerequisite = site.pages | where: "id", prerequisite_id | first %}
                  {% if prerequisite %}
                    {% unless first_prerequisite %},{% endunless %}
                    {"id": {{ prerequisite.id | jsonify }}, "title": {{ prerequisite.title | jsonify }}, "url": {{ prerequisite.url | relative_url | jsonify }}, "kind": {{ prerequisite.content_type | jsonify }}}
                    {% assign first_prerequisite = false %}
                  {% endif %}
                {% endfor %}
              ]
            }
            {% assign first_step = false %}
          {% endif %}
        {% endfor %}
      ]
    }
    {% assign first_course = false %}
  {% endif %}
{% endfor %}
]
</script>
</section>

## Available authored paths

- [Mathematics foundations]({{ '/learning/courses/academic-foundations/' | relative_url }}) builds from fractions through percentages and basic data interpretation.
- [Algebra foundations]({{ '/learning/courses/algebra-foundations/' | relative_url }}) introduces expressions and equations.
- [Intermediate Python]({{ '/learning/courses/python-intermediate/' | relative_url }}) follows the beginner programming path.

The catalogue is generated from each course's `related_resources` and each resource's prerequisite metadata. A path without those explicit links is not presented as a generated plan.
