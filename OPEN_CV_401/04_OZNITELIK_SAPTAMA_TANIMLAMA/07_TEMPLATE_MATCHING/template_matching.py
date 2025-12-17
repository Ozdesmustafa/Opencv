import cv2 as cv
import numpy as np

path = "C:/Users/Mustafa/PycharmProjects/OpenCV/OPEN_CV_401/04_OZNITELIK_SAPTAMA_TANIMLAMA/07_TEMPLATE_MATCHING"

def templat_demo():
    src = cv.imread(path + "/opencv.png")
    tpl = cv.imread(path + "/template.png")

    # Check for valid images
    if src is None:
        print("Error: opencv.png not found!")
        return
    if tpl is None:
        print("Error: template.png not found!")
        return

    cv.imshow("input", src)
    cv.imshow("template", tpl)

    # Convert to gray
    src_gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    tpl_gray = cv.cvtColor(tpl, cv.COLOR_BGR2GRAY)

    # Template size
    th, tw = tpl_gray.shape[:2]

    # ❗ If template is bigger → STOP
    if th > src_gray.shape[0] or tw > src_gray.shape[1]:
        print("Error: Template is larger than source image!")
        print("SRC:", src_gray.shape)
        print("TPL:", tpl_gray.shape)
        return

    # Template matching
    result = cv.matchTemplate(src_gray, tpl_gray, cv.TM_CCOEFF_NORMED)

    # Threshold
    t = 0.8
    loc = np.where(result >= t)

    # Draw rectangles
    for pt in zip(*loc[::-1]):
        cv.rectangle(src, (pt[0], pt[1]), (pt[0] + tw, pt[1] + th), (255, 0, 0), 3)

    cv.imshow("ilk_demo", src)

templat_demo()
cv.waitKey(0)
