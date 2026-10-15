"use strict";

const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const root = path.resolve(__dirname, "..");
const read = (relativePath) => fs.readFileSync(path.join(root, relativePath), "utf8");

const pages = new Map();
const visit = (directory) => {
  for (const entry of fs.readdirSync(directory, { withFileTypes: true })) {
    if (entry.name.startsWith(".") || entry.name === "_site" || entry.name === "vendor") continue;
    const absolute = path.join(directory, entry.name);
    if (entry.isDirectory()) {
      visit(absolute);
      continue;
    }
    if (!entry.isFile() || !entry.name.endsWith(".md")) continue;
    const source = fs.readFileSync(absolute, "utf8");
    const route = source.match(/^permalink:\s*["']?([^"'\r\n]+)["']?\s*$/m)?.[1];
    if (route) pages.set(route, path.relative(root, absolute));
  }
};
visit(root);

const layout = read("_layouts/default.html");
const nav = layout.match(/<nav id="primary-nav"[^>]*>([\s\S]*?)<\/nav>/)?.[1];
assert.ok(nav, "primary navigation should exist");
const links = [...nav.matchAll(/<a href="\{\{\s*'([^']+)'\s*\|\s*relative_url\s*\}\}">([^<]+)<\/a>/g)]
  .map(([, route, label]) => [route, label.replaceAll("&amp;", "&")]);
const expected = [
  ["/explore/", "Explore"],
  ["/learning/subjects/", "Subjects"],
  ["/learning/courses/", "Courses & paths"],
  ["/learning/problem-sets/", "Practice"],
  ["/learning/projects/", "Projects"],
  ["/learning/", "Study resources"],
  ["/careers/", "Career prep"],
  ["/learning/languages/", "Languages"],
  ["/about/", "About & contribute"]
];
assert.deepEqual(links, expected, "student navigation should expose the audited sections in order");
for (const [route] of links) assert.ok(pages.has(route), `navigation route ${route} should have a source page`);
const directory = JSON.parse(read("_data/resource_categories.json"));
assert.equal(directory.categories.length, 18, "the resource directory should cover all 18 target categories");
assert.equal(new Set(directory.categories.map((category) => category.id)).size, 18, "directory category IDs should be unique");
for (const category of directory.categories) {
  assert.ok(category.title && category.summary && category.status_label, `category ${category.id} should explain its scope and current state`);
  assert.ok(["available", "partial", "awaiting-content"].includes(category.status), `category ${category.id} should use a documented state`);
  for (const link of [...category.links, ...category.candidate_links]) {
    const route = link.route.split("?")[0];
    assert.ok(pages.has(route), `directory route ${link.route} should resolve to an authored route`);
    if (link.route.includes("reference=1")) assert.match(link.route, /reference=1/, "candidate links should require the explicit opt-in route");
  }
}
assert.match(read("explore.md"), /directory-navigation[\s\S]*directory-grid[\s\S]*External link candidates/, "Explore should render category navigation and distinguish candidate links");
assert.match(read("explore.md"), /awaiting a complete original learning unit/, "empty categories should explain their current state");
assert.match(layout, /class="brand" href="\{\{ '\/' \| relative_url \}\}"/, "brand should provide the home route");

const homeLayout = read("_layouts/home.html");
assert.match(homeLayout, /href="\{\{ '\/getting-started\/' \| relative_url \}\}"/, "home CTA should lead into the student journey");
assert.ok(pages.has("/getting-started/"), "student journey route should exist");
assert.match(read("getting-started.md"), /optional.*study planner/, "the journey should expose the optional local planner");
assert.ok(pages.has("/learning/planner/"), "the browser-local study planner route should exist");
assert.ok(pages.has("/learning/study-skills/"), "general academic study support should have an authored route");
assert.match(read("getting-started.md"), /academic fundamentals or preparing for an assessment[\s\S]*learning\/study-skills\//, "academic learners should be routed to the study guide");
assert.match(read("getting-started.md"), /mathematics foundations path[\s\S]*academic-foundations/, "the academic route should surface the sequenced mathematics path");
assert.match(read("learning/study-skills/index.md"), /review_status:\s*pending/, "new educational guidance should remain visibly pending human review");
assert.ok(pages.has("/learning/lessons/math-ratios-unit-rates/"), "the mathematics foundations route should exist");
for (const route of [
  "/learning/courses/academic-foundations/",
  "/learning/courses/algebra-foundations/",
  "/learning/lessons/math-algebra-expressions/",
  "/learning/lessons/math-algebra-one-step/",
  "/learning/lessons/math-algebra-two-step/",
  "/learning/problem-sets/algebra-foundations-check/",
  "/learning/lessons/math-fractions-operations/",
  "/learning/lessons/math-decimals-conversions/",
  "/learning/lessons/math-percentages/",
  "/learning/problem-sets/math-foundations-check/"
]) assert.ok(pages.has(route), `academic pathway route ${route} should exist`);
assert.match(read("learning/subjects/index.md"), /mathematics and foundations[\s\S]*academic-foundations/i, "the subject explorer should surface the mathematics pathway");
assert.match(read("learning/courses/index.md"), /Other student learning paths[\s\S]*academic-foundations/, "the course page should expose its academic pathway");
assert.match(read("_layouts/lesson.html"), /where: "topic", page\.topic/, "lesson navigation should stay within the current topic sequence");
assert.match(read("learning/lessons/math-ratios-unit-rates.md"), /review_status:\s*pending/, "the new mathematics lesson should remain pending human review");
assert.match(read("learning/problem-sets/index.md"), /interactive prediction routine[\s\S]*code-reading quiz/, "practice hub should link both interactive formats");
assert.match(read("learning/courses/algebra-foundations.md"), /arithmetic[\s\S]*expressions[\s\S]*one-step[\s\S]*two-step/, "algebra should continue the arithmetic pathway in order");
assert.match(read("learning/planner/index.md"), /site\.pages[\s\S]*related_resources[\s\S]*prerequisites/, "planner catalogue should derive from actual course and prerequisite metadata");
assert.match(read("learning/projects/student-portfolio.md"), /data-local-portfolio/, "the portfolio draft tool should be present");
assert.match(read("learning/projects/student-portfolio.md"), /local storage[\s\S]*not uploaded/, "portfolio drafts should disclose browser-local storage limits");
assert.match(read("assets/js/site.js"), /result\.textContent[\s\S]*answerIsAccepted[\s\S]*recordAttempt/, "practice feedback should use explicit answer formats and record skill evidence");
assert.match(read("assets/js/site.js"), /description\.textContent = record\.summary[\s\S]*link\.href = record\.url[\s\S]*link\.rel = 'external noopener noreferrer'/, "portfolio content should render as text and public links should be isolated");
assert.match(read("assets/js/learning-tools.js"), /requiredAttempts.*: 5[\s\S]*requiredSessions.*: 2[\s\S]*accuracy >= 0\.8/, "mastery evidence should use a transparent multi-attempt threshold");
assert.match(layout, /learning-tools\.js[\s\S]*site\.js/, "shared local learning tools should load before page behavior");

const css = read("assets/css/site.css");
assert.match(css, /@media\s*\(max-width:\s*42rem\)[\s\S]*?\.directory-grid[\s\S]*?grid-template-columns:\s*1fr/, "directory cards should collapse at the existing narrow-screen breakpoint");
assert.match(css, /:focus-visible/, "directory and navigation links should retain a visible keyboard focus style");
assert.match(css, /@media\s*\(max-width:\s*68rem\)/, "navigation should collapse before the student-first labels crowd the header");
assert.match(css, /\.js \.primary-nav\s*\{[^}]*display:\s*none/s, "mobile navigation should be hidden while closed");
assert.match(css, /\.js \.primary-nav\.is-open\s*\{[^}]*display:\s*flex/s, "mobile navigation should display when opened");
assert.match(css, /@media\s*\(max-width:\s*42rem\)[\s\S]*?\.hero,[\s\S]*?grid-template-columns:\s*1fr/, "home panels should stack on narrow screens");

class FakeElement {
  constructor(attributes = {}) {
    this.attributes = new Map(Object.entries(attributes));
    this.listeners = new Map();
    this.classes = new Set();
    this.classList = {
      add: (name) => this.classes.add(name),
      contains: (name) => this.classes.has(name),
      toggle: (name, force) => {
        if (force) this.classes.add(name);
        else this.classes.delete(name);
      }
    };
    this.focused = false;
  }

  addEventListener(type, handler) { this.listeners.set(type, handler); }
  getAttribute(name) { return this.attributes.get(name) ?? null; }
  setAttribute(name, value) { this.attributes.set(name, value); }
  focus() { this.focused = true; }
  dispatch(type, event = {}) { this.listeners.get(type)?.({ target: this, ...event }); }
}

const toggle = new FakeElement({ "aria-expanded": "false" });
const navElement = new FakeElement();
let keydownHandler;
const document = {
  documentElement: { classList: { add() {} } },
  querySelector(selector) {
    if (selector === ".menu-toggle") return toggle;
    if (selector === "#primary-nav") return navElement;
    return null;
  },
  querySelectorAll() { return []; },
  addEventListener(type, handler) { if (type === "keydown") keydownHandler = handler; }
};
vm.runInNewContext(read("assets/js/site.js"), { document, console });

toggle.dispatch("click");
assert.equal(toggle.getAttribute("aria-expanded"), "true", "menu button should announce the open state");
assert.ok(navElement.classList.contains("is-open"), "menu click should open the navigation");
keydownHandler({ key: "Escape" });
assert.equal(toggle.getAttribute("aria-expanded"), "false", "Escape should announce the closed state");
assert.ok(!navElement.classList.contains("is-open"), "Escape should close the navigation");
assert.ok(toggle.focused, "Escape should return focus to the menu button");

toggle.dispatch("click");
navElement.dispatch("click", { target: { closest: (selector) => selector === "a" ? {} : null } });
assert.equal(toggle.getAttribute("aria-expanded"), "false", "following a navigation link should close the menu");

console.log("Navigation checks passed: Explore categories, section and math-path routes, home journey, practice links, responsive breakpoints, menu state, Escape, and focus return.");
