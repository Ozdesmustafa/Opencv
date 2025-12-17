import cv2 as cv
import numpy as np

src = cv.imread("C:/Users/Mustafa/PycharmProjects/OpenCV/OPEN_CV_301/19_GRABCUT_IMAGE_SEGMENTATION/m1.jpg")

if src is None:
    print("Resim yüklenemedi")
    exit()

src = cv.resize(src, (0, 0), fx=0.5, fy=0.5)

r = cv.selectROI("input", src, False, False)
cv.destroyWindow("input")

x, y, w, h = map(int, r)

if w == 0 or h == 0:
    print("ROI seçilmedi!")
    exit()

roi = src[y:y+h, x:x+w]

mask = np.zeros(src.shape[:2], dtype=np.uint8)

bgdmodel = np.zeros((1, 65), np.float64)
fgdmodel = np.zeros((1, 65), np.float64)

rect = (x, y, w, h)

cv.grabCut(src, mask, rect, bgdmodel, fgdmodel, 11, cv.GC_INIT_WITH_RECT)

mask2 = np.where((mask == cv.GC_FGD) | (mask == cv.GC_PR_FGD), 255, 0).astype("uint8")

result = cv.bitwise_and(src, src, mask=mask2)

cv.imshow("ROI", roi)
cv.imshow("Result", result)
cv.waitKey(0)
cv.destroyAllWindows()
