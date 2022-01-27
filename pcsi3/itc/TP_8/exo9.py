import numpy as np
import matplotlib.pyplot as plt


def f_convol(A, B):
    L = len(A)
    C = len(A[0])
    res = 0
    for i in range(L):
        for j in range(C):
            res += A[i][j] * B[i][j]
    return res


def f_filtre(T, A):
    L = len(T)  # nbr de lignes
    C = len(T[0])  # nbr de colonnes
    P = len(T[0][0])  # taille code RGB
    Tfiltre = np.zeros((L, C, P),
                       dtype=np.uint8)  # création d'une matrice de zéros aux mêmes dimensions que la matrice initiale
    for i in range(1, L - 1):  # exclusion des bords
        for j in range(1, C - 1):  # exclusion des bords
            for k in range(P):
                c = f_convol(A, T[i-1:i+2, j-1:j+2, k])
                if c > 0xFF:
                    c = 0xFF
                elif c < 0x00:
                    c = 0x00
                # print(f"{c}:{T[i, j, k]}")
                Tfiltre[i, j, k] = c
    return Tfiltre


image = plt.imread("avion.bmp")


A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
image_filtre = f_filtre(image, np.array([[0, 1, 0], [1, -4, 1], [0, 1, 0]]))

plt.figure(1)
plt.subplot(121)
plt.imshow(image)  # affichage de l'image initiale
plt.axis('off')  # masque les axes

plt.subplot(122)
plt.imshow(image_filtre)  # affichage de l'image en niveau de gris
plt.axis('off')  # masque les axes
plt.show()
