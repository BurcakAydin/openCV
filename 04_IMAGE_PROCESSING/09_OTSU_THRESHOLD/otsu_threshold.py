import numpy as np
import cv2 as cv

# Görüntüdeki gürültüyü azaltmak için binary dönüşüm yapan fonksiyon
def threshold_demo(image):
    dst = cv.GaussianBlur(image, (3, 3), 0)
    gray = cv.cvtColor(dst, cv.COLOR_BGR2GRAY)
    ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
    cv.imshow('binary', binary)
    return binary

def canny_demo(image):
    t = 100  # ön tanımlı threshold
    canny_output = cv.Canny(image, t, t * 2)
    cv.imshow('canny_output', canny_output)
    return canny_output


src = cv.imread('/openCV/04_IMAGE_PROCESSING/09_OTSU_THRESHOLD/lena.png')
cv.namedWindow('input', cv.WINDOW_AUTOSIZE)
cv.imshow('src', src)
cv.waitKey(1)

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

ret, binary = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
# ret: threshold değeri Out[5]: 114.0
h, w = src.shape[:2]

cv.imshow('gray', gray)
cv.waitKey(1)

