from time import sleep

from PIL import Image

from component import Component


class MockCamera(Component):
    def __init__(self, image_path, fps=14):
        super().__init__(name="MockCamera")
        self._image_path = image_path
        self._fps = fps
        self._running = False
        self.frame_count = 0

    def start(self):
        self._running = True
        self._capture()

    def stop(self):
        self._running = False

    def _capture(self):
        while self._running:
            image = Image.open(self._image_path)
            self.frame_count += 1
            self.publish({"frame_count": self.frame_count, "image": image})
            sleep(1 / self._fps)
