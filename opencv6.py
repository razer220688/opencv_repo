# Check later, not getting the correct output

# OpenCV Python Documentation:
# https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html

# Corner Detection

import cv2
import numpy as np

# Load the image
image = cv2.imread('assets/chessboard.png')
image = cv2.resize(image, (0,0), fx=0.75, fy=0.75)
grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(grey, 100, 0.01, 10)
corners = np.int8(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(image, (x, y), 5, (255,0,0), -1)

for i in range(len(corners)):
    for j in range(i + 1, len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        color = tuple(map(lambda x: int(x), np.random.randint(0,255, size=3)))
        cv2.line(image, corner1, corner2, color, 1)



cv2.imshow('Original Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
