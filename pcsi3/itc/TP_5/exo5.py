# Fonction de recherche par dichotomie dans une liste triée
def recherche_dicho(L, x):
    ig = 0
    id = len(L) - 1
    im = (ig + id) // 2  # // = partie entière
    Tm = L[im]
    while ig < id and Tm != x:
        im = (ig + id) // 2  # Milieu "gauche"
        Tm = L[im]
        if x > Tm:  # "Droite"
            ig = im + 1
        else:  # "Gauche"
            id = im - 1
    if Tm == x:
        return True
    else:
        Tm = L[ig]
        return Tm == x


# Jeux de tests
def test(f):
    Res = []

    # len(L) pair - x dans L - 1° terme
    L = [1, 2, 3, 4]
    x = 1
    Res.append(f(L, x))
    # len(L) pair - x dans L - Dernier terme
    L = [1, 2, 3, 4]
    x = 4
    Res.append(f(L, x))
    # len(L) pair - x dans L - Dedans
    L = [1, 2, 3, 4]
    x = 2
    Res.append(f(L, x))
    # len(L) impair - x dans L - 1° terme
    L = [1, 2, 3, 4, 5]
    x = 1
    Res.append(f(L, x))
    # len(L) impair - x dans L - Dernier terme
    L = [1, 2, 3, 4, 5]
    x = 5
    Res.append(f(L, x))
    # len(L) impair - x dans L - Dedans
    L = [1, 2, 3, 4, 5]
    x = 2
    Res.append(f(L, x))
    # len(L) pair - x n'est pas dans L - Avant
    L = [1, 2, 3, 4]
    x = -1
    Res.append(not f(L, x))
    # len(L) pair - x n'est pas dans L - Après
    L = [1, 2, 3, 4]
    x = 5
    Res.append(not f(L, x))
    # len(L) pair - x n'est pas dans L - Dedans
    L = [1, 2, 4, 5]
    x = 3
    Res.append(not f(L, x))
    # len(L) impair - x n'est pas dans L - Avant
    L = [1, 2, 3, 4, 5]
    x = -1
    Res.append(not f(L, x))
    # len(L) impair - x n'est pas dans L - Après
    L = [1, 2, 3, 4, 5]
    x = 6
    Res.append(not f(L, x))
    # len(L) impair - x n'est pas dans L - Dedans
    L = [1, 2, 4, 5, 6]
    x = 3
    Res.append(not f(L, x))

    return Res == [True] * 12


# Vérification

Res = test(recherche_dicho)
print('La fonction est correcte ?', Res)
