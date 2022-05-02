def monnaie(montant, systeme):
    reste = montant
    liste = [0] * len(systeme)
    piece = 0
    while reste != 0:
        if reste >= systeme[piece]:
            reste -= systeme[piece]
            liste[piece] += 1
        else:
            piece += 1
    return liste


# if monnaie(2797, [1000, 200, 50, 10, 2, 1]) == [2, 3, 3, 4, 3, 1]:
#     print('fonction monnaie validée')


def monnaie2(montant, systeme):
    dico = {piece: 0 for piece in systeme}
    reste = montant
    for piece in systeme:
        dico[piece] = reste // piece
        reste %= piece
    return dico


# if monnaie2(2797, [1000, 200, 50, 10, 2, 1]) == {1000: 2, 200: 3, 50: 3, 10: 4, 2: 3, 1: 1}:
#     print('fonction monnaie2 validée')


def monnaie_recursif(reste, systeme, i, reponse):
    if reste == 0:
        return reponse
    elif systeme[i] <= reste:
        reponse[i] += 1
        return monnaie_recursif(reste - systeme[i], systeme, i, reponse)
    else:
        return monnaie_recursif(reste, systeme, i + 1, reponse)


def monnaie3(montant, systeme):
    reponse = [0] * len(systeme)
    return monnaie_recursif(montant, systeme, 0, reponse)


# if monnaie3(2797, [1000, 200, 50, 10, 2, 1]) == [2, 3, 3, 4, 3, 1]:
#     print('fonction monnaie3 validée')
