import numpy as np
import cv2 as cv

def canny_demo(image):
    t = 80  # Default threshold
    canny_output = cv.Canny(image, t, t * 2)
    cv.imshow('canny_output', canny_output)
    return canny_output

src = cv.imread('/openCV/04_IMAGE_PROCESSING/11_HOFFMAN_LINE_DETECTION/sudoku.png')
cv.namedWindow('input', cv.WINDOW_AUTOSIZE)
cv.imshow('src', src)
cv.waitKey(1)

binary = canny_demo(src)

lines = cv.HoughLines(binary, 1, np.pi / 180, 150, None, 0, 0)
if lines is not None:
    for i in range(0, len(lines)):
        rho = lines[i][0][0]
        theta = lines[i][0][1]
        a = np.cos(theta)
        b = np.sin(theta)
        X0 = a * rho
        y0 = b * rho
        pt1 = (int(X0 + 1000 * (-b)), int(y0 + 1000 * (a)))
        pt2 = (int(X0 - 1000 * (-b)), int(y0 - 1000 * (a)))
        cv.line(src, pt1, pt2, (0, 0, 255), 3, cv.LINE_AA)

# Correctly display the image with lines drawn on it
cv.imshow('hoffman_line_demo', src)
cv.waitKey(1)
cv.destroyAllWindows()  # Close all OpenCV windows
