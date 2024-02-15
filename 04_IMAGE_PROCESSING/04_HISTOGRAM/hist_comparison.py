import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv


src1 = cv.imread('/openCV/04_IMAGE_PROCESSING/04_HISTOGRAM/bat.png')
src2 = cv.imread('/openCV/04_IMAGE_PROCESSING/04_HISTOGRAM/lab.png')
src3 = cv.imread('/openCV/04_IMAGE_PROCESSING/04_HISTOGRAM/opencv.png')

# cvtColor

hsv1 = cv.cvtColor(src1, cv.COLOR_BGR2HSV)
hsv2 = cv.cvtColor(src2, cv.COLOR_BGR2HSV)
hsv3 = cv.cvtColor(src3, cv.COLOR_BGR2HSV)

# calcHist
hist1 = cv.calcHist([hsv1], [0, 1], None, [60, 64], [0, 180, 0, 256])
hist2 = cv.calcHist([hsv2], [0, 1], None, [60, 64], [0, 180, 0, 256])
hist3 = cv.calcHist([hsv3], [0, 1], None, [60, 64], [0, 180, 0, 256])

# Normalize

cv.normalize(hist1, hist1, 0, 1.0, cv.NORM_MINMAX)
cv.normalize(hist2, hist2, 0, 1.0, cv.NORM_MINMAX)
cv.normalize(hist3, hist3, 0, 1.0, cv.NORM_MINMAX)

# compareHist

# HISTCOMP_CORREL
cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)  # Out[4]: 0.0030450057822488147 hiç benzemeyen 2 resim
cv.compareHist(hist1, hist3, cv.HISTCMP_CORREL)   # Out[6]: 0.08381127482129354
cv.compareHist(hist3, hist2, cv.HISTCMP_CORREL)   # Out[5]: 0.0705304932225868

