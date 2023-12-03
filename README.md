# Thief Detector

This Python script utilizes the OpenCV library to detect motion in a webcam feed and save frames when significant motion is detected. It can be used as a simple "Thief Detector" for monitoring a space. The script captures frames from the webcam, compares them to the previous frame, and highlights regions with significant differences, indicating potential motion.

## Prerequisites

- Python
- OpenCV (`cv2`)
- NumPy

Install the required libraries using:

```bash
pip install opencv-python numpy
```
## How to use:
1. Run the script (thief_detector.py).
2. The webcam feed will open, and the script will continuously monitor for motion.
3. When motion is detected, the script saves a short video clip (video1.avi) containing the frames with detected motion.
4. Press 'q' to exit the script.
## Code Over-view:
1. detect_motion(frame, prev_frame): Function to detect motion by computing the absolute difference between consecutive frames and applying a threshold.
2. main(): Main function to capture frames from the webcam, detect motion, and save frames when motion is significant.
## Adjusting Motion Sensitivity:
- The script uses a contour area threshold (area > 1000) to determine significant motion. You can adjust this threshold based on your specific requirements.
## File Structure:
1. thief_detector.py: The main Python script.
2. video1.avi: The output video file containing frames with detected motion.
