"""Run the published mathematics examples and check their exact arithmetic."""

from __future__ import annotations

import io
import re
import unittest
from contextlib import redirect_stdout
from decimal import Decimal, ROUND_HALF_UP
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class MathematicsFoundationsTests(unittest.TestCase):
    def test_each_mixed_check_answer_matches_an_independent_calculation(self) -> None:
        source = (ROOT / "learning" / "problem-sets" / "math-foundations-check.md").read_text(encoding="utf-8")
        solution_section = source.split("## Reference solutions", 1)[1].split("## Self-review rubric", 1)[0]
        solutions = {int(number): line for number, line in re.findall(r"(?m)^(\d+)\.\s*(.+)$", solution_section)}
        self.assertEqual(set(solutions), set(range(1, 8)))

        fraction_total = Fraction(18, 30) + Fraction(1, 5)
        decimal = Decimal(7) / Decimal(16)
        rice_share = Decimal("0.6") / Decimal("2.4") * 100
        unit_rate = Decimal(120) / Decimal(4)
        discounted_price = Decimal(250) - Decimal(250) * Decimal("0.12")
        percent_change = (Decimal(60) - Decimal(80)) / Decimal(80) * 100
        recorded = [12, 15, 0, 9]
        recorded_sorted = sorted(recorded)
        derived = {
            1: [str(fraction_total)],
            2: [str(decimal), f"{(decimal * 100).normalize()}%"],
            3: [f"{rice_share.normalize()}%"],
            4: [format(unit_rate.normalize(), "f")],
            5: [format(discounted_price.normalize(), "f")],
            6: [f"{percent_change.normalize()}%"],
            7: [str(sum(recorded)), str((Decimal(sum(recorded)) / Decimal(len(recorded))).normalize()), str(Decimal(recorded_sorted[1] + recorded_sorted[2]) / Decimal(2))],
        }
        for number, values in derived.items():
            with self.subTest(question=number):
                solution = solutions[number].replace("−", "-")
                for value in values:
                    self.assertIn(value, solution)
        self.assertEqual(fraction_total, Fraction(4, 5))
        self.assertEqual(percent_change, Decimal("-25"))

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


if __name__ == "__main__":
    unittest.main()
