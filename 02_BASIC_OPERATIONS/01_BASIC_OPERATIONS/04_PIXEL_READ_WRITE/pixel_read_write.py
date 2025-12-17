import cv2 as cv

path = "C:/Users/Mustafa/PycharmProjects/OpenCV/02_BASIC_OPERATIONS/01_BASIC_OPERATIONS/04_PIXEL_READ_WRITE/"
img = cv.imread(path + "opencv.png")
cv.namedWindow("img", cv.WINDOW_AUTOSIZE)
cv.imshow("img", img)
cv.waitKey(1000)

h, w , ch = img.shape
print("h, w ,ch" , h, w, ch)

#döngü aracılığıyla pixellerde gezme
for row in range(h):
    for col in range(w):
        b, g, r = img[row, col]
        b = 255 - b
        g = 255 - g
        r = 255 - r
        img[row, col] = [b, g, r]

cv.imshow("output", img)
cv.waitKey(1000)
cv.destroyAllWindows()