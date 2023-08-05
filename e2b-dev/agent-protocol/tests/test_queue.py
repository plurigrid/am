```python
import unittest
from e2b_dev.agent_protocol.queue import Queue

class TestQueue(unittest.TestCase):

    def setUp(self):
        self.queue = Queue()

    def test_enqueue(self):
        self.queue.enqueue('Task1')
        self.assertEqual(self.queue.peek(), 'Task1')

    def test_dequeue(self):
        self.queue.enqueue('Task1')
        task = self.queue.dequeue()
        self.assertEqual(task, 'Task1')

    def test_is_empty(self):
        self.assertTrue(self.queue.is_empty())
        self.queue.enqueue('Task1')
        self.assertFalse(self.queue.is_empty())

    def test_peek(self):
        self.queue.enqueue('Task1')
        self.assertEqual(self.queue.peek(), 'Task1')
        self.queue.enqueue('Task2')
        self.assertEqual(self.queue.peek(), 'Task1')

    def test_size(self):
        self.assertEqual(self.queue.size(), 0)
        self.queue.enqueue('Task1')
        self.assertEqual(self.queue.size(), 1)

if __name__ == '__main__':
    unittest.main()
```