```python
class Bid:
    def __init__(self, agent_id, task_id, bid_amount):
        self.agent_id = agent_id
        self.task_id = task_id
        self.bid_amount = bid_amount

    def get_agent_id(self):
        return self.agent_id

    def get_task_id(self):
        return self.task_id

    def get_bid_amount(self):
        return self.bid_amount
```