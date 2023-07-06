from debugger import Debugger
from mock_camera import MockCamera
from pipeline import Pipeline
from slow_consumer import SlowConsumer
from threaded_pipeline import ThreadedPipeline

ThreadedPipeline() \
    .add_component(MockCamera, {"image_path": '/Users/bamdad/Downloads/pepsi-max.png'}) \
    .add_component(Debugger, parent=MockCamera) \
    .add_component(SlowConsumer, parent=MockCamera) \
    .start()

while True:
    pass