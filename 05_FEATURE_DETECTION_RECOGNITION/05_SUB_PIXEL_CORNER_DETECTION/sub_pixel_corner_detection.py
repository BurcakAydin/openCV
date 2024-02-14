import numpy as np
import cv2 as cv

src = cv.imread('/Users/burcakaydin/PycharmProjects/openCV/05_FEATURE_DETECTION_RECOGNITION/05_SUB_PIXEL_CORNER_DETECTION/blocks.png')

def process(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    corners = cv.goodFeaturesToTrack(gray, 35, 0.05, 10)
    for pt in corners:
        print(pt)
        b = np.random.randint(0, 256)
        g = np.random.randint(0, 256)
        r = np.random.randint(0, 256)
        x = np.int32(pt[0][0])
        y = np.int32(pt[0][1])
        cv.circle(image, (x, y), 5, (int(b), int(g), int(r)), 2)

    winSize = (3, 3)
    zeroZone = (-1, -1)

    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_COUNT, 40, 0.001)
    corners = cv.cornerSubPix(gray, corners, winSize, zeroZone, criteria)

    for i in range(corners.shape[0]):
        print(" -- Refined Corner [", i, "] (", corners[i, 0, 0], ", ", corners[i, 0, 1], ")")
    return image

result = process(src)
cv.imshow('result', result)
cv.waitKey(1)