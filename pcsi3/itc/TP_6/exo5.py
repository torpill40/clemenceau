
def enumeration(L: list, sous_L = None):
    if sous_L is None:
        sous_L = []
    if len(L) != 0:
        enumeration(L[:-1], sous_L)
        enumeration(L[:-1], sous_L + [L[-1]])
    else:
        print(sous_L)


enumeration([1, 2, 3])
