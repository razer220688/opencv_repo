# Face and eye detection
# we are going to use HAAR cascades to detect faces and eyes in a video stream.
# it is a pre-trained model provided by OpenCV.

# https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbV9DdjFKRmtuQXJqdmVYZVdqNlpyLUliTk9JUXxBQ3Jtc0trYXdNRUZ0bk84VkZHZGpFWHB5RFBOQW15WEdvS2diMDB6aEdVbnZKc0JTdm5mRFctSUhZWWczR0JLZzMxLTQ4a0NfTUpmNVlwTmdSWDlpaURxQWh2NzNzdWsySjlCdnpHYl9jXzV4SkNrejZXUlBIWQ&q=https%3A%2F%2Fstackoverflow.com%2Fquestions%2F20801015%2Frecommended-values-for-opencv-detectmultiscale-parameters&v=mPCZLOVTEc4
# https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbjN1N1BxQ1F5QmdCX01zRkh5ckZVWGo0VHFjQXxBQ3Jtc0ttMGJhbGtLYnhOOFlpOElSdUZIVjNtal83ZzRFWGFDRGVFNmZ1Y2UxcFR0YnU3Nzk1YVpFYjdpaHlzZ2hibm5qN3J5RU5OR2tLV2F3Mkw4MFFzYkhUaC1pVmNycWltRXh4ZGZDTUZRRF92ejRIZlBvYw&q=https%3A%2F%2Fopencv-python-tutroals.readthedocs.io%2Fen%2Flatest%2Fpy_tutorials%2Fpy_objdetect%2Fpy_face_detection%2Fpy_face_detection.html%23face-detection&v=mPCZLOVTEc4


import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 5)
    # faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 4)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 4)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
