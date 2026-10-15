"""Independent equation and substitution checks for the modeling lesson."""

from __future__ import annotations

import io
import json
import re
import unittest
from contextlib import redirect_stdout
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASSESSMENT = json.loads((ROOT / "_data" / "algebra_modeling_assessment.json").read_text(encoding="utf-8"))
LESSON = ROOT / "learning" / "lessons" / "math-algebra-word-problems.md"


def solve_contract(question: dict) -> Fraction:
    equation = question["verification"]
    coefficient = equation["coefficient"]
    if coefficient == 0:
        raise ZeroDivisionError("a zero rate cannot be divided out")
    return Fraction(equation["rhs"] - equation["constant"], coefficient)


class AlgebraWordProblemTests(unittest.TestCase):
    def test_each_assessment_value_is_derived_and_substitutes_into_its_model(self) -> None:
        self.assertEqual(len(ASSESSMENT["questions"]), 3)
        for question in ASSESSMENT["questions"]:
            with self.subTest(question=question["id"]):
                solution = solve_contract(question)
                self.assertEqual(solution.denominator, 1)
                self.assertIn(str(solution.numerator), question["accepted_answers"])
                equation = question["verification"]
                self.assertEqual(equation["coefficient"] * solution + equation["constant"], equation["rhs"])
                self.assertIn(str(solution.numerator), question["solution"])
                self.assertEqual(question["review_status"], "pending")

    def test_published_python_example_matches_its_documented_output(self) -> None:
        source = LESSON.read_text(encoding="utf-8")
        blocks = re.findall(r"```python\s*\n(.*?)\n```", source, re.S)
        self.assertEqual(len(blocks), 1)
        output = io.StringIO()
        with redirect_stdout(output):
            exec(compile(blocks[0], str(LESSON), "exec"), {})
        self.assertEqual(output.getvalue(), "30\n6\n7\n")

    def test_model_helper_rejects_a_zero_rate(self) -> None:
        source = LESSON.read_text(encoding="utf-8")
        block = re.findall(r"```python\s*\n(.*?)\n```", source, re.S)[0]
        namespace: dict[str, object] = {}
        with redirect_stdout(io.StringIO()):
            exec(compile(block, str(LESSON), "exec"), namespace)
        with self.assertRaises(ValueError):
            namespace["solve_additive_model"](0, 24, 60)


if __name__ == "__main__":
    unittest.main()
