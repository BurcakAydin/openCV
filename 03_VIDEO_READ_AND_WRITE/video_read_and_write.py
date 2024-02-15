import numpy as np
import cv2 as cv

capture = cv.VideoCapture("/openCV/03_VIDEO_READ_AND_WRITE/ds_path.mp4")
height = capture.get(cv.CAP_PROP_FRAME_HEIGHT)
width = capture.get(cv.CAP_PROP_FRAME_WIDTH)
count = capture.get(cv. CAP_PROP_FRAME_COUNT)
fps = capture.get(cv. CAP_PROP_FPS)
print(height, width, count, fps)

put = cv.VideoWriter("/openCV/03_VIDEO_READ_AND_WRITE/ds_path_save.avi",
                     cv.VideoWriter_fourcc("D", "I", "V", "X"), 15,
                     (int(width), int(height)), True)  # (np.int(width), np.int(height)) yazınca hata veriyor

while True:
    # kameradan görüntü al
    ret, frame = capture.read()
    # görüntü basaryla alindi mi kontrol
    if ret is True:
        cv.imshow("video-input", frame)
        put.write(frame) # out.write çalışmadı put ile çalıştı
        # 50 sn sonra çık
        c = cv.waitKey(50)
        if c == 27: # ESC
            break
    else:
        break


capture.release()
put.release()  # Make sure to release your VideoWriter object as well
# Finally, close all OpenCV windows
cv.destroyWindow("video-input")
cv.waitKey(0)  # Bununla video kapandı

