```python
import unittest
from agent import Agent

class TestAgent(unittest.TestCase):

    def setUp(self):
        self.agent = Agent()

    def test_bid(self):
        task = "Task1"
        bid_amount = 100
        self.agent.bid(task, bid_amount)
        self.assertEqual(self.agent.bids[task], bid_amount)

    def test_execute_task(self):
        task = "Task1"
        self.agent.execute_task(task)
        self.assertIn(task, self.agent.completed_tasks)

    def test_receive_message(self):
        message = "Hello, Agent"
        self.agent.receive_message(message)
        self.assertEqual(self.agent.last_received_message, message)

    def test_send_message(self):
        message = "Hello, Other Agent"
        other_agent = Agent()
        self.agent.send_message(message, other_agent)
        self.assertEqual(other_agent.last_received_message, message)

if __name__ == '__main__':
    unittest.main()
```