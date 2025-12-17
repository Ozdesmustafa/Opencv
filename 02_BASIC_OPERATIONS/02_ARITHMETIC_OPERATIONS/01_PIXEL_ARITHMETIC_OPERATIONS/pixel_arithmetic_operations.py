import cv2 as cv
import numpy as np
path = "C:/Users/Mustafa/PycharmProjects/OpenCV/02_BASIC_OPERATIONS/02_ARITHMETIC_OPERATIONS/01_PIXEL_ARITHMETIC_OPERATIONS/"

img1 = cv.imread(path + "manzara1.jpg")
img2 = cv.imread(path + "manzara2.jpg")

#eklenen fotoğrafın yükseklik genişlik gibi değerlerini yazdırır.
h, w, ch = img1.shape
print("h, w, ch", h, w, ch)

#add toplama için
add_result = np.zeros(img1.shape, img1.dtype)
cv.add(img1, img2, dst= add_result)
cv.imshow("add_result", add_result)
cv.waitKey(1000)

#subtract
sub_result = np.zeros(img1.shape, img1.dtype)
cv.subtract(img1, img2, sub_result)
cv.imshow("sub_result", sub_result)
cv.waitKey(1000)

#multiply çarpma
mul_result = np.zeros(img1.shape, img1.dtype)
cv.multiply(img1, img2, mul_result)
cv.imshow("mul_result", mul_result)
cv.waitKey(1000)

#divide bölme
div_result = np.zeros(img1.shape, img1.dtype)
cv.divide(img1, img2, div_result)
cv.imshow("div_result", div_result)
cv.waitKey(1000)

cv.destroyAllWindows()

