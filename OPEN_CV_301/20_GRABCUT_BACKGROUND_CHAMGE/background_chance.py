import cv2 as cv
import numpy as np

import cv2 as cv
import numpy as np

src = cv.imread("C:/Users/Mustafa/PycharmProjects/OpenCV/OPEN_CV_301/20_GRABCUT_BACKGROUND_CHAMGE/m1.jpg")

if src is None:
    print("Src yüklenemedi")
    exit()

src = cv.resize(src, (0,0), fx=0.5, fy=0.5)

r = cv.selectROI("input", src, False, False)
cv.destroyWindow("input")

x, y, w, h = map(int, r)

# 🔴 ZORUNLU ROI KONTROLÜ
if w == 0 or h == 0:
    print("ROI seçilmedi!")
    exit()

mask = np.zeros(src.shape[:2], np.uint8)
bgdmodel = np.zeros((1,65), np.float64)
fgdmodel = np.zeros((1,65), np.float64)

cv.grabCut(
    src,
    mask,
    (x,y,w,h),
    bgdmodel,
    fgdmodel,
    11,
    cv.GC_INIT_WITH_RECT
)

# ✅ DOĞRU maske oluşturma
mask2 = np.where(
    (mask == cv.GC_FGD) | (mask == cv.GC_PR_FGD),
    255,
    0
).astype("uint8")

background = cv.imread("C:/Users/Mustafa/PycharmProjects/OpenCV/OPEN_CV_301/20_GRABCUT_BACKGROUND_CHAMGE/flower.jpg")
background = cv.resize(background, (src.shape[1], src.shape[0]))

# Kenar yumuşatma
kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE, (3,3))
mask2 = cv.dilate(mask2, kernel, iterations=1)
mask2 = cv.GaussianBlur(mask2, (5,5), 0)

background = cv.GaussianBlur(background, (0,0), 15)

alpha = mask2.astype(np.float32) / 255.0
alpha = alpha[..., None]

result = alpha * src.astype(np.float32) + (1 - alpha) * background.astype(np.float32)

cv.imshow("Result", result.astype(np.uint8))
cv.waitKey(0)
cv.destroyAllWindows()
