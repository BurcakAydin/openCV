import numpy as np
import cv2 as cv

src = cv.imread('/openCV/04_IMAGE_PROCESSING/13_HOFFMAN_CIRCLE_DETECTION/coins.png')
if src is None:
    print("Error: Image not found")
    exit()

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
gray = cv.GaussianBlur(gray, (9, 9), 2, 2)

circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 10, param1=100, param2=50, minRadius=20, maxRadius=100)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # draw the outer circle
        cv.circle(src, (i[0], i[1]), i[2], (0, 0, 255), 2)
        # draw the center of the circle
        cv.circle(src, (i[0], i[1]), 2, (0, 255, 0), 3)

cv.imshow('Hough Circle', src)
cv.waitKey(0)  # Wait indefinitely until a key is pressed
cv.destroyAllWindows()
