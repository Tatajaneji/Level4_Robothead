import cv2
import os

# create a video capture to read frames from the webcam
cap = cv2.VideoCapture('#')

# specify the number of images to capture
num_image = 5

# create the CaptureImages folder.
if not os.path.exists('CaptureImages'):
    os.makedirs('CaptureImages')

# capture and save the specified number of images.
for i in range(num_image):
    while True:
        # read a frame from the webcam.
        ret, frame = cap.read()

        # display the frame.
        cv2.imshow('Camera', frame)

        # check if the user pressed the 'c' key.
        if cv2.waitKey(1) == ord('#'):
            cv2.imwrite('CaptureImages/image{}.jpg'.format(i), frame)
            break
# release the video capture.
cap.release()
