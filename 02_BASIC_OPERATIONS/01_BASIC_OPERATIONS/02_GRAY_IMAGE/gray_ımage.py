import cv2 as cv
path = "C:/Users/Mustafa/PycharmProjects/OpenCV/02_BASIC_OPERATIONS/01_BASIC_OPERATIONS/02_GRAY_IMAGE/"
img = cv.imread(path + "opencv.png")
cv.namedWindow("opencv")
cv.imshow("opencv", img)
cv.waitKey( 1000)

#cvtcolor
gray=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("opencv", gray)
cv.waitKey(1000)

#imwrite yapılan fotoğrafı kaydetmek için.
cv.imwrite(path + "opencvgray.png", gray)
cv.destroyAllWindows()

#cv.IMREAD_GRAYSCALE başlangıçta gri skalada gösterilmesini sağlar.
