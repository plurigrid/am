```python
from task import Task

class CaptureTheFlag(Task):
    def __init__(self, task_id, task_description, task_difficulty):
        super().__init__(task_id, task_description, task_difficulty)
        self.solution = None

    def set_solution(self, solution):
        self.solution = solution

    def check_solution(self, proposed_solution):
        return self.solution == proposed_solution

    def execute(self, agent):
        proposed_solution = agent.solve_task(self)
        if self.check_solution(proposed_solution):
            return True, "Task solved successfully"
        else:
            return False, "Task solution incorrect"
```