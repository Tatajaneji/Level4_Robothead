import cv2
import numpy as np

# Start the webcam
cap = cv2.VideoCapture(0)
while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to the HSV color space
    'frame_hsv '
    cv2.imshow('HSV',frame_hsv)
    # Define the range of COLOR to detect
    lower_c = np.array(['#'])
    upper_c = np.array(['#'])
    # Create a mask for the frame using the lower and upper bounds of the color
    mask_c = cv2.inRange('#', lower_c, upper_c)
    # Apply the mask to the frame
    c_result = cv2.bitwise_and(frame, frame, mask='#')

    # Show the result
    cv2.imshow('Color Detection', c_result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


