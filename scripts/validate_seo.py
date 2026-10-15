"""Validate generated canonical metadata, robots, sitemap, and Search Console proof."""

from __future__ import annotations

import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_site import fields

GOOGLE_FILE = "googlef0a0d65fc3e621d7.html"
GOOGLE_CONTENT = b"google-site-verification: googlef0a0d65fc3e621d7.html"
SITEMAP_NS = "http://www.sitemaps.org/schemas/sitemap/0.9"


class PageHead(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.title_count = 0
        self.title_text: list[str] = []
        self.in_title = False
        self.lang: list[str] = []
        self.description: list[str] = []
        self.canonical: list[str] = []
        self.robots: list[str] = []
        self.og_title: list[str] = []
        self.og_description: list[str] = []
        self.og_url: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key.lower(): value or "" for key, value in attrs}
        if tag == "html":
            self.lang.append(values.get("lang", ""))
        elif tag == "title":
            self.title_count += 1
            self.in_title = True
        elif tag == "meta":
            name = values.get("name", "").lower()
            prop = values.get("property", "").lower()
            if name == "description":
                self.description.append(values.get("content", ""))
            elif name == "robots":
                self.robots.append(values.get("content", ""))
            elif prop == "og:title":
                self.og_title.append(values.get("content", ""))
            elif prop == "og:description":
                self.og_description.append(values.get("content", ""))
            elif prop == "og:url":
                self.og_url.append(values.get("content", ""))
        elif tag == "link" and "canonical" in values.get("rel", "").lower().split():
            self.canonical.append(values.get("href", ""))

    def handle_endtag(self, tag: str) -> None:
        if tag == "title":
            self.in_title = False

    def handle_data(self, data: str) -> None:
        if self.in_title:
            self.title_text.append(data)

    @property
    def title(self) -> str:
        return " ".join("".join(self.title_text).split())

    @property
    def is_noindex(self) -> bool:
        return any("noindex" in {part.strip().lower() for part in value.split(",")} for value in self.robots)


def config_site_root(config_path: Path = ROOT / "_config.yml") -> tuple[str, str]:
    config = fields(config_path.read_text(encoding="utf-8"))
    origin = config.get("url", "").rstrip("/")
    baseurl = config.get("baseurl", "").rstrip("/")
    if not origin.startswith("https://"):
        raise ValueError("_config.yml url must be an HTTPS origin")
    return origin, baseurl


def expected_url(origin: str, baseurl: str, route: str) -> str:
    return origin.rstrip("/") + baseurl.rstrip("/") + (route if route.startswith("/") else "/" + route)


def route_for_output(path: Path, site: Path) -> str:
    relative = path.relative_to(site).as_posix()
    if relative == "index.html":
        return "/"
    if relative.endswith("/index.html"):
        return "/" + relative[: -len("index.html")]
    return "/" + relative


def local_html_for_url(site: Path, loc: str, origin: str, baseurl: str) -> Path | None:
    parsed = urlsplit(loc)
    if parsed.scheme != "https" or parsed.netloc != urlsplit(origin).netloc:
        return None
    if parsed.query or parsed.fragment:
        return None
    prefix = baseurl.rstrip("/")
    if prefix and parsed.path != prefix and not parsed.path.startswith(prefix + "/"):
        return None
    route = parsed.path[len(prefix):] if prefix else parsed.path
    if not route:
        route = "/"
    route = unquote(route)
    target = site / route.lstrip("/")
    if route.endswith("/") or target.is_dir():
        target = target / "index.html"
    return target


def validate_site(site: Path, origin: str, baseurl: str) -> list[str]:
    errors: list[str] = []
    if not site.is_dir():
        return [f"generated site directory does not exist: {site}"]

    verification = site / GOOGLE_FILE
    if not verification.is_file():
        errors.append(f"Google Search Console verification file is missing: {GOOGLE_FILE}")
    elif verification.read_bytes() != GOOGLE_CONTENT:
        errors.append(f"Google Search Console verification file content is not exact: {GOOGLE_FILE}")

    robots_path = site / "robots.txt"
    expected_sitemap = expected_url(origin, baseurl, "/sitemap.xml")
    if not robots_path.is_file():
        errors.append("generated robots.txt is missing")
    else:
        lines = [line.strip() for line in robots_path.read_text(encoding="utf-8").splitlines() if line.strip()]
        if "User-agent: *" not in lines:
            errors.append("robots.txt must include User-agent: *")
        if "Allow: /" not in lines:
            errors.append("robots.txt must explicitly allow crawling with Allow: /")
        if any(re.fullmatch(r"Disallow:\s*/", line, re.I) for line in lines):
            errors.append("robots.txt must not block the whole site")
        sitemap_lines = [line for line in lines if line.lower().startswith("sitemap:")]
        if sitemap_lines != [f"Sitemap: {expected_sitemap}"]:
            errors.append(f"robots.txt sitemap directive must be exactly {expected_sitemap}")

    documents = sorted(path for path in site.rglob("*.html") if path.name != GOOGLE_FILE)
    page_by_url: dict[str, tuple[Path, PageHead]] = {}
    for path in documents:
        relative = path.relative_to(site).as_posix()
        parser = PageHead()
        parser.feed(path.read_text(encoding="utf-8"))
        route = route_for_output(path, site)
        canonical = expected_url(origin, baseurl, route)
        if parser.title_count != 1 or not parser.title:
            errors.append(f"expected one non-empty title: {relative}")
        if len(parser.lang) != 1 or not parser.lang[0]:
            errors.append(f"expected one html lang declaration: {relative}")
        if len(parser.canonical) != 1 or parser.canonical[0] != canonical:
            errors.append(f"canonical must occur once and match {canonical}: {relative}")
        if len(parser.description) != 1 or not parser.description[0].strip():
            errors.append(f"expected one non-empty meta description: {relative}")
        # jekyll-seo-tag commonly appends the site title to <title>, while
        # og:title remains the page title. Both should identify the same page.
        title_matches_og = (
            len(parser.og_title) == 1
            and bool(parser.og_title[0].strip())
            and (parser.title == parser.og_title[0] or parser.title.startswith(parser.og_title[0] + " | "))
        )
        if not title_matches_og:
            errors.append(f"Open Graph title must identify the page title: {relative}")
        if len(parser.og_description) != 1 or parser.og_description != parser.description:
            errors.append(f"Open Graph description must match the meta description: {relative}")
        if len(parser.og_url) != 1 or parser.og_url[0] != canonical:
            errors.append(f"Open Graph URL must match the page canonical: {relative}")
        if len(parser.robots) > 1:
            errors.append(f"duplicate robots meta directives: {relative}")
        if canonical in page_by_url:
            errors.append(f"duplicate canonical page URL: {canonical}")
        page_by_url[canonical] = (path, parser)

    if not page_by_url:
        return errors + ["no generated HTML pages with canonical metadata found"]

    sitemap_path = site / "sitemap.xml"
    if not sitemap_path.is_file():
        errors.append("generated sitemap.xml is missing")
        return errors
    try:
        root = ET.parse(sitemap_path).getroot()
    except (ET.ParseError, OSError) as error:
        return errors + [f"sitemap.xml is not valid XML: {error}"]
    if root.tag != f"{{{SITEMAP_NS}}}urlset":
        errors.append("sitemap.xml must use the standard sitemap urlset namespace")
    locs = [element.text or "" for element in root.findall(f".//{{{SITEMAP_NS}}}loc")]
    if not locs:
        errors.append("sitemap.xml has no loc URLs")
    if len(locs) != len(set(locs)):
        errors.append("sitemap.xml contains duplicate URLs")
    seen_titles: Counter[str] = Counter()
    seen_descriptions: Counter[str] = Counter()
    sitemap_set = set(locs)
    for loc in locs:
        target = local_html_for_url(site, loc, origin, baseurl)
        if target is None:
            errors.append(f"sitemap URL is outside the canonical HTTPS host/base path: {loc}")
            continue
        if not target.is_file():
            errors.append(f"sitemap URL has no generated HTML page: {loc}")
            continue
        page = page_by_url.get(loc)
        if page is None:
            errors.append(f"sitemap URL has no matching canonical page: {loc}")
            continue
        _, parser = page
        if parser.is_noindex:
            errors.append(f"noindex page must not appear in sitemap: {loc}")
        seen_titles[parser.title] += 1
        if parser.description:
            seen_descriptions[parser.description[0].strip()] += 1

    for title, count in seen_titles.items():
        if count > 1:
            errors.append(f"duplicate sitemap page title ({count}): {title}")
    for description, count in seen_descriptions.items():
        if count > 1:
            errors.append(f"duplicate sitemap meta description ({count}): {description}")

    expected_indexable = {
        url for url, (path, parser) in page_by_url.items()
        if not parser.is_noindex and path.relative_to(site).as_posix() != "404.html"
    }
    if expected_indexable != sitemap_set:
        missing = sorted(expected_indexable - sitemap_set)
        unexpected = sorted(sitemap_set - expected_indexable)
        if missing:
            errors.append(f"indexable generated pages missing from sitemap: {missing[:8]}")
        if unexpected:
            errors.append(f"non-indexable or unknown pages in sitemap: {unexpected[:8]}")

    return errors


def main() -> int:
    site = Path(sys.argv[1] if len(sys.argv) > 1 else ROOT / "_site").resolve()
    try:
        origin, baseurl = config_site_root()
    except (OSError, ValueError) as error:
        print(f"SEO configuration error: {error}")
        return 2
    errors = validate_site(site, origin, baseurl)
    if errors:
        print("Generated SEO validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    pages = len([path for path in site.rglob("*.html") if path.name != GOOGLE_FILE])
    sitemap_count = len(ET.parse(site / "sitemap.xml").findall(f".//{{{SITEMAP_NS}}}loc"))
    print(f"Validated SEO metadata for {pages} HTML pages and {sitemap_count} indexable URLs; canonical, Open Graph, sitemap, robots, and exact Google verification-file checks pass.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
