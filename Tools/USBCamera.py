import cv2 as cv


class USBCamera(cv.VideoCapture):
    """
    a basic usb connected camera which inherits from cv VideoCapture
    :param port: the usb port to which the camera is connected
    """

    def __init__(self, port, focal_length, fov):
        """
        initializes the camera
        """
        cv.VideoCapture.__init__(self, port)
        self.port = port
        self.focal_length = focal_length
        self.fov = fov

    def is_opened(self) -> bool:
        return self.isOpened()

    def set_exposure(self, exposure):
        return self.set(cv.CAP_PROP_EXPOSURE, exposure)

    def set_auto_exposure(self, auto):
        return self.set(cv.CAP_PROP_AUTO_EXPOSURE, auto)

    def get_width(self):
        return self.get(cv.CAP_PROP_FRAME_WIDTH)

    def get_height(self):
        return self.get(cv.CAP_PROP_FRAME_HEIGHT)

    def set_width(self, width):
        return self.set(cv.CAP_PROP_FRAME_WIDTH, width)

    def set_height(self, height):
        return self.set(cv.CAP_PROP_FRAME_HEIGHT, height)