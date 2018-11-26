#video processing
import cv2
import math


def video_process():
    count = 0
    video_file = "Before Sunrise Trailer.mp4"
    capture = cv2.VideoCapture(video_file)
    frame_rate = capture.get(7)

    while(capture.isOpened()):
        frame_id = capture.get(1)
        ret_val, frame = capture.read()
        if (ret_val != True):
            break
        if (frame_id % math.floor(frame_rate) == 0):
            filename ="frame%d.jpg" % count;count+=1
            cv2.imwrite('images/' + filename, frame)

    capture.release()