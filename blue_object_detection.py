import cv2
import numpy as np
cap = cv2.VideoCapture(0)
while True:
    _, frame = cap.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_red = np.array([100, 100, 100])
    upper_red = np.array([140, 255, 255])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
    cv2.drawContours(frame, contours, -1, (0,255,0), 3)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        print(area)
    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    key = cv2.waitKey(1)
    if key == ord("q"):
        break