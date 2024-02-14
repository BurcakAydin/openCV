import cv2 as cv

cap = cv.VideoCapture('/Users/burcakaydin/PycharmProjects/openCV/04_IMAGE_PROCESSING/14_VIDEO_ANALYSIS_BACKGROUND_FOREGROUND_EXTRACTION/ds_path.mp4')

fgbg = cv.createBackgroundSubtractorMOG2(history=50, varThreshold=50)

while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    background = fgbg.getBackgroundImage()
    cv.imshow('frame', frame)
    cv.imshow('background', background)
    cv.imshow('fgmask', fgmask)
    k = cv.waitKey(10)&0xff
    if k == 27:
        break
cap.release()
# cap.release() yazmadığımda video çalışıyor ama aşağıdaki hata alınıyor
"""
The error you're encountering, (-215:Assertion failed) size.width>0 && size.height>0 in function 'imshow',
indicates that the imshow function was called with an image (in this case, frame) that is empty or has not been
 successfully read. This usually happens at the end of a video file when there are no more frames to read, or if 
 the video file could not be opened correctly.

To handle this situation, you should check whether the frame has been successfully read before proceeding with 
processing and displaying it. You can do this by checking the ret value returned by cap.read(). If ret is False, 
it means the frame has not been successfully read, and you should break out of the loop.
"""

# Bu kodda hata alınmıyor

import cv2 as cv

cap = cv.VideoCapture(
    '/Users/burcakaydin/PycharmProjects/openCV/04_IMAGE_PROCESSING/14_VIDEO_ANALYSIS_BACKGROUND_FOREGROUND_EXTRACTION/ds_path.mp4')

fgbg = cv.createBackgroundSubtractorMOG2(history=50, varThreshold=50)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break  # Exit the loop if no frame is captured

    fgmask = fgbg.apply(frame)
    background = fgbg.getBackgroundImage()

    cv.imshow('frame', frame)
    if background is not None:  # Check if background image is available
        cv.imshow('background', background)
    cv.imshow('fgmask', fgmask)

    k = cv.waitKey(30) & 0xff
    if k == 27:  # Exit loop if ESC is pressed
        break

cap.release()  # Release the VideoCapture object
cv.destroyAllWindows()  # Close all OpenCV windows
