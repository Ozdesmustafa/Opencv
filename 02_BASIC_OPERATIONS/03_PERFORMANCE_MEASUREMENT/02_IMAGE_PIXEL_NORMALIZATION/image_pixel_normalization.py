import cv2 as cv
import numpy as np

path = "C:/Users/Mustafa/PycharmProjects/OpenCV/02_BASIC_OPERATIONS/03_PERFORMANCE_MEASUREMENT/02_IMAGE_PIXEL_NORMALIZATION/"

img = cv.imread(path + "opencv.png")

print(img.shape)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)
cv.waitKey(1000)

print(gray.shape)
print(gray)

gray = np.float32(gray)
print(gray)

# GRAY ÜZERİNDE mean/std AL
means, stddev = cv.meanStdDev(gray)

min_value, max_value, min_loc, max_loc = cv.minMaxLoc(gray)

print("min_value: %.2f, stddev: %.2f" % (means.item(), stddev.item()))

# Tekrar hesaplama
means, stddev = cv.meanStdDev(gray)
print("mean: %.2f, stddev: %.2f" % (means.item(), stddev.item()))

dst = np.zeros(gray.shape, dtype=np.float32)
cv.normalize(gray, dst=dst, alpha=0, beta=1.0, norm_type=cv.NORM_MINMAX)

print(dst)
print(np.uint8(dst * 255))

means, stddev = cv.meanStdDev(np.uint8(dst * 255))
print("mean: %.2f, stddev: %.2f" % (means.item(), stddev.item()))

cv.imshow("NORM_MINMAX", dst)
cv.waitKey(1000)

#NORM_INF
dst = np.zeros(gray.shape, dtype=np.float32)
cv.normalize(gray, dst=dst , alpha=1.0, beta=0, norm_type=cv.NORM_INF)
print(dst)
cv.imshow("NORM_INF", dst)
cv.waitKey(1000)

#NORM_L1
dst = np.zeros(gray.shape, dtype=np.float32)
cv.normalize(gray, dst=dst, alpha=1.0, beta=0, norm_type=cv.NORM_L1)
print(dst)
cv.imshow("NORM_L1", np.uint8(dst*10000000))
cv.waitKey(1000)

#NORM_L2
dst = np.zeros(gray.shape, dtype=np.float32)
cv.normalize(gray, dst=dst, alpha=1.0, beta=0, norm_type=cv.NORM_L2)
print(dst)
cv.imshow("NORM_L2", np.uint8(dst*10000))
cv.waitKey(1000)