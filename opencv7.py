# Template matching and object detection

import numpy as np
import cv2

# Load the main image and the template
img = cv2.imread('assets/soccer_practice.jpg', 0)
template = cv2.imread('assets/ball.PNG', 0)
h, w = template.shape
# h, w = template.shape[:2]

methods = [
    cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED,
    cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED
]

for method in methods:
    img2 = img.copy()

    result = cv2.matchTemplate(img2, template, method)
    # here it performs the template matching using convolution, which means taking our template image and 
    # sliding it over the base image to find matches.
    # The result is a matrix of the same size as the input image, where each pixel value represents how 
    # well the template matches that region of the image.
    # It is given by the formula:
    # (W-w+1, H-h+1)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(min_loc, max_loc)
    if method in ['cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']:
        location = min_loc
    else:
        location = max_loc
    
    bottom_right = (location[0] + w, location[1] + h)
    cv2.rectangle(img2, location, bottom_right, 255, 6)
    cv2.imshow('match', img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

