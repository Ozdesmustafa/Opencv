import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

def custom_hist(gray): #gri resimleri görselleştirmek için kullanılır
    h,w = gray.shape
    hist = np.zeros([256], dtype=np.uint32) #: 0–255 arası her ton için sayaç (histogram) oluşturur.
    for row in range(h):
        for col in range(w):
            pv = gray[row][col]
            hist[pv] += 1

    y_pos = np.arange(0,256,1, dtype=np.uint32) #X-ekseni için 0–255 arası pozisyonlar.
    plt.bar(y_pos,hist,align="center",color="r",alpha=0.5) #x konumlarına çubukları çizer; color/alpha/width ile görünümü ayarlar
    plt.xticks(y_pos,y_pos) #x ekseni tik konum ve etiketlerini ayarlar (seyrekleştirmek okunaklıdır).
    plt.ylabel("Frequency")  #y ekseni etiketini belirler.
    plt.title("Histogram") # grafik başlığını belirler.
    plt.show()#grafiği ekranda gösterir

src = cv.imread("C:/Users/Mustafa/PycharmProjects/OpenCV/OPEN_CV_301/05_HISTOGRAM_EQUALIZATION/img.png")
gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
cv.imshow("input",gray)
cv.waitKey(0)

custom_hist(gray)

dst = cv.equalizeHist(gray)
cv.imshow("eh",dst)
cv.waitKey(0)

custom_hist(dst)