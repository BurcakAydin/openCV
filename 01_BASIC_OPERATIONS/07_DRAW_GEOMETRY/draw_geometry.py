import numpy as np
import cv2 as cv

image = np.zeros((512,512,3), np.uint8)

cv.rectangle(image, (100, 100), (308, 300), (255, 0, 0), 2, cv.LINE_8, 0)
cv.circle(image, (256, 256), 50, (0, 0, 255), 2, cv. LINE_8, 0)
cv.ellipse(image, (256, 256), (150, 50), 360, 0, 360, (0, 255, 0), 2, cv. LINE_8, 0)
cv.imshow("image", image)
cv.waitKey(1)

for i in range(100000):
    image[:, :, :] = 0
    x1 = np.random.rand() * 512
    y1 = np.random.rand() * 512
    x2 = np.random.rand() * 512
    y2 = np.random.rand() * 512
    b = np.random.randint(0, 256)
    g = np.random.randint(0, 256)
    r = np.random.randint(0, 256)
    cv.line(image, (int(x1), int(y1)), (int(x2), int(y2)), (b, g, r), 4, cv.LINE_8, 0)
    # Fixed the typo from 'cv.regtangle' to 'cv.rectangle'
    cv.rectangle(image, (int(x1), int(y1)), (int(x2), int(y2)), (b, g, r), 1, cv.LINE_8, 0)
    cv.imshow("image", image)

    c = cv.waitKey(20)
    if c == 27:  # ESC key
        break
