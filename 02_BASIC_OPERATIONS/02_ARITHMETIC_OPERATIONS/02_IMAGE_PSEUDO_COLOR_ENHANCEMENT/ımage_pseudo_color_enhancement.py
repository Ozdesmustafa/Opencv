import cv2 as cv
path = "C:/Users/Mustafa/PycharmProjects/OpenCV/02_BASIC_OPERATIONS/02_ARITHMETIC_OPERATIONS/02_IMAGE_PSEUDO_COLOR_ENHANCEMENT/"
img = cv.imread(path + "testfoto1.jpg")

cv.namedWindow("testfoto1")
cv.imshow("testfoto1", img)
cv.waitKey(0)

#applycolormap
#COLORMAP_AUTUMN
#COLORMAP_BONE
#COLORMAP_JET
#COLORMAP_WİNTER
#COLORMAP_RAINBOW
#COLORMAP_OCEAN
#COLORMAP_SUMMER
##COLORMAP_COOL

#kullanma kodu
dst = cv.applyColorMap(img, cv.COLORMAP_SUMMER)
cv.imshow("testfotosummer", dst)
cv.waitKey(0)
