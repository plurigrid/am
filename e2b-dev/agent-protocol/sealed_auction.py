```python
from .auction import Auction
from .bid import Bid
from .task import Task
from .agent import Agent

class SealedAuction(Auction):
    def __init__(self, task: Task):
        super().__init__(task)
        self.bids = []

    def place_bid(self, agent: Agent, bid: Bid):
        self.bids.append((agent, bid))

    def resolve_auction(self):
        winning_bid = max(self.bids, key=lambda x: x[1].amount)
        self.task.assign_to(winning_bid[0])
        return winning_bid
```