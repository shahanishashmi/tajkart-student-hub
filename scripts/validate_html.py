"""Check a generated Jekyll site for basic document, control, and index integrity."""

from __future__ import annotations

import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
CONFIG = (ROOT / "_config.yml").read_text(encoding="utf-8")
BASEURL_MATCH = re.search(r'(?m)^baseurl:\s*["\']?([^"\'\s]*)', CONFIG)
BASEURL = BASEURL_MATCH.group(1) if BASEURL_MATCH else ""


class Document(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.ids: set[str] = set()
        self.duplicates: list[str] = []
        self.html_lang = ""
        self.mains = 0
        self.images_missing_alt: int = 0
        self.controls: list[dict[str, str | bool]] = []
        self.labels_for: set[str] = set()
        self.labels_aria: set[str] = set()
        self.label_depth = 0
        self.heading_levels: list[int] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key: value or "" for key, value in attrs}
        element_id = values.get("id", "")
        if element_id:
            if element_id in self.ids:
                self.duplicates.append(element_id)
            self.ids.add(element_id)
        if tag == "html":
            self.html_lang = values.get("lang", "")
        elif tag == "main":
            self.mains += 1
        elif tag == "img" and "alt" not in values:
            self.images_missing_alt += 1
        elif tag in {"input", "select", "textarea"}:
            if tag == "input" and values.get("type", "text").lower() in {"hidden", "submit", "button", "reset"}:
                return
            self.controls.append({"id": element_id, "aria": values.get("aria-label", "") or values.get("aria-labelledby", ""), "wrapped": self.label_depth > 0})
        elif tag == "label":
            self.label_depth += 1
            if values.get("for"):
                self.labels_for.add(values["for"])
            if values.get("aria-label"):
                self.labels_aria.add(values["aria-label"])
        elif re.fullmatch(r"h[1-6]", tag):
            self.heading_levels.append(int(tag[1]))

    def handle_endtag(self, tag: str) -> None:
        if tag == "label" and self.label_depth:
            self.label_depth -= 1


def route_file(site: Path, href: str) -> Path | None:
    parsed = urlsplit(href)
    if parsed.scheme or parsed.netloc or href.startswith(("//", "mailto:", "tel:", "data:", "javascript:")):
        return None
    path = unquote(parsed.path)
    if not path:
        return None
    if path == BASEURL:
        path = "/"
    elif path.startswith(BASEURL + "/"):
        path = path[len(BASEURL):]
    elif path.startswith("/"):
        return site / "__missing_baseurl__" / path.lstrip("/")
    target = site / path.lstrip("/")
    if target.is_file():
        return target
    if path.endswith("/") or not target.suffix:
        return target / "index.html"
    return target


def source_searchable_ids() -> set[str]:
    ids: set[str] = set()
    front = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.S)
    for path in ROOT.rglob("*.md"):
        if any(part.startswith(".") for part in path.relative_to(ROOT).parts) or "vendor" in path.parts:
            continue
        match = front.match(path.read_text(encoding="utf-8"))
        if not match or not re.search(r"(?m)^searchable:\s*true\s*$", match.group(1)):
            continue
        found = re.search(r"(?m)^id:\s*[\"']?([^\s\"']+)", match.group(1))
        if found:
            ids.add(found.group(1))
    return ids


def main() -> int:
    site = Path(sys.argv[1] if len(sys.argv) > 1 else ROOT / "_site").resolve()
    if not site.is_dir():
        print(f"Generated site directory not found: {site}")
        return 2
    errors: list[str] = []
    documents = sorted(site.rglob("*.html"))
    if not documents:
        print(f"No generated HTML files found in {site}")
        return 2
    parsed_documents: dict[Path, Document] = {}
    for path in documents:
        parser = Document()
        html = path.read_text(encoding="utf-8")
        parser.feed(html)
        parsed_documents[path] = parser
        relative = path.relative_to(site)
        if not parser.html_lang:
            errors.append(f"missing html lang: {relative}")
        if parser.mains != 1:
            errors.append(f"expected one main landmark, found {parser.mains}: {relative}")
        if parser.duplicates:
            errors.append(f"duplicate HTML id(s) {', '.join(parser.duplicates)}: {relative}")
        if parser.images_missing_alt:
            errors.append(f"{parser.images_missing_alt} image(s) missing alt attribute: {relative}")
        for control in parser.controls:
            if control["wrapped"] or control["aria"] or (control["id"] and control["id"] in parser.labels_for):
                continue
            errors.append(f"form control lacks an accessible label (id={control['id']!r}): {relative}")
        # Ensure each heading level advances by at most one step.
        previous = 0
        for level in parser.heading_levels:
            if previous and level > previous + 1:
                errors.append(f"heading level skips from h{previous} to h{level}: {relative}")
                break
            previous = level
        for href in re.findall(r"(?is)\bhref\s*=\s*['\"]([^'\"]+)['\"]", html):
            target = route_file(site, href)
            if target is not None and not target.is_file():
                errors.append(f"broken generated link {href}: {relative}")
            parsed_href = urlsplit(href)
            if parsed_href.fragment and not parsed_href.scheme and not parsed_href.netloc:
                fragment_target = path if not parsed_href.path else target
                target_parser = parsed_documents.get(fragment_target) if fragment_target else None
                if target_parser and unquote(parsed_href.fragment) not in target_parser.ids:
                    errors.append(f"broken generated fragment {href}: {relative}")

    index_path = site / "search-index.json"
    indexed_count = 0
    if not index_path.is_file():
        errors.append("generated search-index.json is missing")
    else:
        try:
            items = json.loads(index_path.read_text(encoding="utf-8"))
            if not isinstance(items, list):
                raise ValueError("search index root must be an array")
            indexed_count = len(items)
            seen: set[str] = set()
            for item in items:
                if not isinstance(item, dict):
                    errors.append("search index contains a non-object entry")
                    continue
                required = ("id", "title", "url", "type", "category", "language", "difficulty", "tags", "origin", "content_status", "review_status")
                missing = [key for key in required if key not in item]
                if missing:
                    errors.append(f"search index item missing {', '.join(missing)}")
                    continue
                if item["id"] in seen:
                    errors.append(f"duplicate search index id: {item['id']}")
                seen.add(item["id"])
                if item["origin"] not in {"original", "translation", "external"}:
                    errors.append(f"search index item has invalid origin: {item['id']}")
                if item["origin"] == "translation" and (not item.get("translation_of") or item.get("translation_status") not in {"draft", "review-required", "approved"}):
                    errors.append(f"search index translation is missing source or status: {item['id']}")
                if item["origin"] == "external" and (not item.get("source_url") or not item.get("source_checked") or not item.get("creator") or not item.get("attribution") or not item.get("rights_note") or item.get("rights_status") not in {"link-only", "license-identified", "permission-granted", "public-domain"} or item.get("verification_status") != "verified"):
                    errors.append(f"search index external resource is missing source or rights metadata: {item['id']}")
                target = route_file(site, str(item["url"]))
                if target is not None and not target.is_file():
                    errors.append(f"search index route does not exist: {item['url']}")
            expected = source_searchable_ids()
            if seen != expected:
                errors.append(f"search index/source mismatch: {len(seen)} indexed IDs, {len(expected)} searchable source IDs")
        except (json.JSONDecodeError, ValueError) as error:
            errors.append(f"invalid generated search-index.json: {error}")

    if errors:
        print("Generated-site validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Validated {len(documents)} generated HTML pages and {indexed_count} searchable resources; local links/fragments, unique IDs, labelled controls, language, landmarks, and provenance metadata pass.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
