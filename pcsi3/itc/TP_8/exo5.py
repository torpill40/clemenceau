import numpy as np
import matplotlib.pyplot as plt


def f_rot(image):
    L = len(image)
    C = len(image[0])
    P = len(image[0][0])
    Trot = np.zeros((C, L, P), dtype=np.uint8)

    for i in range(L):
        for j in range(C):
            for k in range(P):
                Trot[j, i, k] = image[i, j, k]
    return Trot


image = plt.imread("Gullfoss.jpg")
image_rot = f_rot(image)


plt.figure(1)
plt.subplot(121)
plt.imshow(image)
plt.axis('off')

plt.subplot(122)
plt.imshow(image_rot)
plt.axis('off')
plt.show()
