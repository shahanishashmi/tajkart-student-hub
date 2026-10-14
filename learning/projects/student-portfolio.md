---
layout: page
title: "Project: student portfolio site"
summary: Present a learner's projects clearly without fabricating experience or sharing private data.
permalink: /learning/projects/student-portfolio/
id: project-student-portfolio
content_type: project
category: web-development
language: en
difficulty: beginner
tags: [html, css, portfolio, writing, accessibility]
prerequisites: [language-path-html-css]
learning_objectives: ["Describe a project, role, decisions, and evidence in an accessible static page."]
estimated_minutes: 180
content_status: drafted
review_status: pending
searchable: true
---

## Goal and requirements

Build a static page with an introduction, skills you can demonstrate, two project summaries, and a contact method you are comfortable making public. Never publish a home address, private phone number, student ID, credentials, or another person's work without permission.

Each project summary should state the problem, your role, tools used, one decision, one challenge, and what you learned. Label unfinished work honestly; do not invent clients, qualifications, or impact metrics.

## Milestones

1. Outline content before styling.
2. Use semantic headings, descriptive links, and meaningful image alternatives.
3. Add responsive styles and visible focus.
4. Check keyboard order, zoom, and mobile width.
5. Ask a peer to follow each project link and explain what you contributed.

## Example and evaluation

Example project statement: “I built a local flashcard page with JavaScript. I wrote the checking and empty-state logic, tested keyboard use, and learned to separate data from display.” Score 0–2 for clarity, evidence, accessibility, and accurate attribution. Extensions: add a project changelog or a short architecture diagram.

## Optional browser-local project notes

The form below lets you keep a short draft of what you built and learned. Entries stay in this browser's local storage; they are not uploaded, synced, or securely private. Anyone with access to this browser profile may be able to view them. Do not enter passwords, access tokens, private student records, contact details, or another person's information. An optional project URL must use HTTPS and should point only to material you intend to make public.

<section data-local-portfolio aria-labelledby="portfolio-workspace-title">
  <h2 id="portfolio-workspace-title">My project drafts on this device</h2>
  <form>
    <label for="project-title">Project title</label>
    <input id="project-title" name="project-title" type="text" maxlength="120" required>
    <label for="project-summary">What did you build, what did you learn, or what is your next milestone?</label>
    <textarea id="project-summary" name="project-summary" rows="5" maxlength="2000" required></textarea>
    <label for="project-skills">Skills shown (comma-separated, optional)</label>
    <input id="project-skills" name="project-skills" type="text" maxlength="500">
    <label for="project-url">Public repository or demo URL (optional; HTTPS only)</label>
    <input id="project-url" name="project-url" type="text" inputmode="url" maxlength="500" autocomplete="url">
    <label for="project-status">Project status</label>
    <select id="project-status" name="project-status">
      <option value="idea">Idea</option>
      <option value="in-progress">In progress</option>
      <option value="complete">Complete</option>
    </select>
    <button class="button" type="button" data-save-portfolio>Save draft in this browser</button>
  </form>
  <p data-portfolio-status role="status" aria-live="polite">These notes are not submitted to Tajkart.</p>
  <ul data-portfolio-list aria-label="Saved local project drafts">
    <li>Enable JavaScript to manage local drafts. The project brief above remains available without it.</li>
  </ul>
  <button type="button" data-clear-local-data>Clear all saved Tajkart learning data in this browser</button>
  <p data-clear-local-status role="status" aria-live="polite"></p>
</section>
