import numpy as np
import cv2 as cv

src = cv.imread('/Users/burcakaydin/PycharmProjects/openCV/04_IMAGE_PROCESSING/08_CANNY_EDGE_DETECTION/keanu.png')

cv.imshow('src', src)
cv.waitKey(1)

edges = cv.Canny(src, 100, 200) # 100-300 dene

cv.imshow('edges', edges)
cv.waitKey(1)

