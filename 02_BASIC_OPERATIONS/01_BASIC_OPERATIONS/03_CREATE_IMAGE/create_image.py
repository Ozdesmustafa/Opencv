import cv2 as cv
import numpy as np

path = "C:/Users/Mustafa/PycharmProjects/OpenCV/02_BASIC_OPERATIONS/01_BASIC_OPERATIONS/03_CREATE_IMAGE/"
img = cv.imread(path + "opencv.png")
cv.namedWindow("create_Image", cv.WINDOW_NORMAL)
cv.imshow("create_Image", img)
cv.waitKey(1000)

#kopyasını alma
m1 = np.copy(img)
m2 = img

img[100:200, 200:300, :] = 0
cv.imshow("m2", m2)
cv.waitKey(1000)

m3 = np.zeros(img.shape, img.dtype)
cv.imshow("m3", m3)
cv.waitKey(1000)

m4 = np.zeros((300, 300, 3), np.uint8)

cv.imshow("m4", m4)
cv.waitKey(1000)

img =  np.ones((550, 770, 3))
black = (0, 0, 0)
red = (0, 0 ,255)
green = (0 ,255 , 0)

cv.rectangle(img, (480, 250), (100, 450), black, 8)
cv.rectangle(img, (580, 150), (200, 350), black, 8)
cv.line(img, (100, 450), (200, 350), black, 8)
cv.line(img, (480, 250), (580, 150), black, 8)
cv.line(img, (100, 250), (200, 150), black, 8)
cv.line(img, (480, 450), (580, 350), black, 8)

start_point = (150, 100)
font_thickness = 2
font_size = 1
font = cv.FONT_HERSHEY_DUPLEX

cv.putText(img, "efsaneviresim", start_point, font, font_size, green, font_thickness)
cv.imshow("dikdörtgen", img)
cv.waitKey(1000)
