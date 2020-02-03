import cv2 as cv
import numpy as np
from copy import deepcopy

def find_contours(frame, mode=0, method=2) -> list:
    """
    Returns a list of all contours
    """
    contours, hierarchy = cv.findContours(frame, mode, method)
    return contours

def draw_circle(frame, center: tuple, radius: float, color=(0, 255, 0), thick=5):
    """
    Draws a bounding cicle
    :param frame: Frame
    :param center: The center of the circle
    :param radius: The radius of the circle
    """
    frame = deepcopy(frame)
    cv.circle(frame, center, int(radius) ,color, thick)
    return frame

def get_circle_value(contour):
    """
    Returns the cicle center coordinate and radius
    :param contour: The contour
    """
    center, radius = cv.minEnclosingCircle(contour)   
    center = list(center)
    for i in range(2):
        center[i] = int(center[i])
    center = tuple(center)
    return center, radius

def draw_cicle_and_return_values(frame_to_draw_on, contour):
    """
    Draws a bounding cicle and
    Returns the cicle radius and center coordinate
    :param frame_to_draw_on: The frame that I want to draw the circle on
    :param contour: The contour
    """
    center, radius = get_circle_value(contour)
    frame_to_draw_on = draw_circle(frame_to_draw_on, center, radius)
    return frame_to_draw_on, center, radius

def draw_rectangle(frame, point1: tuple, point2: tuple, color=(0, 255, 0), thick=5):
    """
    Draws a bounding rectangle
    :param frame: Frame
    :param point1: First point on the rectangle
    :param point2: Second point on the rectangle
    """
    frame = deepcopy(frame)
    frame = cv.rectangle(frame, point1, point2, color, thick)
    return frame

def get_rectangle_value(contour):
    """
    Returns the 2 bounding rectangle points
    :param contour: The contour
    """
    x, y, w, h = cv.boundingRect(contour)
    return (x,y), (x + w, y + h)

def draw_rectangle_and_return_values(frame_to_draw_on, contour):
    """
    Draws a bounding rectangle and
    Returns the 2 bounding rectangle points
    :param frame_to_draw_on: The frame that I want to draw the circle on
    :param contour: The contour
    """
    point1, point2 = get_rectangle_value(contour)
    frame_to_draw_on = draw_rectangle(frame_to_draw_on, point1, point2)
    return frame_to_draw_on, point1, point2

def get_rotated_rect_value(contour):
    """
    Returns the 4 bounding rectangle points
    :param contour: The contour
    """
    box = cv.minAreaRect(contour)
    points = cv.boxPoints(box)
    points = np.int0(points)
    return points


def draw_rotated_rect(frame, points, color=(0, 255, 0), thick=5):
    """
    Draws a bounding rectangle
    :param frame: Frame
    :param points: Points on the rectangle
    """
    frame = deepcopy(frame)
    cv.drawContours(frame, [points], 0, color, thick)
    return frame

def draw_rotated_rect_and_return_values(frame_to_draw_on, contour):
    """
    Draws a rotated bounding rectangle and
    Returns the 4 bounding rectangle points
    :param frame_to_draw_on: The frame that I want to draw the circle on
    :param contour: The contour
    """
    points = get_rotated_rect_value(contour)
    frame_to_draw_on = draw_rotated_rect(frame_to_draw_on, points)
    return frame_to_draw_on, points

