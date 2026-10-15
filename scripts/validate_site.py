"""Validate source routes, searchable metadata, local links, and Python examples."""

from __future__ import annotations

import re
import json
import sys
from decimal import Decimal, InvalidOperation
from fractions import Fraction
from math import gcd
from statistics import mean, median
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
VALID_ANSWER_FORMATS = {"integer", "decimal", "fraction", "text", "manual"}
VALID_ASSESSMENT_REVIEW = {"pending", "technical-reviewed", "approved"}


def validate_assessment_data(assessment: object, resources: dict[str, dict[str, str]], skill_ids: set[str]) -> list[str]:
    """Validate structured question contracts without treating validity as subject approval."""
    errors: list[str] = []
    if not isinstance(assessment, dict) or assessment.get("schema_version") != 1:
        return ["assessment needs schema_version 1"]
    assessment_id = assessment.get("id", "assessment")
    if not isinstance(assessment.get("id"), str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", assessment["id"]):
        errors.append("assessment needs a stable id")
    if not isinstance(assessment.get("title"), str) or not assessment["title"].strip():
        errors.append("assessment needs a title")
    if assessment.get("review_status") not in VALID_ASSESSMENT_REVIEW:
        errors.append("assessment needs a valid review_status")
    questions = assessment.get("questions")
    if not isinstance(questions, list) or not questions:
        return ["assessment needs a non-empty questions list"]
    question_ids: set[str] = set()
    for index, question in enumerate(questions, start=1):
        label = f"{assessment_id} question {index}"
        if not isinstance(question, dict):
            errors.append(f"{label} must be an object")
            continue
        question_id = question.get("id")
        if not isinstance(question_id, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", question_id):
            errors.append(f"{label} has an invalid id")
        elif question_id in question_ids:
            errors.append(f"duplicate assessment question id {question_id}")
        else:
            question_ids.add(question_id)
        for field in ("question", "hint", "solution", "explanation"):
            if not isinstance(question.get(field), str) or not question[field].strip():
                errors.append(f"{label} is missing {field}")
        for field in ("question", "hint", "solution", "explanation"):
            if isinstance(question.get(field), str) and len(question[field]) > 4000:
                errors.append(f"{label} {field} exceeds the supported length")
        if not isinstance(question.get("subject"), str) or not question["subject"].strip():
            errors.append(f"{label} needs a subject")
        constraints = question.get("constraints")
        if not isinstance(constraints, list) or any(not isinstance(item, str) or not item.strip() for item in constraints):
            errors.append(f"{label} constraints must be a list of non-empty strings")
        mistakes = question.get("common_mistakes")
        if not isinstance(mistakes, list) or not mistakes or any(not isinstance(item, str) or not item.strip() for item in mistakes):
            errors.append(f"{label} needs non-empty common_mistakes guidance")
        provenance = question.get("provenance")
        if not isinstance(provenance, dict) or provenance.get("kind") not in {"original", "external-reference"} or not isinstance(provenance.get("source_id"), str) or not provenance["source_id"].strip():
            errors.append(f"{label} needs source provenance")
        else:
            if provenance["source_id"] not in resources:
                errors.append(f"{label} has an unknown provenance source {provenance['source_id']!r}")
            if provenance.get("kind") == "external-reference" and not isinstance(provenance.get("source_url"), str):
                errors.append(f"{label} external provenance needs a source URL")
        question_skills = question.get("skill_ids")
        if not isinstance(question_skills, list) or not question_skills:
            errors.append(f"{label} needs at least one skill mapping")
        else:
            string_skills = [skill for skill in question_skills if isinstance(skill, str)]
            if len(string_skills) != len(set(string_skills)):
                errors.append(f"{label} has duplicate skill mappings")
            for skill in question_skills:
                if not isinstance(skill, str) or skill not in skill_ids:
                    errors.append(f"{label} references unknown skill {skill!r}")
        lesson_id = question.get("lesson_id")
        lesson = resources.get(lesson_id) if isinstance(lesson_id, str) else None
        if lesson is None or lesson.get("content_type") not in {"lesson", "guide"}:
            errors.append(f"{label} has a broken learning-resource link {lesson_id!r}")
        prerequisite_ids = question.get("prerequisite_ids")
        if not isinstance(prerequisite_ids, list) or any(not isinstance(item, str) for item in prerequisite_ids):
            errors.append(f"{label} prerequisite_ids must be a list of resource IDs")
        else:
            if len(prerequisite_ids) != len(set(prerequisite_ids)):
                errors.append(f"{label} has duplicate prerequisites")
            for prerequisite_id in prerequisite_ids:
                if prerequisite_id not in resources:
                    errors.append(f"{label} has a broken prerequisite link {prerequisite_id!r}")
        answer_format = question.get("answer_format")
        if answer_format not in VALID_ANSWER_FORMATS:
            errors.append(f"{label} has an invalid answer_format {answer_format!r}")
        if question.get("difficulty") not in VALID_DIFFICULTY:
            errors.append(f"{label} has an invalid difficulty")
        accepted = question.get("accepted_answers")
        if not isinstance(accepted, list) or any(not isinstance(answer, str) or not answer.strip() for answer in accepted):
            errors.append(f"{label} needs an accepted_answers list containing only non-empty strings")
        elif answer_format == "manual" and accepted:
            errors.append(f"{label} manual-comparison questions cannot advertise machine-accepted answers")
        elif answer_format != "manual" and not accepted:
            errors.append(f"{label} needs a non-empty accepted_answers list")
        else:
            if len(accepted) != len(set(accepted)):
                errors.append(f"{label} has duplicate accepted answers")
            patterns = {
                "integer": re.compile(r"^[+-]?\d{1,30}$"),
                "decimal": re.compile(r"^[+-]?\d{1,24}(?:\.\d{1,12})?$"),
                "fraction": re.compile(r"^(?:[+-]?\d{1,30}/[1-9]\d{0,29}|[+-]?\d{1,24}(?:\.\d{1,12})?)$"),
                "text": re.compile(r"^.{1,200}$", re.S),
                "manual": None
            }
            pattern = patterns.get(answer_format)
            if pattern and any(not pattern.fullmatch(answer.strip()) for answer in accepted):
                errors.append(f"{label} has an answer that does not match {answer_format} format")
        choices = question.get("choices")
        if choices is not None:
            if not isinstance(choices, list) or len(choices) < 2 or any(not isinstance(choice, str) or not choice.strip() for choice in choices):
                errors.append(f"{label} choices must contain at least two non-empty strings")
            elif len(choices) != len(set(choices)):
                errors.append(f"{label} has duplicate choices")
            elif isinstance(accepted, list) and not set(accepted).issubset(choices):
                errors.append(f"{label} has an accepted answer outside its choices")
        verification_method = question.get("verification_method")
        verification = question.get("verification")
        if verification_method not in {"substitution", "direct-evaluation", "special-case", "example-execution"} or not isinstance(verification, dict):
            errors.append(f"{label} needs a valid verification method and derivation")
        else:
            kind = verification.get("kind")
            required = {
                "combine-coefficients": ("coefficients",),
                "evaluate-linear": ("coefficient", "constant", "variable_value"),
                "solve-linear": ("coefficient", "constant", "rhs"),
                "classify-zero-coefficient": ("coefficient", "constant", "rhs"),
                "fraction-sum": ("terms",),
                "fraction-conversion": ("numerator", "denominator", "expected_decimal", "expected_percent", "decimal_terminates"),
                "percentage-share": ("part_units", "whole_units"),
                "unit-rate": ("total", "count"),
                "percentage-discount": ("original_value", "percent"),
                "percentage-change": ("old_value", "new_value"),
                "statistics-summary": ("observations", "expected_total", "expected_mean", "expected_median")
            }.get(kind)
            if verification_method == "example-execution":
                kind = verification.get("kind")
                if kind != "python-output":
                    errors.append(f"{label} example execution must use a python-output record")
                else:
                    code = verification.get("code")
                    expected_output = verification.get("expected_output")
                    answer_from_output = verification.get("answer_from_output")
                    if not isinstance(code, str) or not code.strip():
                        errors.append(f"{label} verification needs Python example code")
                    else:
                        try:
                            compile(code, f"{question_id or assessment_id}-verification", "exec")
                        except SyntaxError as error:
                            errors.append(f"{label} verification code has invalid Python syntax: {error.msg}")
                    if not isinstance(expected_output, str):
                        errors.append(f"{label} verification needs expected_output text")
                    if answer_from_output not in {"stdout", "line-count"}:
                        errors.append(f"{label} verification has an invalid answer_from_output rule")
                    elif isinstance(expected_output, str):
                        derived = expected_output.strip() if answer_from_output == "stdout" else str(len(expected_output.splitlines()))
                        if not isinstance(accepted, list) or derived.casefold() not in {str(item).strip().casefold() for item in accepted}:
                            errors.append(f"{label} accepted_answers do not include the configured example result")
                required = None
            if required is None:
                if verification_method != "example-execution":
                    errors.append(f"{label} has an invalid verification derivation")
            else:
                for field in required:
                    if field not in verification:
                        errors.append(f"{label} verification is missing {field}")
                if kind == "combine-coefficients" and not isinstance(verification.get("coefficients"), list):
                    errors.append(f"{label} verification coefficients must be a list")
                for field in ("coefficient", "constant", "variable_value", "rhs", "numerator", "denominator", "part_units", "whole_units", "total", "count", "original_value", "percent", "old_value", "new_value", "expected_total"):
                    if field in verification and (isinstance(verification[field], bool) or not isinstance(verification[field], int)):
                        errors.append(f"{label} verification {field} must be an integer")
                if kind == "solve-linear" and verification.get("coefficient") == 0:
                    errors.append(f"{label} cannot solve by dividing by a zero coefficient")
                if kind == "classify-zero-coefficient" and verification.get("coefficient") != 0:
                    errors.append(f"{label} zero-coefficient classification needs coefficient 0")
            if kind == "fraction-sum":
                terms = verification.get("terms")
                if not isinstance(terms, list) or not terms or any(not isinstance(term, dict) or isinstance(term.get("numerator"), bool) or not isinstance(term.get("numerator"), int) or isinstance(term.get("denominator"), bool) or not isinstance(term.get("denominator"), int) or term["denominator"] <= 0 for term in terms):
                    errors.append(f"{label} fraction-sum terms need integer numerators and positive denominators")
                elif answer_format == "fraction":
                    derived = sum((Fraction(term["numerator"], term["denominator"]) for term in terms), Fraction())
                    expected = f"{derived.numerator}/{derived.denominator}" if derived.denominator != 1 else str(derived.numerator)
                    if expected not in accepted:
                        errors.append(f"{label} accepted_answers do not match the fraction-sum derivation")
            if answer_format != "manual":
                derived_answer: str | None = None
                if kind == "combine-coefficients" and isinstance(verification.get("coefficients"), list) and all(isinstance(value, int) and not isinstance(value, bool) for value in verification["coefficients"]):
                    derived_answer = str(sum(verification["coefficients"]))
                elif kind == "evaluate-linear" and all(isinstance(verification.get(field), int) and not isinstance(verification.get(field), bool) for field in ("coefficient", "variable_value", "constant")):
                    derived_answer = str(verification["coefficient"] * verification["variable_value"] + verification["constant"])
                elif kind == "solve-linear" and isinstance(verification.get("coefficient"), int) and verification.get("coefficient") != 0 and isinstance(verification.get("constant"), int) and isinstance(verification.get("rhs"), int):
                    result = Fraction(verification["rhs"] - verification["constant"], verification["coefficient"])
                    derived_answer = f"{result.numerator}/{result.denominator}" if result.denominator != 1 else str(result.numerator)
                elif kind == "classify-zero-coefficient" and verification.get("coefficient") == 0 and isinstance(verification.get("constant"), int) and isinstance(verification.get("rhs"), int):
                    derived_answer = "infinitely many" if verification["constant"] == verification["rhs"] else "none"
                if derived_answer is not None and derived_answer.casefold() not in {str(value).strip().casefold() for value in accepted}:
                    errors.append(f"{label} accepted_answers do not match the configured derivation")
            if kind == "fraction-conversion":
                numerator, denominator = verification.get("numerator"), verification.get("denominator")
                if isinstance(numerator, int) and not isinstance(numerator, bool) and isinstance(denominator, int) and not isinstance(denominator, bool) and denominator > 0:
                    reduced_denominator = denominator // gcd(abs(numerator), denominator)
                    while reduced_denominator % 2 == 0:
                        reduced_denominator //= 2
                    while reduced_denominator % 5 == 0:
                        reduced_denominator //= 5
                    terminates = reduced_denominator == 1
                    value = Fraction(numerator, denominator)
                    try:
                        decimal_value = format(Decimal(value.numerator) / Decimal(value.denominator), "f")
                    except (InvalidOperation, ZeroDivisionError):
                        decimal_value = ""
                    if verification.get("decimal_terminates") is not terminates or (terminates and decimal_value != verification.get("expected_decimal")) or value * 100 != verification.get("expected_percent"):
                        errors.append(f"{label} fraction-conversion derivation is inconsistent")
            if kind == "percentage-share" and isinstance(verification.get("whole_units"), int) and verification.get("whole_units", 0) > 0 and isinstance(verification.get("part_units"), int):
                result = Fraction(verification["part_units"] * 100, verification["whole_units"])
                expected = str(result.numerator) if result.denominator == 1 else f"{result.numerator}/{result.denominator}"
                if expected not in accepted:
                    errors.append(f"{label} accepted_answers do not match the percentage-share derivation")
            if kind == "unit-rate" and isinstance(verification.get("count"), int) and verification.get("count", 0) > 0 and isinstance(verification.get("total"), int):
                result = Fraction(verification["total"], verification["count"])
                expected = str(result.numerator) if result.denominator == 1 else f"{result.numerator}/{result.denominator}"
                if expected not in accepted:
                    errors.append(f"{label} accepted_answers do not match the unit-rate derivation")
            if kind == "percentage-discount" and isinstance(verification.get("original_value"), int) and isinstance(verification.get("percent"), int):
                result = Fraction(verification["original_value"] * (100 - verification["percent"]), 100)
                expected = str(result.numerator) if result.denominator == 1 else f"{result.numerator}/{result.denominator}"
                if expected not in accepted:
                    errors.append(f"{label} accepted_answers do not match the percentage-discount derivation")
            if kind == "percentage-change" and isinstance(verification.get("old_value"), int) and verification.get("old_value", 0) != 0 and isinstance(verification.get("new_value"), int):
                result = Fraction((verification["new_value"] - verification["old_value"]) * 100, verification["old_value"])
                expected = str(result.numerator) if result.denominator == 1 else f"{result.numerator}/{result.denominator}"
                if expected not in accepted:
                    errors.append(f"{label} accepted_answers do not match the percentage-change derivation")
            if kind == "statistics-summary":
                observations = verification.get("observations")
                if not isinstance(observations, list) or not observations or any(isinstance(value, bool) or not isinstance(value, int) for value in observations):
                    errors.append(f"{label} statistics-summary observations must be a non-empty integer list")
                elif verification.get("expected_total") != sum(observations) or verification.get("expected_mean") != mean(observations) or verification.get("expected_median") != median(observations):
                    errors.append(f"{label} statistics-summary expected values do not match its observations")
            compatible = {
                "substitution": {"solve-linear", "classify-zero-coefficient"},
                "direct-evaluation": {"combine-coefficients", "evaluate-linear", "fraction-sum", "fraction-conversion", "percentage-share", "unit-rate", "percentage-discount", "percentage-change", "statistics-summary"},
                "special-case": {"classify-zero-coefficient"},
                "example-execution": {"python-output"}
            }
            if kind not in compatible.get(verification_method, set()):
                errors.append(f"{label} verification method does not match its derivation")
        review_status = question.get("review_status")
        if review_status not in VALID_ASSESSMENT_REVIEW:
            errors.append(f"{label} has an invalid review_status")
        if review_status == "approved" and lesson and lesson.get("review_status") != "approved":
            errors.append(f"{label} cannot be approved while its lesson remains unapproved")
    return errors


def validate_inline_question_attributes(attributes: dict[str, str], resources: dict[str, dict[str, str]], skill_ids: set[str]) -> list[str]:
    """Check a static HTML assessment question's stable ID, skill map, answer format, and resource route."""
    errors: list[str] = []
    question_id = attributes.get("data-question-id", "")
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", question_id):
        errors.append("inline assessment question needs a stable data-question-id")
    skills = [item.strip() for item in attributes.get("data-skill-ids", "").split(",") if item.strip()]
    if not skills:
        errors.append(f"inline assessment {question_id or '(unknown)'} needs a skill mapping")
    for skill in skills:
        if skill not in skill_ids:
            errors.append(f"inline assessment {question_id or '(unknown)'} references unknown skill {skill!r}")
    resource_id = attributes.get("data-resource-id", "")
    resource = resources.get(resource_id)
    if not resource:
        errors.append(f"inline assessment {question_id or '(unknown)'} has a broken resource link {resource_id!r}")
    else:
        route = resource.get("permalink", "")
        liquid_route = LIQUID_PATH.search(attributes.get("data-resource-url", ""))
        if not liquid_route or liquid_route.group(1) != route:
            errors.append(f"inline assessment {question_id or '(unknown)'} resource URL does not match {resource_id}")
    answer_format = attributes.get("data-answer-format", "")
    accepted = [item for item in attributes.get("data-accepted-answers", "").split("|") if item]
    if answer_format not in VALID_ANSWER_FORMATS:
        errors.append(f"inline assessment {question_id or '(unknown)'} has an invalid answer format")
    if answer_format == "manual" and accepted:
        errors.append(f"inline assessment {question_id or '(unknown)'} manual response cannot advertise machine-accepted answers")
    elif answer_format != "manual" and not accepted:
        errors.append(f"inline assessment {question_id or '(unknown)'} needs accepted answers")
    else:
        patterns = {
            "integer": re.compile(r"^[+-]?\d{1,30}$"),
            "decimal": re.compile(r"^[+-]?\d{1,24}(?:\.\d{1,12})?$"),
            "fraction": re.compile(r"^(?:[+-]?\d{1,30}/[1-9]\d{0,29}|[+-]?\d{1,24}(?:\.\d{1,12})?)$"),
            "text": re.compile(r"^.{1,200}$", re.S)
        }
        pattern = patterns.get(answer_format)
        if pattern and any(not pattern.fullmatch(value) for value in accepted):
            errors.append(f"inline assessment {question_id or '(unknown)'} has an answer outside {answer_format} format")
    return errors


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


def find_prerequisite_cycles(graph: dict[str, list[str]]) -> list[tuple[str, ...]]:
    """Return prerequisite cycles as paths whose first ID is repeated at the end."""
    state: dict[str, int] = {}
    stack: list[str] = []
    cycles: list[tuple[str, ...]] = []
    seen: set[tuple[str, ...]] = set()

    def visit(resource_id: str) -> None:
        state[resource_id] = 1
        stack.append(resource_id)
        for prerequisite in sorted(graph.get(resource_id, [])):
            if prerequisite not in graph:
                continue
            if state.get(prerequisite, 0) == 0:
                visit(prerequisite)
            elif state.get(prerequisite) == 1:
                start = stack.index(prerequisite)
                cycle = tuple(stack[start:] + [prerequisite])
                if cycle not in seen:
                    seen.add(cycle)
                    cycles.append(cycle)
        stack.pop()
        state[resource_id] = 2

    for resource_id in sorted(graph):
        if state.get(resource_id, 0) == 0:
            visit(resource_id)
    return cycles


def main() -> int:
    files = markdown_files()
    routes: dict[str, Path] = {}
    canonical_routes: dict[str, Path] = {}
    ids: dict[str, Path] = {}
    resource_metadata: dict[str, dict[str, str]] = {}
    skill_ids: set[str] = set()
    searchable: dict[str, Path] = {}
    prerequisites: list[tuple[Path, str]] = []
    prerequisite_graph: dict[str, list[str]] = {}
    related_references: list[tuple[Path, str]] = []
    translations: list[tuple[Path, str]] = []
    errors: list[str] = []
    config = (ROOT / "_config.yml").read_text(encoding="utf-8")
    origin_default_match = re.search(r"(?m)^\s*content_origin:\s*([a-z-]+)\s*$", config)
    default_origin = origin_default_match.group(1) if origin_default_match else ""
    if default_origin not in VALID_ORIGINS:
        errors.append("_config.yml must set a valid default content_origin")

    json_files = list((ROOT / "data").glob("*.json"))
    if (ROOT / "_data").is_dir():
        json_files.extend((ROOT / "_data").glob("*.json"))
    for path in json_files:
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
            resource_metadata[resource_id] = values
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
        for skill_id in list_value(metadata, "skills"):
            if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", skill_id):
                errors.append(f"invalid skill id {skill_id!r}: {relative}")
            elif skill_id in skill_ids:
                # Skills may be taught by several resources; this set is only a registry.
                pass
            skill_ids.add(skill_id)
        resource_id = values.get("id", "")
        prerequisite_ids = list_value(metadata, "prerequisites")
        if resource_id:
            prerequisite_graph[resource_id] = prerequisite_ids
        for prerequisite in prerequisite_ids:
            if re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", prerequisite):
                prerequisites.append((path, prerequisite))
                if prerequisite == resource_id:
                    errors.append(f"resource cannot be its own prerequisite: {resource_id}: {relative}")
        related_references.extend((path, related_id) for related_id in list_value(metadata, "related_resources"))
        if values.get("content_type") == "course" and not list_value(metadata, "related_resources"):
            errors.append(f"course needs explicit related_resources session checkpoints: {relative}")
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
    for cycle in find_prerequisite_cycles(prerequisite_graph):
        errors.append(f"prerequisite cycle: {' -> '.join(cycle)}")
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

    structured_question_ids: set[str] = set()
    for assessment_path in sorted((ROOT / "_data").glob("*_assessment.json")):
        try:
            assessment = json.loads(assessment_path.read_text(encoding="utf-8"))
            errors.extend(validate_assessment_data(assessment, resource_metadata, skill_ids))
            if isinstance(assessment, dict) and isinstance(assessment.get("questions"), list):
                for question in assessment["questions"]:
                    if not isinstance(question, dict) or not isinstance(question.get("id"), str):
                        continue
                    question_id = question["id"]
                    if question_id in structured_question_ids:
                        errors.append(f"duplicate structured assessment question id {question_id}")
                    structured_question_ids.add(question_id)
        except json.JSONDecodeError as error:
            errors.append(f"invalid assessment JSON {assessment_path.name} at line {error.lineno}: {error.msg}")

    inline_question_ids: set[str] = set(structured_question_ids)
    for path in files:
        source = path.read_text(encoding="utf-8")
        for tag in re.findall(r"<fieldset\b[^>]*\bdata-question\b[^>]*>", source):
            if "{{" in tag or "{%" in tag:
                # Liquid-generated questions are validated from their JSON source of truth above.
                continue
            attributes = dict(re.findall(r"([a-zA-Z_:][a-zA-Z0-9_:.-]*)=\"([^\"]*)\"", tag))
            question_id = attributes.get("data-question-id", "")
            if question_id and question_id in inline_question_ids:
                errors.append(f"duplicate inline assessment question id {question_id}: {path.relative_to(ROOT)}")
            inline_question_ids.add(question_id)
            errors.extend(f"{message}: {path.relative_to(ROOT)}" for message in validate_inline_question_attributes(attributes, resource_metadata, skill_ids))

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
                if "{{" in target or "{%" in target:
                    # Data-driven Liquid URLs are checked against generated HTML.
                    continue
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
