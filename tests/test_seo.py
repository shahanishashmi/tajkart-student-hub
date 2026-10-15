"""Regression tests for canonical metadata and crawl/indexing controls."""

from __future__ import annotations

import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import validate_seo


ORIGIN = "https://example.test"
BASEURL = "/student-hub"
SITEMAP_NS = "http://www.sitemaps.org/schemas/sitemap/0.9"


def write_page(site: Path, route: str, *, noindex: bool = False) -> None:
    if route == "/":
        relative = "index.html"
    elif route.endswith("/"):
        relative = route.lstrip("/") + "index.html"
    else:
        relative = route.lstrip("/")
    path = site / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    canonical = f"{ORIGIN}{BASEURL}{route}"
    title = "Example title" if route == "/" else "Lesson title"
    description = "A useful, unique description for this generated page."
    robots = '<meta name="robots" content="noindex, follow">' if noindex else ""
    path.write_text(
        "<!doctype html><html lang=\"en\"><head>"
        f"<title>{title} | Example site</title>"
        f"<meta name=\"description\" content=\"{description}\">"
        f"<link rel=\"canonical\" href=\"{canonical}\">"
        f"<meta property=\"og:title\" content=\"{title}\">"
        f"<meta property=\"og:description\" content=\"{description}\">"
        f"<meta property=\"og:url\" content=\"{canonical}\">{robots}"
        "</head><body></body></html>",
        encoding="utf-8",
    )


def write_sitemap(site: Path, routes: list[str]) -> None:
    urlset = ET.Element(f"{{{SITEMAP_NS}}}urlset")
    for route in routes:
        url = ET.SubElement(urlset, f"{{{SITEMAP_NS}}}url")
        ET.SubElement(url, f"{{{SITEMAP_NS}}}loc").text = f"{ORIGIN}{BASEURL}{route}"
    ET.ElementTree(urlset).write(site / "sitemap.xml", encoding="utf-8", xml_declaration=True)


class SeoValidationTests(unittest.TestCase):
    def make_site(self) -> Path:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        site = Path(temp.name)
        write_page(site, "/")
        write_page(site, "/draft/", noindex=True)
        write_page(site, "/404.html")
        (site / validate_seo.GOOGLE_FILE).write_bytes(validate_seo.GOOGLE_CONTENT)
        (site / "robots.txt").write_text(
            "User-agent: *\nAllow: /\n\nSitemap: https://example.test/student-hub/sitemap.xml\n",
            encoding="utf-8",
        )
        write_sitemap(site, ["/"])
        return site

    def test_validates_project_site_and_excludes_noindex_pages(self) -> None:
        self.assertEqual(validate_seo.validate_site(self.make_site(), ORIGIN, BASEURL), [])

    def test_requires_exact_google_verification_bytes(self) -> None:
        site = self.make_site()
        (site / validate_seo.GOOGLE_FILE).write_bytes(validate_seo.GOOGLE_CONTENT + b"\n")
        errors = validate_seo.validate_site(site, ORIGIN, BASEURL)
        self.assertTrue(any("content is not exact" in error for error in errors))

    def test_rejects_wrong_canonical_and_sitemap_origin(self) -> None:
        site = self.make_site()
        page = site / "index.html"
        page.write_text(page.read_text(encoding="utf-8").replace(
            "https://example.test/student-hub/", "https://wrong.test/student-hub/"
        ), encoding="utf-8")
        write_sitemap(site, ["/"])
        errors = validate_seo.validate_site(site, ORIGIN, BASEURL)
        self.assertTrue(any("canonical must occur once" in error for error in errors))

    def test_rejects_noindex_url_in_sitemap(self) -> None:
        site = self.make_site()
        write_sitemap(site, ["/", "/draft/"])
        errors = validate_seo.validate_site(site, ORIGIN, BASEURL)
        self.assertTrue(any("noindex page must not appear" in error for error in errors))

    def test_rejects_robots_file_that_blocks_crawling(self) -> None:
        site = self.make_site()
        (site / "robots.txt").write_text(
            "User-agent: *\nDisallow: /\nSitemap: https://example.test/student-hub/sitemap.xml\n",
            encoding="utf-8",
        )
        errors = validate_seo.validate_site(site, ORIGIN, BASEURL)
        self.assertTrue(any("must explicitly allow crawling" in error for error in errors))
        self.assertTrue(any("must not block the whole site" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
