from window import *
from USBCamera import USBCamera
import cv2 as cv
import numpy as np

my_range = np.array([40, 40, 40])

camera = USBCamera(0, 100, 100)
window = CameraWindow("Find_HSV_ranges", camera)
tresh_window = FeedWindow("Treshhold")
window.open()

def crop(frame, x, y, w, h):
    return frame[y:y + h, x:x + w]

med = None
while True:
    frame = window.show_and_get_frame()
    if frame is None:
        break
    if window.last_key_pressed == 'r':
        box = cv.selectROI('Find_HSV_ranges', frame)
        cropped_frame = crop(frame, *box)
        med = np.median(cropped_frame, axis=(0, 1)).astype(int)
        print(med)
        break

ranges = np.array([med - my_range, med + my_range])
for tmp_range in ranges:
    for i, num in enumerate(tmp_range):
        num = min(255, max(0, num))
        tmp_range[i] = num
          
        

tresh_window.open()
tresh_window.show_frame(tresh)