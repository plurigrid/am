```python
class ExecutionFeedback:
    def __init__(self, success, message, data=None):
        self.success = success
        self.message = message
        self.data = data

    def is_successful(self):
        return self.success

    def get_message(self):
        return self.message

    def get_data(self):
        return self.data
```