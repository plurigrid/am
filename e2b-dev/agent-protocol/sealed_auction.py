```python
from queue import Queue
from message import Message
from agent import Agent

class SealedAuction:
    def __init__(self):
        self.bids = {}
        self.queue = Queue()

    def add_task(self, task):
        self.queue.put(task)

    def add_bid(self, agent: Agent, task, bid):
        if task not in self.bids:
            self.bids[task] = []
        self.bids[task].append((agent, bid))

    def resolve_auction(self):
        while not self.queue.empty():
            task = self.queue.get()
            if task in self.bids:
                bids = self.bids[task]
                bids.sort(key=lambda x: x[1], reverse=True)
                winner = bids[0][0]
                winner.receive_message(Message("You won the auction for task: " + task))
                self.bids.pop(task)
```