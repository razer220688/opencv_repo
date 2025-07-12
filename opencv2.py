# OpenCV Python Documentation:
# https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html

# Standard is RGB, but OpenCV uses BGR by default
# This means that the red and blue channels are swapped in OpenCV images compared to standard RGB
# Each pixel in an image is represented by three values corresponding to the blue, 
# green, and red channels in OpenCV.
# [[255, 0, 0], [0, 255, 0], [0, 0, 255]] 


# IMAGE MANIPULATIONS
import cv2
import numpy as np
import random

img = cv2.imread('assets/logo.jpg',-1)

print(img)
# prints the numpy array of the image

print(img.shape)
# prints the shape of the image (height, width, channels)

print(img.size)
# prints the size of the image (height * width * channels)

print(img.dtype)
# prints the data type of the image (usually uint8)

for i in range(100):
    for j in range(img.shape[1]):
        # Randomly change the color of each pixel
        img[i, j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]

cv2.imshow('Rand Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Copying and pasting a part of the image
tag = img[500:700, 600:900]
img[100:300, 550:850] = tag
cv2.imshow('Tag Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()