import numpy as np
import cv2 as cv

src = cv.imread('/Users/burcakaydin/PycharmProjects/openCV/04_IMAGE_PROCESSING/06_FAST_IMAGE_EDGE_FILTERING_ALGORİTHM/test.png')
cv.imshow("input", src)
cv.waitKey(1)

h, w = src.shape[:2]

dst = cv.edgePreservingFilter(src, sigma_s=100, sigma_r=0.4, flags=cv.RECURS_FILTER)

result = np.zeros([h, w*2, 3], dtype=src.dtype)
result[0:h, 0:w, :] = src
result[0:h, w:2 * w, :] = dst

result = cv.resize(result, (w, h//2))  # 2 resmi yan yana
cv.imshow("output", result)
cv.waitKey(1)