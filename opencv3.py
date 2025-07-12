# OpenCV Python Documentation:
# https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html

# Camera and Video Capture:
import cv2
import numpy as np
# OpenCV provides a simple interface to capture video from cameras or video files.
# The cv2.VideoCapture class is used to capture video from a camera or a video file
# The first argument is the camera index (0 for the default camera) or the path to a video file.
# The second argument is the API used to capture the video (optional).

cap = cv2.VideoCapture(0)  # 0 for the default camera

# if you have a video file, you can use it by putting the path and name of the video file instead of 0
# cap = cv2.VideoCapture('path_to_video.mp4')

while True:
    ret, frame = cap.read()  # Read a frame from the camera
    width = int(cap.get(3))  # Get the width of the frame
    height = int(cap.get(4))  # Get the height of the frame
    if not ret:
        break  # If no frame is captured, break the loop
    
    image = np.zeros(frame.shape, dtype=np.uint8)
    # Creates a black image with the same shape as the frame
    resized_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)  
    # Resize the frame to half its original size
    
    # image[:height//2, :width//2] = cv2.rotate(resized_frame, cv2.ROTATE_90_CLOCKWISE)
    # # Place the resized frame in the top-left corner of the black image
    # image[height//2:, :width//2] = cv2.rotate(resized_frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    # image[:height//2, width//2:] = cv2.rotate(resized_frame, cv2.ROTATE_180)
    # image[height//2:, width//2:] = resized_frame

    image[:height//2, :width//2] = cv2.rotate(resized_frame, cv2.ROTATE_180)
    # Place the resized frame in the top-left corner of the black image
    image[height//2:, :width//2] = resized_frame
    image[:height//2, width//2:] = cv2.rotate(resized_frame, cv2.ROTATE_180)
    image[height//2:, width//2:] = resized_frame


    cv2.imshow('Cam Feed', image)
    # Display the captured frame
    # cv2.imshow('Cam Feed', frame)

    # Exit the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()