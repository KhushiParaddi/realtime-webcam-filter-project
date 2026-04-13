# Real-Time Webcam Filters using OpenCV

## Overview

This project is a simple real-time webcam filter application built using Python and OpenCV. It captures live video from your webcam and allows you to apply different visual effects instantly using keyboard inputs.

---

## Features

* Live webcam feed
* Multiple real-time filters:

  * Normal view
  * Grayscale
  * Blur
  * Edge Detection
  * Brightness and Contrast Adjustment
* Instant switching between filters using keyboard
* Lightweight and easy to run

---

## Technologies Used

* Python
* OpenCV (cv2)

---

## Installation

1. Install Python (if not already installed)

2. Install OpenCV:

```bash
pip install opencv-python
```

---

## How to Run

1. Save the script as:

```bash
webcam_filters.py
```

2. Run the program:

```bash
python webcam_filters.py
```

---

## Controls

| Key | Function              |
| --- | --------------------- |
| 0   | Normal                |
| 1   | Grayscale             |
| 2   | Blur                  |
| 3   | Edge Detection        |
| 4   | Brightness Adjustment |
| ESC | Exit program          |

---

## How It Works

* `cv2.VideoCapture(0)` is used to access the webcam
* Frames are captured continuously in a loop
* Based on key input, different filters are applied:

  * `cvtColor()` for grayscale conversion
  * `GaussianBlur()` for blur effect
  * `Canny()` for edge detection
  * `convertScaleAbs()` for brightness and contrast adjustment
* Output is displayed using `imshow()`

---

## Notes

* Ensure your webcam is not being used by another application
* If the camera does not open, try changing:

```python
cv2.VideoCapture(0)
```

to:

```python
cv2.VideoCapture(1)
```

---

## Future Improvements

* Add more filters such as sepia, cartoon, or sketch
* Implement face detection and overlay filters
* Add option to save images or record video
* Create a GUI with buttons instead of keyboard controls

---

## Output

The program opens a window showing your webcam feed with filters applied in real time.

---

## Author

KR Tanishkaa 
Khushi Paraddi
Pavithra B
