# pip install opencv-python

import cv2 as cv

path = "/01_BASIC_OPERATIONS/01_LOAD_IMAGE/"

img = cv.imread(path + "bozca.png")

type(img)

print(img.shape)

#  nameWindow
cv.namedWindow("opencv_test", cv.WINDOW_AUTOSIZE)  # bir pencerede tuttuk

# imshow
cv.imshow("opencv_test", img)
cv.waitKey(1)  # resmi ekranda sürekli tutulur

# ctrl + c ile çalışma sonlandırılabilir
# cv.waitKey(0) konsol sürekli meşgul kalacaktır.

cv.destroyAllWindows()  # tüm pencereler kapanmalı, kapanmadı, ben de cv.waitKey(0) ile kapattım.