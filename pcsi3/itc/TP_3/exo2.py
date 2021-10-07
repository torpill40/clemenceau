import numpy as np


def f_Deux_plus_proches_valeurs(L):
    T = len(L)
    dist = np.inf
    valeurs = [0, 0]
    for i in range(T):
        for j in range(T):
            if i != j:
                diff = abs(L[i] - L[j])
                # diff < dist pour avoir le premier couple
                # diff <= dist pour avoir le deuxieme couple
                if diff <= dist:
                    dist = diff
                    valeurs[0], valeurs[1] = L[i], L[j]
    return valeurs


L1 = [-1, 0, 2, 7, 4, 12]
print(f_Deux_plus_proches_valeurs(L1))

L2 = [-1, 3, 5, 2, 14, 53, 4]
print(f_Deux_plus_proches_valeurs(L2))
