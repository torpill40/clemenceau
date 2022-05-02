from TP02module import enleve_diacritiques


def occurences(chaine):
    occ = dict()
    for c in chaine:
        if c not in occ:
            occ[c] = 0
        occ[c] += 1
    return occ


def est_anagramme(chaine1, chaine2):
    return occurences(chaine1) == occurences(chaine2)


# test1 = est_anagramme('ironique', 'ironique')
# test2 = est_anagramme('ironique', 'onirique')
# test3 = not est_anagramme('ironique', 'onir')
# if test1 and test2 and test3:
#     print('fonction est_anagramme validée')


def liste_vers_chaine(L):
    chaine = ""
    for c in L:
        chaine += c
    return chaine


# test1 = (liste_vers_chaine(['t', 'r', 'u', 'c']) == 'truc')
# test2 = (liste_vers_chaine([]) == '')
# if test1 and test2:
#     print('fonction liste_vers_chaine validée')


def anagramme(chaine, L):
    return liste_vers_chaine([chaine[i] for i in L])


# if anagramme('truc', [3, 0, 1, 2]) == 'ctru':
#     print('fonction anagramme validée')


def forme_normale(mot):
    return liste_vers_chaine(sorted(enleve_diacritiques(mot)))


# if forme_normale('fronçât') == 'acfnort':
#     print('fonction forme_normale validée')


def est_anagramme2(mot1, mot2):
    return forme_normale(mot1) == forme_normale(mot2)


# test1 = est_anagramme2('sorti', 'rôtis')
# test2 = not est_anagramme2('sorti', 'rôtas')
# if test1 and test2:
#     print('fonction est_anagramme2 validée')


def fichier_vers_dico(nom_fichier):
    fichier = open(nom_fichier, 'r', encoding='utf-8')
    dico = dict()
    for ligne in fichier:
        mot = ligne.strip('\n')
        fn = forme_normale(mot)
        if fn not in dico:
            dico[fn] = []
        dico[fn].append(mot)
    fichier.close()
    return dico


dictionnaire = fichier_vers_dico("mots_francais.txt")

# print(dictionnaire['eiorst'])


def liste_anagrammes(mot, dictionnaire):
    return dictionnaire[forme_normale(mot)]


# print(liste_anagrammes('sortie', dictionnaire))


def max_anagrammes(dictionnaire):
    L, n = [], 0
    for anagrammes in dictionnaire.values():
        l_anagrammes = len(anagrammes)
        if l_anagrammes > n:
            L = anagrammes
            n = l_anagrammes
    return L


# print(max_anagrammes(dictionnaire))


def concatene(L1, L2):
    for x in L2:
        L1.append(x)


# L1 = [1, 2]
# concatene(L1, [3, 4])
# if L1 == [1, 2, 3, 4]:
#     print('fonction concatene validée')


def anagrammes(chaine):
    def permutations(L, i):
        if i == 1:
            return [L.copy()]
        L_permut = []
        for permut in permutations(L, i - 1):
            for n in range(i):
                permut_courante = permut[:n]
                concatene(permut_courante, [permut[i - 1]])
                concatene(permut_courante, permut[n:i - 1])
                concatene(permut_courante, permut[i:])
                L_permut.append(permut_courante)
        return L_permut
    taille = len(chaine)
    return {anagramme(chaine, L) for L in permutations(list(range(taille)), taille)}


print(anagrammes('oui'))
print(anagrammes('non'))
