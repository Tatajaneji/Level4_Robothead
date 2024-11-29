import cv2
import numpy as np

# Start the webcam
cap = cv2.VideoCapture(0)
while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to the HSV color space
    frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define color range for Color Detection "COLOR 1"
    c1_lower = np.array([0, 0, 0])
    c1_upper = np.array([0, 0, 0])
    c1_mask = cv2.inRange(frame_hsv, c1_lower, c1_upper)
    # Define color range for Color Detection "COLOR 2"
    c2_lower = np.array([0, 0, 0])
    c2_upper = np.array([0, 0, 0])
    c2_mask = cv2.inRange(frame_hsv, c2_lower, c2_upper)

    # Apply the mask to the frame
    mask1 = cv2.bitwise_xor(c1_mask, c2_mask)
    result = cv2.bitwise_and(frame, frame, mask=mask1)

    # Show the result
    cv2.imshow('MULTICOLOR DETECTION', result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
