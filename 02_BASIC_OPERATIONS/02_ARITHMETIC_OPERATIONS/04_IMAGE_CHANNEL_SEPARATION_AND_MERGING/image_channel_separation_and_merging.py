import cv2 as cv
path = "C:/Users/Mustafa/PycharmProjects/OpenCV/02_BASIC_OPERATIONS/02_ARITHMETIC_OPERATIONS/04_IMAGE_CHANNEL_SEPARATION_AND_MERGING/"
img = cv.imread(path + "opencv.png")

#split

mv = cv.split(img)
mv[0] [:, :] = 0

dst1 = cv.merge(mv)
cv.imshow("output1", dst1)
cv.waitKey(1000)

mv = cv.split(img)
mv[1] [:, :] = 0

dst2 = cv.merge(mv)
cv.imshow("output2", dst2)
cv.waitKey(1000)

mv = cv.split(img)
mv[2] [:, :] = 0

dst3 = cv.merge(mv)
cv.imshow("output3", dst3)
cv.waitKey(1000)