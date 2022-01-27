import matplotlib.pyplot as plt  # import des bibliothèques
import numpy as np

image = plt.imread("avion.bmp")  # ouverture de l'image et affectation à la variable image


def f_flou(T):
    L = len(T)  # nbr de lignes
    C = len(T[0])  # nbr de colonnes
    P = len(T[0][0])  # taille code RGB
    Tflou = np.zeros((L, C, P),
                     dtype=np.uint8)  # création d'une matrice de zéros aux mêmes dimensions que la matrice initiale
    for i in range(1, L - 1):  # exclusion des bords
        for j in range(1, C - 1):  # exclusion des bords
            Rmoy, Gmoy, Bmoy = 0, 0, 0
            for lig in range(i - 1, i + 2):
                for col in range(j - 1, j + 2):
                    Rmoy = Rmoy + T[lig][col][0]
                    Gmoy = Gmoy + T[lig][col][1]
                    Bmoy = Bmoy + T[lig][col][2]
            Tflou[i, j, 0] = Rmoy / 9  # remplissage de la matrice de zéros
            Tflou[i, j, 1] = Gmoy / 9  # remplissage de la matrice de zéros
            Tflou[i, j, 2] = Bmoy / 9  # remplissage de la matrice de zéros
    return Tflou


image_flou = f_flou(image)  # appel de la fonction

plt.figure(1)
plt.subplot(121)
plt.imshow(image)  # affichage de l'image initiale
plt.axis('off')  # masque les axes

plt.subplot(122)
plt.imshow(image_flou)  # affichage de l'image en niveau de gris
plt.axis('off')  # masque les axes
plt.show()
