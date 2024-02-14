import numpy as np
import cv2 as cv

path = "/01_BASIC_OPERATIONS/05_MERGING_TWO_IMAGES/"

img1 = cv.imread(path + "rightimage.png")
img2 = cv.imread(path + "leftimage.png")
cv.imshow("right", img1)
cv.imshow("left", img2)


horizontal = np.hstack((img2, img1))
cv.imshow("horizontal", horizontal)
cv.waitKey(1)

