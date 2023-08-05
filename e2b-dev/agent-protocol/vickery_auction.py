```python
from queue import PriorityQueue
from agent import Agent
from message import Message

class VickeryAuction:
    def __init__(self):
        self.bids = PriorityQueue()
        self.messages = []

    def place_bid(self, agent: Agent, bid: int):
        self.bids.put((-bid, agent))

    def send_message(self, message: Message):
        self.messages.append(message)

    def run_auction(self):
        if self.bids.qsize() < 2:
            raise Exception("Not enough bids to run the auction")

        highest_bid = self.bids.get()
        second_highest_bid = self.bids.get()

        winner_message = Message(highest_bid[1], "You won the auction with a bid of " + str(-highest_bid[0]))
        self.send_message(winner_message)

        price_message = Message(highest_bid[1], "The price you need to pay is " + str(-second_highest_bid[0]))
        self.send_message(price_message)

    def get_messages(self):
        return self.messages
```