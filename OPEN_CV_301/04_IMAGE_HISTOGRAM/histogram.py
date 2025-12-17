import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
def custom_hist(gray): #gri resimleri görselleştirmek için kullanılır
    h,w = gray.shape
    hist = np.zeros([256], dtype=np.uint32)
    for row in range(h):
        for col in range(w):
            pv = gray[row][col]
            hist[pv] += 1

    y_pos = np.arange(0,256,1, dtype=np.uint32)
    plt.bar(y_pos,hist,align="center",color="r",alpha=0.5)#x konumlarına çubukları çizer; color/alpha/width ile görünümü ayarlar
    plt.xticks(y_pos,y_pos)#x ekseni tik konum ve etiketlerini ayarlar (seyrekleştirmek okunaklıdır).
    plt.ylabel("Frequency") #y ekseni etiketini belirler.
    plt.title("Histogram")# grafik başlığını belirler.

def image_hist(image):#renli görseler için histogram oluşyurma
    cv.imshow("image",image)
    color = ('blue','green','red')
    for i,col in enumerate(color):
        hist = cv.calcHist([image],[i],None,[256],[0,256])#cv.calcHist birden fazla histogram oluşturmak içim
        plt.plot(hist,color=col)
        plt.xlim([0,256])
    plt.show()

src = cv.imread("C:/Users/Mustafa/PycharmProjects/OpenCV/OPEN_CV_301/04_IMAGE_HISTOGRAM/img.png")
cv.imshow("input",src)
cv.waitKey(0)

gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
custom_hist(gray)
image_hist(src)

cv.destroyAllWindows()
