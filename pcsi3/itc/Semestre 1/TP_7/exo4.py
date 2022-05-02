from random import randint

# Génération d'une liste aléatoire
N = 10

Linit = [randint(0, 20) for k in range(N)]
# Linit = [14, 2, 19, 6, 17, 7, 6, 15, 13.0, 13, 18]
print('Liste à trier :', Linit)


def f_combine(Listes: list[list]) -> list:
    L = []
    for l in Listes:
        L += l
    return L


print(f_combine([[1, 2, 3], [5], [6, 4]]))


def f_divise(L: list) -> list:
    pivot = L[0]
    L1, L2 = [], []
    for i in range(1, len(L)):
        if L[i] < pivot:
            L1 += [L[i]]
        elif L[i] >= pivot:
            L2 += [L[i]]
    return [L1, [pivot], L2]


print(f_divise([5, 2, 9, 4, 7, 3, 6]))


def f_tri_rapide(L: list) -> list:
    N = len(L)
    if N <= 1:
        return L
    else:
        L1, pivot, L2 = f_divise(L)
        return f_combine([f_tri_rapide(L1), pivot, f_tri_rapide(L2)])


# Validation tri
LLinit = sorted(Linit)
Lrapide = f_tri_rapide(Linit)
print('Liste triée par tri rapide :', Lrapide)
if LLinit == Lrapide:
    print('Le tri a réussi')
else:
    print('Le tri a échoué')
