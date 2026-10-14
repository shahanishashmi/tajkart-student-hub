"""Validate source routes, searchable metadata, local links, and Python examples."""

from __future__ import annotations

import re
import json
import sys
from datetime import date
from pathlib import Path, PurePosixPath
from urllib.parse import urlsplit


ROOT = Path(__file__).resolve().parents[1]
FRONT_MATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.S)
MARKDOWN_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
LIQUID_PATH = re.compile(r"\{\{\s*['\"]([^'\"]+)['\"]\s*\|\s*relative_url\s*\}\}")
PYTHON_BLOCK = re.compile(r"```python\s*\n(.*?)\n```", re.S)
SCALAR = re.compile(r"(?m)^([a-z_]+):[ \t]*([^\r\n]*?)[ \t]*$")
VALID_TYPES = {"lesson", "guide", "course", "cheatsheet", "problem-set", "project", "interactive", "career", "opportunity-guide"}
VALID_CONTENT = {"not-started", "in-progress", "drafted", "review-required", "validated", "complete"}
VALID_REVIEW = {"not-reviewed", "pending", "technical-reviewed", "language-reviewed", "accessibility-reviewed", "approved"}
VALID_DIFFICULTY = {"beginner", "intermediate", "advanced", "all-levels"}
VALID_ORIGINS = {"original", "translation", "external"}
VALID_TRANSLATION_STATES = {"draft", "review-required", "approved"}
VALID_RIGHTS_STATES = {"link-only", "license-identified", "permission-granted", "public-domain"}
VALID_EXTERNAL_VERIFICATION = {"verified"}


def valid_http_url(value: str) -> bool:
    try:
        parsed = urlsplit(value)
        return parsed.scheme in {"http", "https"} and bool(parsed.hostname) and not parsed.username and not parsed.password
    except ValueError:
        return False


def markdown_files() -> list[Path]:
    return [
        path for path in ROOT.rglob("*.md")
        if not any(part.startswith(".") for part in path.relative_to(ROOT).parts)
        and "vendor" not in path.parts
    ]


def fields(metadata: str) -> dict[str, str]:
    return {key: value.strip().strip("\"'") for key, value in SCALAR.findall(metadata)}


def route_for(path: Path, metadata: str | None) -> str:
    if metadata:
        route = fields(metadata).get("permalink")
        if route:
            return route
    relative = path.relative_to(ROOT).with_suffix("")
    if relative.name.lower() == "index":
        relative = relative.parent
    elif relative.name.lower() == "readme":
        return "/" + relative.as_posix() + ".html"
    return "/" + relative.as_posix().strip("/") + "/"


def list_value(metadata: str, key: str) -> list[str]:
    inline = re.search(rf"(?m)^{re.escape(key)}:\s*\[([^]]*)\]", metadata)
    if inline:
        return [value.strip().strip("\"'") for value in inline.group(1).split(",") if value.strip()]
    block = re.search(rf"(?ms)^{re.escape(key)}:\s*\n((?:[ \t]+-\s+.*\n?)*)", metadata)
    if block:
        return [re.sub(r"^\s+-\s+", "", line).strip().strip("\"'") for line in block.group(1).splitlines() if line.strip()]
    return []


def main() -> int:
    files = markdown_files()
    routes: dict[str, Path] = {}
    canonical_routes: dict[str, Path] = {}
    ids: dict[str, Path] = {}
    searchable: dict[str, Path] = {}
    prerequisites: list[tuple[Path, str]] = []
    related_references: list[tuple[Path, str]] = []
    translations: list[tuple[Path, str]] = []
    errors: list[str] = []
    config = (ROOT / "_config.yml").read_text(encoding="utf-8")
    origin_default_match = re.search(r"(?m)^\s*content_origin:\s*([a-z-]+)\s*$", config)
    default_origin = origin_default_match.group(1) if origin_default_match else ""
    if default_origin not in VALID_ORIGINS:
        errors.append("_config.yml must set a valid default content_origin")

    for path in (ROOT / "data").glob("*.json"):
        try:
            json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            errors.append(f"invalid JSON in {path.relative_to(ROOT)} at line {error.lineno}: {error.msg}")

    for path in files:
        source = path.read_text(encoding="utf-8")
        match = FRONT_MATTER.match(source)
        if not match:
            continue
        metadata = match.group(1)
        values = fields(metadata)
        relative = path.relative_to(ROOT)
        route = route_for(path, metadata)
        if not route.startswith("/"):
            errors.append(f"permalink must start with /: {route} in {relative}")
        suffix = PurePosixPath(route).suffix.lower()
        canonical_route = route if suffix in {".html", ".json", ".xml", ".txt", ".svg", ".css", ".js", ".yml", ".yaml"} else route.rstrip("/") + "/"
        if suffix not in {".html", ".json", ".xml", ".txt", ".svg", ".css", ".js", ".yml", ".yaml"} and not route.endswith("/"):
            errors.append(f"page permalink should use a trailing slash: {route} in {relative}")
        if canonical_route in canonical_routes:
            errors.append(f"duplicate route/slug {canonical_route}: {canonical_routes[canonical_route].relative_to(ROOT)} and {relative}")
        canonical_routes[canonical_route] = path
        routes[route] = path
        if "title" not in values or not values["title"]:
            errors.append(f"missing title in front matter: {relative}")
        if values.get("searchable") != "true":
            continue

        required = ("id", "permalink", "content_type", "category", "language", "difficulty", "content_status", "review_status")
        for key in required:
            if not values.get(key):
                errors.append(f"searchable resource missing {key}: {relative}")
        origin = values.get("content_origin", default_origin)
        if origin not in VALID_ORIGINS:
            errors.append(f"invalid content_origin {origin!r}: {relative}")
        if origin == "translation":
            translation_of = values.get("translation_of", "")
            translation_status = values.get("translation_status", "")
            if not translation_of:
                errors.append(f"translation is missing translation_of: {relative}")
            else:
                translations.append((path, translation_of))
            if translation_status not in VALID_TRANSLATION_STATES:
                errors.append(f"invalid or missing translation_status {translation_status!r}: {relative}")
            if translation_status == "draft" and values.get("review_status") == "approved":
                errors.append(f"draft translation cannot have approved review_status: {relative}")
        elif values.get("translation_of") or values.get("translation_status"):
            errors.append(f"non-translation resource has translation metadata: {relative}")
        if origin == "external":
            for key in ("creator", "source_url", "attribution", "rights_status", "rights_note", "source_checked", "verification_status"):
                if not values.get(key):
                    errors.append(f"external resource missing {key}: {relative}")
            source_url = values.get("source_url", "")
            if source_url and not valid_http_url(source_url):
                errors.append(f"external resource has invalid source_url {source_url!r}: {relative}")
            rights_status = values.get("rights_status", "")
            if rights_status and rights_status not in VALID_RIGHTS_STATES:
                errors.append(f"external resource needs a resolved rights_status, got {rights_status!r}: {relative}")
            checked = values.get("source_checked", "")
            try:
                if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", checked):
                    raise ValueError("expected YYYY-MM-DD")
                date.fromisoformat(checked)
            except ValueError:
                errors.append(f"external resource has invalid source_checked date {checked!r}: {relative}")
            if rights_status == "license-identified" and not values.get("terms_or_license"):
                errors.append(f"licensed external resource is missing terms_or_license: {relative}")
            if values.get("verification_status") not in VALID_EXTERNAL_VERIFICATION:
                errors.append(f"external resource must be verified before publication: {relative}")
        resource_id = values.get("id", "")
        if resource_id:
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", resource_id):
                errors.append(f"invalid resource id {resource_id!r}: {relative}")
            if resource_id in ids:
                errors.append(f"duplicate resource id {resource_id}: {ids[resource_id].relative_to(ROOT)} and {relative}")
            ids[resource_id] = path
            searchable[resource_id] = path
        if values.get("content_type") not in VALID_TYPES:
            errors.append(f"invalid content_type {values.get('content_type')!r}: {relative}")
        if values.get("difficulty") not in VALID_DIFFICULTY:
            errors.append(f"invalid difficulty {values.get('difficulty')!r}: {relative}")
        if values.get("content_status") not in VALID_CONTENT:
            errors.append(f"invalid content_status {values.get('content_status')!r}: {relative}")
        if values.get("review_status") not in VALID_REVIEW:
            errors.append(f"invalid review_status {values.get('review_status')!r}: {relative}")
        for key in ("tags", "learning_objectives"):
            if not list_value(metadata, key):
                errors.append(f"searchable resource needs a non-empty {key} list: {relative}")
        for prerequisite in list_value(metadata, "prerequisites"):
            if re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", prerequisite):
                prerequisites.append((path, prerequisite))
        related_references.extend((path, related_id) for related_id in list_value(metadata, "related_resources"))
        body = FRONT_MATTER.sub("", source, count=1).strip()
        if len(body) < 240:
            errors.append(f"searchable resource has too little explanatory content: {relative}")
        headings = {heading.strip().lower() for heading in re.findall(r"(?m)^#{2,6}\s+(.+?)\s*#*\s*$", body)}
        if values.get("content_type") == "lesson":
            if values.get("language") == "en":
                for section in ("prerequisites", "common mistakes"):
                    if not any(section in heading for heading in headings):
                        errors.append(f"lesson missing a {section} section: {relative}")
                if not any("practice" in heading for heading in headings):
                    errors.append(f"lesson missing a practice section: {relative}")
                if not any("next step" in heading or "further learning" in heading for heading in headings):
                    errors.append(f"lesson missing a next-step section: {relative}")
            if not re.search(r"```(?:python|sh|bash)\s*\n", body):
                errors.append(f"lesson missing a runnable code or command example: {relative}")
        elif values.get("content_type") == "problem-set":
            if not any("problem" in heading for heading in headings):
                errors.append(f"problem set missing its statement section: {relative}")
            if not any("example" in heading or "input" in heading or "sample" in heading for heading in headings):
                errors.append(f"problem set missing an example or input/output section: {relative}")
            if not any("hint" in heading for heading in headings):
                errors.append(f"problem set missing a hint section: {relative}")
            if not any("solution" in heading for heading in headings):
                errors.append(f"problem set missing a reference solution: {relative}")

    for path, prerequisite in prerequisites:
        if prerequisite not in ids:
            errors.append(f"unknown prerequisite id {prerequisite}: {path.relative_to(ROOT)}")
    for path, related_id in related_references:
        if related_id not in ids:
            errors.append(f"unknown related resource id {related_id}: {path.relative_to(ROOT)}")
    for path, source_id in translations:
        if source_id not in ids:
            errors.append(f"unknown translation source id {source_id}: {path.relative_to(ROOT)}")
        else:
            source_match = FRONT_MATTER.match(ids[source_id].read_text(encoding="utf-8"))
            source_origin = fields(source_match.group(1)).get("content_origin", default_origin) if source_match else default_origin
            if source_origin != "original":
                errors.append(f"translation source must be an original resource: {source_id}: {path.relative_to(ROOT)}")

    for path in files:
        source = path.read_text(encoding="utf-8")
        for number, block in enumerate(PYTHON_BLOCK.findall(source), start=1):
            def include(match: re.Match[str]) -> str:
                include_path = ROOT / "_includes" / "solutions" / match.group(1)
                if not include_path.is_file():
                    errors.append(f"missing Python solution include {match.group(1)}: {path.relative_to(ROOT)}")
                    return ""
                return include_path.read_text(encoding="utf-8")

            expanded = re.sub(r"\{%\s*include\s+solutions/([a-z0-9_.-]+)\s*%\}", include, block)
            if "{%" in expanded or "{{" in expanded:
                errors.append(f"unresolved Liquid in Python example: {path.relative_to(ROOT)} block {number}")
                continue
            try:
                compile(expanded, f"{path.relative_to(ROOT)}:python-example-{number}", "exec")
            except SyntaxError as error:
                errors.append(f"invalid Python example in {path.relative_to(ROOT)} block {number}: {error.msg} (line {error.lineno})")

        for solution in re.findall(r"(?m)^\s*\{%\s*include\s+solutions/([a-z0-9_.-]+)\s*%\}\s*$", source):
            if not (ROOT / "_includes" / "solutions" / solution).is_file():
                errors.append(f"missing solution include {solution}: {path.relative_to(ROOT)}")

        source = FRONT_MATTER.sub("", source, count=1)
        for match in MARKDOWN_LINK.finditer(source):
            target = match.group(1).strip("<>\"'")
            liquid = LIQUID_PATH.search(target)
            if liquid:
                target = liquid.group(1)
            else:
                target = target.split()[0]
            if not target or target.startswith(("http://", "https://", "mailto:", "tel:", "#", "data:")):
                continue
            target = target.split("#", 1)[0].split("?", 1)[0]
            if not target:
                continue
            if target.startswith("/"):
                if target in routes or target.rstrip("/") + "/" in routes or target == "/404.html":
                    continue
                if (ROOT / target.lstrip("/")).is_file():
                    continue
                errors.append(f"unresolved site route {target}: {path.relative_to(ROOT)}")
                continue
            if target.endswith("/") and ("/" + target.strip("/") + "/") in routes:
                continue
            resolved = (path.parent / PurePosixPath(target)).resolve()
            if resolved.is_file() and ROOT in resolved.parents:
                continue
            errors.append(f"missing local file {target}: {path.relative_to(ROOT)}")

    if errors:
        print("Site validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Validated {len(files)} Markdown files, {len(routes)} routes, and {len(searchable)} searchable resources; 0 missing titles/required fields, duplicate resource IDs/routes, invalid curated source URLs, unknown references, Python syntax errors, or broken local Markdown links.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
