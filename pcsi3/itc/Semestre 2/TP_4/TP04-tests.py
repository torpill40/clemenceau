# TP-01-tests.py
# Lignes de tests

# Test question 1
if decoder('1110001000101', ('t', (('a', 'e'), 'p'))) == 'patate':
    print('fonction decoder validée')

# Test question 2 (comportement normal)
if decoder('1110001000101', ('t', (('a', 'e'), 'p'))) == 'patate':
    print('fonction decoder validée')
# Test question 2 (assertions)
# Décommenter une des lignes ci-dessous pour voir l'effet d'une assertion
# print(decoder([1110001000101], ('t', (('a', 'e'), 'p'))))
# print(decoder('1110001000101', ('t', (('a', 'e', 'x'), 'p'))))
# print(decoder('2110001000101', ('t', (('a', 'e'), 'p'))))

# Test question 3
if dict_frequences('abracadabra') == {'a': 5, 'b': 2, 'r': 2, 'c': 1, 'd': 1}:
    print('fonction dict_frequences validée')

# Test question 4
L = [('e', 6), ('t', 2), ('p', 2), ('a', 3), ('r', 5)]
trier(L)
if L == [('e', 6), ('r', 5), ('a', 3), ('t', 2), ('p', 2)]:
    print('fonction trier validée')

# Test question 5
if fusion( (('t', 'p'), 4), ('a', 3) ) == ((('t', 'p'), 'a'), 7):
    print('fonction fusion validée')

# Test question 6
L = []
inserer(('t', 2),L)
assert L == [('t', 2)]
inserer(('r', 5),L)
assert L == [('r', 5), ('t', 2)]
inserer(('a', 3), L)
assert L == [('r', 5), ('a', 3), ('t', 2)]
inserer(('x', 7), L)
assert L == [('x', 7), ('r', 5), ('a', 3), ('t', 2)]
inserer(('z', 1), L)
assert L == [('x', 7), ('r', 5), ('a', 3), ('t', 2), ('z', 1)]
print('fonction inserer validée')

# Test question 7
assert arbre_huffman('aaaaa') == ('a', 'a')
def equiv(a1,a2):
    if len(a1) == 1 or len(a2) == 1:
        return a1 == a2
    else :
        return (equiv(a1[0],a2[0]) and equiv(a1[1],a2[1]))\
        or (equiv(a1[0],a2[1]) and  equiv(a1[1],a2[0]))
assert equiv(arbre_huffman('tictactacotactotac'), (('t', 'c'), ('a', ('o', 'i'))))
print('fonction arbre_huffman validée')

# Test question 8
if arbre_vers_dico(('t', (('a', 'e'), 'p'))) == {'t': '0', 'a': '100', 'e': '101', 'p': '11'}:
    print('fonction arbre_vers_dico validée')

# Test question 9
if encoder('patate', ('t', (('a', 'e'), 'p'))) == '1110001000101':
    print('fonction encoder validée')

# Test question 10
def essai_huffman(texte):
    print()
    print('texte initial:', texte)
    print()
    print('fréquences:', dict_frequences(texte))
    print()
    arbre = arbre_huffman(texte)
    print('arbre :',  arbre)
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



