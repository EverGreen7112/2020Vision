from __future__ import print_function
import cv2 as cv
import argparse
import numpy as np
import math
import imutils

KNOWN_WIDTH = 18
max_value = 255
max_value_H = 360 // 2
low_H = 20
low_S = 115
low_V = 80
high_H = 38
high_S = 242
high_V = 255
kernel_value = 15
kernel_value_name = "Kernel"
focal_length = 801
focal_length_name = "Focal length"
window_capture_name = 'Video Capture'
window_detection_name = 'Object Detection'
low_H_name = 'Low H'
low_S_name = 'Low S'
low_V_name = 'Low V'
high_H_name = 'High H'
high_S_name = 'High S'
high_V_name = 'High V'
image_mid_x = 640
image_mid_y = 360
camera_fov = 50
image_total_pixels = 1280

def on_low_H_thresh_trackbar(val):
    global low_H
    global high_H
    low_H = val
    low_H = min(high_H - 1, low_H)
    cv.setTrackbarPos(low_H_name, window_detection_name, low_H)


def on_high_H_thresh_trackbar(val):
    global low_H
    global high_H
    high_H = val
    high_H = max(high_H, low_H + 1)
    cv.setTrackbarPos(high_H_name, window_detection_name, high_H)


def on_low_S_thresh_trackbar(val):
    global low_S
    global high_S
    low_S = val
    low_S = min(high_S - 1, low_S)
    cv.setTrackbarPos(low_S_name, window_detection_name, low_S)


def on_high_S_thresh_trackbar(val):
    global low_S
    global high_S
    high_S = val
    high_S = max(high_S, low_S + 1)
    cv.setTrackbarPos(high_S_name, window_detection_name, high_S)


def on_low_V_thresh_trackbar(val):
    global low_V
    global high_V
    low_V = val
    low_V = min(high_V - 1, low_V)
    cv.setTrackbarPos(low_V_name, window_detection_name, low_V)


def on_high_V_thresh_trackbar(val):
    global low_V
    global high_V
    high_V = val
    high_V = max(high_V, low_V + 1)
    cv.setTrackbarPos(high_V_name, window_detection_name, high_V)


def set_kernel_value(val):
    global kernel_value
    kernel_value = val
    cv.setTrackbarPos(kernel_value_name, window_detection_name, kernel_value)


def set_focal_length(val):
    global focal_length
    focal_length = val
    cv.setTrackbarPos(focal_length_name, window_detection_name, focal_length)

cap = cv.VideoCapture(0)

cv.namedWindow(window_capture_name, cv.WINDOW_NORMAL)
cv.namedWindow(window_detection_name, cv.WINDOW_NORMAL)


cv.createTrackbar(focal_length_name, window_detection_name, focal_length, 1500, set_focal_length)
cv.createTrackbar(kernel_value_name, window_detection_name, kernel_value, 50, set_kernel_value)
cv.createTrackbar(low_H_name, window_detection_name, low_H, max_value_H, on_low_H_thresh_trackbar)
cv.createTrackbar(high_H_name, window_detection_name, high_H, max_value_H, on_high_H_thresh_trackbar)
cv.createTrackbar(low_S_name, window_detection_name, low_S, max_value, on_low_S_thresh_trackbar)
cv.createTrackbar(high_S_name, window_detection_name, high_S, max_value, on_high_S_thresh_trackbar)
cv.createTrackbar(low_V_name, window_detection_name, low_V, max_value, on_low_V_thresh_trackbar)
cv.createTrackbar(high_V_name, window_detection_name, high_V, max_value, on_high_V_thresh_trackbar)


def get_width(cntr):
    marker = cv.minAreaRect(cntr)
    return marker[1][0]

def covert_center_touple_to_int(center):
    center = list(center)
    for i in range(2):
        center[i] = int(center[i])
    center = tuple(center)
    return center
def clean_image(frame, kernel):
    opening = cv.morphologyEx(frame, cv.MORPH_OPEN, kernel)
    closing = cv.morphologyEx(opening, cv.MORPH_CLOSE, kernel)
    return closing

def distance_to_camera(knownWidth, focalLength, perWidth):
	return (knownWidth * focalLength) / perWidth

while True:
    res, frame = cap.read()

    #frame = cv.imread("powercell.jpg")

    if frame is None:
        break

    frame_HSV = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
  
    frame_threshold = cv.inRange(frame_HSV, (low_H, low_S, low_V), (high_H, high_S, high_V))

    kernel = np.ones((kernel_value, kernel_value), np.uint8)
   
    closing = clean_image(frame_threshold, kernel)

    contours, hierarchy = cv.findContours(closing, cv.RETR_EXTERNAL, 2)

    if len(contours) > 0:
        for cnt in contours:

            contour_width = get_width(cnt)
            if contour_width == 0:
                break

            #peri = cv.arcLength(cnt, True)
            #approx = cv.approxPolyDP(cnt, 0.01 * peri, True)
            #cv.drawContours(frame, [approx], -1, (0, 0, 0), 5)

            distance = distance_to_camera(KNOWN_WIDTH, focal_length, contour_width)

            x, y, w, h = cv.boundingRect(cnt)

            cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 7)

            center, radius = cv.minEnclosingCircle(cnt)   

            center = covert_center_touple_to_int(center)     

            cv.circle(frame, center, int(radius) ,(0, 255, 0), 5)

            distance_between_the_ball_and_the_center_of_the_image = image_mid_x - center[0]

            angle = (distance_between_the_ball_and_the_center_of_the_image * camera_fov)/ image_total_pixels

            cv.putText(frame, str(angle), (center), cv.FONT_HERSHEY_SIMPLEX, 2.0, (0, 0, 0), 3)

    cv.imshow(window_capture_name, frame)
    cv.imshow(window_detection_name, closing)
    

    key = cv.waitKey(30)
    if key == ord('q') or key == 27:
        break