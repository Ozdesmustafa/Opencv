import cv2 as cv
import numpy as np

src = cv.imread("blox.jpg")

def process(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # 1. Detect corners
    corners = cv.goodFeaturesToTrack(gray, 100, 0.05, 10)

    # 2. Refine corners
    winSize = (3,3)
    zeroZone = (-1,-1)
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_COUNT, 40, 0.001)
    corners = cv.cornerSubPix(gray, corners, winSize, zeroZone, criteria)

    # 3. Draw colorful circles (AFTER refinement)
    for corner in corners:
        b = np.random.randint(0,256)
        g = np.random.randint(0,256)
        r = np.random.randint(0,256)

        x = int(corner[0][0])
        y = int(corner[0][1])

        cv.circle(image, (x,y), 5, (b,g,r), 2)

    return image

result = process(src)
cv.imshow("sub pixel", result)
cv.waitKey(0)
cv.destroyAllWindows()
