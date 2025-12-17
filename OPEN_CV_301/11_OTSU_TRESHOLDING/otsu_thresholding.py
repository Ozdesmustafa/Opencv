import cv2 as cv
import numpy as np
#görüntüyü ikili(binary yapmayı amaçlar)

src = cv.imread("C:/Users/Mustafa/PycharmProjects/OpenCV/OPEN_CV_301/11_OTSU_TRESHOLDING/lena.jpg")
cv.namedWindow("input", cv.WINDOW_AUTOSIZE)
cv.imshow("input", src)
cv.waitKey(0)

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

ret, binary = cv.threshold(gray,0,255,cv.THRESH_BINARY | cv.THRESH_OTSU) #| işareti bitwise işaretidir

h, w = src.shape[:2]

cv.imshow("binary", binary)
cv.waitKey(0)