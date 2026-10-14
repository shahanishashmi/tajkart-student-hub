"use strict";

const assert = require("node:assert/strict");
const tools = require("../assets/js/learning-tools.js");

const at = "2026-10-15T12:00:00.000Z";
const attempt = (correct, sessionId, questionId = "algebra-question-001", skillIds = ["algebra-equations-one-step"]) => ({
  correct,
  sessionId,
  questionId,
  skillIds,
  at
});

assert.deepEqual(tools.loadState({ getItem: () => null }), tools.emptyState(), "empty browser storage starts with no progress");
assert.deepEqual(tools.normalizeState("not-json"), tools.emptyState(), "malformed storage recovers to an empty state");
assert.deepEqual(tools.normalizeState(JSON.stringify({ version: 99, attempts: [] })), tools.emptyState(), "unknown storage versions are ignored");

const memory = new Map();
const storage = {
  getItem: (key) => memory.get(key) ?? null,
  setItem: (key, value) => memory.set(key, value),
  removeItem: (key) => memory.delete(key)
};
let state = tools.emptyState();
assert.equal(tools.saveState(state, storage), true, "valid local state can be saved");
assert.deepEqual(tools.loadState(storage), state, "local state round-trips without network services");
assert.equal(tools.clearLocalData(storage), true, "learners can clear all browser-local learning records");
assert.deepEqual(tools.loadState(storage), tools.emptyState(), "cleared local records reset progress, attempts, and project drafts");
assert.equal(tools.saveState(state, { getItem: () => null, setItem: () => { throw new Error("quota"); } }), false, "storage failures do not crash the learning page");

state = tools.recordAttempt(state, attempt(false, "session-a"));
state = tools.recordAttempt(state, attempt(false, "session-a", "algebra-question-002"));
assert.equal(tools.skillEvidence(state, "algebra-equations-one-step").status, "insufficient-evidence", "repeated errors from one small session are not mastery evidence");
const repeatedError = tools.recommendStudyStep([{
  id: "math-algebra-one-step-001",
  title: "One-step equations",
  url: "/learning/lessons/math-algebra-one-step/",
  skills: ["algebra-equations-one-step"],
  prerequisites: []
}], state);
assert.equal(repeatedError.kind, "review", "a recent wrong answer recommends the linked lesson");
assert.match(repeatedError.reason, /two most recent attempts/i, "repeated errors explain the recommendation");
assert.equal(tools.recordAttempt(state, attempt(false, "session-a", "unmapped-question", [])).attempts.length, state.attempts.length, "questions without a skill mapping are not counted");

state = tools.emptyState();
for (const [index, correct] of [true, true, true, false].entries()) state = tools.recordAttempt(state, attempt(correct, index < 2 ? "session-a" : "session-b", `algebra-question-00${index + 1}`));
assert.equal(tools.skillEvidence(state, "algebra-equations-one-step").status, "insufficient-evidence", "four of five attempts is below the sample threshold");
state = tools.recordAttempt(state, attempt(false, "session-b", "algebra-question-005"));
assert.equal(tools.skillEvidence(state, "algebra-equations-one-step").status, "practice-recommended", "three correct of five is below the 80 percent boundary");
state = tools.recordAttempt(state, attempt(true, "session-c", "algebra-question-006"));
state = tools.recordAttempt(state, attempt(true, "session-c", "algebra-question-007"));
state = tools.recordAttempt(state, attempt(true, "session-c", "algebra-question-008"));
state = tools.recordAttempt(state, attempt(true, "session-c", "algebra-question-009"));
assert.equal(tools.skillEvidence(state, "algebra-equations-one-step").status, "evidence-threshold-met", "four of the five most recent attempts across two or more sessions meets the explicit threshold");

state = tools.emptyState();
const path = [{
  id: "algebra-expressions-001",
  title: "Expressions",
  url: "/learning/lessons/math-algebra-expressions/",
  skills: ["algebra-expressions"],
  prerequisites: []
}, {
  id: "algebra-one-step-001",
  title: "One-step equations",
  url: "/learning/lessons/math-algebra-one-step/",
  skills: ["algebra-equations-one-step"],
  prerequisites: [{ id: "algebra-expressions-001", title: "Expressions", url: "/learning/lessons/math-algebra-expressions/" }]
}];
assert.equal(tools.recommendStudyStep(path.slice(1), state).kind, "prerequisite", "a changed prerequisite relationship blocks the next lesson until its prerequisite is complete");
state = tools.setLessonCompleted(state, "algebra-expressions-001", true);
assert.equal(tools.recommendStudyStep(path.slice(1), state).kind, "next", "completing the prerequisite unlocks the lesson");
state = tools.setLessonCompleted(state, "algebra-expressions-001", false);
assert.equal(tools.recommendStudyStep(path.slice(1), state).kind, "prerequisite", "unmarking a prerequisite recalculates the recommendation");

assert.equal(tools.answerIsAccepted("06", ["6"], "integer"), true, "integer formatting normalizes leading zeros");
assert.equal(tools.answerIsAccepted("3/2", ["3/2", "1.5"], "fraction"), true, "explicitly listed exact fraction answers are accepted");
assert.equal(tools.answerIsAccepted("6/4", ["3/2", "1.5"], "fraction"), false, "unlisted equivalent fractions are not silently accepted");
assert.equal(tools.answerIsAccepted("1.50", ["1.5"], "decimal"), true, "decimal formatting ignores insignificant trailing zeros");
assert.equal(tools.answerIsAccepted("1/0", ["1/0"], "fraction"), false, "division by zero is rejected as an input format");
assert.equal(tools.answerIsAccepted("", ["no solution"], "text"), false, "empty answers are not accepted");

const portfolio = tools.validatePortfolioRecord({
  title: "Study tracker",
  summary: "A local tool for recording practice sessions.",
  skills: "Python, testing",
  url: "https://github.com/example/study-tracker",
  status: "in-progress"
});
assert.equal(portfolio.ok, true, "a complete learner-authored project record is valid");
assert.equal(tools.validatePortfolioRecord({ ...portfolio.value, url: "javascript:alert(1)" }).ok, false, "unsafe project URLs are rejected");
assert.equal(tools.validatePortfolioRecord({ ...portfolio.value, url: "https://student:secret@example.org/project" }).ok, false, "URLs with embedded credentials are rejected");
assert.equal(tools.validatePortfolioRecord({ ...portfolio.value, title: "" }).ok, false, "project titles are required");
const savedProject = tools.upsertPortfolioRecord(tools.emptyState(), portfolio.value, "portfolio-study-tracker", at);
assert.equal(savedProject.ok, true, "valid projects can be stored as browser-local drafts");
assert.equal(tools.deletePortfolioRecord(savedProject.state, "portfolio-study-tracker").portfolio.length, 0, "a learner can delete a local draft");

console.log("Learning-tool checks passed: resilient local storage, mastery evidence thresholds, skill-linked recommendations, prerequisites, answer formats, and safe portfolio records.");
