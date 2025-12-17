import cv2 as cv
import numpy as npq

src = cv.imread("C:/Users/Mustafa/PycharmProjects/OpenCV/OPEN_CV_301/09_SOBEL_OPERATOR/opencv.png")

h,w = src.shape[:2]

x_grad = cv.Sobel(src,cv.CV_32F,1,0)#x'e göre türev
y_grad = cv.Sobel(src,cv.CV_32F,0,1)#y'ye göre türev

cv.imshow("x_grad",x_grad)
cv.imshow("y_grad",y_grad)
cv.waitKey(0)
cv.destroyAllWindows()

dst = cv.add(x_grad,y_grad,dtype=cv.CV_16S)
dst = cv.convertScaleAbs(dst)
cv.imshow("dst", dst)
cv.waitKey(0)