
def recherche_dicho(L, x):
    ig, id = 0, len(L) - 1
    im = (ig + id) // 2
    Tm = L[im]
    while ig < id and Tm != x:
        im = (ig + id) // 2
        Tm = L[im]
        if x < Tm:
            id = im -1
        else:
            ig = im + 1
    return (x == Tm) or (ig == id and x == L[ig])


L = [1, 8, 15, 22, 34, 53, 61, 64, 78, 84, 93]
print(recherche_dicho(L, 88))
