import cv2
import numpy as np
import cv2 as cv

path = "C:/Users/Mustafa/PycharmProjects/OpenCV/02_BASIC_OPERATIONS/02_ARITHMETIC_OPERATIONS/03_IMAGE_PIXEL_OPERATION/"

#resim1
img1 = np.zeros([400,400,3], dtype=np.uint8)
img1[100:200, 100:200, 1] = 255
img1[100:200, 100:200, 2] = 255
cv.imshow("input1",img1)
cv.waitKey(1000)

#resim2
img2 = np.zeros([400,400,3], dtype=np.uint8)
img2[150:250, 150:250, 2] = 255
cv.imshow("input2",img2)
cv.waitKey(1000)

#RGB Python da BGR dır

# and
dst1 = cv.bitwise_and(img1, img2)
cv.imshow("dst1",dst1)
cv.waitKey(1000)

#or iki pikselden biri sıfırdan büyükse true

dst2 = cv.bitwise_or(img1, img2)
cv.imshow("dst2",dst2)
cv.waitKey(1000)

dst3 = cv.bitwise_xor(img1, img2)
cv.imshow("dst3",dst3)
cv.waitKey(1000)

#bitwise_not piksel değerlerini tersine çevirir

img = cv.imread(path + "opencv.png")
cv.namedWindow("opencv", cv.WINDOW_NORMAL)
cv.imshow("opencv", img)
cv.waitKey(1000)

dst = cv.bitwise_not(img)
cv.imshow("dst", dst)
cv.waitKey(1000)
