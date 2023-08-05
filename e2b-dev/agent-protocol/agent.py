```python
import uuid
from .message import Message
from .queue import TaskQueue

class Agent:
    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name
        self.task_queue = TaskQueue()

    def bid(self, task, bid_amount):
        message = Message(sender=self.id, task=task, bid_amount=bid_amount)
        self.task_queue.add_message(message)

    def perform_task(self, task):
        if task in self.task_queue.tasks:
            # Perform the task
            print(f"Agent {self.name} is performing task {task.id}")
            self.task_queue.remove_task(task)
        else:
            print(f"Task {task.id} is not in the task queue of Agent {self.name}")

    def receive_task(self, task):
        self.task_queue.add_task(task)
```