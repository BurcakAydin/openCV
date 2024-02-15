import numpy as np
import cv2 as cv

path = "openCV/02_PERFORMANCE_MEASUREMENTS/01_IMAGE_PIXEL_VALUE_STATISTICS/"

src = cv.imread(path + "opencv.png", cv.IMREAD_GRAYSCALE)


# minMaxLoc

min_value, max_value, min_loc, max_loc = cv.minMaxLoc(src)
print("min_value: %.2f, max_value: %.2f" % (min_value, max_value))
# min_value: 0.00, max_value: 247.00
# This means that the darkest pixel in the image has a value of 0 (black)
# and the brightest pixel has a value of 247 (almost white).

print("min_loc", min_loc, ",", "max_loc", max_loc)
# min_loc (27, 261) , max_loc (0, 0)


#meanStdDev
means, stddev = cv.meanStdDev(src)
print("mean: %.2f, stddev: %.2f" % (means, stddev))
# mean: 196.82, stddev: 80.07

src[np.where(src < means)] = 0
src[np.where(src > means)] = 255
cv.imshow("binary", src)
cv.waitKey(1)


"""
cv.imshow("output", src)
cv.waitKey(1)
cv.destroyAllWindows()
"""
