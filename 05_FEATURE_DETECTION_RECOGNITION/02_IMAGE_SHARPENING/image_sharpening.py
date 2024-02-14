import numpy as np
import cv2 as cv

img = cv.imread('/Users/burcakaydin/PycharmProjects/openCV/05_FEATURE_DETECTION_RECOGNITION/02_IMAGE_SHARPENING/opencv.png')
sharpened_op = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]], dtype=np.float32)

sharpened_img = cv.filter2D(img, cv.CV_32F, sharpened_op)
sharpened_img = cv.convertScaleAbs(sharpened_img)

cv.imshow('sharpened_img', sharpened_img)
cv.waitKey(1)

# daha keskin hatlara sahip daha düşük kalitede resim ortaya çıkmış