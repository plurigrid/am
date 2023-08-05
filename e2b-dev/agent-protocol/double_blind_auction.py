```python
from auction import Auction
from bid import Bid

class DoubleBlindAuction(Auction):
    def __init__(self, task):
        super().__init__(task)
        self.bids = []

    def place_bid(self, bid: Bid):
        self.bids.append(bid)

    def resolve_auction(self):
        winning_bid = max(self.bids, key=lambda bid: bid.amount)
        self.task.assign_to(winning_bid.agent)
        self.task.set_price(winning_bid.amount)

    def get_bids(self):
        return self.bids
```