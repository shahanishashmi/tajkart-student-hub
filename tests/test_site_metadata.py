"""Regression tests for resource provenance and external-source metadata."""

from __future__ import annotations

import io
import sys
import tempfile
import unittest
from contextlib import redirect_stdout
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from scripts import validate_site


def metadata(resource_id: str = "example-resource", route: str = "/example/") -> str:
    return f"""---
title: Example resource
permalink: {route}
id: {resource_id}
content_type: guide
category: programming-languages
language: en
difficulty: beginner
tags: [example]
prerequisites: []
learning_objectives: [Read an external learning resource]
content_status: validated
review_status: approved
searchable: true
content_origin: external
creator: Example Foundation
source_url: https://example.org/guide/
source_checked: 2026-10-14
attribution: Created by Example Foundation.
rights_status: link-only
rights_note: Link and descriptive metadata only; source content is not redistributed.
verification_status: verified
---
"""


class ResourceMetadataTests(unittest.TestCase):
    def setUp(self) -> None:
        self.tempdir = tempfile.TemporaryDirectory()
        self.root = Path(self.tempdir.name)
        (self.root / "data").mkdir()
        (self.root / "resources").mkdir()
        (self.root / "_config.yml").write_text("content_origin: original\n", encoding="utf-8")
        self.old_root = validate_site.ROOT
        validate_site.ROOT = self.root

    def tearDown(self) -> None:
        validate_site.ROOT = self.old_root
        self.tempdir.cleanup()

    def run_validator(self) -> tuple[int, str]:
        output = io.StringIO()
        with redirect_stdout(output):
            result = validate_site.main()
        return result, output.getvalue()

    def write_resource(self, name: str, source: str) -> None:
        (self.root / "resources" / name).write_text(source + "\n" + ("Original editorial summary. " * 12), encoding="utf-8")

    def test_verified_external_source_with_resolved_rights_passes(self) -> None:
        self.write_resource("example.md", metadata())
        result, output = self.run_validator()
        self.assertEqual(result, 0, output)

    def test_invalid_external_url_is_rejected(self) -> None:
        self.write_resource("example.md", metadata().replace("https://example.org/guide/", "javascript:alert(1)"))
        result, output = self.run_validator()
        self.assertEqual(result, 1)
        self.assertIn("invalid source_url", output)

    def test_invalid_source_check_date_is_rejected(self) -> None:
        self.write_resource("example.md", metadata().replace("2026-10-14", "2026-02-30"))
        result, output = self.run_validator()
        self.assertEqual(result, 1)
        self.assertIn("invalid source_checked date", output)

    def test_missing_attribution_is_rejected(self) -> None:
        self.write_resource("example.md", metadata().replace("attribution: Created by Example Foundation.", "attribution: "))
        result, output = self.run_validator()
        self.assertEqual(result, 1)
        self.assertIn("missing attribution", output)

    def test_identified_license_requires_license_terms(self) -> None:
        self.write_resource("example.md", metadata().replace("rights_status: link-only", "rights_status: license-identified"))
        result, output = self.run_validator()
        self.assertEqual(result, 1)
        self.assertIn("missing terms_or_license", output)

    def test_unresolved_rights_or_unverified_source_is_rejected(self) -> None:
        source = metadata().replace("rights_status: link-only", "rights_status: unknown").replace("verification_status: verified", "verification_status: unverified")
        self.write_resource("example.md", source)
        result, output = self.run_validator()
        self.assertEqual(result, 1)
        self.assertIn("resolved rights_status", output)
        self.assertIn("must be verified", output)

    def test_duplicate_resource_ids_are_rejected(self) -> None:
        self.write_resource("first.md", metadata())
        self.write_resource("second.md", metadata(route="/second/"))
        result, output = self.run_validator()
        self.assertEqual(result, 1)
        self.assertIn("duplicate resource id", output)


if __name__ == "__main__":
    unittest.main()
