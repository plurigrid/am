```python
import docker
from docker.errors import ContainerError
from .bash_env import BashEnvironment
from .sql_env import SQLEnvironment

class InterCode:
    def __init__(self, language):
        self.language = language
        self.client = docker.from_env()
        self.container = None
        self.env = None
        self.set_environment()

    def set_environment(self):
        if self.language == 'bash':
            self.env = BashEnvironment(self.client)
        elif self.language == 'sql':
            self.env = SQLEnvironment(self.client)
        else:
            raise ValueError(f"Unsupported language: {self.language}")

    def start_container(self):
        self.container = self.env.start_container()

    def stop_container(self):
        self.env.stop_container(self.container)

    def execute_code(self, code):
        try:
            result = self.env.execute_code(self.container, code)
            return result
        except ContainerError as e:
            return str(e)

    def reset(self):
        self.stop_container()
        self.start_container()
```