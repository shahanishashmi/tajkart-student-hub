"use strict";

const assert = require("node:assert/strict");
const fs = require("node:fs");
const vm = require("node:vm");

class Element {
  constructor(tagName = "") {
    this.tagName = tagName;
    this.children = [];
    this.listeners = {};
    this.dataset = {};
    this.value = "";
    this.textContent = "";
    this.className = "";
  }

  addEventListener(type, handler) {
    this.listeners[type] = handler;
  }

  dispatch(type) {
    return this.listeners[type]?.({ target: this, preventDefault() {} });
  }

  append(child) {
    this.children.push(child);
  }

  replaceChildren(...children) {
    this.children = children;
  }
}

const selectors = new Map();
const search = new Element("section");
search.dataset.indexUrl = "/search-index.json";
search.dataset.referenceIndexUrl = "/data/reference_resources.json";
const query = new Element("input");
const results = new Element("ul");
const status = new Element("p");
const includeReference = new Element("input");
includeReference.checked = false;
const sort = new Element("select");
sort.value = "relevance";
const controls = ["type", "category", "tag", "language", "sourceLocale", "difficulty", "origin"].map((name) => {
  const control = new Element("select");
  search.controls ||= {};
  search.controls[name] = control;
  return control;
});
const searchElements = new Map([
  ["#resource-query", query], ["#search-results", results], ["#search-status", status], ["#sort-results", sort],
  ["#include-reference-candidates", includeReference],
  ["#filter-type", search.controls.type], ["#filter-category", search.controls.category],
  ["#filter-tag", search.controls.tag],
  ["#filter-language", search.controls.language], ["#filter-source-locale", search.controls.sourceLocale],
  ["#filter-difficulty", search.controls.difficulty],
  ["#filter-origin", search.controls.origin]
]);
search.querySelector = (selector) => searchElements.get(selector) || null;
selectors.set(".resource-search", search);

const original = (id, title, summary, tags) => ({
  id, title, summary, tags, url: `/${id}/`, type: "lesson", category: "programming-languages",
  language: "en", difficulty: "beginner", origin: "original", content_status: "drafted", review_status: "pending"
});
const items = [
  original("vars", "Python variables", "Name values clearly.", ["python", "variables"]),
  original("course", "Python course overview", "Learn Python variables with examples.", ["python", "course"]),
  {
    ...original("hi-vars", "Python में नाम और मान", "चर के नाम रखें।", ["python", "variables"]),
    language: "hi", origin: "translation", translation_status: "draft", translation_of: "vars"
  },
  {
    ...original("external-python-guide", "Python tutorial reference", "An official tutorial for learning Python.", ["python", "tutorial"]),
    type: "external-reference", origin: "external", creator: "Example Foundation",
    attribution: "Created by Example Foundation.", source_url: "https://example.test/python/",
    source_checked: "2026-10-14", rights_note: "Link only; no source content is republished.",
    rights_status: "link-only", verification_status: "verified", content_status: "validated", review_status: "approved"
  }
];
const referencePayload = {
  dataset_kind: "unverified-reference-link-candidates",
  source: { repository: "https://github.com/EbookFoundation/free-programming-books", revision: "abc123" },
  records: [{
    id: "reference-0123456789abcdefabcd",
    title: "JavaScript course listing",
    url: "https://example.test/javascript-course",
    resource_types: ["course"],
    topics: ["JavaScript", "Web"],
    source_list_locales: ["hi"],
    verification_status: "unverified",
    rights_status: "not-assessed",
    access_status: "not-checked",
    source_occurrences: [{
      source_path: "courses/free-courses-hi.md", source_line: 42,
      topic_path: ["JavaScript"], source_annotation: " - Example provider"
    }]
  }]
};
let referenceFetches = 0;

const document = {
  documentElement: { classList: { add() {} } },
  querySelector(selector) { return selectors.get(selector) || null; },
  querySelectorAll() { return []; },
  createElement(tagName) { return new Element(tagName); }
};
const context = {
  document,
  fetch: async (url) => {
    if (url === "/data/reference_resources.json") {
      referenceFetches += 1;
      return { ok: true, json: async () => referencePayload };
    }
    return { ok: true, json: async () => items };
  },
  console,
  setTimeout,
  clearTimeout
};
vm.runInNewContext(fs.readFileSync("assets/js/site.js", "utf8"), context);

setImmediate(async () => {
  query.value = "python variables";
  query.dispatch("input");
  assert.ok(search.controls.tag.children.some((option) => option.value === "variables"), "skill options should be generated from resource tags");
  const titles = results.children.map((row) => row.children[0].textContent);
  assert.equal(titles.length, 3, "all query tokens should match across indexed fields");
  assert.equal(titles[0], "Python variables", "exact title matches should rank first");

  query.value = "";
  query.dispatch("input");
  search.controls.origin.value = "external";
  search.controls.origin.dispatch("change");
  assert.equal(results.children.length, 1, "provenance filter should isolate external references");
  assert.equal(results.children[0].children[0].href, "https://example.test/python/");
  assert.equal(results.children[0].children[0].target, "_blank");
  assert.match(results.children[0].children[2].textContent, /by Example Foundation/);
  assert.match(results.children[0].children[2].textContent, /verified/);

  search.controls.origin.value = "";
  search.controls.origin.dispatch("change");
  search.controls.tag.value = "variables";
  search.controls.tag.dispatch("change");
  assert.equal(results.children.length, 2, "skill filter should match tagged original and translation resources");
  search.controls.origin.value = "original";
  search.controls.origin.dispatch("change");
  assert.equal(results.children.length, 1, "skill filter should compose with provenance filters");

  search.controls.origin.value = "translation";
  search.controls.origin.dispatch("change");
  assert.equal(results.children.length, 1, "provenance filter should isolate translations");
  assert.match(results.children[0].children[2].textContent, /हिन्दी translation draft/);

  query.value = "python nonexistent";
  query.dispatch("input");
  assert.equal(results.children.length, 0, "all query tokens must match");
  assert.match(status.textContent, /No resources match/);
  assert.equal(referenceFetches, 0, "large candidate index should not load until explicitly enabled");

  Object.values(search.controls).forEach((control) => { control.value = ""; });
  query.value = "javascript";
  includeReference.checked = true;
  await includeReference.dispatch("change");
  assert.equal(referenceFetches, 1, "candidate index loads after explicit opt-in");
  assert.equal(results.children.length, 1, "candidate title and topic are searchable");
  assert.equal(results.children[0].children[0].href, "https://example.test/javascript-course");
  assert.match(results.children[0].children[2].textContent, /unverified/);
  assert.match(results.children[0].children[2].textContent, /rights not assessed/);
  assert.equal(results.children[0].children[3].href.endsWith("courses/free-courses-hi.md#L42"), true);

  search.controls.sourceLocale.value = "hi";
  search.controls.sourceLocale.dispatch("change");
  assert.equal(results.children.length, 1, "reference list locale filter matches imported source metadata");
  includeReference.checked = false;
  await includeReference.dispatch("change");
  assert.equal(results.children.length, 0, "unverified candidates disappear when opt-in is disabled");
  console.log("Search checks passed: local matching, ranking and filters, plus opt-in unverified candidates, source attribution, and locale filtering.");
});
