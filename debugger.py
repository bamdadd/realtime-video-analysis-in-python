from component import Component


class Debugger(Component):
    def __init__(self):
        super().__init__(name="Debugger")

    def start(self):
        pass

    def stop(self):
        pass

    def on_data(self, data):
        print("Debugger", data)
