```python
import docker

class DockerEnvironment:
    def __init__(self):
        self.client = docker.from_env()

    def create_container(self, image, command=None):
        return self.client.containers.run(image, command, detach=True)

    def get_container_logs(self, container):
        return container.logs()

    def stop_container(self, container):
        container.stop()

    def remove_container(self, container):
        container.remove()

    def execute_in_container(self, container, command):
        exec_id = self.client.api.exec_create(container.id, cmd=command)
        return self.client.api.exec_start(exec_id)
```