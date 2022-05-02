import matplotlib.pyplot as plt  # import des bibliothèques
import numpy as np

image = plt.imread("Gullfoss.jpg")  # ouverture de l'image Gullfoss.jpg et affectation à la variable image


def f_sym(T):
    L = len(T)  # nbr de lignes
    C = len(T[0])  # nbr de colonnes
    P = len(T[0][0])  # taille code RGB
    Tsym = np.zeros((L, C, P),
                    dtype=np.uint8)  # création d'une matrice de zéros aux mêmes dimensions que la matrice initiale
    for i in range(L):
        for j in range(C):
            for k in range(P):
                Tsym[i, j, k] = T[L - i - 1, j, k]  # remplissage de la matrice de zéros
    return Tsym


image_sym = f_sym(image)  # appel de la fonction

plt.figure(1)
plt.imshow(image)  # affichage de l'image initiale
plt.axis('off')  # masque les axes

plt.figure(2)
plt.imshow(image_sym)  # affichage de l'image symétrique
plt.axis('off')  # masque les axes
plt.show()
