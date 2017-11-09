import numpy as np
import argparse
import time
import cv2
 
# color values in BGR
colorLower = np.array([255, 255, 0], dtype = "uint8")
colorUpper = np.array([255, 255, 150], dtype = "uint8")
camera = cv2.VideoCapture(0)

while True:
    (grabbed, frame) = camera.read()
    if not grabbed:
        break

    color = cv2.inRange(frame, colorLower, colorUpper)
    color = cv2.GaussianBlur(color, (3, 3), 0)
    (_, contours, _) = cv2.findContours(color.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # See if we any regions of the specified color
    if len(contours) > 0:
        # Detect the largest region
        contour = sorted(contours, key = cv2.contourArea, reverse = True)[0]
        rect = np.int32(cv2.cv.BoxPoints(cv2.minAreaRect(contour)))
        
        # Draw a rectangular frame around the detected object
        cv2.drawContours(frame, [rect], -1, (0, 255, 0), 2)
    
    cv2.imshow("Color Tracker", frame)
    time.sleep(0.025)
    if cv2.waitKey(1) & 0xFF == ord("q"):
	    break

camera.release()
cv2.destroyAllWindows()
