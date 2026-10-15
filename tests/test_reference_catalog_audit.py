"""Tests for full-tree reconciliation and source-derived directory facets."""

from __future__ import annotations

import hashlib
import tempfile
import unittest
import zipfile
from pathlib import Path

from scripts.import_reference_resources import build_inventory
from scripts.reference_catalog_audit import build_facets, build_source_manifest, validate_generated


REVISION = "f" * 40
ROOT = f"free-programming-books-{REVISION}/"


class ReferenceCatalogAuditTests(unittest.TestCase):
    def make_snapshot(self, archive_path: Path, extra: dict[str, str] | None = None) -> dict:
        files = {
            "books/free-programming-books-fr.md": (
                "### JavaScript\n"
                "* [JavaScript book](https://example.test/javascript) - Author\n"
                "[EPUB](https://example.test/javascript.epub)\n"
            ),
            "courses/free-courses-en.md": "## Python\n- [Python course](https://example.test/python)\n",
            "books/free-programming-books-langs.md": "### Rust\n* [Rust book](https://example.test/rust)\n",
            "more/free-programming-playgrounds-cs-cp.md": "## C++\n",
            "docs/CONTRIBUTING-fr.md": "- [Illustrative example](https://example.test/example)\n",
            "docs/CODE_OF_CONDUCT.md": "Community policy.\n",
            ".github/PULL_REQUEST_TEMPLATE.md": "- [ ] Read contributing guidance.\n",
            "scripts/lint.py": "print('not executed')\n",
            "README.md": "# Project overview\n",
            "LICENSE": "CC BY 4.0\n",
            "_config.yml": "title: Source\n",
        }
        if extra:
            files.update(extra)
        with zipfile.ZipFile(archive_path, "w") as archive:
            for path, content in files.items():
                archive.writestr(ROOT + path, content)
        digest = hashlib.sha256(archive_path.read_bytes()).hexdigest()
        inventory = build_inventory(archive_path, expected_archive_sha256=digest, source_revision=REVISION)
        return inventory

    def test_full_tree_reconciles_every_candidate_and_documents_exclusions(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            archive_path = Path(temporary) / "snapshot.zip"
            inventory = self.make_snapshot(archive_path)
            manifest = build_source_manifest(archive_path, inventory)
            facets = build_facets(inventory)
            errors = validate_generated(manifest, facets, inventory)

        self.assertEqual(errors, [])
        self.assertEqual(manifest["summary"]["repository_file_count"], 11)
        self.assertEqual(manifest["summary"]["included_resource_list_file_count"], 4)
        self.assertEqual(manifest["summary"]["source_entry_appearances"], 3)
        self.assertEqual(manifest["summary"]["unique_destination_count"], 3)
        self.assertEqual(manifest["summary"]["alternate_links"], 1)
        self.assertEqual(manifest["summary"]["parser_exceptions"], 0)
        self.assertEqual(manifest["reconciliation"]["source_only_unique_destinations"], [])
        self.assertEqual(manifest["reconciliation"]["target_only_unique_destinations"], [])
        self.assertTrue(manifest["reconciliation"]["exact_candidate_records_match"])
        self.assertTrue(all(file["reason"] for file in manifest["files"] if file["disposition"] == "excluded-repository-file"))

    def test_facets_include_all_present_categories_locales_and_full_topic_paths(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            archive_path = Path(temporary) / "snapshot.zip"
            inventory = self.make_snapshot(archive_path)
            facets = build_facets(inventory)

        self.assertEqual({item["id"] for item in facets["source_categories"]}, {"books", "courses", "more"})
        self.assertEqual({item["id"] for item in facets["resource_types"]}, {"book", "course", "playground"})
        self.assertEqual({item["code"] for item in facets["source_locales"]}, {"en", "fr", "__unlabeled__", "cs-cp"})
        self.assertIn("JavaScript", {item["label"] for item in facets["topic_paths"]})
        self.assertTrue(any(item["source_entry_appearances"] == 0 for item in facets["source_locales"]))
        self.assertTrue(all("source_category=" in item["search_url"] for item in facets["source_categories"]))

    def test_unknown_markdown_directory_is_flagged_for_category_review(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            archive_path = Path(temporary) / "snapshot.zip"
            inventory = self.make_snapshot(archive_path, {"languages/language-list.md": "# New category\n"})
            with self.assertRaisesRegex(ValueError, "unclassified Markdown source directory"):
                build_source_manifest(archive_path, inventory)

    def test_pinned_full_snapshot_rejects_resource_only_archive(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            archive_path = Path(temporary) / "partial.zip"
            inventory = self.make_snapshot(archive_path)
            inventory["source"]["revision"] = "4c301cce10db10026d632606b5167a9d1b8cd4ec"
            with self.assertRaisesRegex(ValueError, "must contain 233 files"):
                build_source_manifest(archive_path, inventory)

    def test_validator_rejects_changed_facet_or_unexplained_exclusion(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            archive_path = Path(temporary) / "snapshot.zip"
            inventory = self.make_snapshot(archive_path)
            manifest = build_source_manifest(archive_path, inventory)
            facets = build_facets(inventory)
        facets["source_categories"].pop()
        manifest["files"][-1]["reason"] = ""

        errors = validate_generated(manifest, facets, inventory)
        self.assertTrue(any("facets do not match" in error for error in errors))
        self.assertTrue(any("lacks a reason" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
