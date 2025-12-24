import cv2 as cv

model_bin = "C:/Users/Mustafa/PycharmProjects/OpenCV/1_DNN_VIDEO_FACE_DETECTION_BASED_ON_RESIDUAL_NETWORK/res10_300x300_ssd_iter_140000.caffemodel"
config_text = "C:/Users/Mustafa/PycharmProjects/OpenCV/1_DNN_VIDEO_FACE_DETECTION_BASED_ON_RESIDUAL_NETWORK/deploy.prototxt.txt"

net = cv.dnn.readNetFromCaffe(config_text, model_bin)

net.setPreferableBackend(cv.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv.dnn.DNN_TARGET_CPU)

cap = cv.VideoCapture(0)

while True:
    ret,image = cap.read()
    image = cv.flip(image, 1)
    if ret is False:
        break

    h,w = image.shape[:2]
    blobImage = cv.dnn.blobFromImage(image, 1.0, (300,300), [104,177,123], False, False)
    net.setInput(blobImage)
    cvOut = net.forward()

    # FPS
    t,_ = net.getPerfProfile()
    fps = 1000/(t*1000/cv.getTickFrequency())
    label = "FPS: %.2f" % fps
    cv.putText(image,label,(0,15),cv.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0))

    for detection in cvOut[0,0,:,:]:
        score = float(detection[2])
        if score > 0.5:
            left = int(detection[3] * w)
            top = int(detection[4] * h)
            right = int(detection[5] * w)
            bottom = int(detection[6] * h)

            cv.rectangle(image,(left,top),(right,bottom),(0,255,0),2)
            cv.putText(image,"score:%.2f"%score,(left,top),
                       cv.FONT_HERSHEY_SIMPLEX,0.6,(0,0,255),2)

    cv.imshow("Face-detection-demo",image)
    c = cv.waitKey(2)
    if c == 27:
        break

cap.release()
cv.destroyAllWindows()
