# OpenCV Python Documentation:
# https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html

# Colors:
import cv2
import numpy as np


cap = cv2.VideoCapture(0)  # 0 for the default camera

while True:
    ret, frame = cap.read()  # Read a frame from the camera
    width = int(cap.get(3))  # Get the width of the frame
    height = int(cap.get(4))  # Get the height of the frame
    if not ret:
        break  # If no frame is captured, break the loop    

    hsv_image = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # Convert the frame to HSV color space
    low_blue = np.array([100, 50, 50])  # Define lower bound for blue color
    high_blue = np.array([140, 255, 255])  # Define upper
    mask = cv2.inRange(hsv_image, low_blue, high_blue)  # Create a mask for blue color
    masked_image = cv2.bitwise_and(frame, frame, mask=mask)  # Apply the mask to the original frame
    
    # cv2.imshow('Cam Feed', masked_image)  # Display the captured frame
    # cv2.imshow('mask', mask)  # Display the mask



    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()