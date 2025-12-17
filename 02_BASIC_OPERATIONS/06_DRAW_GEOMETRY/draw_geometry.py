import cv2 as cv
import numpy as np
img = np.zeros((512, 512, 3), dtype=np.uint8)
cv.rectangle(img, (100, 100), (300, 300), (255, 0, 0),2,cv.LINE_8,0)
cv.circle(img, (256, 256), 50, (0, 0, 255), 2, cv.LINE_8,0)
cv.ellipse(
    img,
    (256, 256),     # center
    (150, 50),      # axes
    0,              # angle
    0,              # startAngle
    360,            # endAngle
    (0, 255, 0),    # color
    2,              # thickness
    cv.LINE_8,      # lineType
    0               # shift
)
cv.imshow("dst", img)
cv.waitKey(0)
cv.destroyAllWindows()

for i in range(100000):

    img[:] = 0  # ekranı temizle

    x1 = int(np.random.rand() * 512)
    y1 = int(np.random.rand() * 512)
    x2 = int(np.random.rand() * 512)
    y2 = int(np.random.rand() * 512)

    b = np.random.randint(0, 256)
    g = np.random.randint(0, 256)
    r = np.random.randint(0, 256)

    cv.line(img, (x1, y1), (x2, y2), (b, g, r), 2, cv.LINE_8)
    cv.rectangle(img, (x1, y1), (x2, y2), (b, g, r), 2, cv.LINE_8)

    cv.imshow("dst1", img)

    c = cv.waitKey(1) & 0xFF
    if c == 27:  # ESC
        break