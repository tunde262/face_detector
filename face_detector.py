# Face Detector w/ Computer Vision
import cv2
import numpy as numpy

# Load pre-trained face data XML file
trained_face_data = cv2.CascadeClassifier \
    (cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Load Webcam Video
webcam = cv2.VideoCapture(0)

while True:

    # Capture current frame
    successful_frame_read, frame = webcam.read()

    # gray-scale the frame picture
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 

    # apply face detection algorithm 
    face_coordinates = trained_face_data.detectMultiScale(gray, 1.3, 5)

    # Draw rectangles around faces
    for(x, y, w, h) in face_coordinates:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 5)

    # Load window onto screen
    cv2.imshow('Webcam Face Detector', frame)

    # Hit 'q' key to quit progam
    if cv2.waitKey(1) == ord('q'):
        break

webcam.release()
cv2.destroyAllWindows()