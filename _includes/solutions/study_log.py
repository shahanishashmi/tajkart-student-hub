"""Small, validated JSON helpers used by the Python study-log path."""

from __future__ import annotations

import json
from pathlib import Path


Session = dict[str, str | int]


def validate_session(topic: object, minutes: object) -> Session:
    """Return a normalized session or explain why its fields are invalid."""
    if not isinstance(topic, str) or not topic.strip():
        raise ValueError("topic must be non-empty text")
    if isinstance(minutes, bool) or not isinstance(minutes, int) or minutes <= 0:
        raise ValueError("minutes must be a positive whole number")
    return {"topic": topic.strip(), "minutes": minutes}


def normalize_sessions(records: object) -> list[Session]:
    """Validate an untrusted JSON value and return clean session records."""
    if not isinstance(records, list):
        raise ValueError("session data must be a list")

    normalized: list[Session] = []
    for position, record in enumerate(records, start=1):
        if not isinstance(record, dict):
            raise ValueError(f"session {position} must be an object")
        normalized.append(validate_session(record.get("topic"), record.get("minutes")))
    return normalized


def summarize_minutes(records: object) -> dict[str, int]:
    """Group validated session minutes by topic, in stable alphabetical order."""
    totals: dict[str, int] = {}
    for record in normalize_sessions(records):
        topic = record["topic"]
        minutes = record["minutes"]
        assert isinstance(topic, str) and isinstance(minutes, int)
        totals[topic] = totals.get(topic, 0) + minutes
    return dict(sorted(totals.items()))


def load_sessions(path: str | Path) -> list[Session]:
    """Load local JSON; a missing file means a new, empty log."""
    file_path = Path(path)
    try:
        raw = json.loads(file_path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        return []
    except json.JSONDecodeError as error:
        raise ValueError(f"invalid JSON in {file_path.name}") from error
    return normalize_sessions(raw)


def save_sessions(path: str | Path, records: object) -> None:
    """Validate and write a local JSON log with readable, stable formatting."""
    normalized = normalize_sessions(records)
    Path(path).write_text(
        json.dumps(normalized, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
