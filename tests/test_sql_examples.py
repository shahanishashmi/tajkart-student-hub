import sqlite3
import unittest


class SqlExampleTests(unittest.TestCase):
    def test_session_total_query(self):
        connection = sqlite3.connect(":memory:")
        connection.execute("CREATE TABLE sessions (student_id TEXT, minutes INTEGER)")
        connection.executemany(
            "INSERT INTO sessions VALUES (?, ?)",
            [("L1", 20), ("L1", 15), ("L2", 0), ("L2", 45)],
        )
        result = connection.execute(
            """SELECT student_id, SUM(minutes) AS total_minutes
               FROM sessions
               WHERE minutes > 0
               GROUP BY student_id
               ORDER BY total_minutes DESC"""
        ).fetchall()
        self.assertEqual(result, [("L2", 45), ("L1", 35)])
        connection.close()


if __name__ == "__main__":
    unittest.main()
