# OpenCV Python Documentation:
# https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html

# Camera and Video Capture:
import cv2
import numpy as np


cap = cv2.VideoCapture(0)  # 0 for the default camera

while True:
    ret, frame = cap.read()  # Read a frame from the camera
    width = int(cap.get(3))  # Get the width of the frame
    height = int(cap.get(4))  # Get the height of the frame
    if not ret:
        break  # If no frame is captured, break the loop    
    
    # Draw a line on the captured frame
    # syntax: cv2(source_image, start_point, end_point, color, thickness)
    img = cv2.line(frame, (0,0), (width, height), (255,0,0), 10)
    img = cv2.line(frame, (0, height), (width, 0), (0,0,255), 10)
    # Draw a rectangle on the captured frame
    # syntax: cv2.rectangle(source_image, (start_point), (end_point), color, thickness)
    img = cv2.rectangle(frame, (50, 50), (width-50, height-50), (0,255,0), 8)
    # img = cv2.rectangle(frame, (50, 50), (100, 100), (0,255,0), 8)
    # img = cv2.rectangle(frame, (50, 50), (width-50, height-50), (0,255,0), -1)  # -1 fills the rectangle
    
    # Draw a circle on the captured frame
    # syntax: cv2.circle(source_image, center, radius, color, thickness)
    img = cv2.circle(frame, (200, 200), 50, (128,0,128), 10)

    # Drawing text
    text_font = cv2.FONT_HERSHEY_SIMPLEX  # Font type
    img_text = cv2.putText(frame, 'OpenCV is good', (150, height - 20), text_font, 1, (255, 255, 0), 2, cv2.LINE_AA)

    cv2.imshow('Cam Feed', frame)  # Display the captured frame

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()