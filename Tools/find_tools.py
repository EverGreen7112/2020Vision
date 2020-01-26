import math

def find_distance_from_objecet(focal_length, area, known_area):
    """
    :param focal_lenght: Focal lenght of the camera - need calibration
    :param area: The area of the object (pixels^2)
    :param known_area: The known area of the object (m^2)
    """
    return focal_length * math.sqrt(known_area / area)

def find_angle(distance_from_center, camera_fov, image_total_pixels):
    """
    :param distance_from_center: The distance between the center of the object to the center of the picture (in pixels)
    :param camera_fov: The camera's fov
    :param image_total_pixels: image totalpixels
    """
    return (distance_from_center * camera_fov) / image_total_pixels
