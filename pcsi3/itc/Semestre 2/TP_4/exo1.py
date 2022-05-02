def decoder(bits, arbre):
    assert isinstance(bits, str)
    reponse = ""
    arbre1 = arbre
    bits1 = bits + '0'
    for b in bits1:
        if len(arbre1) == 1:
            reponse += arbre1
            arbre1 = arbre
        assert isinstance(arbre1, tuple) and len(arbre1) == 2
        assert b in {'0', '1'}
        arbre1 = arbre1[int(b)]
    return reponse


# if decoder('1110001000101', ('t', (('a', 'e'), 'p'))) == 'patate':
#     print('fonction decoder validée')

# Décommenter une des lignes ci-dessous pour voir l'effet d'une assertion
# print(decoder([1110001000101], ('t', (('a', 'e'), 'p'))))
# print(decoder('1110001000101', ('t', (('a', 'e', 'x'), 'p'))))
# print(decoder('2110001000101', ('t', (('a', 'e'), 'p'))))


def dict_frequences(texte):
    dico = {}
    for c in texte:
        if c not in dico:
            dico[c] = 0
        dico[c] += 1
    return dico


# if dict_frequences('abracadabra') == {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}:
#     print('fonction dict_frequences validée')


def trier(liste):
    liste.sort(key=lambda x: -x[1])


# L = [('e', 6), ('t', 2), ('p', 2), ('a', 3), ('r', 5)]
# trier(L)
# if L == [('e', 6), ('r', 5), ('a', 3), ('t', 2), ('p', 2)]:
#     print('fonction trier validée')


def fusion(couple1, couple2):
    return (couple1[0], couple2[0]), couple1[1] + couple2[1]


# if fusion((('t', 'p'), 4), ('a', 3)) == ((('t', 'p'), 'a'), 7):
#     print('fonction fusion validée')


def inserer(couple, liste):
    n = len(liste) - 1
    liste.append(couple)
    while n >= 0 and liste[n][1] < liste[n + 1][1]:
        liste[n], liste[n + 1] = liste[n + 1], liste[n]
        n -= 1


# L = []
# inserer(('t', 2), L)
# assert L == [('t', 2)]
# inserer(('r', 5), L)
# assert L == [('r', 5), ('t', 2)]
# inserer(('a', 3), L)
# assert L == [('r', 5), ('a', 3), ('t', 2)]
# inserer(('x', 7), L)
# assert L == [('x', 7), ('r', 5), ('a', 3), ('t', 2)]
# inserer(('z', 1), L)
# assert L == [('x', 7), ('r', 5), ('a', 3), ('t', 2), ('z', 1)]
# print('fonction inserer validée')


def arbre_huffman(texte):
    reste = list(dict_frequences(texte).items())
    trier(reste)
    if len(reste) == 1:
        reste *= 2
    while len(reste) >= 2:
        inserer(fusion(reste.pop(), reste.pop()), reste)
    return reste[0][0]


# assert arbre_huffman('aaaaa') == ('a', 'a')
#
#
# def equiv(a1, a2):
#     if len(a1) == 1 or len(a2) == 1:
#         return a1 == a2
#     else:
#         return (equiv(a1[0], a2[0]) and equiv(a1[1], a2[1])) \
#                or (equiv(a1[0], a2[1]) and equiv(a1[1], a2[0]))
#
#
# assert equiv(arbre_huffman('tictactacotactotac'), (('t', 'c'), ('a', ('o', 'i'))))
# print('fonction arbre_huffman validée')


def arbre_vers_dico(arbre):
    def arbre_vers_dico_recursif(arbre, bits):
        if len(arbre) == 1:
            return [(arbre, bits)]
        else:
            return arbre_vers_dico_recursif(arbre[0], bits + '0') + arbre_vers_dico_recursif(arbre[1], bits + '1')

    return {k: v for k, v in arbre_vers_dico_recursif(arbre, '')}


# print(arbre_vers_dico(('t', (('a', 'e'), 'p'))))
# if arbre_vers_dico(('t', (('a', 'e'), 'p'))) == {'t': '0', 'a': '100', 'e': '101', 'p': '11'}:
#     print('fonction arbre_vers_dico validée')


def encoder(texte, arbre):
    dico = arbre_vers_dico(arbre)
    reponse = ""
    for c in texte:
        reponse += dico[c]
    return reponse


# if encoder('patate', ('t', (('a', 'e'), 'p'))) == '1110001000101':
#     print('fonction encoder validée')


def huffman(texte):
    return encoder(texte, arbre_huffman(texte))


def essai_huffman(texte):
    print()
    print('texte initial:', texte)
    print()
    print('fréquences:', dict_frequences(texte))
    print()
    arbre = arbre_huffman(texte)
    print('arbre :', arbre)
    print()
    dico = arbre_vers_dico(arbre)
    print('dictionnaire:', dico)
    print()
    bits = huffman(texte)
    print('chaîne binaire:', bits)
    print()
    texte1 = decoder(bits, arbre)
    print('décodage de la chaine binaire:', texte1)
    print()


def test_huffman():
    if len(huffman('tactictactoctactictactuctactictactoctactictac')) == 100:
        print('fonction huffman validée')


essai_huffman('Longtemps, je me suis couché de bonne heure.')
test_huffman()
