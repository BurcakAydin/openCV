import numpy as np
import cv2 as cv

path = "/openCV/01_BASIC_OPERATIONS/06_IMAGE_FLIP/"
img = cv.imread(path + "opencv.png")

# X Flip
dst1 = cv.flip(img, 0)
cv.imshow("Original", img)
cv.imshow("Flipped-x", dst1)
cv.waitKey(1)

# Y Flip
dst2 = cv.flip(img, 1)
cv.imshow("Original", img)
cv.imshow("Flipped-y", dst2)
cv.waitKey(1)

# XY Flip
dst3 = cv.flip(img, -1)
cv.imshow("Original", img)
cv.imshow("Flipped-xy", dst3)
cv.waitKey(1)

### Fizik 1 Vektör dersini ne güzel anlardık bu örnekle
