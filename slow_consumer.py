import threading
import time
from threading import Lock

from component import Component


class SlowConsumer(Component):
    def __init__(self):
        super().__init__(name="SlowConsumer")
        self.lock = threading.Lock()


    def start(self):
        pass

    def stop(self):
        pass

    def on_data(self, data):
        if self.lock.acquire(blocking=True, timeout=1):
            print("Slow Consumer", data['frame_count'])
            time.sleep(1)
            self.lock.release()
