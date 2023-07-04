from debugger import Debugger
from mock_camera import MockCamera
from pipeline import Pipeline
from slow_consumer import SlowConsumer

camera = MockCamera('/Users/bamdad/Downloads/pepsi-max.png')
debugger = Debugger()
slow_consumer = SlowConsumer()
Pipeline() \
    .add_component(camera) \
    .add_component(slow_consumer, parent=camera) \
    .add_component(debugger, parent=camera) \
    .start()
