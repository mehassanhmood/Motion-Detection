# Import necessary libraries
import cv2
import numpy as np

def detect_motion(frame, prev_frame):
    # Convert frames to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_prev_frame = cv2.cvtColor(prev_frame, cv2.COLOR_BGR2GRAY)

    # Compute absolute difference between frames
    diff_frame = cv2.absdiff(gray_prev_frame, gray_frame)

    # Apply threshold to highlight the regions with significant differences
    _, threshold_frame = cv2.threshold(diff_frame, 30, 255, cv2.THRESH_BINARY)

    # Find contours in the thresholded frame
    contours, _ = cv2.findContours(threshold_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Check if any contour has significant area (motion)
    for contour in contours:
        # Calculate the area of the contour
        area = cv2.contourArea(contour)
    
        # Set a threshold for contour area
        if area > 1000:  # You can adjust this threshold based on your specific requirements
            # Draw a rectangle around the object
            x, y, w, h = cv2.boundingRect(contour)
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  # Green rectangle
    
            # Output "UNSAFE" text in red color
            cv2.putText(frame, "UNSAFE", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    return False

def main():
    # Open webcam
    video_capture = cv2.VideoCapture(0)
    
    # Set up video writer
    fourcc = cv2.VideoWriter_fourcc(*"XVID")
    out = cv2.VideoWriter("video1.avi", fourcc, 20.0, (640, 480))

    # Initialize previous frame
    _, prev_frame = video_capture.read()

    while True:
        # Capture frame-by-frame
        ret, frame = video_capture.read()

        if not ret:
            print("Error reading frame from the webcam.")
            break

        # Check for motion
        if detect_motion(frame, prev_frame):
            print("Motion detected! Saving video...")
            for _ in range(30):  # Save 30 frames (approx. 1.5 seconds)
                out.write(frame)
                _, frame = video_capture.read()

        # Update previous frame
        prev_frame = frame.copy()

        # Display the resulting frame
        cv2.imshow('Thief Detector', frame)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release resources
    video_capture.release()
    out.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
