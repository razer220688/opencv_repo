# Steps to create a virtual env and link it to the notebook

# creating a virtual env titled as opencv_env
# python -m venv opencv_env

# activating the virtual env
# source opencv_env/bin/activate

# installing ipykernel to link to the jupyter notebook
# pip install ipykernel

# linking the kernel to jupyter notebook after creation (virtual env -> opencv_env)
# python -m ipykernel install --user --name=opencv_env --display-name "opencvenv"

# installing opencv in the created virtual env
# pip install opencv-python

# This is not working in jupyter notebook, so we have to use either pycharm or VSC.


# OpenCV Python Documentation:
# https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html

import cv2

img = cv2.imread('assets/logo.jpg')
# img = cv2.imread('assets/logo.jpg',-1)
# img = cv2.imread('assets/logo.jpg',0)
# img = cv2.imread('assets/logo.jpg',1)
# -1 or cv2.IMREAD_COLOR : loads a color image
# 0 or cv2.IMREAD_GRAYSCALE : loads image in grayscale mode
# 1 or cv2.IMREAD_UNCHANGED : loads image as is including the alpha

# Resizing the image
# img = cv2.resize(img, (400, 400))
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
# cv2.resize() resizes the image to the specified width and height
# The first argument is the image to be resized, and the second argument is a tuple of (width, height)
# The fx and fy parameters are the scaling factors for the width and height respectively
# If the image is larger than the specified size, it will be resized
# If the image is smaller than the specified size, it will be stretched to fit the size

# Rotating the image
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
# cv2.rotate() rotates the image by 90 degrees clockwise
# The first argument is the image to be rotated, and the second argument is the rotation flag

cv2.imshow('Image', img)
# cv2.imshow() displays an image in a window
# The first argument is the window name, and the second argument is the image to be displayed
# The window will automatically fit the image size
# If the image is larger than the screen, it will be resized to fit the screen
# The window will be closed when the user presses any key
# cv2.waitKey(0)
# cv2.waitKey(0) waits for a key event indefinitely, 0 means wait
cv2.waitKey(5000)
# if any other number is passed, it will wait for that many milliseconds
cv2.destroyAllWindows()
# cv2.destroyAllWindows() closes all the windows opened by OpenCV
# cv2.destroyWindow('Image') closes the window with the specified name
# cv2.imshow() does not block the execution of the code, so we need to wait

# Writing the image to a file
cv2.imwrite('assets/logo_changed.jpg', img)
# cv2.imwrite() writes the image to a file
# The first argument is the file name, and the second argument is the image to be written
# The file will be saved in the current working directory
# If the file already exists, it will be overwritten
# If the file does not exist, it will be created
# The file format will be determined by the file extension
# For example, if the file name is 'image.png', the image will be saved in PNG format
# If the file name is 'image.jpg', the image will be saved in JPEG format
# If the file name is 'image.bmp', the image will be saved in BMP format
# If the file name is 'image.tiff', the image will be saved in TIFF format
# If the file name is 'image.gif', the image will be saved in GIF format
# If the file name is 'image.webp', the image will be saved in WebP format
# If the file name is 'image.ppm', the image will be saved in PPM format
# If the file name is 'image.pgm', the image will be saved in PGM format
# If the file name is 'image.pbm', the image will be saved in PBM format
# If the file name is 'image.exr', the image will be saved in EXR format
# If the file name is 'image.hdr', the image will be saved in HDR format
# If the file name is 'image.jp2', the image will be saved in JPEG 2000 format
# If the file name is 'image.png', the image will be saved in PNG format