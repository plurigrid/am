```python
from .message import Message
from .agent import Agent
from .task import Task
from .bid import Bid

class Communication:
    def __init__(self):
        self.messages = []

    def send_message(self, sender: Agent, receiver: Agent, content: str):
        message = Message(sender, receiver, content)
        self.messages.append(message)
        receiver.receive_message(message)

    def broadcast_task(self, sender: Agent, task: Task):
        for agent in Agent.all_agents:
            if agent != sender:
                self.send_message(sender, agent, f"New task available: {task.description}")

    def send_bid(self, sender: Agent, receiver: Agent, bid: Bid):
        self.send_message(sender, receiver, f"New bid: {bid.amount} for task {bid.task_id}")

    def announce_winner(self, sender: Agent, receiver: Agent, task: Task, bid: Bid):
        self.send_message(sender, receiver, f"Winner for task {task.id}: Agent {bid.agent_id} with bid {bid.amount}")
```