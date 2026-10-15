"""Build and validate a pinned source-tree manifest and browse facets.

The full archive is inspected as data only. Curated list rows remain in the
separate unverified candidate inventory; non-list repository files receive an
explicit exclusion reason in the generated manifest.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import zipfile
from collections import Counter, defaultdict
from pathlib import Path, PurePosixPath
from typing import Any
from urllib.parse import urlencode

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from scripts.import_reference_resources import (
    RESOURCE_DIRS,
    build_inventory,
    classify_file,
    detect_archive_root,
)


INVENTORY_DEFAULT = ROOT / "data" / "reference_resources.json"
MANIFEST_DEFAULT = ROOT / "data" / "reference_source_manifest.json"
FACETS_DEFAULT = ROOT / "_data" / "reference_resource_facets.json"
SOURCE_URL = "https://github.com/EbookFoundation/free-programming-books"
PINNED_TREE_FILE_COUNTS = {"4c301cce10db10026d632606b5167a9d1b8cd4ec": 233}


def _search_url(**filters: str) -> str:
    return "/learning/?" + urlencode({"reference": "1", **filters})


def build_facets(inventory: dict[str, Any]) -> dict[str, Any]:
    """Derive all source categories, formats, locales, lists, and topics."""
    records = inventory["records"]
    files = inventory["source_files"]
    appearances: list[tuple[dict[str, Any], dict[str, Any]]] = [
        (record, occurrence)
        for record in records
        for occurrence in record["source_occurrences"]
    ]

    rows_by_file: Counter[str] = Counter()
    candidates_by_file: dict[str, set[str]] = defaultdict(set)
    rows_by_folder: Counter[str] = Counter()
    candidates_by_folder: dict[str, set[str]] = defaultdict(set)
    rows_by_locale: Counter[str] = Counter()
    candidates_by_locale: dict[str, set[str]] = defaultdict(set)
    rows_by_type: Counter[str] = Counter()
    candidates_by_type: dict[str, set[str]] = defaultdict(set)
    rows_by_topic: Counter[tuple[str, ...]] = Counter()
    candidates_by_topic: dict[tuple[str, ...], set[str]] = defaultdict(set)

    for record, occurrence in appearances:
        path = occurrence["source_path"]
        folder = occurrence["source_list_category"]
        locale = occurrence.get("source_list_locale") or "__unlabeled__"
        rows_by_file[path] += 1
        candidates_by_file[path].add(record["id"])
        rows_by_folder[folder] += 1
        candidates_by_folder[folder].add(record["id"])
        rows_by_locale[locale] += 1
        candidates_by_locale[locale].add(record["id"])
        resource_type = occurrence["resource_type"]
        rows_by_type[resource_type] += 1
        candidates_by_type[resource_type].add(record["id"])
        topic_path = tuple(occurrence.get("topic_path") or [])
        if topic_path:
            rows_by_topic[topic_path] += 1
            candidates_by_topic[topic_path].add(record["id"])

    file_info: list[dict[str, Any]] = []
    files_by_folder: dict[str, list[dict[str, Any]]] = defaultdict(list)
    files_by_locale: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for source_file in files:
        path = source_file["path"]
        folder = PurePosixPath(path).parts[0]
        inferred_type, locale = classify_file(path)
        rows_by_type.setdefault(inferred_type, 0)
        candidates_by_type.setdefault(inferred_type, set())
        locale_key = locale or "__unlabeled__"
        info = {
            "path": path,
            "dom_id": "reference-source-list-" + hashlib.sha256(path.encode("utf-8")).hexdigest()[:16],
            "source_url": f"{SOURCE_URL}/blob/{inventory['source']['revision']}/{path}",
            "source_category": folder,
            "resource_type_hint": inferred_type,
            "source_list_locale": locale,
            "source_entry_appearances": rows_by_file[path],
            "unique_destinations": len(candidates_by_file[path]),
        }
        file_info.append(info)
        files_by_folder[folder].append(info)
        files_by_locale[locale_key].append(info)

    source_categories = []
    for folder in sorted(files_by_folder):
        category_files = sorted(files_by_folder[folder], key=lambda item: item["path"])
        source_categories.append({
            "id": folder,
            "source_files": len(category_files),
            "source_entry_appearances": rows_by_folder[folder],
            "unique_destinations": len(candidates_by_folder[folder]),
            "search_url": _search_url(source_category=folder),
            "lists": category_files,
        })

    locales = []
    for locale_key in sorted(files_by_locale, key=lambda value: (value == "__unlabeled__", value)):
        locale_files = sorted(files_by_locale[locale_key], key=lambda item: item["path"])
        label = "No locale label in source list" if locale_key == "__unlabeled__" else locale_key
        locales.append({
            "code": locale_key,
            "label": label,
            "source_files": len(locale_files),
            "source_entry_appearances": rows_by_locale[locale_key],
            "unique_destinations": len(candidates_by_locale[locale_key]),
            "search_url": _search_url(locale=locale_key),
            "lists": [item["path"] for item in locale_files],
        })

    types = []
    for resource_type in sorted(rows_by_type):
        types.append({
            "id": resource_type,
            "source_entry_appearances": rows_by_type[resource_type],
            "unique_destinations": len(candidates_by_type[resource_type]),
            "search_url": _search_url(type=resource_type),
        })

    topics = []
    for topic_path in sorted(rows_by_topic, key=lambda parts: tuple(part.casefold() for part in parts)):
        label = " / ".join(topic_path)
        topics.append({
            "path": list(topic_path),
            "label": label,
            "source_entry_appearances": rows_by_topic[topic_path],
            "unique_destinations": len(candidates_by_topic[topic_path]),
            "search_url": _search_url(topic_path=label),
        })

    return {
        "schema_version": 1,
        "source_revision": inventory["source"]["revision"],
        "source_repository": SOURCE_URL,
        "candidate_count": inventory["inventory"]["unique_destination_count"],
        "source_entry_appearances": inventory["inventory"]["source_list_entry_count"],
        "duplicate_appearances": inventory["inventory"]["duplicate_appearances"],
        "alternate_link_count": inventory["inventory"]["additional_destination_link_count"],
        "parser_exception_count": inventory["inventory"]["exception_count"],
        "source_categories": source_categories,
        "resource_types": types,
        "source_locales": locales,
        "topic_paths": topics,
        "source_list_files": file_info,
    }


def exclusion_reason(path: str) -> tuple[str, str]:
    """Return a file-specific disposition for known non-catalog repository data."""
    parts = PurePosixPath(path).parts
    if not parts:
        raise ValueError(f"cannot classify empty source path: {path!r}")
    first = parts[0]
    name = parts[-1]
    if first in RESOURCE_DIRS:
        if path.lower().endswith(".md"):
            raise ValueError(f"resource-list Markdown file missing from import: {path}")
        return "non-markdown-resource-directory-file", "Repository asset or metadata file; the pinned source lists are Markdown records."
    if first == "docs":
        if name.startswith("CONTRIBUTING"):
            return "contributor-guidance", "Contributor policy and examples, not the curated published resource-list files."
        if name.startswith("HOWTO"):
            return "maintenance-guidance", "Repository maintenance instructions, not the curated published resource-list files."
        if name.startswith("CODE_OF_CONDUCT"):
            return "community-policy", "Community conduct policy, not an educational resource directory."
        return "repository-documentation", "Repository documentation and project process pages, not curated resource-list entries."
    if first == ".github":
        return "repository-automation-document", "GitHub contribution or workflow document, not curated educational resource-list data."
    if first == "scripts":
        return "repository-maintenance-script", "Source-maintenance script; inspected as repository structure only and not executed or imported."
    if len(parts) == 1 and name == "README.md":
        return "project-overview", "Repository landing page links to project/list indexes; curated list entries are imported from their source files."
    if len(parts) == 1 and name == "LICENSE":
        return "license-document", "Source license text retained as attribution context; it is not a resource-list entry."
    if first in {"_includes"}:
        return "site-template", "Source repository presentation template, not an educational resource-list file."
    if first in {".editorconfig", ".gitignore", "_config.yml", "favicon.ico"} or len(parts) == 1:
        return "repository-configuration-or-asset", "Repository configuration or site asset, not an educational resource-list file."
    if name.lower().endswith(".md"):
        raise ValueError(f"unclassified Markdown source directory; inspect for a new resource category: {path}")
    return "repository-support-file", "Non-list repository support file outside the curated resource-list directories."


def build_source_manifest(archive_path: Path, inventory: dict[str, Any]) -> dict[str, Any]:
    """Inspect every path in the full pinned repository ZIP and reparse its lists."""
    revision = inventory.get("source", {}).get("revision")
    if not isinstance(revision, str) or len(revision) != 40:
        raise ValueError("candidate inventory must identify a full source commit SHA")

    expected_files = {item["path"]: item for item in inventory["source_files"]}
    occurrences_by_file: Counter[str] = Counter(
        occurrence["source_path"]
        for record in inventory["records"]
        for occurrence in record["source_occurrences"]
    )
    destinations_by_file: dict[str, set[str]] = defaultdict(set)
    for record in inventory["records"]:
        for occurrence in record["source_occurrences"]:
            destinations_by_file[occurrence["source_path"]].add(record["id"])

    with zipfile.ZipFile(archive_path) as archive:
        root = detect_archive_root(archive)
        tree_files: list[dict[str, Any]] = []
        discovered_paths = sorted(
            name[len(root) + 1:]
            for name in archive.namelist()
            if name.startswith(root + "/") and not name.endswith("/")
        )
        tree_dirs = sorted({PurePosixPath(path).parts[0] for path in discovered_paths if len(PurePosixPath(path).parts) > 1})
        expected_tree_count = PINNED_TREE_FILE_COUNTS.get(revision)
        if expected_tree_count is not None and len(discovered_paths) != expected_tree_count:
            raise ValueError(
                f"full source snapshot at {revision} must contain {expected_tree_count} files; "
                f"archive contains {len(discovered_paths)}"
            )
        if revision in PINNED_TREE_FILE_COUNTS and root != f"free-programming-books-{revision}":
            raise ValueError(f"expected complete archive root free-programming-books-{revision}; found {root}")
        for path in discovered_paths:
            raw = archive.read(root + "/" + path)
            digest = hashlib.sha256(raw).hexdigest()
            if path in expected_files:
                expected = expected_files[path]
                disposition = "imported-resource-list"
                reason_code = "included"
                reason = "Markdown resource-list file parsed into source occurrences and destination records."
                resource_type, locale = classify_file(path)
                entry = {
                    "path": path,
                    "sha256": digest,
                    "bytes": len(raw),
                    "disposition": disposition,
                    "reason_code": reason_code,
                    "reason": reason,
                    "source_category": PurePosixPath(path).parts[0],
                    "resource_type_hint": resource_type,
                    "source_list_locale": locale,
                    "source_entry_appearances": occurrences_by_file[path],
                    "unique_destinations": len(destinations_by_file[path]),
                }
            else:
                reason_code, reason = exclusion_reason(path)
                entry = {
                    "path": path,
                    "sha256": digest,
                    "bytes": len(raw),
                    "disposition": "excluded-repository-file",
                    "reason_code": reason_code,
                    "reason": reason,
                }
            tree_files.append(entry)

        missing = sorted(set(expected_files) - set(discovered_paths))
        if missing:
            raise ValueError(f"source-list files missing from full repository archive: {missing[:5]}")
        markdown_source_dirs = sorted(
            directory
            for directory in tree_dirs
            if any(path.startswith(directory + "/") and path.lower().endswith(".md") for path in discovered_paths)
        )
        unexpected_resource_dirs = sorted(set(markdown_source_dirs) - RESOURCE_DIRS - {"docs", ".github"})
        if unexpected_resource_dirs:
            raise ValueError(
                "new Markdown source directory needs category review: "
                + ", ".join(unexpected_resource_dirs)
            )

    # Reparse the full tree with the production importer. Exact equality of
    # source rows and records establishes source/target reconciliation at this pin.
    rebuilt = build_inventory(
        archive_path,
        expected_archive_sha256=hashlib.sha256(archive_path.read_bytes()).hexdigest(),
        source_revision=revision,
    )
    rebuilt_records = {record["normalized_url"]: record for record in rebuilt["records"]}
    target_records = {record["normalized_url"]: record for record in inventory["records"]}
    source_only = sorted(set(rebuilt_records) - set(target_records))
    target_only = sorted(set(target_records) - set(rebuilt_records))
    record_mismatches = sum(
        rebuilt_records[url] != target_records[url]
        for url in set(rebuilt_records) & set(target_records)
    )
    rebuilt_source_paths = [item["path"] for item in rebuilt["source_files"]]
    candidate_source_paths = [item["path"] for item in inventory["source_files"]]
    if rebuilt_source_paths != candidate_source_paths:
        raise ValueError("full source-tree reimport did not match the candidate source-file paths")
    if rebuilt["exceptions"] != inventory["exceptions"]:
        raise ValueError("full source-tree reimport did not match the candidate parser-exception report")

    tree_hash_input = "\n".join(f"{item['path']}\0{item['sha256']}" for item in tree_files)
    excluded = [item for item in tree_files if item["disposition"] == "excluded-repository-file"]
    included = [item for item in tree_files if item["disposition"] == "imported-resource-list"]
    excluded_counts = Counter(item["reason_code"] for item in excluded)
    resource_list_dirs = sorted({PurePosixPath(item["path"]).parts[0] for item in included})
    return {
        "schema_version": 1,
        "source_repository": SOURCE_URL,
        "source_revision": inventory["source"]["revision"],
        "source_tree_sha256": hashlib.sha256(tree_hash_input.encode("utf-8")).hexdigest(),
        "source_archive_root": root,
        "source_root_directories": tree_dirs,
        "resource_list_directories": resource_list_dirs,
        "markdown_source_directories": markdown_source_dirs,
        "summary": {
            "repository_file_count": len(tree_files),
            "included_resource_list_file_count": len(included),
            "excluded_repository_file_count": len(excluded),
            "source_entry_appearances": inventory["inventory"]["source_list_entry_count"],
            "unique_destination_count": inventory["inventory"]["unique_destination_count"],
            "duplicate_appearances": inventory["inventory"]["duplicate_appearances"],
            "alternate_links": inventory["inventory"]["additional_destination_link_count"],
            "parser_exceptions": inventory["inventory"]["exception_count"],
            "source_files_without_entries": sum(item["source_entry_appearances"] == 0 for item in included),
            "source_files_with_entries": sum(item["source_entry_appearances"] > 0 for item in included),
            "excluded_files_by_reason": dict(sorted(excluded_counts.items())),
        },
        "reconciliation": {
            "source_only_unique_destinations": source_only,
            "target_only_unique_destinations": target_only,
            "record_content_mismatches": record_mismatches,
            "source_file_path_manifest_matches": rebuilt_source_paths == candidate_source_paths,
            "exact_candidate_records_match": not source_only and not target_only and record_mismatches == 0,
            "source_rows_without_disposition": 0,
            "imported_source_rows": inventory["inventory"]["source_list_entry_count"],
            "exception_rows": inventory["inventory"]["exception_count"],
        },
        "files": tree_files,
    }


def validate_generated(manifest: object, facets: object, inventory: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    if not isinstance(manifest, dict) or manifest.get("schema_version") != 1:
        return ["source manifest must be an object with schema_version 1"]
    if not isinstance(facets, dict) or facets.get("schema_version") != 1:
        return errors + ["reference facets must be an object with schema_version 1"]
    revision = inventory.get("source", {}).get("revision")
    if manifest.get("source_revision") != revision or facets.get("source_revision") != revision:
        errors.append("manifest/facets source revision does not match the candidate inventory")
    if facets != build_facets(inventory):
        errors.append("reference facets do not match the imported candidate inventory")

    files = manifest.get("files")
    if not isinstance(files, list):
        return errors + ["source manifest files must be an array"]
    paths: set[str] = set()
    included: dict[str, dict[str, Any]] = {}
    excluded_count = 0
    for item in files:
        if not isinstance(item, dict) or not isinstance(item.get("path"), str):
            errors.append("source manifest contains an invalid file record")
            continue
        path = item["path"]
        if path in paths:
            errors.append(f"duplicate source manifest path: {path}")
        paths.add(path)
        if not re.fullmatch(r"[a-f0-9]{64}", str(item.get("sha256", ""))):
            errors.append(f"source manifest has an invalid SHA-256 for {path}")
        if not isinstance(item.get("bytes"), int) or item["bytes"] < 0:
            errors.append(f"source manifest has an invalid byte count for {path}")
        if item.get("disposition") == "imported-resource-list":
            included[path] = item
            if not isinstance(item.get("source_entry_appearances"), int) or item["source_entry_appearances"] < 0:
                errors.append(f"included source file has an invalid entry count: {path}")
        elif item.get("disposition") == "excluded-repository-file":
            excluded_count += 1
            if not item.get("reason") or not item.get("reason_code"):
                errors.append(f"excluded source file lacks a reason: {path}")
        else:
            errors.append(f"unknown source file disposition: {path}")
    expected = {item["path"]: item for item in inventory.get("source_files", [])}
    if set(included) != set(expected):
        errors.append("included full-tree paths do not equal candidate source-file paths")
    for path, expected_file in expected.items():
        actual = included.get(path)
        if actual and not isinstance(actual.get("sha256"), str):
            errors.append(f"source manifest lacks a full-snapshot file hash: {path}")
        if actual and actual.get("source_entry_appearances") != sum(
            occurrence["source_path"] == path
            for record in inventory.get("records", [])
            for occurrence in record.get("source_occurrences", [])
        ):
            errors.append(f"source manifest row count does not match imported occurrences: {path}")
    summary = manifest.get("summary", {})
    if summary.get("repository_file_count") != len(paths):
        errors.append("repository file count does not match manifest paths")
    expected_tree_count = PINNED_TREE_FILE_COUNTS.get(revision)
    if expected_tree_count is not None and len(paths) != expected_tree_count:
        errors.append(f"pinned full source tree must contain {expected_tree_count} files")
    if expected_tree_count is not None and manifest.get("source_archive_root") != f"free-programming-books-{revision}":
        errors.append("pinned source archive root does not match its commit")
    if summary.get("included_resource_list_file_count") != len(expected):
        errors.append("included file count does not match candidate source manifest")
    if summary.get("excluded_repository_file_count") != excluded_count:
        errors.append("excluded file count does not match manifest paths")
    if summary.get("source_entry_appearances") != inventory.get("inventory", {}).get("source_list_entry_count"):
        errors.append("manifest source-entry total does not match candidate inventory")
    if summary.get("unique_destination_count") != inventory.get("inventory", {}).get("unique_destination_count"):
        errors.append("manifest unique-destination total does not match candidate inventory")
    if summary.get("duplicate_appearances") != inventory.get("inventory", {}).get("duplicate_appearances"):
        errors.append("manifest duplicate total does not match candidate inventory")
    if summary.get("alternate_links") != inventory.get("inventory", {}).get("additional_destination_link_count"):
        errors.append("manifest alternate-link total does not match candidate inventory")
    if summary.get("parser_exceptions") != inventory.get("inventory", {}).get("exception_count"):
        errors.append("manifest parser exception total does not match candidate inventory")
    if sum(item.get("source_entry_appearances", 0) for item in included.values()) != summary.get("source_entry_appearances"):
        errors.append("included file row counts do not reconcile to the source-entry total")
    expected_resource_dirs = sorted({PurePosixPath(path).parts[0] for path in expected})
    if manifest.get("resource_list_directories") != expected_resource_dirs:
        errors.append("source-list directory inventory does not match included resource lists")
    if set(manifest.get("markdown_source_directories", [])) - RESOURCE_DIRS - {"docs", ".github"}:
        errors.append("manifest contains a Markdown source directory without category review")
    excluded_by_reason = Counter(
        item.get("reason_code") for item in files
        if isinstance(item, dict) and item.get("disposition") == "excluded-repository-file"
    )
    if summary.get("excluded_files_by_reason") != dict(sorted(excluded_by_reason.items())):
        errors.append("excluded-file reason counts do not reconcile to the manifest")
    tree_hash_input = "\n".join(
        f"{item['path']}\0{item['sha256']}"
        for item in sorted(files, key=lambda row: row["path"])
        if isinstance(item, dict) and isinstance(item.get("path"), str)
    )
    if manifest.get("source_tree_sha256") != hashlib.sha256(tree_hash_input.encode("utf-8")).hexdigest():
        errors.append("source tree hash does not match manifest paths and file hashes")
    reconciliation = manifest.get("reconciliation", {})
    if not reconciliation.get("exact_candidate_records_match"):
        errors.append("source/target candidate reconciliation is not exact")
    if reconciliation.get("source_rows_without_disposition") != 0:
        errors.append("source rows are missing a disposition")
    if reconciliation.get("source_only_unique_destinations") or reconciliation.get("target_only_unique_destinations"):
        errors.append("source/target reconciliation has unmatched destinations")
    if reconciliation.get("record_content_mismatches") != 0:
        errors.append("source/target reconciliation contains record mismatches")
    if not reconciliation.get("source_file_path_manifest_matches"):
        errors.append("source file path reconciliation is incomplete")
    return errors


def _read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", type=Path, help="complete repository ZIP at the pinned source commit")
    parser.add_argument("--inventory", type=Path, default=INVENTORY_DEFAULT)
    parser.add_argument("--manifest-output", type=Path, default=MANIFEST_DEFAULT)
    parser.add_argument("--facets-output", type=Path, default=FACETS_DEFAULT)
    parser.add_argument("--check", action="store_true", help="validate generated manifest/facets against candidate inventory")
    args = parser.parse_args(argv)
    try:
        inventory = _read_json(args.inventory)
        if args.check:
            manifest = _read_json(args.manifest_output)
            facets = _read_json(args.facets_output)
            errors = validate_generated(manifest, facets, inventory)
            if errors:
                raise ValueError("\n".join(errors))
            summary = manifest["summary"]
            print(
                "Validated complete reference snapshot audit: "
                f"{summary['repository_file_count']} repository files, "
                f"{summary['included_resource_list_file_count']} included lists, "
                f"{summary['source_entry_appearances']} source appearances, "
                f"{summary['unique_destination_count']} unique candidates, "
                f"{summary['excluded_repository_file_count']} documented exclusions."
            )
            return 0
        if not args.archive:
            parser.error("--archive is required unless --check is used")
        manifest = build_source_manifest(args.archive, inventory)
        facets = build_facets(inventory)
        errors = validate_generated(manifest, facets, inventory)
        if errors:
            raise ValueError("\n".join(errors))
        args.manifest_output.parent.mkdir(parents=True, exist_ok=True)
        args.facets_output.parent.mkdir(parents=True, exist_ok=True)
        args.manifest_output.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
        args.facets_output.write_text(json.dumps(facets, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
        summary = manifest["summary"]
        print(
            "Wrote complete reference snapshot audit: "
            f"{summary['repository_file_count']} repository files, "
            f"{summary['included_resource_list_file_count']} included lists, "
            f"{summary['source_entry_appearances']} source appearances, "
            f"{summary['unique_destination_count']} unique candidates, "
            f"{summary['excluded_repository_file_count']} documented exclusions."
        )
        return 0
    except (OSError, zipfile.BadZipFile, json.JSONDecodeError, ValueError, KeyError) as error:
        print(f"Reference snapshot audit failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
