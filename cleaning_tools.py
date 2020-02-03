import cv2 as cv
import numpy as np

def median_blur(frame, blur_size : int):
    """
    Blurs the image with cv.medianBlue() function, returns the blured frame
    """
    return cv.medianBlur(frame, blur_size)

def erode_and_dilate(frame, kernel, iterations):
    """
    Erodes and dialate the frame with the same kernel, returns the frame
    """
    if iterations is None:
        frame = cv.erode(frame, kernel)
        frame = cv.dilate(frame, kernel)
    else:
        frame = cv.erode(frame, kernel , iterations=iterations)
        frame = cv.dilate(frame, kernel, iterations=iterations)
    return frame    

def open_and_close(frame, kernel):
    """
    Opens and Closes the frame with the same kernel, returns the frame
    """
    opening = cv.morphologyEx(frame, cv.MORPH_OPEN, kernel)
    closing = cv.morphologyEx(opening, cv.MORPH_CLOSE, kernel)
    return closing

def get_kernel(kernel_value):
    """
    Returns the kernel for a specific value
    """
    return np.ones((kernel_value, kernel_value), np.uint8)
