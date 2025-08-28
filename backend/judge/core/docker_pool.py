import queue
from docker import DockerClient


class DockerPool:
    def __init__(self, image, pool_size=10):
        self.client = DockerClient.from_env()
        self.image = image
        self.pool = queue.Queue(maxsize=pool_size)
        self._init_pool(pool_size)

    def _init_pool(self, pool_size):
        for _ in range(pool_size):
            container = self.client.containers.run(
                self.image,
                command=["sleep", "infinity"],
                detach=True,
                mem_limit="256m",
                cpu_period=100000,
                cpu_quota=50000,
                network_mode="none",
                user="1000:1000",
                security_opt=["no-new-privileges"],
            )
            self.pool.put(container)

    def acquire(self):
        return self.pool.get()

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
