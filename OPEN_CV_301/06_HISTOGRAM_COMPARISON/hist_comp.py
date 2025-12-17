import cv2 as cv

src1 = cv.imread("C:/Users/Mustafa/PycharmProjects/OpenCV/OPEN_CV_301/06_HISTOGRAM_COMPARISON/akdeniz.jpg")
src2 = cv.imread("C:/Users/Mustafa/PycharmProjects/OpenCV/OPEN_CV_301/06_HISTOGRAM_COMPARISON/opencv.png")
src3 = cv.imread("C:/Users/Mustafa/PycharmProjects/OpenCV/OPEN_CV_301/06_HISTOGRAM_COMPARISON/labirent.jpg")

#cvtColor
hsv1 = cv.cvtColor(src1, cv.COLOR_BGR2HSV) #renk uzayını değiştirmek için(rgb'den hsv'ye çeviriyoruz.Daha kolay nesne takibi ve renk takibi için.)
hsv2 = cv.cvtColor(src2, cv.COLOR_BGR2HSV)
hsv3 = cv.cvtColor(src3, cv.COLOR_BGR2HSV)
print(hsv1)
print(hsv2)
print(hsv3)

#calcHist
hist1 = cv.calcHist([hsv1], [0,1], None, [60,64], [0, 180, 0,256]) #resimler,histogramları hesaplamak için gerekli olan kanallar,
hist2 = cv.calcHist([hsv2], [0,1], None, [60,64], [0, 180, 0,256]) #taslak olmadığı için none, histogramların boyutları, range(aralıklar)
hist3 = cv.calcHist([hsv3], [0,1], None, [60,64], [0, 180, 0,256])
print(hist1)
print(hist2)
print(hist3)

#normalize
cv.normalize(hist1, hist1, 0, 1, cv.NORM_MINMAX)
cv.normalize(hist2, hist2, 0, 1, cv.NORM_MINMAX)
cv.normalize(hist3, hist3, 0, 1, cv.NORM_MINMAX)

#compareHist

#HISTCMP_CORREL(Histogramlar arası benzerlik)
print(cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL))
print(cv.compareHist(hist1, hist3, cv.HISTCMP_CORREL))
print(cv.compareHist(hist2, hist3, cv.HISTCMP_CORREL))
