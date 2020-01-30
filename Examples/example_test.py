from USBCamera import USBCamera
import cv2 as cv
from window import *
from constants import Cameras, HSV_ranges
from cleaning_tools import *
from draw_on_frame import *

camera = USBCamera(0, 1.5, 50)
cam_window = CameraWindow("cam", camera)
tresh_window = FeedWindow("treshhold")
circled_window = FeedWindow("cicle")
circled_window.open()
tresh_window.open()
cam_window.open()
while True:
    hsv_frame, frame = cam_window.show_and_get_color_frame(cv.COLOR_BGR2HSV)
    if frame is None:
        break
    tresh = cv.inRange(hsv_frame, HSV_ranges.Powercell.low, HSV_ranges.Powercell.high)
    tresh = median_blur(tresh, 11)
    contours = find_contours(tresh)
    if len(contours) > 0:
        biggest_contour = max(contours, key = cv.contourArea)
        cicrle_frame, center, radius = draw_cicle_and_return_values(frame, biggest_contour)
        circled_window.show_frame(cicrle_frame)

    tresh_window.show_frame(tresh)
        
