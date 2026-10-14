"""Tests for the structured assessment metadata and its honest review gate."""

from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from scripts.validate_site import validate_assessment_data, validate_inline_question_attributes


ROOT = Path(__file__).resolve().parents[1]


def question() -> dict:
    return {
        "id": "sample-solve-001",
        "question": "Solve x + 2 = 5.",
        "skill_ids": ["algebra-equations-one-step"],
        "difficulty": "beginner",
        "lesson_id": "lesson-example",
        "answer_format": "integer",
        "accepted_answers": ["3"],
        "hint": "Subtract 2.",
        "solution": "x = 3.",
        "explanation": "Subtracting 2 from both sides preserves equality.",
        "verification_method": "substitution",
        "verification": {"kind": "solve-linear", "coefficient": 1, "constant": 2, "rhs": 5},
        "review_status": "pending",
    }


class AssessmentContractTests(unittest.TestCase):
    def setUp(self) -> None:
        self.resources = {"lesson-example": {"content_type": "lesson", "review_status": "pending"}}
        self.skills = {"algebra-equations-one-step"}
        self.data = {"schema_version": 1, "id": "sample-assessment", "title": "Sample check", "review_status": "pending", "questions": [question()]}

    def errors(self, data: dict | None = None) -> list[str]:
        return validate_assessment_data(data or self.data, self.resources, self.skills)

    def test_current_algebra_assessment_satisfies_the_contract(self) -> None:
        data = json.loads((ROOT / "_data" / "algebra_assessment.json").read_text(encoding="utf-8"))
        resources = {
            "math-algebra-expressions-001": {"content_type": "lesson", "review_status": "pending"},
            "math-algebra-one-step-001": {"content_type": "lesson", "review_status": "pending"},
            "math-algebra-two-step-001": {"content_type": "lesson", "review_status": "pending"},
        }
        skills = {"algebra-expressions", "algebra-substitution", "algebra-equations-one-step", "algebra-equations-two-step"}
        self.assertEqual(validate_assessment_data(data, resources, skills), [])

    def test_missing_explanation_is_rejected(self) -> None:
        data = copy.deepcopy(self.data)
        data["questions"][0]["explanation"] = " "
        self.assertTrue(any("missing explanation" in item for item in self.errors(data)))

    def test_duplicate_question_ids_are_rejected(self) -> None:
        data = copy.deepcopy(self.data)
        data["questions"].append(copy.deepcopy(data["questions"][0]))
        self.assertTrue(any("duplicate assessment question id" in item for item in self.errors(data)))

    def test_invalid_answer_format_and_answer_are_rejected(self) -> None:
        data = copy.deepcopy(self.data)
        data["questions"][0]["answer_format"] = "magic"
        errors = self.errors(data)
        self.assertTrue(any("invalid answer_format" in item for item in errors))
        data["questions"][0]["answer_format"] = "fraction"
        data["questions"][0]["accepted_answers"] = ["3/0"]
        errors = self.errors(data)
        self.assertTrue(any("does not match" in item for item in errors))

    def test_missing_skill_and_broken_lesson_link_are_rejected(self) -> None:
        data = copy.deepcopy(self.data)
        data["questions"][0]["skill_ids"] = ["unknown-skill"]
        data["questions"][0]["lesson_id"] = "missing-lesson"
        errors = self.errors(data)
        self.assertTrue(any("unknown skill" in item for item in errors))
        self.assertTrue(any("broken lesson link" in item for item in errors))

    def test_approved_question_cannot_outpace_pending_lesson_review(self) -> None:
        data = copy.deepcopy(self.data)
        data["questions"][0]["review_status"] = "approved"
        self.assertTrue(any("cannot be approved" in item for item in self.errors(data)))

    def test_verification_method_must_match_its_derivation(self) -> None:
        data = copy.deepcopy(self.data)
        data["questions"][0]["verification_method"] = "direct-evaluation"
        self.assertTrue(any("does not match" in item for item in self.errors(data)))

    def test_inline_quiz_contract_checks_mapping_and_route(self) -> None:
        resources = {"lesson-example": {"content_type": "lesson", "permalink": "/lesson/"}}
        attrs = {
            "data-question-id": "inline-question-001",
            "data-skill-ids": "algebra-equations-one-step",
            "data-resource-id": "lesson-example",
            "data-resource-url": "{{ '/lesson/' | relative_url }}",
            "data-answer-format": "integer",
            "data-accepted-answers": "3",
        }
        self.assertEqual(validate_inline_question_attributes(attrs, resources, self.skills), [])
        attrs["data-resource-url"] = "{{ '/elsewhere/' | relative_url }}"
        attrs["data-skill-ids"] = "missing-skill"
        errors = validate_inline_question_attributes(attrs, resources, self.skills)
        self.assertTrue(any("resource URL does not match" in item for item in errors))
        self.assertTrue(any("unknown skill" in item for item in errors))


if __name__ == "__main__":
    unittest.main()
