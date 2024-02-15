import numpy as np
import cv2 as cv

src = cv.imread('openCV/04_IMAGE_PROCESSING/05_GAUSSIAN_BILATERAL_BLUR/test.png')
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
cv.waitKey(1)

h, w = src.shape[:2]

dst = cv.bilateralFilter(src,0, 50, 10)  # 100 ve 20 ile daha blur oluyor

result = np.zeros([h, w*2, 3], dtype=src.dtype)
result[0:h, 0:w, :] = src
result[0:h, w:2 * w, :] = dst
cv.imshow("output", result)
cv.waitKey(1)
