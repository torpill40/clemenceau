
def recherche_dicho_recursif(L: list, x: float) -> bool:
    T = len(L)
    m = T // 2
    if L[m] == x:
        return True
    elif T == 1:
        return False
    elif L[m] < x:
        return recherche_dicho_recursif(L[m + 1:], x)
    else:
        return recherche_dicho_recursif(L[:m], x)


print(recherche_dicho_recursif([10, 20, 30], 20))
