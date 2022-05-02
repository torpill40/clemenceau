
def occurrences_mots(texte):
    dico = dict()
    for mot in texte.split():
        dico[mot] = dico.get(mot, 0) + 1
    return dico


# texte = 'tic tac toc tac tic tac toc tac tic tuc'
# print(occurrences_mots(texte))


def plus_frequent(texte):
    res, occ = None, 0
    for (mot, n) in occurrences_mots(texte).items():
        if n > occ:
            res, occ = mot, n
    return res


# texte = 'tic tac toc tac tic tac toc tac tic tuc'
# print(plus_frequent(texte))
