# Real-Time Face Detection using Computer Vision

This project demonstrates real-time face detection using Python and OpenCV. It utilizes a pre-trained Haar cascade classifier to detect faces from live webcam footage and overlays rectangles around detected faces.

![thumbnail](https://github.com/tunde262/face_detector_opencv/blob/main/assets/thumbnail.png?raw=true)

## Features
- Real-time face detection using a webcam feed.
- Drawing rectangles around faces as they are detected.
- Designed to be easy to run and modify for other applications of computer vision.

## Requirements
- Python 3.x
- OpenCV (`opencv-python` package)
- NumPy (`numpy` package)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/tunde262/face_detector_opencv.git
   cd face_detector_opencv

2. Install the necessary dependencies:

   ```bash
   pip install opencv-python numpy

## How To Run

1. Make sure your webcam is connected and functional.

2. Run the Python script to start the program:
   
   ```bash
   python face_detector.py

3. The webcam feed will appear with rectangles drawn around any detected faces. Press the q key to exit the program.

## Code Explanation
- The program uses OpenCV’s `CascadeClassifier` with a pre-trained Haar Cascade model to detect faces.
- The webcam feed is captured using `cv2.VideoCapture(0)`, and each frame is converted to grayscale before passing through the detection algorithm.
- Detected faces are highlighted using rectangles (`cv2.rectangle()`).
- The program runs in a loop, processing the video frames until the `q` key is pressed.

## Project Goal

The goal of this project was to explore the applications of computer vision in object detection and build an app using OpenCV to process video for face detection.
