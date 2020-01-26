from USBCamera import USBCamera
import cv2 as cv
from window import CameraWindow, FeedWindow
from constants import *
from cleaning_tools import *

camera = USBCamera(0, 1.5, 50)
cam_window = CameraWindow("cam", camera)
cam_window.open()
while True:
    frame = cam_window.show_and_get_frame()
    if frame is None:
        break



