"""Run the published mathematics examples and check their exact arithmetic."""

from __future__ import annotations

import io
import json
import re
import unittest
from contextlib import redirect_stdout
from decimal import Decimal, ROUND_HALF_UP
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DATA = json.loads((ROOT / "_data" / "math_foundations_assessment.json").read_text(encoding="utf-8"))


class MathematicsFoundationsTests(unittest.TestCase):
    def test_each_mixed_check_answer_matches_an_independent_calculation(self) -> None:
        self.assertEqual(len(DATA["questions"]), 7)
        self.assertEqual(len({item["id"] for item in DATA["questions"]}), 7)
        for question in DATA["questions"]:
            with self.subTest(question=question["id"]):
                verification = question["verification"]
                kind = verification["kind"]
                if kind == "fraction-sum":
                    result = sum((Fraction(term["numerator"], term["denominator"]) for term in verification["terms"]), Fraction())
                    derived = f"{result.numerator}/{result.denominator}" if result.denominator != 1 else str(result.numerator)
                elif kind == "fraction-conversion":
                    result = Fraction(verification["numerator"], verification["denominator"])
                    decimal = Decimal(result.numerator) / Decimal(result.denominator)
                    reduced_denominator = result.denominator
                    for factor in (2, 5):
                        while reduced_denominator % factor == 0:
                            reduced_denominator //= factor
                    self.assertEqual(format(decimal, "f"), verification["expected_decimal"])
                    self.assertEqual(float(result * 100), verification["expected_percent"])
                    self.assertEqual(reduced_denominator == 1, verification["decimal_terminates"])
                    self.assertEqual(question["answer_format"], "manual")
                    self.assertEqual(question["accepted_answers"], [])
                    self.assertIn("0.4375", question["solution"])
                    self.assertIn("43.75%", question["solution"])
                    continue
                elif kind == "percentage-share":
                    result = Fraction(verification["part_units"] * 100, verification["whole_units"])
                    derived = str(result.numerator) if result.denominator == 1 else f"{result.numerator}/{result.denominator}"
                elif kind == "unit-rate":
                    result = Fraction(verification["total"], verification["count"])
                    derived = str(result.numerator) if result.denominator == 1 else f"{result.numerator}/{result.denominator}"
                elif kind == "percentage-discount":
                    result = Fraction(verification["original_value"] * (100 - verification["percent"]), 100)
                    derived = str(result.numerator) if result.denominator == 1 else f"{result.numerator}/{result.denominator}"
                elif kind == "percentage-change":
                    result = Fraction((verification["new_value"] - verification["old_value"]) * 100, verification["old_value"])
                    derived = str(result.numerator) if result.denominator == 1 else f"{result.numerator}/{result.denominator}"
                elif kind == "statistics-summary":
                    observations = verification["observations"]
                    total = sum(observations)
                    ordered = sorted(observations)
                    middle = len(ordered) // 2
                    median_value = ordered[middle] if len(ordered) % 2 else Fraction(ordered[middle - 1] + ordered[middle], 2)
                    self.assertEqual(total, verification["expected_total"])
                    self.assertEqual(total / len(observations), verification["expected_mean"])
                    self.assertEqual(median_value, verification["expected_median"])
                    self.assertIn(str(total), question["solution"])
                    self.assertIn("10.5", question["solution"])
                    self.assertEqual(question["answer_format"], "manual")
                    self.assertEqual(question["accepted_answers"], [])
                    continue
                else:
                    self.fail(f"unsupported math verification: {kind}")
                self.assertIn(derived, question["accepted_answers"])
                self.assertIn(derived, question["solution"])

    def test_lesson_code_examples_match_documented_output(self) -> None:
        expected = {
            "math-fractions-operations.md": "11/12\n3/4\n",
            "math-decimals-conversions.md": "0.375 = 37.5%\n2.68\n",
            "math-percentages.md": "68.00\n73.44\n25.0% increase\n",
            "math-data-interpretation.md": "180\n36.0\n45\n33.3%\n",
        }
        for filename, output_expected in expected.items():
            with self.subTest(lesson=filename):
                source = (ROOT / "learning" / "lessons" / filename).read_text(encoding="utf-8")
                snippets = re.findall(r"```python\s*\n(.*?)\n```", source, re.S)
                self.assertEqual(len(snippets), 1, f"expected one runnable example in {filename}")
                output = io.StringIO()
                with redirect_stdout(output):
                    exec(compile(snippets[0], filename, "exec"), {})
                self.assertEqual(output.getvalue(), output_expected)

    def test_fraction_operations_and_mixed_assessment_answers(self) -> None:
        self.assertEqual(Fraction(21, 28), Fraction(3, 4))
        self.assertEqual(Fraction(3, 5) + Fraction(1, 4), Fraction(17, 20))
        self.assertEqual(Fraction(7, 9) - Fraction(1, 6), Fraction(11, 18))
        self.assertEqual(Fraction(4, 7) * Fraction(14, 15), Fraction(8, 15))
        self.assertEqual(Fraction(3, 8) / Fraction(9, 16), Fraction(2, 3))
        self.assertEqual(Fraction(18, 30) + Fraction(1, 5), Fraction(4, 5))
        self.assertEqual(Fraction(7, 20), Fraction(35, 100))
        self.assertEqual(Fraction(45, 100), Fraction(9, 20))
        self.assertEqual(Fraction(3, 8), Fraction("0.375"))
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 0)

    def test_decimal_and_percentage_assessment_answers(self) -> None:
        self.assertEqual(Decimal(7) / Decimal(16), Decimal("0.4375"))
        self.assertEqual(Decimal(1) / Decimal(6), Decimal("0.1666666666666666666666666667"))
        self.assertEqual(Decimal("12.8") + Decimal("0.37"), Decimal("13.17"))
        self.assertEqual((Decimal("0.6") / Decimal("2.4")) * 100, Decimal("25"))
        self.assertEqual(Decimal("0.18") * 250, Decimal("45.00"))
        discount = Decimal("250") * Decimal("0.12")
        self.assertEqual(Decimal("250") - discount, Decimal("220.00"))
        self.assertEqual((Decimal("75") - Decimal("60")) / Decimal("60") * 100, Decimal("25"))
        self.assertEqual((Decimal("60") - Decimal("80")) / Decimal("80") * 100, Decimal("-25"))

    def test_explicit_half_up_currency_rounding(self) -> None:
        cents = Decimal("0.01")
        reduced = (Decimal("120") * (Decimal("1") - Decimal("0.20"))).quantize(cents, rounding=ROUND_HALF_UP)
        total = (reduced * (Decimal("1") + Decimal("0.05"))).quantize(cents, rounding=ROUND_HALF_UP)
        self.assertEqual(reduced, Decimal("96.00"))
        self.assertEqual(total, Decimal("100.80"))
        self.assertEqual(Decimal("6.245").quantize(cents, rounding=ROUND_HALF_UP), Decimal("6.25"))

    def test_data_interpretation_summaries_keep_recorded_zero(self) -> None:
        from statistics import mean, median

        observations = [30, 45, 0, 60, 45]
        self.assertEqual(sum(observations), 180)
        self.assertEqual(mean(observations), 36)
        self.assertEqual(median(observations), 45)
        share = Decimal(60) / Decimal(sum(observations)) * 100
        self.assertEqual(share.quantize(Decimal("0.1")), Decimal("33.3"))


    def test_math_verification_boundary_cases(self) -> None:
        self.assertEqual(Fraction(1, 3) + Fraction(-1, 6), Fraction(1, 6))
        self.assertEqual(Fraction(0, 7), Fraction(0, 1))
        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 0)
        self.assertEqual(Fraction(7, 16) * 100, Fraction(175, 4))
        self.assertEqual(Fraction(1, 6) * 100, Fraction(50, 3))
        self.assertEqual(Fraction((60 - 80) * 100, 80), -25)
        self.assertEqual(Fraction(250 * (100 - 100), 100), 0)
        with self.assertRaises(ZeroDivisionError):
            Fraction((60 - 0) * 100, 0)

    def test_data_summary_handles_single_odd_even_and_all_zero_samples(self) -> None:
        from statistics import StatisticsError, mean, median

        for values, expected_mean, expected_median in [
            ([0], 0, 0),
            ([1, 3, 8], 4, 3),
            ([0, 0, 0, 0], 0, 0),
            ([2, 9], 5.5, 5.5),
        ]:
            with self.subTest(values=values):
                self.assertEqual(mean(values), expected_mean)
                self.assertEqual(median(values), expected_median)
        with self.assertRaises(StatisticsError):
            mean([])


if __name__ == "__main__":
    unittest.main()
