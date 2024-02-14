import numpy as np
import cv2 as cv

src = cv.imread('/Users/burcakaydin/PycharmProjects/openCV/05_FEATURE_DETECTION_RECOGNITION/06_HOG_PEDESTRIAN_DETECTION/pedestrain.png')


hog = cv.HOGDescriptor()  # svm method

hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())

rects, weights = hog.detectMultiScale(src,
                                      winStride=(4, 4),
                                      padding=(8, 8),
                                      scale=1.05)  # 1.25 çift dikdörtgen gösteriyordu, bu tam yakaladı

for (x, y, w, h) in rects:
    cv.rectangle(src, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv.imshow('src', src)
cv.waitKey(1)