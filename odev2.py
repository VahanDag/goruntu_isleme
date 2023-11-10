import cv2
import numpy as np


# Webcam'den görüntü yakalama
cap = cv2.VideoCapture(0)

while True:
    # Görüntüyü frame olarak oku
    _, frame = cap.read()

    # BGR'den HSV'ye renk dönüşümü
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Kırmızı renk için alt ve üst sınır değerler
    # Bu değerler farklı kırmızı tonları için ayarlanabilir
    lower_red = np.array([161, 155, 84])
    upper_red = np.array([179, 255, 255])

    # Sadece kırmızı renkleri maskele
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Maskeyi ve orijinal görüntüyü birleştir
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Sonuçları göster
    cv2.imshow('frame', frame) # Orijinal görüntüyü göster
    cv2.imshow('mask', mask) # Maskeyi göster (sadece kırmızı)
    cv2.imshow('result', result) # Sonucu göster (kırmızı nesne ve arka plan)

    # 'q' tuşuna basıldığında döngüden çık
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#pencereleri kapat
cap.release()
cv2.destroyAllWindows()
