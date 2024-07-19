import queue


class Publisher:
    def __init__(self, queue):
        self.queue = queue

    async def publish(self, item = queue):
        return self.queue.put(item)

class Subscriber:
    def __init__(self, queue):
        self.queue = queue

    async def consume(self):
        return self.queue.get()