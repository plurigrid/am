```python
import unittest
from double_blind_auction import DoubleBlindAuction
from agent import Agent
from queue import Queue
from message import Message

class TestDoubleBlindAuction(unittest.TestCase):

    def setUp(self):
        self.auction = DoubleBlindAuction()
        self.agent1 = Agent("Agent1")
        self.agent2 = Agent("Agent2")
        self.queue = Queue()

    def test_bid(self):
        self.queue.add_task("Task1")
        self.agent1.send_message(Message("bid", "Task1", 100))
        self.agent2.send_message(Message("bid", "Task1", 200))
        self.auction.process_bids(self.queue)
        self.assertEqual(self.queue.get_task("Task1").get_highest_bid(), 200)

    def test_double_blind(self):
        self.queue.add_task("Task2")
        self.agent1.send_message(Message("bid", "Task2", 300))
        self.agent2.send_message(Message("bid", "Task2", 300))
        self.auction.process_bids(self.queue)
        self.assertIsNone(self.queue.get_task("Task2").get_highest_bid())

    def test_no_bids(self):
        self.queue.add_task("Task3")
        self.auction.process_bids(self.queue)
        self.assertIsNone(self.queue.get_task("Task3").get_highest_bid())

if __name__ == '__main__':
    unittest.main()
```