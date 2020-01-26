import math

def find_distance_from_objecet(focal_length, area, known_area):
    return focal_length * math.sqrt(known_area / area)

def find_angle(distance_from_center, camera_fov, image_total_pixels):
    """
    :param distance_from_center: The distance between the center of the object to the center of the picture (in pixels)
    :param camera_fov: The camera's fov
    :param image_total_pixels: image totalpixels
    """
    return (distance_from_center * camera_fov) / image_total_pixels
