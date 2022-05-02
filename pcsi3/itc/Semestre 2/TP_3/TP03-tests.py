# TP-01-tests.py
# Lignes de tests

# Exercice 1

# Test question 1
if monnaie(2797, [1000, 200, 50, 10, 2, 1]) == [2, 3, 3, 4, 3, 1]:
        print('fonction monnaie validée')

# Test question 2
if monnaie2(2797, [1000, 200, 50, 10, 2, 1]) == {1000:2, 200:3, 50:3, 10:4, 2:3, 1:1}:
        print('fonction monnaie2 validée')

# Test question 3
if monnaie3(2797, [1000, 200, 50, 10, 2, 1]) == [2, 3, 3, 4, 3, 1]:
        print('fonction monnaie3 validée')

# Exercice 2

# Test question 1
conferences = [(19, 22), (6, 28), (21, 24), (18, 31), (8, 13), (15, 27), (3, 16),
(25, 29), (5, 9), (12, 20), (4, 7), (1, 10), (11, 23), (26, 30), (2, 6), (14, 17)]
trier_par_debut(conferences)
if conferences == [(1, 10), (2, 6), (3, 16), (4, 7), (5, 9), (6, 28), (8, 13),
(11, 23), (12, 20), (14, 17), (15, 27), (18, 31), (19, 22), (21, 24), (25, 29), (26, 30)]:
    print('fonction trier_par_debut validée')
trier_par_fin(conferences)
if conferences == [(2, 6), (4, 7), (5, 9), (1, 10), (8, 13), (3, 16), (14, 17),
(12, 20), (19, 22), (11, 23), (21, 24), (15, 27), (6, 28), (25, 29), (26, 30), (18, 31)]:
    print('fonction trier_par_fin validée')

# Test question 2
conferences = [(19, 22), (6, 28), (21, 24), (18, 31), (8, 13), (15, 27), (3, 16),
(25, 29), (5, 9), (12, 20), (4, 7), (1, 10), (11, 23), (26, 30), (2, 6), (14, 17)]
if planning_glouton(conferences) == [(2, 6), (8, 13), (14, 17), (19, 22), (25, 29)]:
    print('fonction planning_glouton validée')

# Test question 3
conferences = [(19, 22), (6, 28), (21, 24), (18, 31), (8, 13), (15, 27), (3, 16),
(25, 29), (5, 9), (12, 20), (4, 7), (1, 10), (11, 23), (26, 30), (2, 6), (14, 17)]
if planning_glouton2(conferences) == [(2, 6), (8, 13), (14, 17), (19, 22), (25, 29)]:
    print('fonction planning_glouton2 validée')

# Test question 5
c = (26, 30)
salles = [[(1, 10), (11, 23), (25, 29)],
[(2, 6), (8, 13), (14, 17), (18, 31)],
[(3, 16), (19, 22)],
[(4, 7), (12, 20), (21, 24)],
[(5, 9), (15, 27)],
[(6, 28)]]
if trouver_salle(salles, c) == 2:
    print('fonction trouver_salle validée')

# test question 6
conferences = [(19, 22), (6, 28), (21, 24), (18, 31), (8, 13), (15, 27), (3, 16),
(25, 29), (5, 9), (12, 20), (4, 7), (1, 10), (11, 23), (26, 30), (2, 6), (14, 17)]
salles = [[(1, 10), (11, 23), (25, 29)],
[(2, 6), (8, 13), (14, 17), (18, 31)],
[(3, 16), (19, 22), (26, 30)],
[(4, 7), (12, 20), (21, 24)],
[(5, 9), (15, 27)],
[(6, 28)]]
if allouer_salles(conferences) == salles:
     print('fonction allouer_salles validée')
