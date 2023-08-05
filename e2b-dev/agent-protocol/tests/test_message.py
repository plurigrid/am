```python
import unittest
from e2b_dev.agent_protocol.message import Message

class TestMessage(unittest.TestCase):

    def setUp(self):
        self.message = Message()

    def test_create_message(self):
        self.message.create("Hello, Agent!")
        self.assertEqual(self.message.content, "Hello, Agent!")

    def test_send_message(self):
        self.message.create("Hello, Agent!")
        response = self.message.send()
        self.assertEqual(response, "Message sent: Hello, Agent!")

    def test_receive_message(self):
        self.message.create("Hello, Agent!")
        self.message.send()
        received_message = self.message.receive()
        self.assertEqual(received_message, "Message received: Hello, Agent!")

if __name__ == '__main__':
    unittest.main()
```