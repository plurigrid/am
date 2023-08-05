```python
import sqlite3
from intercode import InterCode

class SQLEnvironment(InterCode):
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()

    def execute(self, sql_command):
        try:
            self.cursor.execute(sql_command)
            self.connection.commit()
            return self.cursor.fetchall()
        except sqlite3.Error as e:
            return str(e)

    def reset(self):
        self.cursor.execute("DROP TABLE IF EXISTS auction")
        self.cursor.execute("CREATE TABLE auction (id INTEGER PRIMARY KEY, agent_id INTEGER, bid INTEGER)")
        self.connection.commit()

    def close(self):
        self.connection.close()
```