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
const controls = ["type", "category", "sourceCategory", "sourceTopic", "tag", "language", "sourceLocale", "difficulty", "origin"].map((name) => {
  const control = new Element("select");
  search.controls ||= {};
  search.controls[name] = control;
  return control;
});
const searchElements = new Map([
  ["#resource-query", query], ["#search-results", results], ["#search-status", status], ["#sort-results", sort],
  ["#include-reference-candidates", includeReference],
  ["#filter-type", search.controls.type], ["#filter-category", search.controls.category],
  ["#filter-source-category", search.controls.sourceCategory], ["#filter-source-topic", search.controls.sourceTopic],
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
      source_list_category: "courses",
      source_list_locale: "hi", topic_path: ["JavaScript"], source_annotation: " - Example provider",
      additional_links: [{ label: "EPUB", url: "https://example.test/javascript.epub", source_line: 42 }]
    }, {
      source_path: "books/free-programming-books-langs.md", source_line: 77,
      source_list_category: "books", source_list_locale: null,
      topic_path: ["JavaScript"], source_annotation: ""
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
  URLSearchParams,
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
  const sourceDetails = results.children[0].children.find((child) => child.tagName === "details");
  assert.ok(sourceDetails, "candidate results expose duplicate source appearances and alternate links");
  assert.match(sourceDetails.children[0].textContent, /Source appearances and alternate links \(2\)/);
  assert.equal(sourceDetails.children[1].children.length, 2, "each duplicate source occurrence keeps its own detail row");
  assert.match(sourceDetails.children[1].children[0].children[2].textContent, /Source annotation:\s*-?\s*Example provider/);
  assert.equal(sourceDetails.children[1].children[0].children[3].children[0].href, "https://example.test/javascript.epub");

  query.value = "Example provider";
  query.dispatch("input");
  assert.equal(results.children.length, 1, "source annotations should be searchable when the source row includes them");

  search.controls.sourceLocale.value = "hi";
  search.controls.sourceLocale.dispatch("change");
  assert.equal(results.children.length, 1, "reference list locale filter matches imported source metadata");
  search.controls.sourceCategory.value = "courses";
  search.controls.sourceCategory.dispatch("change");
  assert.equal(results.children.length, 1, "source-list category filter matches imported occurrence provenance");
  search.controls.sourceTopic.value = "JavaScript";
  search.controls.sourceTopic.dispatch("change");
  assert.equal(results.children.length, 1, "full source topic path filter matches imported section hierarchy");
  search.controls.sourceLocale.value = "__unlabeled__";
  search.controls.sourceLocale.dispatch("change");
  assert.equal(results.children.length, 1, "unlabeled source-list locale filter retains provenance without guessing destination language");
  includeReference.checked = false;
  await includeReference.dispatch("change");
  assert.equal(results.children.length, 0, "unverified candidates disappear when opt-in is disabled");

  const deepSearch = new Element("section");
  deepSearch.dataset.indexUrl = "/search-index.json";
  deepSearch.dataset.referenceIndexUrl = "/data/reference_resources.json";
  const deepQuery = new Element("input");
  const deepResults = new Element("ul");
  const deepStatus = new Element("p");
  const deepIncludeReference = new Element("input");
  const deepSort = new Element("select");
  deepSort.value = "relevance";
  const deepControls = {};
  for (const name of ["type", "category", "sourceCategory", "sourceTopic", "tag", "language", "sourceLocale", "difficulty", "origin"]) {
    deepControls[name] = new Element("select");
  }
  const deepSelectors = new Map([
    ["#resource-query", deepQuery], ["#search-results", deepResults], ["#search-status", deepStatus],
    ["#sort-results", deepSort], ["#include-reference-candidates", deepIncludeReference],
    ["#filter-type", deepControls.type], ["#filter-category", deepControls.category],
    ["#filter-source-category", deepControls.sourceCategory], ["#filter-source-topic", deepControls.sourceTopic],
    ["#filter-tag", deepControls.tag], ["#filter-language", deepControls.language],
    ["#filter-source-locale", deepControls.sourceLocale], ["#filter-difficulty", deepControls.difficulty],
    ["#filter-origin", deepControls.origin]
  ]);
  deepSearch.querySelector = (selector) => deepSelectors.get(selector) || null;
  const deepDocument = {
    location: { search: "?reference=1&type=course&source_category=courses&locale=hi&topic_path=JavaScript&q=javascript" },
    documentElement: { classList: { add() {} } },
    querySelector: (selector) => selector === ".resource-search" ? deepSearch : null,
    querySelectorAll: () => [],
    createElement: (tagName) => new Element(tagName)
  };
  let deepReferenceFetches = 0;
  vm.runInNewContext(fs.readFileSync("assets/js/site.js", "utf8"), {
    document: deepDocument,
    URLSearchParams,
    fetch: async (url) => {
      if (url === "/data/reference_resources.json") {
        deepReferenceFetches += 1;
        return { ok: true, json: async () => referencePayload };
      }
      return { ok: true, json: async () => items };
    },
    console,
    setTimeout,
    clearTimeout
  });
  await new Promise((resolve) => setImmediate(resolve));
  assert.equal(deepIncludeReference.checked, true, "a deliberate directory link should enable candidate search");
  assert.equal(deepReferenceFetches, 1, "a category deep link should fetch the candidate index once");
  assert.equal(deepQuery.value, "javascript", "directory search terms should populate the search input");
  assert.equal(deepControls.type.value, "course", "directory resource-type filters should be applied after candidate metadata loads");
  assert.equal(deepControls.sourceCategory.value, "courses", "source category facet deep links should populate after opt-in loads");
  assert.equal(deepControls.sourceLocale.value, "hi", "source-list locale facet deep links should populate after opt-in loads");
  assert.equal(deepControls.sourceTopic.value, "JavaScript", "hierarchical topic-path facet deep links should populate after opt-in loads");
  assert.equal(deepResults.children.length, 1, "a directory deep link should show matching candidate results");
  console.log("Search checks passed: local matching, ranking and filters, opt-in candidates, provenance, locale filtering, and category deep links.");
});
