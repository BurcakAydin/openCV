# ROI (Region of Interest)

import numpy as np
import cv2 as cv

src = cv.imread('/Users/burcakaydin/PycharmProjects/openCV/04_IMAGE_PROCESSING/03_REGION_OF_INTEREST/opencv.png')

h, w = src.shape[:2]
img = src.copy()

roi = img[100:200, 100:200, :]
roi.shape

cv.imshow('ROI', roi)
cv.waitKey(1)


img[50:150, 50:150, :] = roi
cv.imshow('img', img)
cv.waitKey(1)


res = cv.resize(roi, None, fx=0.4, fy=0.4, interpolation=cv.INTER_CUBIC)
cv.imshow("res", res)
cv.waitKey(1)

res.shape[:2]