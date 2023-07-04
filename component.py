from abc import ABC, abstractmethod

class Component(ABC):
    def __init__(self, name: str):
        self._name = name
        self._pipeline = None

    @property
    def name(self):
        return self._name

    def set_pipeline(self, pipeline):
        self._pipeline = pipeline

    def publish(self, data):
        self._pipeline.publish(self, data)

    def on_data(self):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


