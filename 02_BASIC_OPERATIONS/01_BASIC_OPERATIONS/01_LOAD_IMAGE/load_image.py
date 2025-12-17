import cv2 as cv
#dosya yolu ve değişken atama
path = "C:/Users/Mustafa/PycharmProjects/OpenCV/02_BASIC_OPERATIONS/01_BASIC_OPERATIONS/01_LOAD_IMAGE/"
img = cv.imread(path + "biyometrikfotograf.jpg")
#dosya tipini gösterir
type(img)
#pencere ismini ve boyutunu atar.
cv.namedWindow("opencv_Test", cv.WINDOW_AUTOSIZE)
#kaç saniye kalacağını hangi isimde göstereceğini ve pencereleri temiz şekilde kapatmamızı sağlar
cv.imshow("opencv_test", img)
cv.waitKey(1000)
cv.destroyAllWindows()




