import cv2 as cv

#HSV
img = cv.imread("C:/Users/Mustafa/PycharmProjects/OpenCV/OPEN_CV_301/01_CHANCING_COLORSPACE/opencv.png")
cv.namedWindow("rgb", cv.WINDOW_AUTOSIZE)
cv.imshow("rgb", img)
cv.waitKey(0)

#RGB to GRAY
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)
cv.waitKey(0)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("hsv", hsv)
cv.waitKey(0)