```python
import threading
from collections import deque

class TaskQueue:
    def __init__(self):
        self.queue = deque()
        self.lock = threading.Lock()

    def add_task(self, task):
        with self.lock:
            self.queue.append(task)

    def get_task(self):
        with self.lock:
            if not self.is_empty():
                return self.queue.popleft()
            else:
                return None

    def is_empty(self):
        return len(self.queue) == 0
```