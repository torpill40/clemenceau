import numpy as np
import matplotlib.pyplot as plt


def f_gris(image):
    L = len(image)
    C = len(image[0])
    P = len(image[0][0])
    Tgris = np.zeros((L, C, P), dtype=np.uint8)
    for i in range(L):
        for j in range(C):
            pix = image[i, j]
            niv = np.uint8(0.2125 * pix[0] + 0.7154 * pix[1] + 0.0721 * pix[2])
            for k in range(P):
                Tgris[i, j, k] = niv
    return Tgris


image = plt.imread("Gullfoss.jpg")
image_grise = f_gris(image)


plt.figure(1)
plt.subplot(121)
plt.imshow(image)
plt.axis('off')

plt.subplot(122)
plt.imshow(image_grise)
plt.axis('off')
plt.show()
