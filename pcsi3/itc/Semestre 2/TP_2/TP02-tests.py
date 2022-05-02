
# Test question 1
test1 = est_anagramme('ironique', 'ironique')
test2 = est_anagramme('ironique', 'onirique')
test3 = not est_anagramme('ironique', 'onir')
if test1 and test2 and test3:
    print('fonction est_anagramme validée')

# Test question 2
test1 = (liste_vers_chaine(['t', 'r', 'u', 'c']) == 'truc')
test2 =  (liste_vers_chaine([]) == '')
if test1 and test2:
    print('fonction liste_vers_chaine validée')

# Test question 3
if anagramme('truc', [3,0,1,2]) == 'ctru':
    print('fonction anagramme validée')

# Test question 6
if forme_normale('fronçât') == 'acfnort':
    print('fonction forme_normale validée')

# Test question 7
test1 = est_anagramme2('sorti', 'rôtis')
test2 = not est_anagramme2('sorti', 'rôtas')
if test1 and test2:
    print('fonction est_anagramme2 validée')

# Test question 8
print(dictionnaire['eiorst'])

# Test question 9
print(liste_anagrammes('sortie', dictionnaire))

# Test question 10
print(max_anagrammes(dictionnaire))

# # Test question 11
L1 = [1, 2]
concatene(L1, [3, 4])
if L1 == [1, 2, 3, 4]:
    print('fonction concatene validée')

# Test question 12
print(anagrammes('oui'))
print(anagrammes('non'))
