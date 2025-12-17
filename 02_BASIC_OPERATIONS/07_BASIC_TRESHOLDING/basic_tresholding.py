import cv2 as cv
path = "C:/Users/Mustafa/PycharmProjects/OpenCV/02_BASIC_OPERATIONS/07_BASIC_TRESHOLDING/"
src = cv.imread(path + "work.png")

T = 127
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
for i in range(5):
    ret, binary = cv.threshold(gray, T, 255, i)
cv.imshow("binary_" + str(i), binary)
cv.waitKey(0)
cv.destroyAllWindows()