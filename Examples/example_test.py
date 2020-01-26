from USBCamera import USBCamera
import cv2 as cv
from window import CameraWindow

camera = USBCamera(0, 1.5, 50)
window = CameraWindow("lol", camera)
window.open()
while True:
    frame = window.show_and_get_frame()
    if frame is None:
        break