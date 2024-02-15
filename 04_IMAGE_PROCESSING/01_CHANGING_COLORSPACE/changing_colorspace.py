# Renk uzayının değiştirilmesi

import cv2 as cv

# HSV

img = cv.imread('/openCV/04_IMAGE_PROCESSING/01_CHANGING_COLORSPACE/opencv.png')
cv.namedWindow("rgb", cv.WINDOW_AUTOSIZE)
cv.imshow("rgb", img)
cv.waitKey(1)

# RGB to GRAY
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)
cv.waitKey(1)


# RGB to GRAY
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("hsv", hsv)
cv.waitKey(1)
