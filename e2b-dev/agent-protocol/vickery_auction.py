```python
from .auction import Auction
from .bid import Bid

class VickeryAuction(Auction):
    def __init__(self, task):
        super().__init__(task)
        self.highest_bid = None
        self.second_highest_bid = None

    def place_bid(self, bid: Bid):
        if not self.highest_bid or bid.amount > self.highest_bid.amount:
            self.second_highest_bid = self.highest_bid
            self.highest_bid = bid
        elif not self.second_highest_bid or bid.amount > self.second_highest_bid.amount:
            self.second_highest_bid = bid

    def get_winner(self):
        return self.highest_bid.agent if self.highest_bid else None

    def get_price(self):
        return self.second_highest_bid.amount if self.second_highest_bid else 0
```