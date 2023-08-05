```python
class Task:
    def __init__(self, id, description, complexity):
        self.id = id
        self.description = description
        self.complexity = complexity
        self.status = "open"

    def get_id(self):
        return self.id

    def get_description(self):
        return self.description

    def get_complexity(self):
        return self.complexity

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status
```