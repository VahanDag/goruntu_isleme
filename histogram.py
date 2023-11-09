import cv2
import numpy as np
import matplotlib.pyplot as plt


# Bir görüntünün histogramını elde etme işlevi
def hist_plot(img):
    # sayımı saklamak için boş liste
    # her bir yoğunluk değerinin
    count = []

    # oğunluğu depolamak için boş liste
    #  değer
    r = []

    #
    # her yoğunluğu geçmek için döngü
    #  değer
    for k in range(0, 256):
        r.append(k)
        count1 = 0

        # her pikseli geçmek için döngüler
        # görüntü
        for i in range(m):
            for j in range(n):
                if img[i, j] == k:
                    count1 += 1
        count.append(count1)

    return (r, count)


img = cv2.imread('resim.jpg', 0)

# Toplam satır sayısını ve
# görüntünün sütunları, görüntünün boyutu
m, n = img.shape
r1, count1 = hist_plot(img)

# histogramı çizmek
plt.stem(r1, count1)
plt.xlabel('intensity value')
plt.ylabel('number of pixels')
plt.title('Histogram of the original image')

# Gerilme elde etmek için dönüşüm
constant = (255 - 0) / (img.max() - img.min())
img_stretch = img * constant
r, count = hist_plot(img_stretch)

# histogramı çizmek
plt.stem(r, count)
plt.xlabel('intensity value')
plt.ylabel('number of pixels')
plt.title('Histogram of the stretched image')