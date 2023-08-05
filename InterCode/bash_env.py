```python
import subprocess
import shlex

class BashEnvironment:
    def __init__(self):
        self.state = None

    def reset(self):
        self.state = None
        return self.state

    def step(self, action):
        try:
            process = subprocess.Popen(shlex.split(action), stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
            return_code = process.returncode
            if return_code == 0:
                self.state = stdout.decode('utf-8')
                reward = 1
            else:
                self.state = stderr.decode('utf-8')
                reward = -1
            done = True
        except Exception as e:
            self.state = str(e)
            reward = -1
            done = True
        return self.state, reward, done

    def render(self):
        print(self.state)
```