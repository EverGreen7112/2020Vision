import math
import cv2 as cv
from draw_on_frame import get_rectangle_value

def find_distance_from_objecet(focal_length: float, area: int, known_area: float) -> float:
    """
    Calculates the distance between the center of the object and the camera
    :param focal_lenght: Focal lenght of the camera - need calibration
    TODO Calibrate the focal lenght
    :param area: The area of the object (pixels^2)
    :param known_area: The known area of the object (m^2)
    """
    return focal_length * math.sqrt(known_area / area)

def find_angle(distance_from_center :float, camera_fov: float, image_total_pixels: int) -> float:
    """
    Calculates the angle between the camera and the center of the object
    :param distance_from_center: The distance between the center of the object to the center of the picture (in pixels)
    :param camera_fov: The camera's fov
    :param image_total_pixels: image total pixels
    """
    return (distance_from_center * camera_fov) / image_total_pixels

def middle_of_rect(point1: tuple, point2: tuple) -> tuple:
    """
    Returns a tuple that represents the midle of the rect coordinate (x,y)
    :param: point1: First point in the rect
    :param: point2: Second point in the rect
    """
    mid_x = int((point1[0] + point2[0])/2)
    mid_y = int((point1[1] + point2[1])/2)
    return (mid_x, mid_y)

def distance_from_center(center_of_object: tuple, center_of_image: tuple) -> int:
    """
    Returns the distance from the center_of_image (x,y) to the center of the object (x,y)
    :param center_of_object: Center of the object tuple (x,y)
    :param center_of_image: Center of the image tuple (x,y)
    """
    obj_mid_x = center_of_object[0]
    img_mid_x = center_of_image[0]
    return img_mid_x - obj_mid_x

def distance_from_center__rect(point1: tuple, point2: tuple, center_of_image: tuple) -> int:
    """
    Returns the distance between the center of the rect to the center of the image
    :param: point1: First point in the rect
    :param: point2: Second point in the rect
    :param center_of_image: Center of the image tuple (x,y)
    """
    rect_mid = middle_of_rect(point1, point2)
    return distance_from_center(rect_mid, center_of_image)

def get_circle_area(radius) -> float:
    """
    Returns the area of the circle (radius^2 * pi)
    :param radius: The radius of the circle
    """
    return radius*radius*math.pi

def get_rect_area(point1, point2) -> float:
    """
    Retues the area of the circle
    :param: point1: First point in the rect
    :param: point2: Second point in the rect
    """
    width = abs(point1[0] - point2[0])
    height = abs(point1[1] - point2[1])
    return width * height

def get_shape_center(contour) -> tuple:
    """
    Retuns the center of the contour by building a counding rect and calculating his center
    :param contour: The contour
    """
    point1, point2 = get_rectangle_value(contour)
    return middle_of_rect(point1, point2)

def get_shape_area(contour) -> float:
    """
    Simple function that returns the area of the contour
    :param contour: The contour
    """
    return cv.contourArea(contour)