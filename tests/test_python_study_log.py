import json
import tempfile
import unittest
from pathlib import Path

from _includes.solutions.study_log import (
    load_sessions,
    normalize_sessions,
    save_sessions,
    summarize_minutes,
    validate_session,
)


class StudyLogTests(unittest.TestCase):
    def test_validates_and_normalizes_session_fields(self):
        self.assertEqual(validate_session("  Python  ", 25), {"topic": "Python", "minutes": 25})
        for topic, minutes in ((" ", 10), ("Python", 0), ("Python", -1), ("Python", True), (4, 10)):
            with self.subTest(topic=topic, minutes=minutes), self.assertRaises(ValueError):
                validate_session(topic, minutes)

    def test_normalizes_records_and_rejects_malformed_shapes(self):
        self.assertEqual(
            normalize_sessions([{"topic": "SQL", "minutes": 15}]),
            [{"topic": "SQL", "minutes": 15}],
        )
        for records in ({}, ["not an object"], [{"topic": "Python", "minutes": "20"}]):
            with self.subTest(records=records), self.assertRaises(ValueError):
                normalize_sessions(records)

    def test_summarizes_topics_in_stable_order_and_handles_empty_log(self):
        records = [
            {"topic": "Python", "minutes": 20},
            {"topic": "SQL", "minutes": 15},
            {"topic": "Python", "minutes": 10},
        ]
        self.assertEqual(summarize_minutes(records), {"Python": 30, "SQL": 15})
        self.assertEqual(summarize_minutes([]), {})

    def test_missing_file_is_an_empty_log_and_save_round_trips(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sessions.json"
            self.assertEqual(load_sessions(path), [])
            records = [{"topic": "Python", "minutes": 25}]
            save_sessions(path, records)
            self.assertEqual(load_sessions(path), records)
            self.assertEqual(json.loads(path.read_text(encoding="utf-8")), records)

    def test_invalid_json_and_invalid_records_are_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "sessions.json"
            path.write_text("{broken", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "invalid JSON"):
                load_sessions(path)
            path.write_text('[{"topic":"Python","minutes":0}]', encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "positive whole number"):
                load_sessions(path)


if __name__ == "__main__":
    unittest.main()
