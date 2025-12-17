import cv2 as cv
import numpy as np

capture=cv.VideoCapture("C:/Users/Mustafa/PycharmProjects/OpenCV/02_BASIC_OPERATIONS/04_VIDEO_READ_AND_WRITE/video.mp4")
height=capture.get(cv.CAP_PROP_FRAME_HEIGHT)
width=capture.get(cv.CAP_PROP_FRAME_WIDTH)
count=capture.get(cv.CAP_PROP_FRAME_COUNT)
fps=capture.get(cv.CAP_PROP_FPS)
print(height,width,count,fps)

out=cv.VideoWriter("C:/Users/Mustafa/PycharmProjects/OpenCV/02_BASIC_OPERATIONS/04_VIDEO_READ_AND_WRITE/video1.avi",
                    cv.VideoWriter_fourcc("D","I","V","X"), 15,
                    (np.int_(width),np.int_(height)),True)

while True:
    ret, frame = capture.read()
    # görüntü başarıyla alındı mı kontrol et
    if ret is True:
        #okunan görübtüyü ekranda göster
        cv.imshow("video-input", frame)
        out.write(frame)
        #50sn sonra çık
        c = cv.waitKey(50)
        if c == 27:  # esc
            break
    else:
        break

capture.release()
out.release()