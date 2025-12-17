import cv2 as cv
import numpy as np

path = "C:/Users/Mustafa/PycharmProjects/OpenCV/02_BASIC_OPERATIONS/01_BASIC_OPERATIONS/05_MERGING_TWO_IMAGES/"
img1 = cv.imread(path + "venom1.png")
img2 = cv.imread(path + "venom2.png")

cv.imshow("venom1", img1)
cv.waitKey(1000)
cv.imshow("venom2", img2)
cv.waitKey(1000)

#np.hstack iki resmi birleştirmemize yarayan komuttur
horizontal = np.hstack((img1, img2))
cv.imshow("horizontal", horizontal)
cv.waitKey(1000)
cv.destroyAllWindows()
