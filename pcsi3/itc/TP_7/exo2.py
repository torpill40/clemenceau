# Tri par insertion
from random import randint

# Génération d'une liste aléatoire
N = 10

# Linit = [randint(0,20) for k in range(N)]
Linit = [3, 2, 4, 1.0, 1]
print('Liste à trier :', Linit)


# Fonction tri par insertion
def f_tri_insertion(L: list):
    N = len(L)
    for i in range(1, N):
        j = i
        while j > 0 and L[j] < L[j - 1]:
            L[j], L[j - 1] = L[j - 1], L[j]
            j -= 1

# Validation
LLinit = sorted(Linit)
f_tri_insertion(Linit) # Tri en place donc pas d'affectation nécessaire
print('Liste triée par insertion :', Linit)
if LLinit == Linit :
    print('Le tri a réussi')
else:
    print('Le tri a échoué')
