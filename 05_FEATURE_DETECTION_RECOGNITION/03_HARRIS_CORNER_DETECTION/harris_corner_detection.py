import numpy as np
import cv2 as cv

src = cv.imread(
    '/openCV/05_FEATURE_DETECTION_RECOGNITION/03_HARRIS_CORNER_DETECTION/chessboard.png')


def harris(image):
    blocksize = 2
    apertureSize = 3
    k = 0.04

    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    dst = cv.cornerHarris(gray, blocksize, apertureSize, k)
    dst_norm = np.empty(dst.shape, dtype=np.float32)
    cv.normalize(dst, dst_norm, 0, 255, cv.NORM_MINMAX)

    for i in range(dst_norm.shape[0]):
        for j in range(dst.shape[1]):
            if int(dst_norm[i, j]) > 20:
                cv.circle(image, (j, i), 2, (0, 255, 0), 2)
    return image


result = harris(src)
cv.imshow('result', result)
cv.waitKey(1)

