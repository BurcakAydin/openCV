import numpy as np
import cv2 as cv

path = "openCV/01_BASIC_OPERATIONS/08_BASIC_THRESHOLDING/"
img = cv.imread(path + "work.png")

T = 100

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

for i in range(5):
    ret, binary = cv.threshold(gray, T, 255, i)
    cv.imshow("binary_" + str(i), binary)

cv.waitKey(1)
