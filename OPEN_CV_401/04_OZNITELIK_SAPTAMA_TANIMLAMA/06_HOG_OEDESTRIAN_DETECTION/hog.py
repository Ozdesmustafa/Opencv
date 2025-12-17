import cv2 as cv

src = cv.imread("pedestrianai.png")

# TRY ONE OF THESE:
# src = cv.resize(src, (640, 360))
# src = cv.resize(src, (640, 400))
src = cv.resize(src, (640, 420))

hog = cv.HOGDescriptor()
hog.setSVMDetector(cv.HOGDescriptor_getDefaultPeopleDetector())

rects, weights = hog.detectMultiScale(
    src,
    winStride=(8, 8),
    padding=(32, 32),
    scale=1.05
)

for (x, y, w, h) in rects:
    cv.rectangle(src, (x, y), (x + w, y + h), (0, 255, 0), 2)

cv.imshow("rect", src)
cv.waitKey(0)
