import cv2 as cv

cap = cv.VideoCapture("C:/Users/Mustafa/PycharmProjects/OpenCV/OPEN_CV_301/16_VIDEO_ANALYSIS_BACKGROUND_FOREGROUND_EXTRACTION/lab3.mp4")
fgbg = cv.createBackgroundSubtractorMOG2(history=250 , varThreshold = 500) #histroy= frameler , threshold =odaklanıcak olan görüntüdeki hassaslık değeri

while True:
    ret, frame = cap.read()
    fgmask = fgbg.apply(frame)
    background = fgbg.getBackgroundImage() #arka planı hesaplayan yer
    cv.imshow("input", frame)
    cv.imshow("mask", fgmask)
    cv.imshow("background", background)
    k = cv.waitKey(10) & 0xFF
    if k == 27:
        break

cap.release()