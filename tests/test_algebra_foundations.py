"""Independently derive the deterministic algebra answer keys and lesson examples."""

from __future__ import annotations

import json
import re
import unittest
import io
from contextlib import redirect_stdout
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
LESSONS = [
    ROOT / "learning" / "lessons" / "math-algebra-expressions.md",
    ROOT / "learning" / "lessons" / "math-algebra-one-step.md",
    ROOT / "learning" / "lessons" / "math-algebra-two-step.md",
]
DATA = json.loads((ROOT / "_data" / "algebra_assessment.json").read_text(encoding="utf-8"))


def derived_answer(question: dict) -> str:
    verification = question["verification"]
    kind = verification["kind"]
    if kind == "combine-coefficients":
        result = sum(verification["coefficients"])
        return str(result)
    if kind == "evaluate-linear":
        result = verification["coefficient"] * verification["variable_value"] + verification["constant"]
        return str(result)
    if kind == "solve-linear":
        coefficient = verification["coefficient"]
        if coefficient == 0:
            raise ZeroDivisionError("A zero coefficient cannot be divided out")
        result = Fraction(verification["rhs"] - verification["constant"], coefficient)
        return str(result.numerator) if result.denominator == 1 else f"{result.numerator}/{result.denominator}"
    if kind == "classify-zero-coefficient":
        if verification["coefficient"] != 0:
            raise AssertionError("special case must use a zero coefficient")
        return "infinitely many" if verification["constant"] == verification["rhs"] else "none"
    raise AssertionError(f"Unsupported derivation: {kind}")


class AlgebraFoundationsTests(unittest.TestCase):
    def test_each_assessment_answer_is_derived_from_its_contract(self) -> None:
        for question in DATA["questions"]:
            with self.subTest(question=question["id"]):
                derived = derived_answer(question)
                self.assertIn(derived, question["accepted_answers"])
                if question["verification"]["kind"] == "solve-linear":
                    verification = question["verification"]
                    solution = Fraction(verification["rhs"] - verification["constant"], verification["coefficient"])
                    self.assertEqual(verification["coefficient"] * solution + verification["constant"], verification["rhs"])

    def test_special_zero_coefficient_classifications(self) -> None:
        self.assertEqual(derived_answer({"verification": {"kind": "classify-zero-coefficient", "coefficient": 0, "constant": 0, "rhs": 0}}), "infinitely many")
        self.assertEqual(derived_answer({"verification": {"kind": "classify-zero-coefficient", "coefficient": 0, "constant": 0, "rhs": 5}}), "none")

    def test_fractional_and_negative_answers_remain_exact(self) -> None:
        answers = {question["id"]: derived_answer(question) for question in DATA["questions"]}
        self.assertEqual(answers["algebra-two-step-fraction-001"], "3/2")
        self.assertEqual(answers["algebra-two-step-negative-001"], "-5/2")

    def test_worked_equation_examples_satisfy_the_original_statements(self) -> None:
        examples = [
            (1, 8, 13, 5), (1, -9, 4, 13), (7, 0, 0, 0), (4, 0, -48, -12),
            (1, 6, 10, 4), (1, -4, -2, 2), (4, 3, 19, 4), (5, -7, 8, 3),
            (3, 2, -7, -3), (2, 1, 4, Fraction(3, 2)), (2, 5, 17, 6), (3, -4, 8, 4)
        ]
        for coefficient, constant, rhs, proposed in examples:
            with self.subTest(coefficient=coefficient, constant=constant, rhs=rhs):
                solution = Fraction(proposed)
                self.assertEqual(coefficient * solution + constant, rhs)

    def test_expression_examples_calculate_as_written(self) -> None:
        self.assertEqual(4 * 4 + 3, 19)
        self.assertEqual(35 * 4 + 20, 160)
        self.assertEqual(4 * 2 + 12, 20)
        self.assertEqual(2 * 7 + 5, 19)
        self.assertEqual((6 + 2) * 3 - 4, 20)

    def test_all_lesson_python_examples_match_their_stated_output(self) -> None:
        for lesson in LESSONS:
            source = lesson.read_text(encoding="utf-8")
            blocks = re.findall(r"```python\s*\n(.*?)\n```", source, re.S)
            self.assertGreaterEqual(len(blocks), 1, lesson.name)
            expected = re.search(r"Expected output:\s*`([^`]+)`", source)
            if not expected:
                expected = re.search(r"Expected output:\s*```text\s*\n(.*?)\n```", source, re.S)
            self.assertIsNotNone(expected, lesson.name)
            output = io.StringIO()
            with redirect_stdout(output):
                exec(compile(blocks[0], str(lesson), "exec"), {})
            self.assertEqual(output.getvalue().strip(), expected.group(1).strip(), lesson.name)

    def test_two_step_zero_coefficient_is_rejected_by_the_example(self) -> None:
        namespace: dict[str, object] = {}
        source = LESSONS[2].read_text(encoding="utf-8")
        code = re.findall(r"```python\s*\n(.*?)\n```", source, re.S)[0]
        with redirect_stdout(io.StringIO()):
            exec(compile(code, str(LESSONS[2]), "exec"), namespace)
        with self.assertRaises(ValueError):
            namespace["solve_two_step"](0, 5, 17)


if __name__ == "__main__":
    unittest.main()
