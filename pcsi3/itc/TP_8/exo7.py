import numpy as np
import matplotlib.pyplot as plt


def f_neg(image):
    L = len(image)
    C = len(image[0])
    P = len(image[0][0])
    Tneg = np.zeros((L, C, P), dtype=np.uint8)
    for i in range(L):
        for j in range(C):
            for k in range(P):
                Tneg[i, j, k] = 0xFF - image[i, j, k]
    return Tneg


image = plt.imread("Gullfoss.jpg")
image_neg = f_neg(image)


plt.figure(1)
plt.subplot(121)
plt.imshow(image)
plt.axis('off')

plt.subplot(122)
plt.imshow(image_neg)
plt.axis('off')
plt.show()
