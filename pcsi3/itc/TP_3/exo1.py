

def f_Recherche_motif_1(mot, texte):
    T, M = len(texte), len(mot)
    for i in range(0, T - M):
        sous_mot = texte[i:i + M]
        if sous_mot == mot:
            return True
    return False


def f_Recherche_motif_2(mot, texte):
    T, M = len(texte), len(mot)
    for i in range(0, T - M):
        present = True
        for j in range(0, M):
            if texte[i + j] != mot[j]:
                present = False
        if present:
            return True
    return False


def f_Positions_motif(mot, texte):
    T, M = len(texte), len(mot)
    positions = []
    for i in range(0, T - M):
        present = True
        for j in range(0, M):
            if texte[i + j] != mot[j]:
                present = False
        if present:
            positions += [i]
    return positions


def f_Positions_motif_slice(mot, texte):
    T, M = len(texte), len(mot)
    positions = []
    for i in range(0, T - M):
        sous_mot = texte[i:i + M]
        if sous_mot == mot:
            positions += [i]
    return positions

