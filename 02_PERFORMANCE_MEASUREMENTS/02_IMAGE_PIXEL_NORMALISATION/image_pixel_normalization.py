import numpy as np
import cv2 as cv

path = "/openCV/02_PERFORMANCE_MEASUREMENTS/02_IMAGE_PIXEL_NORMALISATION/"

src = cv.imread(path + "opencv.png")
print(src.shape)  # (338, 300, 3)

# cvtColor
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)
cv.waitKey(1)

print(gray.shape)

print(gray)


gray = np.float32(gray)  # Ondalıklı sayıya  çevirme. Int yuvarlama yaptığı için
print(gray)

# Min MAx Normalizasyon: verilen iki değer arasında dönüşüm yapar

min_value, max_value, min_loc, max_loc = cv.minMaxLoc(gray)
print("min_value: %.2f, max_value: %.2f" % (min_value, max_value))
# min_value: 0.00, max_value: 247.00

means, stddev = cv.meanStdDev(gray)
print("mean: %.2f, stddev: %.2f" % (means, stddev))
# mean: 197.08, stddev: 79.81

# Sıfırlardan oluşan bir array oluşturalım
dst = np.zeros(gray.shape, dtype=np.float32)
cv.normalize(gray, dst=dst, alpha=0, beta=1.0, norm_type=cv.NORM_MINMAX)
print(dst)


print(np.uint8(dst*255))
means, stddev = cv.meanStdDev(dst)
print("mean: %.2f, stddev: %.2f" % (means, stddev))
cv.imshow("NORM_MINMAX", dst)
cv.waitKey(1)


# Print results with two decimal places
print("mean: %.2f, stddev: %.2f" % (mean, stddev))
cv.imshow("NORM_MINMAX", dst)
cv.waitKey(1)

min_value, max_value, min_loc, max_loc = cv.minMaxLoc(dst)
print("min_value: %.2f, max_value: %.2f" % (min_value, max_value))
#  min_value: 0.00, max_value: 1.00

means, stddev = cv.meanStdDev(dst)
print("mean: %.2f, stddev: %.2f" % (means, stddev))
#  mean: 0.80, stddev: 0.32
#  Aynı çıktıları/resimleri aldık, resmin ama hattını koruyorum.
#  Gösterim şeklini değiştirdim, bellekte daha az yer kaplıyor.
#  Float hesaplama yapmak için veri kaybını engellemede, işlemlerden sonra int yaptık.


### NORM_INF ###
dst = np.zeros(gray.shape, dtype=np.float32)
cv.normalize(gray, dst=dst, alpha=0, beta=1.0, norm_type=cv.NORM_INF)
print(dst)
cv.imshow("NORM_INF", np.uint8(dst*255))
cv.waitKey(1)

### NORM_L1 ###
dst = np.zeros(gray.shape, dtype=np.float32)
cv.normalize(gray, dst=dst, alpha=0, beta=1.0, norm_type=cv.NORM_L1)
print(dst)
cv.imshow("NORM_L1", np.uint8(dst*10000000))
cv.waitKey(1)

