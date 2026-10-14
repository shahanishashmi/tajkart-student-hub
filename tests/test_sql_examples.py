import sqlite3
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SQL_SOURCE = (ROOT / "learning" / "problem-sets" / "sql-session-summary.md").read_text(encoding="utf-8")
SQL_MATCH = re.search(r"```sql\s*\n(.*?)\n```", SQL_SOURCE, re.S)
if not SQL_MATCH:
    raise RuntimeError("SQL problem must contain a runnable query")
SESSION_TOTAL_QUERY = SQL_MATCH.group(1)


class SqlExampleTests(unittest.TestCase):
    def query(self, connection):
        return connection.execute(SESSION_TOTAL_QUERY).fetchall()

    def setUp(self):
        connection = sqlite3.connect(":memory:")
        connection.execute("CREATE TABLE sessions (student_id TEXT, minutes INTEGER)")
        self.addCleanup(connection.close)
        self.connection = connection

    def test_session_totals_ignore_non_positive_and_null_minutes(self):
        self.connection.executemany(
            "INSERT INTO sessions VALUES (?, ?)",
            [
                ("L1", 20), ("L1", 15), ("L1", None),
                ("L2", 0), ("L2", 45), ("L3", -8),
                ("L4", 12), ("L5", 12),
            ],
        )
        self.assertEqual(self.query(self.connection), [("L2", 45), ("L1", 35), ("L4", 12), ("L5", 12)])

    def test_no_rows_returns_no_students(self):
        self.assertEqual(self.query(self.connection), [])

    def test_only_non_positive_rows_returns_no_students(self):
        self.connection.executemany(
            "INSERT INTO sessions VALUES (?, ?)",
            [("L1", 0), ("L1", -4), ("L2", None)],
        )
        self.assertEqual(self.query(self.connection), [])


if __name__ == "__main__":
    unittest.main()
