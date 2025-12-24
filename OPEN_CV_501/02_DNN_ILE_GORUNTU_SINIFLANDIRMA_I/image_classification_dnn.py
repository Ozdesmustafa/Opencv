import numpy as np
import cv2 as cv

path = "C:/Users/Mustafa/PycharmProjects/OpenCV/02_DNN_ILE_GORUNTU_SINIFLANDIRMA_I/"

# MODEL DOSYALARI
protxt = "deploy.prototxt"
bin_model = "bvlc_googlenet.caffemodel"

# DNN AĞINI YÜKLE
net = cv.dnn.readNetFromCaffe(protxt, bin_model)

# LAYER İSİMLERİNİ AL
layer_names = net.getLayerNames()

# TÜM LAYER BİLGİLERİNİ YAZDIR
for name in layer_names:
    id = net.getLayerId(name)
    layer = net.getLayer(id)
    print("layer id : %d, type : %s, name: %s" %
          (id, layer.type, layer.name))

# SINIF LİSTESİ
with open("classification_classes_ILSVRC2012.txt", "r") as f:
    classes = f.read().split("\n")

net = cv.dnn.readNetFromCaffe(protxt, bin_model)

image2 = cv.imread(path + "dog.jpg")

blob = cv.dnn.blobFromImage(image2, 1.0, (224,224), (104,117,123), False, crop=False)

result = np.copy(image2)

net.setInput(blob)
out = net.forward()

out = out.flatten()

classId = np.argmax(out)
print(classId)

confidence = out[classId]
print(confidence)

t, _ = net.getPerfProfile()
label = "cost time: %.2f ms" % (t * 1000.0 / cv.getTickFrequency())
cv.putText(result, label, (0,20), cv.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,0), 2)

label = "%s: %.4f" % (classes[classId] if classes else "Class #%d" % classId, confidence)
cv.putText(result, label, (0,60), cv.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

result = cv.resize(result, (image2.shape[1], image2.shape[0]))

show_img = np.hstack((image2, result))
cv.namedWindow("demo", cv.WINDOW_NORMAL)
cv.imshow("demo", show_img)
cv.waitKey(0)
