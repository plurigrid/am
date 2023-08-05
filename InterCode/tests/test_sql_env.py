```python
import unittest
from InterCode.sql_env import SQLEnvironment

class TestSQLEnvironment(unittest.TestCase):

    def setUp(self):
        self.sql_env = SQLEnvironment()

    def test_initial_state(self):
        self.assertEqual(self.sql_env.get_state(), "")

    def test_execute_valid_sql(self):
        self.sql_env.execute("CREATE TABLE test (id INT, name VARCHAR(20));")
        result = self.sql_env.execute("INSERT INTO test VALUES (1, 'John');")
        self.assertEqual(result, "Query executed successfully")

    def test_execute_invalid_sql(self):
        with self.assertRaises(Exception):
            self.sql_env.execute("INSERT INTO non_existent_table VALUES (1, 'John');")

    def test_reset(self):
        self.sql_env.execute("CREATE TABLE test (id INT, name VARCHAR(20));")
        self.sql_env.reset()
        with self.assertRaises(Exception):
            self.sql_env.execute("INSERT INTO test VALUES (1, 'John');")

if __name__ == '__main__':
    unittest.main()
```