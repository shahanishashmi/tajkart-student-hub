"""Check Jekyll page metadata and local Markdown links without dependencies."""

from __future__ import annotations

import re
import sys
from pathlib import Path, PurePosixPath


ROOT = Path(__file__).resolve().parents[1]
FRONT_MATTER = re.compile(r"\A---\s*\n(.*?)\n---\s*(?:\n|\Z)", re.S)
PERMALINK = re.compile(r"^permalink:\s*[\"']?([^\"'\s]+)", re.M)
TITLE = re.compile(r"^title:\s*.+", re.M)
MARKDOWN_LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
LIQUID_PATH = re.compile(r"\{\{\s*['\"]([^'\"]+)['\"]\s*\|\s*relative_url\s*\}\}")
PYTHON_BLOCK = re.compile(r"```python\s*\n(.*?)\n```", re.S)


def markdown_files() -> list[Path]:
    return [
        path
        for path in ROOT.rglob("*.md")
        if not any(part.startswith(".") for part in path.relative_to(ROOT).parts)
        and "vendor" not in path.parts
    ]


def route_for(path: Path, metadata: str | None) -> str:
    if metadata:
        match = PERMALINK.search(metadata)
        if match:
            return match.group(1)
    relative = path.relative_to(ROOT).with_suffix("")
    if relative.name.lower() == "index":
        relative = relative.parent
    elif relative.name.lower() == "readme":
        return "/" + relative.as_posix() + ".html"
    return "/" + relative.as_posix().strip("/") + "/"


def main() -> int:
    files = markdown_files()
    routes: dict[str, Path] = {}
    errors: list[str] = []
    for path in files:
        source = path.read_text(encoding="utf-8")
        match = FRONT_MATTER.match(source)
        if not match:
            continue
        metadata = match.group(1)
        route = route_for(path, metadata)
        if route in routes:
            errors.append(f"duplicate route {route}: {routes[route].relative_to(ROOT)} and {path.relative_to(ROOT)}")
        routes[route] = path
        if not TITLE.search(metadata):
            errors.append(f"missing title in front matter: {path.relative_to(ROOT)}")

    for path in files:
        source = path.read_text(encoding="utf-8")
        for number, block in enumerate(PYTHON_BLOCK.findall(source), start=1):
            try:
                compile(block, f"{path.relative_to(ROOT)}:python-example-{number}", "exec")
            except SyntaxError as error:
                errors.append(f"invalid Python example in {path.relative_to(ROOT)} block {number}: {error.msg} (line {error.lineno})")
        source = FRONT_MATTER.sub("", source, count=1)
        for match in MARKDOWN_LINK.finditer(source):
            target = match.group(1).strip("<>\"'")
            liquid = LIQUID_PATH.search(target)
            if liquid:
                target = liquid.group(1)
            else:
                target = target.split()[0]
            if not target or target.startswith(("http://", "https://", "mailto:", "#", "data:")):
                continue
            target = target.split("#", 1)[0].split("?", 1)[0]
            if not target:
                continue
            if target.startswith("/"):
                if target in routes or target.rstrip("/") + "/" in routes or target == "/404.html":
                    continue
                errors.append(f"unresolved site route {target}: {path.relative_to(ROOT)}")
                continue
            if target.endswith("/"):
                route = "/" + target.strip("/") + "/"
                if route in routes:
                    continue
            resolved = (path.parent / PurePosixPath(target)).resolve()
            if resolved.is_file() and ROOT in resolved.parents:
                continue
            errors.append(f"missing local file {target}: {path.relative_to(ROOT)}")

    if errors:
        print("Site validation failed:")
        print("\n".join(f"- {error}" for error in errors))
        return 1
    print(f"Validated {len(files)} Markdown files and {len(routes)} Jekyll routes; no duplicate routes or broken local Markdown links found.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
