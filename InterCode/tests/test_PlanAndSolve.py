```python
import unittest
from InterCode.PlanAndSolve import PlanAndSolve

class TestPlanAndSolve(unittest.TestCase):

    def setUp(self):
        self.plan_and_solve = PlanAndSolve()

    def test_initial_state(self):
        self.assertEqual(self.plan_and_solve.current_state, None)

    def test_plan(self):
        self.plan_and_solve.plan('Test task')
        self.assertIsNotNone(self.plan_and_solve.current_state)

    def test_solve(self):
        self.plan_and_solve.plan('Test task')
        result = self.plan_and_solve.solve()
        self.assertIsNotNone(result)

    def test_reset(self):
        self.plan_and_solve.plan('Test task')
        self.plan_and_solve.reset()
        self.assertEqual(self.plan_and_solve.current_state, None)

if __name__ == '__main__':
    unittest.main()
```