```python
from queue import Queue
from message import Message
from agent import Agent

class DoubleBlindAuction:
    def __init__(self):
        self.bids = Queue()
        self.winners = []

    def place_bid(self, agent: Agent, bid: int):
        message = Message(agent, bid)
        self.bids.put(message)

    def resolve_auction(self):
        highest_bid = None
        while not self.bids.empty():
            message = self.bids.get()
            if highest_bid is None or message.content > highest_bid.content:
                highest_bid = message
        self.winners.append(highest_bid.sender)

    def get_winners(self):
        return self.winners
```