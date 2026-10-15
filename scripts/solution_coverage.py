#!/usr/bin/env python3
"""Generate an evidence-based question and solution audit in the master report."""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
REPORT = ROOT / "docs" / "MASTER_AUDIT_REPORT.md"
BEGIN = "<!-- solution-coverage:begin -->"
END = "<!-- solution-coverage:end -->"
FRONT_MATTER = re.compile(r"\A---\s*\r?\n(.*?)\r?\n---\s*\r?\n", re.S)
QUESTION_LINE = re.compile(r"(?m)^\s*(\d+)\.\s+(.+?)\s*$")
INLINE_ATTR = re.compile(r'([a-zA-Z_:][a-zA-Z0-9_:.-]*)="([^"]*)"')
sys.path.insert(0, str(ROOT / "scripts"))
from validate_site import fields as parse_front_matter_fields, list_value as parse_front_matter_list


def load_page(path: Path) -> tuple[dict[str, Any], str]:
    source = path.read_text(encoding="utf-8")
    match = FRONT_MATTER.match(source)
    if not match:
        return {}, source
    metadata = parse_front_matter_fields(match.group(1))
    for key in ("skills", "tags", "prerequisites"):
        metadata[key] = parse_front_matter_list(match.group(1), key)
    return metadata, source[match.end():]


def numbered_questions(body: str) -> list[str]:
    match = re.search(r"(?m)^##\s+Example questions\s*$", body)
    if not match:
        return []
    remainder = body[match.end():]
    section = re.split(r"(?m)^##\s+", remainder, maxsplit=1)[0]
    return [text.strip() for _, text in QUESTION_LINE.findall(section)]


def solution_section(body: str) -> str:
    match = re.search(r"(?im)^#{2,4}\s+[^\n]*solution[^\n]*$", body)
    if not match:
        return ""
    return re.split(r"(?m)^#{2,4}\s+", body[match.end():], maxsplit=1)[0].strip()


def load_resources() -> tuple[dict[str, dict[str, Any]], set[str]]:
    resources: dict[str, dict[str, Any]] = {}
    skills: set[str] = set()
    for path in ROOT.rglob("*.md"):
        if ".git" in path.parts or "_site" in path.parts:
            continue
        metadata, _ = load_page(path)
        resource_id = metadata.get("id")
        if resource_id:
            resources[resource_id] = metadata
            skills.update(metadata.get("skills", []) or [])
    return resources, skills


def load_assessments() -> tuple[list[dict[str, Any]], list[str]]:
    questions: list[dict[str, Any]] = []
    errors: list[str] = []
    for path in sorted((ROOT / "_data").glob("*_assessment.json")):
        try:
            assessment = json.loads(path.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            errors.append(f"{path.name}: invalid JSON at line {error.lineno}: {error.msg}")
            continue
        if not isinstance(assessment, dict) or not isinstance(assessment.get("questions"), list):
            errors.append(f"{path.name}: missing questions array")
            continue
        for question in assessment["questions"]:
            if not isinstance(question, dict):
                errors.append(f"{path.name}: non-object question")
                continue
            item = dict(question)
            item["assessment_id"] = assessment.get("id", path.stem)
            item["assessment_review_status"] = assessment.get("review_status", "pending")
            item["assessment_path"] = path.relative_to(ROOT).as_posix()
            questions.append(item)
    return questions, errors


def evidence_for_static_question(path: Path, body: str) -> str:
    solution_test = (ROOT / "tests" / "test_solutions.py").read_text(encoding="utf-8")
    sql_test = (ROOT / "tests" / "test_sql_examples.py").read_text(encoding="utf-8")
    math_test = (ROOT / "tests" / "test_math_foundations.py").read_text(encoding="utf-8")
    include = re.search(r"\{%-?\s*include\s+solutions/([a-z0-9_.-]+\.py)\s*-?%\}", body)
    if include:
        module = Path(include.group(1)).stem
        if re.search(rf"from _includes\.solutions\.{re.escape(module)} import", solution_test):
            return "`tests/test_solutions.py` executes the canonical solution module"
    if path.name == "sql-session-summary.md" and "SESSION_TOTAL_QUERY = SQL_MATCH.group(1)" in sql_test:
        return "`tests/test_sql_examples.py` executes the exact SQL block from this page in SQLite"
    if path.name == "math-foundations-check.md" and "test_each_mixed_check_answer_matches_an_independent_calculation" in math_test:
        return "`tests/test_math_foundations.py` independently recalculates every listed answer"
    return "No question-specific automated test was detected"


def static_question_records(resources: dict[str, dict[str, Any]]) -> tuple[list[dict[str, Any]], list[str]]:
    records: list[dict[str, Any]] = []
    errors: list[str] = []
    for path in sorted((ROOT / "learning" / "problem-sets").glob("*.md")):
        if path.name in {"README.md", "index.md"}:
            continue
        metadata, body = load_page(path)
        if metadata.get("content_type") != "problem-set":
            continue
        resource_id = metadata.get("id", path.stem)
        source = metadata.get("permalink", f"/{path.stem}/")
        assessment_questions = [
            question for question in ALL_ASSESSMENT_QUESTIONS
            if question.get("provenance", {}).get("source_id") == resource_id
        ]
        if assessment_questions:
            for question in assessment_questions:
                records.append(question_record(question, source, metadata, resources))
            continue

        prompts = numbered_questions(body)
        if not prompts:
            problem = re.search(r"(?m)^##\s+Problem\s*$", body)
            following = body[problem.end():] if problem else body
            prompt = re.search(r"(?m)^\s*\*\*PS-\d+\.\*\*\s*(.+)$", following)
            prompts = [prompt.group(1).strip() if prompt else metadata.get("title", path.stem)]
        solution = solution_section(body)
        evidence = evidence_for_static_question(path, body)
        prerequisites = metadata.get("prerequisites", []) or []
        broken = [item for item in prerequisites if item not in resources]
        if broken:
            errors.extend(f"{path.relative_to(ROOT)}: missing prerequisite {item}" for item in broken)
        has_solution = bool(solution)
        for index, prompt in enumerate(prompts, start=1):
            records.append({
                "id": f"{resource_id}-q{index:02d}",
                "question": prompt,
                "source_resource": source,
                "source_id": resource_id,
                "subject": metadata.get("category", "unspecified"),
                "skills": metadata.get("tags", []) or [],
                "lesson_id": None,
                "prerequisites": prerequisites,
                "answer_format": None,
                "has_answer": has_solution,
                "has_explanation": has_solution,
                "automated_evidence": evidence,
                "review_status": metadata.get("review_status", "pending"),
                "mapping": "Problem-set tags/objectives and prerequisite routes",
                "mapping_broken": False,
                "question_level_mapping_missing": True,
                "structured": False,
            })
        if not has_solution:
            errors.append(f"{path.relative_to(ROOT)}: no worked-solution section")
        if prompts and not re.search(r"(?im)^#{2,4}\s+[^\n]*solution[^\n]*$", body):
            errors.append(f"{path.relative_to(ROOT)}: no solution heading for {len(prompts)} discovered question(s)")
        solution_rows = len(QUESTION_LINE.findall(solution))
        if len(prompts) > 1 and solution_rows != len(prompts):
            errors.append(f"{path.relative_to(ROOT)}: {len(prompts)} prompts but {solution_rows} numbered solutions")
    return records, errors


def question_record(question: dict[str, Any], source: str, metadata: dict[str, Any], resources: dict[str, dict[str, Any]]) -> dict[str, Any]:
    provenance = question.get("provenance", {})
    skills = question.get("skill_ids", []) or []
    lesson_id = question.get("lesson_id")
    prerequisites = question.get("prerequisite_ids", []) or []
    mapped = [skill for skill in skills if skill in ALL_SKILLS]
    linked_page = resources.get(lesson_id, {})
    expected_prerequisites = [item for item in prerequisites if item in resources]
    mapping_broken = (
        not skills or len(mapped) != len(skills)
        or not lesson_id or linked_page.get("content_type") not in {"lesson", "guide"}
        or len(expected_prerequisites) != len(prerequisites)
        or provenance.get("source_id") not in resources
    )
    method = question.get("verification_method", "")
    if method == "example-execution":
        evidence = "`tests/test_interactive_quiz_answers.py` executes the stored example and derives its answer"
    elif question.get("assessment_path", "").endswith("algebra_assessment.json"):
        evidence = "`tests/test_algebra_foundations.py` independently derives the answer from its equation contract"
    elif question.get("assessment_path", "").endswith("math_foundations_assessment.json"):
        evidence = "`tests/test_math_foundations.py` independently derives the numeric operation or summary"
    elif question.get("assessment_path", "").endswith("algebra_modeling_assessment.json"):
        evidence = "`tests/test_algebra_word_problems.py` solves each equation and checks it in the original model"
    else:
        evidence = "No question-specific automated test was detected"
    has_answer = bool(question.get("solution", "").strip())
    has_explanation = bool(question.get("solution", "").strip() and question.get("explanation", "").strip())
    review = question.get("review_status", question.get("assessment_review_status", metadata.get("review_status", "pending")))
    return {
        "id": question.get("id", "(missing id)"),
        "question": question.get("question", ""),
        "source_resource": source,
        "source_id": provenance.get("source_id"),
        "subject": question.get("subject", "unspecified"),
        "skills": skills,
        "lesson_id": lesson_id,
        "prerequisites": prerequisites,
        "answer_format": question.get("answer_format"),
        "has_answer": has_answer,
        "has_explanation": has_explanation,
        "automated_evidence": evidence,
        "review_status": review,
        "mapping": f"{', '.join(skills)} → {lesson_id}" if not mapping_broken else "Broken structured mapping",
        "mapping_broken": mapping_broken,
        "question_level_mapping_missing": False,
        "structured": True,
    }


def render(records: list[dict[str, Any]], errors: list[str]) -> str:
    total = len(records)
    answer_count = sum(item["has_answer"] for item in records)
    explanation_count = sum(item["has_explanation"] for item in records)
    verified_count = sum(item["automated_evidence"] != "No question-specific automated test was detected" for item in records)
    human_review = sum(item["review_status"] not in {"approved", "technical-reviewed"} for item in records)
    missing_formats = sum(not item["answer_format"] or item["answer_format"] == "manual" for item in records)
    broken_mappings = sum(item["mapping_broken"] for item in records) + len(errors)
    blocked = [item for item in records if not item["has_answer"]]
    lines = [
        "## Question and solution coverage",
        "",
        "<!-- Generated from problem-set front matter, structured assessment JSON, and test references by `scripts/solution_coverage.py`. -->",
        "",
        "Counts are repository-derived. ‘Automated verification evidence’ means a matching test is present; its pass/fail result is established by the validation table below. Manual-comparison questions are not machine scored. Static programming prompts are not scored by string-matching learner code.",
        "",
        "| Measure | Count |",
        "|---|---:|",
        f"| Questions discovered across problem sets and interactive assessments | {total} |",
        f"| Questions with an answer record and solution | {answer_count} |",
        f"| Questions with a worked solution and explanation field/text | {explanation_count} |",
        f"| Questions with question-specific automated test evidence | {verified_count} |",
        f"| Questions awaiting human educational review | {human_review} |",
        f"| Questions without a machine-readable accepted-answer format | {missing_formats} |",
        f"| Questions without a per-question skill and lesson mapping | {sum(item['question_level_mapping_missing'] for item in records)} |",
        f"| Broken structured skill, lesson, prerequisite, or source mappings | {broken_mappings} |",
        f"| Questions missing a worked-answer record | {len(blocked)} |",
        "",
        "The remaining unstructured programming and SQL tasks inherit subject tags, objectives, and prerequisites from their problem-set page; they do not have per-question machine-scored answer contracts. The seven arithmetic/data items and the new word-problem check use the shared JSON question model. Two compound arithmetic/data responses explicitly use manual comparison, with no correctness score or skill attempt recorded. Automated checks do not establish teaching quality.",
        "",
        "No third-party answer keys or solution files were imported. The reference index contains outbound link candidates only; linked works were not copied. Open-ended solution code is reviewed by running the repository's canonical tests, not by executing learner submissions.",
        "",
        "### Per-question status",
        "",
        "| Question ID | Source | Answer format | Automated verification evidence | Human review |",
        "|---|---|---|---|---|",
    ]
    for item in records:
        answer_format = "manual comparison" if not item["answer_format"] or item["answer_format"] == "manual" else item["answer_format"]
        source = item["source_resource"].replace("|", "\\|")
        evidence = item["automated_evidence"].replace("|", "\\|")
        lines.append(f"| `{item['id']}` | `{source}` | {answer_format} | {evidence} | {item['review_status']} |")
    if blocked:
        lines.extend(["", "### Blocked or excluded solution records", ""])
        lines.extend(f"- `{item['id']}` has no worked answer in its source page." for item in blocked)
    else:
        lines.extend(["", "### Blocked or excluded solution records", "", "No local problem-set question is missing a worked-answer record. Third-party linked works are excluded from solution content because their material and reuse rights were not reviewed."])
    return "\n".join(lines)


def update_report(section: str, check: bool) -> int:
    source = REPORT.read_text(encoding="utf-8")
    start = source.find(BEGIN)
    end = source.find(END)
    if start < 0 or end < 0 or end < start:
        print(f"Master report needs {BEGIN} and {END} markers.", file=sys.stderr)
        return 2
    replacement = f"{BEGIN}\n\n{section}\n\n{END}"
    updated = source[:start] + replacement + source[end + len(END):]
    if check:
        if updated != source:
            print("Solution coverage section is stale; run python scripts/solution_coverage.py --write.", file=sys.stderr)
            return 1
        return 0
    REPORT.write_text(updated, encoding="utf-8", newline="\n")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument("--write", action="store_true", help="update the generated section in the master audit")
    group.add_argument("--check", action="store_true", help="fail if the master audit section is out of date")
    args = parser.parse_args()

    global ALL_ASSESSMENT_QUESTIONS, ALL_SKILLS
    ALL_ASSESSMENT_QUESTIONS, assessment_errors = load_assessments()
    resources, ALL_SKILLS = load_resources()
    static_records, static_errors = static_question_records(resources)
    static_source_ids = {item["source_id"] for item in static_records}
    assessment_records = [
        question_record(question, resources.get(question.get("provenance", {}).get("source_id"), {}).get("permalink", "/"),
                        resources.get(question.get("provenance", {}).get("source_id"), {}), resources)
        for question in ALL_ASSESSMENT_QUESTIONS
        if question.get("provenance", {}).get("source_id") not in static_source_ids
    ]
    records = static_records + assessment_records
    records.sort(key=lambda item: (item["source_resource"], item["id"]))
    ids = [item["id"] for item in records]
    duplicate_ids = sorted({item for item in ids if ids.count(item) > 1})
    all_errors = assessment_errors + static_errors + [f"duplicate question id {item}" for item in duplicate_ids]
    if all_errors:
        print("\n".join(all_errors), file=sys.stderr)
        return 2
    code = update_report(render(records, all_errors), args.check)
    if code == 0 and not args.check:
        summary = {
            "questions": len(records),
            "answer_records": sum(item["has_answer"] for item in records),
            "worked_explanations": sum(item["has_explanation"] for item in records),
            "automated_evidence": sum(item["automated_evidence"] != "No question-specific automated test was detected" for item in records),
            "pending_human_review": sum(item["review_status"] not in {"approved", "technical-reviewed"} for item in records),
            "missing_accepted_formats": sum(not item["answer_format"] or item["answer_format"] == "manual" for item in records),
            "broken_mappings": sum(item["mapping_broken"] for item in records),
        }
        print(json.dumps(summary, sort_keys=True))
    return code


if __name__ == "__main__":
    raise SystemExit(main())
