import math

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
    :param image_total_pixels: image totalpixels
    """
    return (distance_from_center * camera_fov) / image_total_pixels
