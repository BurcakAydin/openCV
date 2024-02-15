import numpy as np
import cv2 as cv

path = "/openCV/06_OBJECT_DETECTION/01_TEMPLATE_MATCHING/"

def template_demo():
    src = cv.imread(path + "test.png")
    tpl = cv.imread(path + "test01.png")

    cv.imshow("src", src)
    cv.imshow("tpl", tpl)

    th, tw = tpl.shape[:2]

    result = cv.matchTemplate(src, tpl, method=cv.TM_CCORR_NORMED)

    t = 0.98  # threshold
    loc = np.where(result >= t)

    for pt in zip(*loc[::-1]):
        cv.rectangle(src, pt, (pt[0] + tw, pt[1] + th), (255, 0, 0), 1, 8, 0)

    cv.imshow("first_demo", src)

template_demo()
cv.waitKey(1)
