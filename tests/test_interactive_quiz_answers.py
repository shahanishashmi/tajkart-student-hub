"""Execute the curated code-reading examples and derive their answer records."""

from __future__ import annotations

import contextlib
import io
import json
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASSESSMENT = json.loads((ROOT / "_data" / "code_reading_assessment.json").read_text(encoding="utf-8"))


class InteractiveQuizAnswerTests(unittest.TestCase):
    def test_each_answer_matches_the_executed_example(self) -> None:
        question_ids = [question["id"] for question in ASSESSMENT["questions"]]
        self.assertEqual(len(question_ids), len(set(question_ids)))
        for question in ASSESSMENT["questions"]:
            with self.subTest(question=question["id"]):
                verification = question["verification"]
                output = io.StringIO()
                with contextlib.redirect_stdout(output):
                    exec(compile(verification["code"], question["id"], "exec"), {})
                actual_output = output.getvalue()
                self.assertEqual(actual_output, verification["expected_output"])
                if verification["answer_from_output"] == "stdout":
                    derived_answer = actual_output.strip()
                else:
                    derived_answer = str(len(actual_output.splitlines()))
                self.assertIn(derived_answer.casefold(), {item.casefold() for item in question["accepted_answers"]})


if __name__ == "__main__":
    unittest.main()
