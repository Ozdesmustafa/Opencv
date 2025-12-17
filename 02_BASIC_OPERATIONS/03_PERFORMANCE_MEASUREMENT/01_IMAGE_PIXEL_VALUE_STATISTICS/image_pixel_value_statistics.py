import cv2 as cv
import numpy as np

path = "C:/Users/Mustafa/PycharmProjects/OpenCV/02_BASIC_OPERATIONS/03_PERFORMANCE_MEASUREMENT/01_IMAGE_PIXEL_VALUE_STATISTICS/"
img = cv.imread(path + "opencv.png", cv.IMREAD_GRAYSCALE)
cv.imshow("opencv", img)
cv.waitKey(1000)

#minMaxLoc min maks pixel değerlerini verir

min_value, max_value, min_loc, max_loc = cv.minMaxLoc(img)
print("min_value: %.2f, max_value: %.2f" % (min_value, max_value))
print("min loc:", min_loc, ",", "max loc:", max_loc)

# meanStdDev ortalama ve standart sapma
means, stddev = cv.meanStdDev(img)

img[np.where(img < means)] = 0
img[np.where(img > means)] = 255
cv.imshow("output", img)
cv.waitKey(1000)
cv.destroyAllWindows()