```python
from abc import ABC, abstractmethod
from .bid import Bid
from .agent import Agent
from .task import Task

class Auction(ABC):
    def __init__(self, task: Task):
        self.task = task
        self.bids = []

    @abstractmethod
    def place_bid(self, agent: Agent, bid: Bid):
        pass

    @abstractmethod
    def determine_winner(self):
        pass

    def add_bid(self, agent: Agent, bid: Bid):
        self.bids.append((agent, bid))

    def get_task(self):
        return self.task

    def get_bids(self):
        return self.bids
```