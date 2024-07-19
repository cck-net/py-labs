import asyncio
import threading
import time
from pubsub import Publisher, Subscriber
import queue


q = queue.Queue()
pub = Publisher(q)
sub = Subscriber(q)
counter = 0

def start_publisher():
    def task():
        global counter

        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        while True:
            loop.run_until_complete(pub.publish(f'item {counter}'))
            time.sleep(0.001)  # 1 ms
            counter += 1

    pub_thread = threading.Thread(target=task)
    pub_thread.start()

def start_consumer():
    async def task():
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)

        while True:
            loop.run_until_complete(await sub.consume())
            time.sleep(0.002)

    sub_thread = threading.Thread(target=task)
    sub_thread.start()

def watch_queue():
    def watch_task():
        while True:
            print(f'[{q.qsize()}]')
            time.sleep(1)

    q_thread = threading.Thread(target=watch_task)
    q_thread.start()

start_publisher()
watch_queue()
start_consumer()