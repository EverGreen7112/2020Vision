from find_tools import *
from draw_on_frame import *
from constants import Cameras
import cv2 as cv

class Shape:
    def __init__(self, contour):
        self.contour = contour
        self.center = get_shape_center(contour)
        self.area = get_shape_area(contour)

    def calculate_distance(self, original_area: float, focal_length: float) -> float:
        distance_from_rect = find_distance_from_objecet(focal_length, self.area, original_area)
        return distance_from_rect
    
    def calculate_angle(self, camera) -> float:
        distance_from_center_of_image = distance_from_center(self.center, camera.middle)
        angle = find_angle(distance_from_center_of_image, camera.fov, camera.image_total_pixels)
        return angle
    
    def draw(self, frame_to_draw_on, color=(0, 255, 0), thick=5):
        frame_to_draw_on = deepcopy(frame_to_draw_on)
        cv.drawContours(frame_to_draw_on, self.contour, -1, color, thick)
        return frame_to_draw_on

class Circle(Shape):
    def __init__(self, contour):
        self.center, self.radius = get_circle_value(contour)
        self.area = get_circle_area(self.radius)
    
    def draw(self, frame_to_draw_on):
        return draw_circle(frame_to_draw_on, self.center, self.radius)

class Rectangle(Shape):
    def __init__(self, contour):
        self.point1, self.point2 = get_rectangle_value(contour)
        self.area = get_rect_area(point1, point2)
        self.center = middle_of_rect(point1, point2)

    def calculate_angle(self, camera) -> float:
        distance_from_center = distance_from_center__rect(self.point1, self.point2, camera.middle)
        angle = find_angle(distance_from_center, camera.fov, camera.image_total_pixels)
        return angle
    
    def draw(self, frame_to_draw_on):
        return draw_rectangle(frame_to_draw_on, self.point1, self.point2)        