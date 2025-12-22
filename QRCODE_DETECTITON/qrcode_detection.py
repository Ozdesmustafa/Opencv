from dis import code_info

import cv2 as cv
import numpy as np

path = "C:/Users/Mustafa/PycharmProjects/OpenCV/QRCODE_DETECTITON/"
src = cv.imread(path + "qr.png")

gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
qrcoder = cv.QRCodeDetector()

data, points, straight_qrcode = qrcoder.detectAndDecode(gray)

print(points)

result = np.copy(src)

cv.drawContours(result,[np.int32(points)], 0,(0,0, 255), 2)

print("qrcode information is :\n%s" % data)
cv.imshow("qrcode", result)
cv.waitKey(0)
cv.destroyAllWindows()