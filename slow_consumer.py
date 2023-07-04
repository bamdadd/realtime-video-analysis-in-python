import time

from component import Component


class SlowConsumer(Component):
    def __init__(self):
        super().__init__(name="SlowConsumer")

    def start(self):
        pass

    def stop(self):
        pass

    def on_data(self, data):
        time.sleep(1)
        print("Slow Consumer", data)
