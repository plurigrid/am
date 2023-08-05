```python
import random
from intercode import InterCode

class CaptureTheFlag(InterCode):
    def __init__(self, num_agents, num_flags):
        super().__init__()
        self.num_agents = num_agents
        self.num_flags = num_flags
        self.flags = [False] * num_flags
        self.agent_positions = [0] * num_agents

    def reset(self):
        self.flags = [False] * self.num_flags
        self.agent_positions = [0] * self.num_agents

    def step(self, agent_id, action):
        if action == 'move_forward':
            self.agent_positions[agent_id] += 1
        elif action == 'move_backward':
            self.agent_positions[agent_id] -= 1
        elif action == 'capture_flag':
            if self.agent_positions[agent_id] in range(self.num_flags):
                self.flags[self.agent_positions[agent_id]] = True

    def get_observation(self, agent_id):
        return {
            'position': self.agent_positions[agent_id],
            'flag_status': self.flags[self.agent_positions[agent_id]] if self.agent_positions[agent_id] in range(self.num_flags) else None
        }

    def is_done(self):
        return all(self.flags)

    def get_reward(self, agent_id):
        return sum(self.flags)
```