# YOLO Detection

A computer vision project built using **Ultralytics YOLO** and **OpenCV** for experimenting with real-time object detection and other YOLO-based computer vision tasks.

## Features

- Object Detection
- Object Tracking
- Object Counting
- Object Segmentation
- Pose Estimation
- Custom Object Detection
- Image and Video Processing
- Real-time webcam/video inference

## Technologies Used

- Python
- YOLO / Ultralytics
- OpenCV
- NumPy

## Project Structure


YOLO/
│
├── customer_detection.py
├── object_counting.py
├── object_segmentation.py
├── object_tracking.py
├── pose_estimation.py
├── yolo-check.py
├── yolov8_basics.py
├── yolov8_n_opencv.py
├── coco.txt
│
├── weights/
├── runs/
│
└── README.md


## YOLO Models

This project uses YOLO models for different computer vision tasks.

Examples include:


yolo11n.pt
yolov8n.pt
yolov8n-seg.pt


The model files are excluded from Git tracking when appropriate because trained/pretrained weight files can be large.

## Installation

Clone the repository:


git clone https://github.com/likithm19/yolo-detection.git
cd yolo-detection


Create a virtual environment:


python -m venv .venv


Activate the virtual environment on Windows:


.venv\Scripts\activate


Install the required packages:


pip install ultralytics opencv-python numpy


## Running YOLO

For YOLO11 object detection:

python
from ultralytics import YOLO

model = YOLO("yolo11n.pt")

results = model("image.jpg")

results[0].show()


For video or webcam-based detection, the project also contains OpenCV-based Python scripts.

## Project Scripts

### Object Detection

`customer_detection.py`

Used for object detection with a YOLO model.

### Object Tracking

`object_tracking.py`

Used for tracking detected objects across video frames.

### Object Counting

`object_counting.py`

Used for counting objects detected in a video or image.

### Object Segmentation

`object_segmentation.py`

Used for image segmentation using a YOLO segmentation model.

### Pose Estimation

`pose_estimation.py`

Used for human pose estimation using YOLO.

## Notes

Model weight files such as `.pt` files may be excluded from the repository using `.gitignore`.

The project is intended for learning and experimenting with YOLO-based computer vision applications.
Author
 
Likith
