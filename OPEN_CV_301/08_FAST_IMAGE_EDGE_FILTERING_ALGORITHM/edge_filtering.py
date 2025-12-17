#Fast Image Edge Filtering
#edgePreservingFilter

import cv2 as cv
import numpy as np

src = cv.imread("C:/Users/Mustafa/PycharmProjects/OpenCV/OPEN_CV_301/08_FAST_IMAGE_EDGE_FILTERING_ALGORITHM/sarisin.jpg")
cv.imshow("input", src)
cv.waitKey(0)

h, w = src.shape[:2]

dst = cv.edgePreservingFilter(src, sigma_s=100 , sigma_r=0.4,flags=cv.RECURS_FILTER)
result = np.zeros([h, w*2,3], dtype=src.dtype)
result[0:h,0:w :] = src
result[0:h:,w:2*w,:] = dst

result = cv.resize(result,(h,w//2))
cv.imshow("result", result)
cv.waitKey(0)