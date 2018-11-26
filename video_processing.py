#video processing
import cv2
import math


def video_process():
    count = 0
    video_file = "Before Sunrise Trailer.mp4"
    capture = cv2.VideoCapture(video_file)
    frameRate = capture.get(5)
    x=1
    while(capture.isOpened()):
        frame_id = capture.get(1)
        ret, frame = capture.read()
        if (ret != True):
            break
        if (frame_id % math.floor(frameRate) == 0):
            filename ="frame%d.jpg" % count;count+=1
            cv2.imwrite('images/' + filename, frame)

    capture.release()

video_process()