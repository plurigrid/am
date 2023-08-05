```python
import sqlite3
from execution_feedback import ExecutionFeedback

class SQLEnvironment:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def execute(self, sql_command):
        try:
            self.cursor.execute(sql_command)
            self.connection.commit()
            return ExecutionFeedback(True, "Command executed successfully")
        except Exception as e:
            return ExecutionFeedback(False, str(e))

    def fetch(self, sql_command):
        try:
            self.cursor.execute(sql_command)
            rows = self.cursor.fetchall()
            return ExecutionFeedback(True, "Command executed successfully", rows)
        except Exception as e:
            return ExecutionFeedback(False, str(e))

    def close(self):
        self.connection.close()
```