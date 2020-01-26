import cv2 as cv
import numpy as np
from USBCamera import USBCamera

class Window():
    """
    Simple window class who inherits to the other windows classes
    """
    def __init__(self, window_name: str):
        self.window_name = window_name

    def open(self):
        cv.namedWindow(self.window_name)

    def close(self):
        cv.destroyWindow(self.window_name)
    
    def add_trackbar(self, trackbar_name: str, value: int, max_value: int, onChange):
        cv.createTrackbar(trackbar_name, self.window_name, value, max_value, onChange)

    def get_trackbar_pos(self, trackbar_name):
        return cv.getTrackbarPos(trackbar_name, self.window_name)

class CameraWindow(Window):
    """
    A window for displaying information from a given camera
    """
    def __init__(self, window_name: str, camera: USBCamera, exit_button='qQ'):
        """
        Initializes the window
        :param window_name: The window's name
        :param exit_button: The exit button
        :param: camera: camera to read image from
        """
        self.window_name = window_name
        self.exit_button = exit_button
        self.camera = camera
        self.last_key_pressed = None

    def show_frame(self, frame) -> bool:
        if frame is None:
            return False

        cv.imshow(self.window_name, frame)
        k = chr(cv.waitKey(1) & 0xFF)
        self.last_key_pressed = k
        if k in self.exit_button:
            return False
        return True

    def show_and_get_frame(self):
        frame = self.get_frame()
        if self.show_frame(frame):
            return frame
        return None
          
    def get_frame(self):
        ret, frame = self.camera.read()
        return frame

class FeedWindow(Window):
    """
    Basic feed window
    """
    def __init__(self, window_name: str, exit_button='qQ'):
        """
        Initializes the window
        :param window_name: The window's name
        :param exit_button: The exit button
        """
        self.window_name = window_name
        self.exit_button = exit_button
        self.last_key_pressed = None

    def show_frame(self, frame) -> bool:
        if frame is None:
            return False
        cv.imshow(self.window_name, frame)
        k = chr(cv.waitKey(1) & 0xFF)
        self.last_key_pressed = k
        if k in self.exit_button:
            return False
        return True