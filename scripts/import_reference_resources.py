"""Import a provenance-preserving index of reference repository link entries.

The generated records are unverified link candidates. They do not establish a
resource's availability, quality, access terms, or rights. Run with --help for
build and validation modes.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import sys
import zipfile
from collections import Counter, defaultdict
from pathlib import Path, PurePosixPath
from typing import Any
from urllib.parse import urlsplit, urlunsplit


ROOT = Path(__file__).resolve().parents[1]
ARCHIVE_ROOT = "free-programming-books-main/"
REFERENCE_REPOSITORY = "https://github.com/EbookFoundation/free-programming-books"
REFERENCE_REVISION = "2574d859ecf34dd8d1643cc5c7c9f11ae99f845c"
REFERENCE_LICENSE = "CC BY 4.0"
def attribution_for(revision: str) -> str:
    return (
        "Free Ebook Foundation, Free Programming Books, CC BY 4.0 "
        "(https://creativecommons.org/licenses/by/4.0/), "
        "https://github.com/EbookFoundation/free-programming-books/tree/"
        f"{revision}"
    )
EXPECTED_ARCHIVE_SHA256 = "a57382573afb96eed8623f41884e049b12b9fab54dcf43815629437906abd1e1"
OUTPUT_DEFAULT = ROOT / "data" / "reference_resources.json"

RESOURCE_DIRS = {"books", "courses", "casts", "more"}
LIST_ITEM = re.compile(r"^\s{0,12}(?:[-*+]\s+|\d+[.)]\s+)")
HEADING = re.compile(r"^\s{0,3}(#{1,6})\s+(.+?)\s*#*\s*$")
HTML_TAG = re.compile(r"<[^>]+>")
HTTP_IN_LINE = re.compile(r"https?://", re.I)


def _escaped(text: str, index: int) -> bool:
    backslashes = 0
    index -= 1
    while index >= 0 and text[index] == "\\":
        backslashes += 1
        index -= 1
    return backslashes % 2 == 1


def markdown_links(line: str) -> list[dict[str, str]]:
    """Read inline Markdown links with balanced labels and destination parens."""
    links: list[dict[str, str]] = []
    index = 0
    while index < len(line):
        opening = line.find("[", index)
        if opening < 0 or _escaped(line, opening):
            break
        # Do not treat an image's alt text as its resource title.
        if opening > 0 and line[opening - 1] == "!" and not _escaped(line, opening - 1):
            index = opening + 1
            continue
        depth = 1
        cursor = opening + 1
        while cursor < len(line) and depth:
            if not _escaped(line, cursor):
                if line[cursor] == "[":
                    depth += 1
                elif line[cursor] == "]":
                    depth -= 1
            cursor += 1
        if depth or cursor >= len(line) or line[cursor] != "(":
            index = opening + 1
            continue
        label = line[opening + 1 : cursor - 1]
        dest_start = cursor + 1
        while dest_start < len(line) and line[dest_start].isspace():
            dest_start += 1
        if dest_start >= len(line):
            break
        if line[dest_start] == "<":
            end = line.find(">", dest_start + 1)
            if end < 0:
                index = opening + 1
                continue
            destination = line[dest_start + 1 : end]
            close = line.find(")", end + 1)
        else:
            end = dest_start
            parens = 0
            while end < len(line):
                char = line[end]
                if _escaped(line, end):
                    end += 1
                    continue
                if char == "(" :
                    parens += 1
                elif char == ")":
                    if parens == 0:
                        break
                    parens -= 1
                elif char.isspace() and parens == 0:
                    break
                end += 1
            destination = line[dest_start:end]
            close = end if end < len(line) and line[end] == ")" else line.find(")", end)
        if close >= 0:
            destination = destination.replace(r"\(", "(").replace(r"\)", ")")
            destination = html.unescape(destination.strip())
            if urlsplit(destination).scheme.lower() in {"http", "https"}:
                cleaned_label = html.unescape(HTML_TAG.sub("", label)).strip()
                links.append({"label": cleaned_label, "url": destination, "end": str(close + 1)})
            index = close + 1
        else:
            index = opening + 1
    return links


def normalized_url(value: str) -> str:
    """Normalize only scheme/host case and fragments for duplicate grouping."""
    parsed = urlsplit(value)
    host = parsed.netloc.lower()
    scheme = parsed.scheme.lower()
    path = parsed.path
    return urlunsplit((scheme, host, path, parsed.query, ""))


def clean_heading(raw: str) -> str:
    text = re.sub(r"<a\s+id=[\"'][^\"']+[\"']\s*></a>", "", raw, flags=re.I)
    text = HTML_TAG.sub("", text)
    text = re.sub(r"\\([\\`*_{}\[\]()#+.!<>|])", r"\1", text)
    text = html.unescape(text)
    return " ".join(text.split()).strip(" #")


def classify_file(path: str) -> tuple[str, str | None]:
    parts = PurePosixPath(path).parts
    area = parts[0]
    stem = PurePosixPath(path).stem
    if area == "books":
        resource_type = "book"
        prefix = "free-programming-books-"
    elif area == "courses":
        resource_type = "course"
        prefix = "free-courses-"
    elif area == "casts":
        resource_type = "media"
        prefix = "free-podcasts-screencasts-"
    else:
        if "cheatsheet" in stem:
            resource_type = "cheatsheet"
            prefix = ""
        elif "interactive-tutorial" in stem:
            resource_type = "interactive-tutorial"
            prefix = "free-programming-interactive-tutorials-"
        elif "playground" in stem:
            resource_type = "playground"
            prefix = "free-programming-playgrounds-"
        elif "problem-set" in stem or "competitive-programming" in stem:
            resource_type = "problem-set"
            prefix = ""
        else:
            resource_type = "other-learning-resource"
            prefix = ""
    locale = stem[len(prefix) :] if prefix and stem.startswith(prefix) else None
    if locale in {"", "langs", "subjects"}:
        locale = None
    return resource_type, locale


def source_file_paths(archive: zipfile.ZipFile) -> list[str]:
    return sorted(
        name
        for name in archive.namelist()
        if name.startswith(ARCHIVE_ROOT)
        and name.lower().endswith(".md")
        and len(PurePosixPath(name).parts) >= 3
        and PurePosixPath(name).parts[1] in RESOURCE_DIRS
    )


def build_inventory(
    archive_path: Path,
    expected_archive_sha256: str | None = EXPECTED_ARCHIVE_SHA256,
    source_revision: str = REFERENCE_REVISION,
) -> dict[str, Any]:
    archive_digest = hashlib.sha256(archive_path.read_bytes()).hexdigest()
    if expected_archive_sha256 and archive_digest != expected_archive_sha256:
        raise ValueError(
            "archive SHA-256 does not match the audited source snapshot: "
            f"expected {expected_archive_sha256}, got {archive_digest}"
        )

    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    exceptions: list[dict[str, Any]] = []
    file_manifest: list[dict[str, Any]] = []
    line_entries = 0
    by_file_counts: Counter[str] = Counter()

    with zipfile.ZipFile(archive_path) as archive:
        paths = source_file_paths(archive)
        for archive_path_name in paths:
            raw = archive.read(archive_path_name)
            content = raw.decode("utf-8-sig", errors="replace")
            file_manifest.append({
                "path": archive_path_name.removeprefix(ARCHIVE_ROOT),
                "sha256": hashlib.sha256(raw).hexdigest(),
                "bytes": len(raw),
            })
            section_stack: list[tuple[int, str]] = []
            category, source_locale = classify_file(archive_path_name.removeprefix(ARCHIVE_ROOT))
            last_occurrence: dict[str, Any] | None = None
            for line_number, line in enumerate(content.splitlines(), start=1):
                heading = HEADING.match(line)
                if heading:
                    level = len(heading.group(1))
                    title = clean_heading(heading.group(2))
                    while section_stack and section_stack[-1][0] >= level:
                        section_stack.pop()
                    if title and title.lower() != "index":
                        section_stack.append((level, title))
                    continue
                links = markdown_links(line)
                external_links = [link for link in links if urlsplit(link["url"]).scheme.lower() in {"http", "https"}]
                if not line.strip():
                    last_occurrence = None
                    continue
                if not HTTP_IN_LINE.search(line):
                    continue
                if external_links and not LIST_ITEM.match(line) and last_occurrence and line.lstrip().startswith("["):
                    for link in external_links:
                        last_occurrence["additional_links"].append({
                            "label": link["label"],
                            "url": link["url"],
                            "source_line": line_number,
                        })
                    continue
                if not LIST_ITEM.match(line) or not external_links:
                    exceptions.append({
                        "source_path": archive_path_name.removeprefix(ARCHIVE_ROOT),
                        "line": line_number,
                        "reason": "external URL line is not a parsed resource list item",
                        "content_sha256": hashlib.sha256(line.encode("utf-8")).hexdigest(),
                        "source_text": line,
                    })
                    continue
                line_entries += 1
                by_file_counts[archive_path_name.removeprefix(ARCHIVE_ROOT)] += 1
                primary = external_links[0]
                key = normalized_url(primary["url"])
                occurrence = {
                    "source_path": archive_path_name.removeprefix(ARCHIVE_ROOT),
                    "source_line": line_number,
                    "source_list_category": PurePosixPath(archive_path_name).parts[1],
                        "resource_type": (
                            "podcast" if category == "media" and re.search(r"\(podcast\)", line, re.I)
                            else "screencast" if category == "media" and re.search(r"\(screencast\)", line, re.I)
                            else category
                        ),
                    "source_list_locale": source_locale,
                    "topic_path": [title for _, title in section_stack],
                    "title": primary["label"] or primary["url"],
                    "url": primary["url"],
                    "additional_links": [
                        {"label": link["label"], "url": link["url"], "source_line": line_number}
                        for link in external_links[1:]
                    ],
                    "source_annotation": line[int(primary["end"]) :].strip(),
                }
                grouped[key].append(occurrence)
                last_occurrence = occurrence

    records: list[dict[str, Any]] = []
    for key in sorted(grouped):
        occurrences = sorted(
            grouped[key],
            key=lambda item: (item["source_path"], item["source_line"], item["title"]),
        )
        first = occurrences[0]
        identifier = "reference-" + hashlib.sha256(key.encode("utf-8")).hexdigest()[:20]
        records.append({
            "id": identifier,
            "title": first["title"],
            "url": first["url"],
            "normalized_url": key,
            "resource_types": sorted({item["resource_type"] for item in occurrences}),
            "topics": sorted({topic for item in occurrences for topic in item["topic_path"]}),
            "source_list_locales": sorted({item["source_list_locale"] for item in occurrences if item["source_list_locale"]}),
            "verification_status": "unverified",
            "rights_status": "not-assessed",
            "access_status": "not-checked",
            "source_occurrences": occurrences,
        })

    type_counts: Counter[str] = Counter()
    for record in records:
        type_counts.update(record["resource_types"])
    return {
        "schema_version": 1,
        "dataset_kind": "unverified-reference-link-candidates",
        "license": REFERENCE_LICENSE,
        "attribution": attribution_for(source_revision),
        "derivative_note": (
            "Tajkart extracted and deduplicated destination links while retaining "
            "source file, source line, topic path, list locale, and available row annotations."
        ),
        "source": {
            "repository": REFERENCE_REPOSITORY,
            "revision": source_revision,
            "input_archive_sha256": archive_digest,
            "archive_root": ARCHIVE_ROOT.rstrip("/"),
            "scope": "books, courses, casts, and more Markdown resource lists",
        },
        "inventory": {
            "source_file_count": len(file_manifest),
            "source_list_entry_count": line_entries,
            "unique_destination_count": len(records),
            "duplicate_appearances": line_entries - len(records),
            "additional_destination_link_count": sum(
                len(occurrence["additional_links"])
                for record in records
                for occurrence in record["source_occurrences"]
            ),
            "exception_count": len(exceptions),
            "resource_types_by_unique_destination": dict(sorted(type_counts.items())),
            "source_files_with_entries": len(by_file_counts),
        },
        "publication_policy": (
            "These are link candidates transcribed from a CC BY 4.0 source index. "
            "Tajkart has not checked destination availability, provider identity, "
            "quality, access terms, or rights for any candidate. Do not describe "
            "them as verified or redistribute linked works."
        ),
        "source_files": file_manifest,
        "records": records,
        "exceptions": sorted(exceptions, key=lambda item: (item["source_path"], item["line"])),
    }


def validate_inventory(
    inventory: object,
    expected_archive_sha256: str | None = EXPECTED_ARCHIVE_SHA256,
) -> list[str]:
    errors: list[str] = []
    if not isinstance(inventory, dict) or inventory.get("schema_version") != 1:
        return ["inventory must be an object with schema_version 1"]
    if inventory.get("dataset_kind") != "unverified-reference-link-candidates":
        errors.append("dataset_kind must preserve the unverified candidate state")
    if inventory.get("license") != REFERENCE_LICENSE or "CC BY 4.0" not in str(inventory.get("attribution", "")):
        errors.append("dataset must include the source license and attribution")
    source = inventory.get("source")
    input_digest = source.get("input_archive_sha256") if isinstance(source, dict) else None
    if not isinstance(source, dict) or not isinstance(input_digest, str) or not re.fullmatch(r"[a-f0-9]{64}", input_digest):
        errors.append("source snapshot SHA-256 is missing or unexpected")
    elif expected_archive_sha256 and input_digest != expected_archive_sha256:
        errors.append("source snapshot SHA-256 does not match the expected input")
    if not isinstance(source, dict) or not isinstance(source.get("revision"), str) or not re.fullmatch(r"[a-f0-9]{40}", source.get("revision", "")):
        errors.append("source revision must be a pinned 40-character commit")
    source_files = inventory.get("source_files")
    if not isinstance(source_files, list):
        errors.append("source_files must be an array")
        source_paths: set[str] = set()
    else:
        source_paths = set()
        for source_file in source_files:
            if not isinstance(source_file, dict) or not isinstance(source_file.get("path"), str):
                errors.append("source file manifest contains an invalid entry")
                continue
            if source_file["path"] in source_paths:
                errors.append(f"duplicate source file manifest path {source_file['path']}")
            source_paths.add(source_file["path"])
            if not re.fullmatch(r"[a-f0-9]{64}", str(source_file.get("sha256", ""))):
                errors.append(f"invalid source file hash for {source_file['path']}")
    records = inventory.get("records")
    if not isinstance(records, list):
        return errors + ["records must be an array"]
    ids: set[str] = set()
    urls: set[str] = set()
    occurrence_count = 0
    additional_link_count = 0
    occurrence_files: set[str] = set()
    type_counts: Counter[str] = Counter()
    for index, record in enumerate(records):
        label = f"record {index + 1}"
        if not isinstance(record, dict):
            errors.append(f"{label} must be an object")
            continue
        identifier = record.get("id")
        if not isinstance(identifier, str) or not re.fullmatch(r"reference-[a-f0-9]{20}", identifier):
            errors.append(f"{label} has an invalid stable id")
        elif identifier in ids:
            errors.append(f"duplicate candidate id {identifier}")
        ids.add(identifier)
        url = record.get("url")
        normalized = record.get("normalized_url")
        if not isinstance(url, str) or urlsplit(url).scheme.lower() not in {"http", "https"}:
            errors.append(f"{label} has no HTTP(S) destination")
        elif normalized in urls:
            errors.append(f"duplicate normalized candidate URL {normalized}")
        else:
            urls.add(normalized)
        if isinstance(normalized, str) and isinstance(url, str):
            if normalized_url(url) != normalized:
                errors.append(f"{label} has a mismatched normalized destination")
            expected_id = "reference-" + hashlib.sha256(normalized.encode("utf-8")).hexdigest()[:20]
            if identifier != expected_id:
                errors.append(f"{label} id is not stable for its normalized destination")
        if record.get("verification_status") != "unverified":
            errors.append(f"{label} must remain unverified until human review")
        if record.get("rights_status") != "not-assessed" or record.get("access_status") != "not-checked":
            errors.append(f"{label} must not imply rights/access review")
        resource_types = record.get("resource_types")
        if isinstance(resource_types, list):
            type_counts.update(set(resource_types))
        occurrences = record.get("source_occurrences")
        if not isinstance(occurrences, list) or not occurrences:
            errors.append(f"{label} must preserve at least one source occurrence")
            continue
        occurrence_count += len(occurrences)
        for occurrence in occurrences:
            if not all(occurrence.get(field) for field in ("source_path", "source_line", "title", "url", "resource_type")):
                errors.append(f"{label} contains an occurrence missing source provenance")
            elif normalized_url(occurrence["url"]) != normalized:
                errors.append(f"{label} source occurrence does not point to its grouped destination")
            if not isinstance(occurrence.get("source_line"), int) or occurrence.get("source_line", 0) < 1:
                errors.append(f"{label} has an invalid source line number")
            path = occurrence.get("source_path")
            if isinstance(path, str):
                occurrence_files.add(path)
                if path not in source_paths:
                    errors.append(f"{label} references a source file absent from the manifest: {path}")
            if isinstance(occurrence.get("additional_links"), list):
                additional_link_count += len(occurrence["additional_links"])
    stats = inventory.get("inventory", {})
    if isinstance(stats, dict):
        if stats.get("source_file_count") != len(source_paths):
            errors.append("source_file_count does not match the source file manifest")
        if stats.get("unique_destination_count") != len(records):
            errors.append("unique_destination_count does not match records")
        if stats.get("source_list_entry_count") != occurrence_count:
            errors.append("source_list_entry_count does not match preserved occurrences")
        if stats.get("duplicate_appearances") != occurrence_count - len(records):
            errors.append("duplicate_appearances does not match preserved occurrences")
        if stats.get("additional_destination_link_count") != additional_link_count:
            errors.append("additional_destination_link_count does not match occurrences")
        if stats.get("source_files_with_entries") != len(occurrence_files):
            errors.append("source_files_with_entries does not match source occurrences")
        if stats.get("resource_types_by_unique_destination") != dict(sorted(type_counts.items())):
            errors.append("resource type counts do not match candidate records")
        exceptions = inventory.get("exceptions")
        if not isinstance(exceptions, list) or stats.get("exception_count") != len(exceptions):
            errors.append("exception_count does not match exception report")
        elif any(not isinstance(item, dict) or item.get("source_path") not in source_paths for item in exceptions):
            errors.append("exception report references an unknown source file")
    return errors


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", type=Path, help="source ZIP at the selected --revision; required to build")
    parser.add_argument("--revision", default=REFERENCE_REVISION, help="source repository commit recorded in provenance")
    parser.add_argument("--expected-sha256", help="expected input ZIP hash; defaults to the supplied audited snapshot hash")
    parser.add_argument("--output", type=Path, default=OUTPUT_DEFAULT)
    parser.add_argument("--check", action="store_true", help="validate an existing generated JSON file")
    args = parser.parse_args(argv)

    try:
        if args.check:
            data = json.loads(args.output.read_text(encoding="utf-8"))
            errors = validate_inventory(data, expected_archive_sha256=args.expected_sha256)
            if errors:
                raise ValueError("\n".join(errors))
            stats = data["inventory"]
            print(
                "Validated reference candidate inventory: "
                f"{stats['source_file_count']} source files, "
                f"{stats['source_list_entry_count']} list appearances, "
                f"{stats['unique_destination_count']} unique destinations, "
                f"{stats['exception_count']} exceptions."
            )
            return 0
        if not args.archive:
            parser.error("--archive is required unless --check is used")
        expected = args.expected_sha256
        if expected is None and args.revision == REFERENCE_REVISION:
            expected = EXPECTED_ARCHIVE_SHA256
        inventory = build_inventory(args.archive, expected, args.revision)
        errors = validate_inventory(inventory, expected)
        if errors:
            raise ValueError("\n".join(errors))
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(
            json.dumps(inventory, ensure_ascii=False, separators=(",", ":")) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        stats = inventory["inventory"]
        print(
            f"Wrote {args.output}: {stats['source_file_count']} source files, "
            f"{stats['source_list_entry_count']} list appearances, "
            f"{stats['unique_destination_count']} unique destinations, "
            f"{stats['exception_count']} exceptions."
        )
        return 0
    except (OSError, zipfile.BadZipFile, json.JSONDecodeError, ValueError) as error:
        print(f"Reference inventory import failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
