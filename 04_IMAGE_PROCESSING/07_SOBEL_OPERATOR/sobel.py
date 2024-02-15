import numpy as np
import cv2 as cv

src = cv.imread('/openCV/04_IMAGE_PROCESSING/07_SOBEL_OPERATOR/opencv.png')

h, w = src.shape[:2]

x_grad = cv.Sobel(src, cv.CV_32F, 1, 0)
y_grad = cv.Sobel(src, cv.CV_32F, 0, 1)

x_grad = cv.convertScaleAbs(x_grad)
y_grad = cv.convertScaleAbs(y_grad)

cv.imshow("x_grad", x_grad)
cv.waitKey(1)

cv.imshow("y_grad", y_grad)
cv.waitKey(1)

dst = cv.add(x_grad, y_grad, dtype=cv.CV_16S)
dst = cv.convertScaleAbs(dst)
cv.imshow("dst", dst)
cv.waitKey(1)
