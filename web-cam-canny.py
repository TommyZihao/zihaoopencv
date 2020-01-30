import cv2
import numpy as np


cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)
cap.open(0)

while cap.isOpened():
    flag, frame = cap.read()
    if not flag:
        break
    key_pressed = cv2.waitKey(60)

    # frame = cv2.resize(frame, (100,100))
    frame = cv2.Canny(frame, 100, 200)
    frame = np.dstack((frame, frame, frame))
    cv2.imshow('frame2',frame)

    # Break if escape key pressed
    if key_pressed == 27:
        break
cap.release()
cv2.destroyAllWindows()
