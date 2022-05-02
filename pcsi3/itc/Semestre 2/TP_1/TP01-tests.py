
# TP-01-tests.py
# Lignes de tests

# Exercice 2
# Test question 1
stock = {'pommes':143, 'poires': 97, 'oranges': 155}
print(total(stock))
# Test question 2
stock = {'pommes':143, 'poires': 7, 'oranges': 155}
print(stock)
maj_heure(stock)
print(stock)
# Test question 3
stock = {'pommes':143, 'poires': 97, 'oranges': 155}
print(stock)
maj_totale(stock, 10)
print(stock)
# Test question 4
stock = {'pommes':143, 'poires': 97, 'oranges': 155}
print(stock)
maj_totale1(stock, 10)
print(stock)
# Test question 5
stock = {'pommes':143, 'poires': 97, 'oranges': 155}
arrivage = [('cerises', 144), ('poires',100), ('cerises',200)]
print(stock)
maj_arrivage(stock, arrivage)
print(stock)

# Exercice 3
# Test
villes = ['Nantes', 'Madrid', 'Paris', 'Naples']
pays = ['France', 'Espagne', 'France', 'Italie']
print(listes_vers_dico(villes, pays))

# Exercice 4
# Test question 1
texte = 'tic tac toc tac tic tac toc tac tic tuc'
print(occurrences_mots(texte))
# Test question 2
texte = 'tic tac toc tac tic tac toc tac tic tuc'
print(plus_frequent(texte))

# Exercice 5
# Test
dico = {'pomme':'apple', 'banane':'banana', 'poire':'pear', 'cerise':'cherry'}
print(inverse(dico))

# Exercice 6
# Test question 1
amis = {}
amis['Joe'] = ['Emmanuel', 'Boris']
amis['Emmanuel'] = ['Joe', 'Xi']
amis['Vladimir'] = ['Xi']
amis['Boris']=['Joe']
amis['Kim'] = ['Xi']
amis['Xi'] = []
print(nombre_amis(amis, 'Emmanuel'))
# Test question 2
amis = {}
amis['Joe'] = ['Emmanuel', 'Boris']
amis['Emmanuel'] = ['Joe', 'Xi']
amis['Vladimir'] = ['Xi']
amis['Boris']=['Joe']
amis['Kim'] = ['Xi']
amis['Xi'] = []
print(est_ami(amis, 'Kim', 'Xi'))
print(est_ami(amis, 'Kim', 'Emmanuel'))
# Test question 3
amis = {}
amis['Joe'] = ['Emmanuel', 'Boris']
amis['Emmanuel'] = ['Joe', 'Xi']
amis['Vladimir'] = ['Xi']
amis['Boris']=['Joe']
amis['Kim'] = ['Xi']
amis['Xi'] = []
print(transpose(amis))
# Test question 4
amis = {}
amis['Joe'] = ['Emmanuel', 'Boris']
amis['Emmanuel'] = ['Joe', 'Xi']
amis['Vladimir'] = ['Xi']
amis['Boris']=['Joe']
amis['Kim'] = ['Xi']
amis['Xi'] = []
print(est_ami_dami(amis,'Joe', 'Boris'))
print(est_ami_dami(amis,'Joe', 'Xi'))


