"""Checks that resource prerequisites form a directed acyclic graph."""

from __future__ import annotations

import io
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts import validate_site


class PrerequisiteGraphTests(unittest.TestCase):
    def test_acyclic_path_has_no_cycles(self) -> None:
        graph = {"course": ["lesson"], "lesson": ["guide"], "guide": []}
        self.assertEqual(validate_site.find_prerequisite_cycles(graph), [])

    def test_self_prerequisite_is_a_cycle(self) -> None:
        graph = {"lesson": ["lesson"]}
        self.assertEqual(validate_site.find_prerequisite_cycles(graph), [("lesson", "lesson")])

    def test_multi_resource_cycle_is_reported(self) -> None:
        graph = {"alpha": ["beta"], "beta": ["gamma"], "gamma": ["alpha"]}
        self.assertEqual(
            validate_site.find_prerequisite_cycles(graph),
            [("alpha", "beta", "gamma", "alpha")],
        )

    def test_missing_nodes_are_left_for_unknown_reference_check(self) -> None:
        graph = {"course": ["not-present"]}
        self.assertEqual(validate_site.find_prerequisite_cycles(graph), [])

    def test_validator_reports_resource_cycle(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            (root / "data").mkdir()
            (root / "resources").mkdir()
            (root / "_config.yml").write_text("content_origin: original\n", encoding="utf-8")
            for resource_id, prerequisite, name in (
                ("alpha-resource", "beta-resource", "alpha"),
                ("beta-resource", "alpha-resource", "beta"),
            ):
                source = f"""---
title: {name.title()} resource
permalink: /{name}/
id: {resource_id}
content_type: guide
category: testing
language: en
difficulty: beginner
tags: [testing]
prerequisites: [{prerequisite}]
learning_objectives: [Explain one test]
content_status: drafted
review_status: pending
searchable: true
---

""" + ("A sufficiently detailed original explanation for this temporary validator fixture. " * 5)
                (root / "resources" / f"{name}.md").write_text(source, encoding="utf-8")

            previous_root = validate_site.ROOT
            validate_site.ROOT = root
            try:
                output = io.StringIO()
                with redirect_stdout(output):
                    result = validate_site.main()
            finally:
                validate_site.ROOT = previous_root

        self.assertEqual(result, 1)
        self.assertIn("prerequisite cycle: alpha-resource -> beta-resource -> alpha-resource", output.getvalue())


if __name__ == "__main__":
    unittest.main()
