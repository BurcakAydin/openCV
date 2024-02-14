import numpy as np
import matplotlib.pyplot as plt
import cv2 as cv


def custom_hist(gray):
    h, w = gray.shape
    hist = np.zeros([256], dtype=np.int32)
    for row in range(h):
        for col in range(w):
            pv = gray[row, col]
            hist[pv] += 1

    y_pos = np.arange(0, 256, 1, dtype=np.int32)
    plt.bar(y_pos, hist, align='center', color='r', alpha=0.5)
    plt.xticks(y_pos, y_pos)
    plt.ylabel('Frequency')
    plt.title('Histogram')
    plt.show()



def image_hist (image):
    cv.imshow("input", image)
    color = ('blue', 'green', 'red')
    for i, color in enumerate(color):
        hist = cv.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)
        plt.xlim([0, 256])
        plt. show()


src = cv.imread('/Users/burcakaydin/PycharmProjects/openCV/04_IMAGE_PROCESSING/04_HISTOGRAM/lab.png')
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
cv.waitKey(1)


gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
custom_hist(gray)
image_hist(src)


def plot_combined_hist(image):
    # Calculate grayscale histogram
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    hist_gray = cv.calcHist([gray], [0], None, [256], [0, 256]).flatten()

    # Prepare figure
    plt.figure(figsize=(10, 6))

    # Plot Grayscale Histogram as bars
    bars = plt.bar(range(256), hist_gray, color='red', alpha=0.5, label='Grayscale')

    # Calculate and Plot Color Histograms
    colors = ('b', 'g', 'r')
    for i, color in enumerate(colors):
        hist_color = cv.calcHist([image], [i], None, [256], [0, 256]).flatten()
        plt.plot(hist_color, color=color, label=color.capitalize(), linewidth=1.5)

    plt.title('Combined Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.legend()
    plt.xlim([0, 256])

    plt.show()

    plot_combined_hist(src)
    cv.waitKey(1)