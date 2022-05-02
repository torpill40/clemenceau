# Tri par sélection
from random import randint

# Génération d'une liste aléatoire
N = 10

Linit = [randint(0,20) for k in range(N)]
print('Liste à trier :', Linit)


# Fonction recherche indice du minimum
def f_ind_mini(L: list) -> int:
    mini, ind = L[0], 0
    for i in range(1, len(L)):
        if mini > L[i]:
            mini, ind = L[i], i
    return ind


# Fonction tri par sélection
def f_tri_selection(L: list):
    N = len(L)
    for i in range(N):
        min_i = f_ind_mini(L[i:]) + i
        L[i], L[min_i] = L[min_i], L[i]


# print(f_ind_mini(Linit))

# Validation
LLinit = sorted(Linit)
f_tri_selection(Linit)  # Tri en place donc pas d'affectation nécessaire
print('Liste triée par sélection :', Linit)
if LLinit == Linit:
    print('Le tri a réussi')
else:
    print('Le tri a échoué')
