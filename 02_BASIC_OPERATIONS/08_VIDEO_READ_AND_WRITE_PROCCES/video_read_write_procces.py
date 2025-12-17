import cv2 as cv

capture = cv.VideoCapture(0)

if not capture.isOpened():
    print("Kamera açılamadı")
    exit()

def process(image, opt=0):
    if opt == 0:
        return cv.bitwise_not(image)
    elif opt == 1:
        return cv.GaussianBlur(image, (0, 0), 15)
    elif opt == 2:
        return cv.Canny(image, 100, 200)
    else:
        return image

index = 0  # aktif filtre

while True:
    ret, frame = capture.read()
    if not ret:
        break

    # HER FRAME İŞLENİR
    result = process(frame, index)

    cv.imshow("video-input", frame)
    cv.imshow("result", result)

    key = cv.waitKey(1) & 0xFF

    # 1,2,3 tuşları filtre değiştirir
    if key in [49, 50, 51]:
        index = key - 49

    # ESC çıkış
    if key == 27:
        break

capture.release()
cv.destroyAllWindows()
