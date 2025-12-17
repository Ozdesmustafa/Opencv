import cv2 as cv
import numpy as np

path="C:/Users/Mustafa/PycharmProjects/OpenCV/02_BASIC_OPERATIONS/05_IMAGE_FLIP/"
src = cv.imread(path + "opencv.png")

#X flip
dst1 = cv.flip(src,0)#x ekseninde 90 derece çevirmek için
cv.imshow("x-flip",dst1)
cv.waitKey(0)

#Y Flip
dst2 = cv.flip(src,1)
cv.imshow("y-flip",dst2)
cv.waitKey(0)
cv.destroyAllWindows()

#XY Flip
dst3 = cv.flip(src,-1)
cv.imshow("xy-flip",dst3)
cv.waitKey(0)
cv.destroyAllWindows()