
L = [1, 8, 15, 22, 34, 53, 61, 64, 78, 84, 93]


def recherche_naive(x, L):
    for i in range(len(L)):
        if L[i] == x:
            return True
    return False


print(recherche_naive(22, L))
