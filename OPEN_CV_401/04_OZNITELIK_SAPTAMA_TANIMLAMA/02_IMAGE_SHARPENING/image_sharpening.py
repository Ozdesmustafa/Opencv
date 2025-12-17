import cv2 as cv
import numpy as np

src = cv.imread("opencv.png")

sharpen_op = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]], dtype=np.float32)



shared_image = cv.filter2D(src,cv.CV_32F,sharpen_op)

shared_image = cv.convertScaleAbs(shared_image)
cv.imshow("output",shared_image)
cv.waitKey(0)
#amaç daha düşük kalitede daha keskin hatlara ait bir resim oluşturmak