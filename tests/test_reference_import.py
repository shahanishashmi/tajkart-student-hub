"""Regression tests for archive link parsing and source reconciliation."""

from __future__ import annotations

import hashlib
import tempfile
import unittest
import zipfile
from pathlib import Path

from scripts.import_reference_resources import (
    build_inventory,
    classify_file,
    markdown_links,
    normalized_url,
    validate_inventory,
)


class ReferenceImportTests(unittest.TestCase):
    def test_markdown_links_keep_balanced_parentheses_and_multiple_links(self) -> None:
        links = markdown_links("* [Guide [v2]](https://example.test/a_(b)) and [Author](https://author.test)")
        self.assertEqual([item["label"] for item in links], ["Guide [v2]", "Author"])
        self.assertEqual(links[0]["url"], "https://example.test/a_(b)")
        self.assertEqual(links[1]["url"], "https://author.test")

    def test_file_classification_preserves_source_locale(self) -> None:
        self.assertEqual(classify_file("books/free-programming-books-pt_BR.md"), ("book", "pt_BR"))
        self.assertEqual(classify_file("courses/free-courses-hi.md"), ("course", "hi"))
        self.assertEqual(classify_file("casts/free-podcasts-screencasts-en.md"), ("media", "en"))
        self.assertEqual(classify_file("more/free-programming-interactive-tutorials-en.md"), ("interactive-tutorial", "en"))
        self.assertEqual(classify_file("more/free-programming-playgrounds-zh.md"), ("playground", "zh"))

    def test_url_normalization_only_groups_host_case_and_fragments(self) -> None:
        self.assertEqual(
            normalized_url("HTTPS://Example.Test/path?q=A#section"),
            "https://example.test/path?q=A",
        )

    def test_inventory_groups_duplicates_and_keeps_every_source_appearance(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            archive_path = Path(temporary) / "fixture.zip"
            source = (
                "### Python\n"
                "* [Python guide](https://Example.test/python#intro) - Example author\n"
                "[EPUB](https://example.test/python.epub)\n"
                "* [Python guide](https://example.test/python#another) - Example author\n"
                "broken https://unparsed.example/path\n"
            )
            with zipfile.ZipFile(archive_path, "w") as archive:
                archive.writestr(
                    "free-programming-books-main/books/free-programming-books-en.md",
                    source,
                )
            digest = hashlib.sha256(archive_path.read_bytes()).hexdigest()
            inventory = build_inventory(archive_path, expected_archive_sha256=digest)
            errors = validate_inventory(inventory, expected_archive_sha256=digest)

        self.assertEqual(errors, [])
        self.assertEqual(inventory["inventory"]["source_file_count"], 1)
        self.assertEqual(inventory["inventory"]["source_list_entry_count"], 2)
        self.assertEqual(inventory["inventory"]["unique_destination_count"], 1)
        self.assertEqual(inventory["inventory"]["duplicate_appearances"], 1)
        self.assertEqual(inventory["inventory"]["exception_count"], 1)
        record = inventory["records"][0]
        self.assertEqual(record["title"], "Python guide")
        self.assertEqual(record["resource_types"], ["book"])
        self.assertEqual(len(record["source_occurrences"]), 2)
        self.assertEqual(record["source_occurrences"][0]["additional_links"][0]["label"], "EPUB")
        self.assertEqual(record["verification_status"], "unverified")
        self.assertEqual(record["rights_status"], "not-assessed")

    def test_validator_rejects_promoted_or_unattributed_records(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            archive_path = Path(temporary) / "fixture.zip"
            with zipfile.ZipFile(archive_path, "w") as archive:
                archive.writestr(
                    "free-programming-books-main/books/free-programming-books-en.md",
                    "* [Guide](https://example.test/guide)\n",
                )
            digest = hashlib.sha256(archive_path.read_bytes()).hexdigest()
            inventory = build_inventory(archive_path, expected_archive_sha256=digest)
        inventory["records"][0]["verification_status"] = "verified"
        inventory["attribution"] = ""
        errors = validate_inventory(inventory, expected_archive_sha256=digest)
        self.assertTrue(any("must remain unverified" in error for error in errors))
        self.assertTrue(any("license and attribution" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
