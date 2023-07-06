from concurrent.futures import ThreadPoolExecutor
from typing import Type

from component import Component


class ThreadedPipeline:
    def __init__(self):
        self.component_configs = {}
        self.components = {}
        self._pool = ThreadPoolExecutor(max_workers=10)

    def add_component(self, component: Type[Component], arguments={}, parent=None):
        if parent is None:
            self.component_configs[component] = {"arguments": arguments, "children": []}
        else:
            self.component_configs[parent]["children"].append([component, arguments])
        return self

    def publish(self, component: Component, data):

        children = self.component_configs.get(type(component)).get("children", [])
        for child in children:
            child_class = child[0]
            child = self.components.get(child_class)
            if child:
                self._pool.submit(child.on_data, data)


    def start(self):
        for component_cls in self.component_configs:
            arguments = self.component_configs[component_cls]['arguments']
            def init_component(component, arguments):
                c = component(**arguments)
                c.set_pipeline(self)
                self.components[component] = c
                c.start()
            self._pool.submit(init_component, component_cls, arguments)
            for child in self.component_configs[component_cls]["children"]:
                self._pool.submit(init_component, child[0], child[1])

    def stop(self):
        for component in self.component_configs:
            component.stop()

