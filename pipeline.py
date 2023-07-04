from component import Component


class Pipeline:
    def __init__(self):
        self._components = {}

    def add_component(self, component: Component, parent=None):
        if parent is None:
            self._components[component] = []
        else:
            self._components[parent].append(component)
        return self

    def publish(self, component: Component, data):
        for child in self._components.get(component, []):
            child.on_data(data)

    def start(self):
        for component in self._components:
            component.set_pipeline(self)
            component.start()

    def stop(self):
        for component in self._components:
            component.stop()
