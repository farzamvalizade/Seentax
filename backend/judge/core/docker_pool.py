import queue
import time
from docker import DockerClient


class DockerPool:
    def __init__(self, image, pool_size=10, max_age=1800):
        self.client = DockerClient.from_env()
        self.image = image
        self.pool = queue.Queue(maxsize=pool_size)
        self.max_age = max_age
        self._init_pool(pool_size)

    def _create_container(self):
        container = self.client.containers.run(
            self.image,
            command=["sleep", "infinity"],
            detach=True,
            mem_limit="256m",
            cpu_period=100000,
            cpu_quota=50000,
            network_mode="none",
            user="1000:1000",
            security_opt=["no-new-privileges", "apparmor=docker-default"],
            cap_drop=["ALL"],
            pids_limit=300
        )
        container.start_time = time.time()
        return container

    def _init_pool(self, pool_size):
        for _ in range(pool_size):
            container = self._create_container()
            self.pool.put(container)

    def acquire(self):
        container = self.pool.get()

        if time.time() - container.start_time > self.max_age:
            try:
                container.stop()
                container.remove()
            except Exception:
                pass
            container = self._create_container()

        return container

    def release(self, container):
        self.pool.put(container)

    def cleanup(self):
        while not self.pool.empty():
            container = self.pool.get()
            try:
                container.stop()
                container.remove()
            except:
                pass
