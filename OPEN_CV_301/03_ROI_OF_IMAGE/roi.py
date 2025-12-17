#ROI (Region of interest) (İlgilenilen alan)
import cv2 as cv
import numpy as np

src = cv.imread("C:/Users/Mustafa/PycharmProjects/OpenCV/OPEN_CV_301/03_ROI_OF_IMAGE/opencv.png")

h,w = src.shape[:2]

img = src.copy()

roi = img[100:150, 250:330, :]

roi.shape[:2]

print(roi)

print(roi.shape)

cv.imshow("roi",roi)
cv.waitKey(0)

img[0:50, 0:80, :] = roi
cv.imshow("img", img)
cv.waitKey(0)

res=cv.resize(roi,None, fx=0.3, fy=0.3, interpolation=cv.INTER_CUBIC)
cv.imshow("res",res)
cv.waitKey(0)

res.shape[:2]

img[0:15, 0:24, :] = res
cv.imshow("img", img)
cv.waitKey(0)

src[0:15,0:24,:] = res
cv.imshow("img", src)
cv.waitKey(0)
