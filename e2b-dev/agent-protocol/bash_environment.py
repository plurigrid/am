```python
import subprocess
from execution_feedback import ExecutionFeedback

class BashEnvironment:
    def __init__(self):
        self.feedback = ExecutionFeedback()

    def execute(self, command):
        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
            self.feedback.set_output(output)
            self.feedback.set_error(None)
        except subprocess.CalledProcessError as e:
            self.feedback.set_output(None)
            self.feedback.set_error(str(e))

        return self.feedback
```