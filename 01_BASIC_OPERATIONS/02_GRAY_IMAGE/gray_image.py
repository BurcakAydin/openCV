
import cv2 as cv

path = "//"
img = cv.imread(path + "opencv.png")
cv.namedWindow("colored", cv.WINDOW_AUTOSIZE)
cv.imshow("colored", img)
cv.waitKey(1)

# cvtColor
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)
cv.waitKey(1)

# imwrite
cv.imwrite(path + "gray_opencv.png", gray)

cv.destroyAllWindows()

img = cv.imread(path + "opencv.png", cv.IMREAD_GRAYSCALE)
cv.namedWindow("gray", cv.WINDOW_AUTOSIZE)
cv.imshow("gray", img)
cv.waitKey(1)