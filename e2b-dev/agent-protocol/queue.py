```python
import queue
from task import Task

class TaskQueue:
    def __init__(self):
        self._queue = queue.Queue()

    def add_task(self, task: Task):
        self._queue.put(task)

    def get_task(self) -> Task:
        return self._queue.get()

    def is_empty(self) -> bool:
        return self._queue.empty()
```