import numpy as np
import cv2 as cv

# Shifting

img = cv.imread('/openCV/04_IMAGE_PROCESSING/02_GEOMETRIC_SHIFTING/opencv.png')

rows = img.shape[0]  # satırlara ait bilgi
cols = img.shape[1]  # sütunlara ait bilgi
print(rows,cols)

M = np.float32([[1, 0, 30], [0, 1, 10]])  # 30 ve 90 kullandım daha büyük resimde daha çok çift olabilir
shifted = cv.warpAffine(img, M, (cols, rows))
cv.imshow("original", img)
cv.waitKey(1)


cv.imshow('shifted', shifted)
cv.waitKey(1)

# Rotation
M = cv.getRotationMatrix2D(((cols/2), rows/2), 90, 1)
dst = cv.warpAffine(img, M, (cols, rows))
cv.imshow("rotated", dst)
cv.waitKey(1)

# Scaling
res = cv.resize(img, None, fx=0.4, fy=0.4, interpolation=cv.INTER_CUBIC)
# fx fy 1den büyük sayılar resmi büyütür
cv.imshow("res", res)
cv.waitKey(1)


# küçük resim

rows = res.shape[0]
cols = res.shape[1]
M = np.float32([[1, 0, 30], [0, 1, 10]])  # 30 ve 90 kullandım daha büyük resimde daha çok çift olabilir
shifted = cv.warpAffine(img, M, (cols, rows))
cv.imshow("kucuk", res)
cv.waitKey(1)

shifted = cv.warpAffine(res, M, (cols, rows))
cv.imshow('shifted', shifted)
cv.waitKey(1)

cv.destroyAllWindows()
