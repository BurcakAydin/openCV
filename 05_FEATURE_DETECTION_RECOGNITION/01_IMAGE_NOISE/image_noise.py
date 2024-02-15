import numpy as np
import cv2 as cv

src = cv.imread('/openCV/05_FEATURE_DETECTION_RECOGNITION/01_IMAGE_NOISE/opencv.png')
def add_salt_pepper_noise(image):
    h, w = image.shape[:2]
    nums = 10000
    rows = np.random.randint(0, h, nums, dtype=int)
    cols = np.random.randint(0, w, nums, dtype=int)
    for i in range(nums):
        if i % 2 == 0:
            image[rows[i], cols[i]] = (255, 255, 255)
        else:
            image[rows[i], cols[i]] = (0, 0, 0)
    return image

h, w = src.shape[:2]

copy = np.copy(src)
copy = add_salt_pepper_noise(copy)

# 2 resmi yan yana göster

result = np.zeros([h, w*2, 3], dtype=src.dtype)
result[0:h, 0:w, :] = src
result[0:h, w:2*w:, :] = copy
cv.imshow("Original vs Noisy", result)
cv.waitKey(1)

#################
# 2. YOL
#################

def add_salt_pepper_noise(image):
    h, w = image.shape[:2]
    nums = 10000
    rows = np.random.randint(0, h, nums, dtype=int)  # Use Python's built-in int
    cols = np.random.randint(0, w, nums, dtype=int)  # Use Python's built-in int
    for i in range(nums):
        if i % 2 == 0:
            image[rows[i], cols[i]] = (255, 255, 255)  # Salt
        else:
            image[rows[i], cols[i]] = (0, 0, 0)  # Pepper
    return image

copy = add_salt_pepper_noise(src.copy())

# Combine the original and noisy images side by side
result_ = np.hstack((src, copy))  # This is a simpler way to concatenate images horizontally

cv.imshow("Original and Noisy", result_)
cv.waitKey(1)
cv.destroyAllWindows()
