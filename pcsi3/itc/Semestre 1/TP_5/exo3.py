# Importation des modules
import random as rd
from pylab import *


# Partie 1
# Fonction de recherche par dichotomie dans une liste triée
def recherche_dicho(L, x):
    ig = 0
    id = len(L) - 1
    im = (ig + id) // 2  # // = partie entière
    Tm = L[im]
    it = 1
    while ig < id and Tm != x:
        im = (ig + id) // 2
        Tm = L[im]
        if x > Tm:  # "Droite"
            ig = im + 1
        else:  # "Gauche"
            id = im - 1
        it += 1
    if Tm == x:
        return True, it
    else:
        Tm = L[ig]
        return Tm == x, it


# Partie 2
# Test de la fonction recherche_dicho pour différentes tailles de liste
taille, nb_ope = [], []
for n in range(0, 6):
    N = 10 ** n
    L = [rd.randint(0, 100 * N) for k in range(N)]
    L.sort()
    x = -1
    taille.append(N)
    nb_ope.append(recherche_dicho(L, x)[1])

# Partie 3
# Tracé du nombre d'opération en fonction de la taille
semilogx(taille, nb_ope, 'o')
xlabel('Taille de la liste')
ylabel('Nombre d\'opérations')
grid(True)
show()
