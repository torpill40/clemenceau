M = [[4, 7, 10, 3], [3, 2, 9, 6], [13, 0, 5, 8], [7, 1, 6, 25]]


def somme_ligne(M, i):
    s = 0
    for e in M[i]:
        s += e
    return s


# assert somme_ligne(M, 1) == 20
# print("fonction somme_ligne validée")


def somme_colonne(M, j):
    s = 0
    for ligne in M:
        s += ligne[j]
    return s


# assert somme_colonne(M, 0) == 27
# print("fonction somme_colonne validée")


def somme_diag1(M):
    s = 0
    for i in range(len(M)):
        s += M[i][i]
    return s


# assert somme_diag1(M) == 36
# print("fonction somme_diag1 validée")


def somme_diag2(M):
    n = len(M)
    s = 0
    for i in range(n):
        s += M[i][n - i - 1]
    return s


# assert somme_diag2(M) == 19
# print("fonction somme_diag2 validée")


def carre_magique(C):
    s = somme_diag1(C)
    if somme_diag2(C) != s:
        return False
    for i in range(len(C)):
        if somme_ligne(C, i) != s or somme_colonne(C, i) != s:
            return False
    return True


# assert carre_magique([[21, 7, 17], [11, 15, 19], [13, 23, 9]])
# assert not carre_magique([[7, 1, 6], [1, 15, 9], [3, 2, 4]])
# print("fonction carre_magique validée")


def magique_normal(C):
    n = len(C)
    absents = {i for i in range(1, n ** 2 + 1)}
    for i in range(n):
        for j in range(n):
            if C[i][j] not in absents:
                return False
            absents.remove(C[i][j])
    return True


# assert magique_normal([[8, 1, 6], [3, 5, 7], [4, 9, 2]])
# assert not magique_normal([[21, 7, 17], [11, 15, 19], [13, 23, 9]])
# print("fonction magique_normal validée")


def matrice_nulle(n):
    return [[0 for _ in range(n)] for _ in range(n)]


# assert matrice_nulle(5) == [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
# print("fonction matrice_nulle validée")


def siamoise(n):
    C = matrice_nulle(n)
    i, j = 0, n // 2
    v = 1
    C[i][j] = v
    while v < n ** 2:
        v += 1
        i -= 1
        if i < 0: i += n
        j += 1
        if j >= n: j -= n
        if C[i][j] != 0:
            i += 2
            j -= 1
            if i >= n: i -= n
            if j < 0: j += n
        C[i][j] = v
    return C


# assert siamoise(7) == [[30, 39, 48, 1, 10, 19, 28], [38, 47, 7, 9, 18, 27, 29], [46, 6, 8, 17, 26, 35, 37], [5, 14, 16, 25, 34, 36, 45], [13, 15, 24, 33, 42, 44, 4], [21, 23, 32, 41, 43, 3, 12], [22, 31, 40, 49, 2, 11, 20]]
# print("fonction siamoise validée")


def constante_magique(n):
    return n * (n * n + 1) // 2


# assert constante_magique(5) == 65
# assert constante_magique(7) == 175
# print("fonction constante_magique validée")
