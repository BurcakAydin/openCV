import numpy as np
import cv2 as cv

def canny_demo(image):
    t = 80  # Default threshold
    canny_output = cv.Canny(image, t, t * 2)
    cv.imshow('canny_output', canny_output)
    return canny_output

src = cv.imread('/Users/burcakaydin/PycharmProjects/openCV/04_IMAGE_PROCESSING/12_PROBABILITY_HOFFMAN_LINE_DETECTION/morph01.png')
cv.namedWindow('input', cv.WINDOW_AUTOSIZE)
cv.imshow('src', src)
cv.waitKey(1)

binary = canny_demo(src)
cv.imshow('binary', binary)
cv.waitKey(1)



linesP = cv.HoughLinesP(binary, 1, np.pi / 180, 55, None, 50, 10)
cv.HoughLinesP
if linesP is not None:
    for i in range(0, len(linesP)):
        l = linesP[i][0]
        cv.line(src, (l[0], l[1]), (l[2], l[3]), (255, 0, 0), 1, cv.LINE_AA)


cv.imshow('hoffman_line_demo', src)
cv.waitKey(1)
cv.destroyAllWindows()  # Close all OpenCV windows
