# Tri par partition - fusion
from random import randint

# Génération d'une liste aléatoire
N = 10

# Linit = [randint(0, 20) for k in range(N)]
Linit = [14, 2, 19, 6, 17, 7, 6, 15, 13.0, 13, 18]
print('Liste à trier :', Linit)


# Fonction fusion ordonnée
# Permet d'obtenir la liste L composée des éléments ordonnés des listes L1 et L2
def f_fusion(L1, L2):
    i1, i2 = 0, 0  # initialisation des indices des éléments comparés
    L = []  # initialisation de la liste fusionnée
    n1, n2 = len(L1), len(L2)
    while i1 < n1 and i2 < n2:
        if L1[i1] < L2[i2]:
            L.append(L1[i1])  # On rajoute le terme courant de L1 à L s(il est inferieur a celui de L2
            i1 = i1 + 1  # On passe au terme suivant
        else:
            L.append(L2[i2])  # On rajoute celui de L2 sinon
            i2 = i2 + 1  # On passe au suivant
    # Quand on sort de la boucle while, c'est qu'on a inséré tous les éléments
    # d'une des deux listes.
    for k in range(i1, n1):
        L.append(L1[k])  # On ajoute les derniers elements de L1 s'il en reste et qu'il n'en reste donc plus dans L2
    for k in range(i2, n2):
        L.append(L2[k])  # On ajoute les derniers elements de L2 s'il en reste et qu'il n'en reste donc plus dans L1
    return L


# Validation fusion
L1 = [1, 4, 7, 9]
L2 = [3, 5, 6, 10]
print(f_fusion(L1, L2))


# Fonction tri par partition - fusion
def f_tri_fusion(L: list) -> list:
    N = len(L)
    if N == 1:
        return L
    else:
        N_2 = N // 2
        return f_fusion(f_tri_fusion(L[:N_2]), f_tri_fusion(L[N_2:]))


# Validation tri
LLinit = sorted(Linit)
Lfusion = f_tri_fusion(Linit)
print('Liste triée par partition-fusion :', Lfusion)
if LLinit == Lfusion :
    print('Le tri a réussi')
else:
    print('Le tri a échoué')
