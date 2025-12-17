import cv2 as cv
import numpy as np

src = cv.imread("C:/Users/Mustafa/PycharmProjects/OpenCV/OPEN_CV_301/15_HOFFMAN_CIRCLE_DETECTION/coins.jpg")

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
gray = cv.medianBlur(gray, 7)

circles = cv.HoughCircles(
    gray,
    cv.HOUGH_GRADIENT,
    dp=1,
    minDist=10,     # coin'ler birbirine yakın → 10 çok küçük
    param1=100,     # daha güçlü kenar için
    param2=50,      # yüksek threshold = sadece gerçek daireler
    minRadius=20,   # coin boyutuna göre alt sınır
    maxRadius=100    # coin boyutuna göre üst sınır
)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for (cx, cy, r) in circles[0, :]:
        cv.circle(src, (cx, cy), r, (0, 0, 255), 3)
        cv.circle(src, (cx, cy), 2, (0, 255, 0), 3)

cv.imshow("result", src)
cv.waitKey(0)
