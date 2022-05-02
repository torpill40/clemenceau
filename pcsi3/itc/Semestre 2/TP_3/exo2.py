import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def debut(conf): return conf[0]


def fin(conf): return conf[1]


def trier_par_debut(conferences): conferences.sort(key=debut)


def trier_par_fin(conferences): conferences.sort(key=fin)


# conferences = [(19, 22), (6, 28), (21, 24), (18, 31), (8, 13), (15, 27), (3, 16),
#                (25, 29), (5, 9), (12, 20), (4, 7), (1, 10), (11, 23), (26, 30), (2, 6), (14, 17)]
# trier_par_debut(conferences)
# if conferences == [(1, 10), (2, 6), (3, 16), (4, 7), (5, 9), (6, 28), (8, 13),
#                    (11, 23), (12, 20), (14, 17), (15, 27), (18, 31), (19, 22), (21, 24), (25, 29), (26, 30)]:
#     print('fonction trier_par_debut validée')
# trier_par_fin(conferences)
# if conferences == [(2, 6), (4, 7), (5, 9), (1, 10), (8, 13), (3, 16), (14, 17),
#                    (12, 20), (19, 22), (11, 23), (21, 24), (15, 27), (6, 28), (25, 29), (26, 30), (18, 31)]:
#     print('fonction trier_par_fin validée')


def planning_glouton(conferences):
    copie_conferences = conferences.copy()
    trier_par_fin(copie_conferences)
    reponse = [copie_conferences[0]]
    for conf in copie_conferences[1:]:
        if fin(reponse[-1]) < debut(conf):
            reponse.append(conf)
    return reponse


conferences = [(19, 22), (6, 28), (21, 24), (18, 31), (8, 13), (15, 27), (3, 16),
               (25, 29), (5, 9), (12, 20), (4, 7), (1, 10), (11, 23), (26, 30), (2, 6), (14, 17)]
if planning_glouton(conferences) == [(2, 6), (8, 13), (14, 17), (19, 22), (25, 29)]:
    print('fonction planning_glouton validée')

trier_par_fin(conferences)
planning = planning_glouton(conferences)
fig, ax = plt.subplots()
ax.set_xlim(0, 32)
ax.set_ylim(-len(conferences), 2)
for i in range(len(conferences)):
    c = conferences[i]
    if c not in planning:
        ax.add_patch(Rectangle((debut(c), -i), fin(c) - debut(c), 1, edgecolor='k', fill=False))
    else:
        ax.add_patch(Rectangle((debut(c), -i), fin(c) - debut(c), 1, edgecolor='k', facecolor='grey'))
ax.set_aspect(1)
plt.show()


def planning_recursif(conferences, i, reponse):
    if i == len(conferences):
        return reponse
    elif fin(reponse[-1]) < debut(conferences[i]):
        reponse.append(conferences[i])
    return planning_recursif(conferences, i + 1, reponse)


def planning_glouton2(conferences):
    copie_conferences = conferences.copy()
    trier_par_fin(copie_conferences)
    reponse = [copie_conferences[0]]
    return planning_recursif(copie_conferences, 1, reponse)


# conferences = [(19, 22), (6, 28), (21, 24), (18, 31), (8, 13), (15, 27), (3, 16),
#                (25, 29), (5, 9), (12, 20), (4, 7), (1, 10), (11, 23), (26, 30), (2, 6), (14, 17)]
# if planning_glouton2(conferences) == [(2, 6), (8, 13), (14, 17), (19, 22), (25, 29)]:
#     print('fonction planning_glouton2 validée')


def trouver_salle(salles, c):
    i = 0
    while i < len(salles) and fin(salles[i][-1]) >= debut(c):
        i += 1
    return i


# c = (26, 30)
# salles = [[(1, 10), (11, 23), (25, 29)],
#           [(2, 6), (8, 13), (14, 17), (18, 31)],
#           [(3, 16), (19, 22)],
#           [(4, 7), (12, 20), (21, 24)],
#           [(5, 9), (15, 27)],
#           [(6, 28)]]
# if trouver_salle(salles, c) == 2:
#     print('fonction trouver_salle validée')


def allouer_salles(conferences):
    trier_par_debut(conferences)
    salles = []
    for c in conferences:
        i = trouver_salle(salles, c)
        if i == len(salles):
            salles.append([])
        salles[i].append(c)
    return salles


# conferences = [(19, 22), (6, 28), (21, 24), (18, 31), (8, 13), (15, 27), (3, 16),
#                (25, 29), (5, 9), (12, 20), (4, 7), (1, 10), (11, 23), (26, 30), (2, 6), (14, 17)]
# salles = [[(1, 10), (11, 23), (25, 29)],
#           [(2, 6), (8, 13), (14, 17), (18, 31)],
#           [(3, 16), (19, 22), (26, 30)],
#           [(4, 7), (12, 20), (21, 24)],
#           [(5, 9), (15, 27)],
#           [(6, 28)]]
# if allouer_salles(conferences) == salles:
#     print('fonction allouer_salles validée')
