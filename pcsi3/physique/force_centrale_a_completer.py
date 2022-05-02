################################
##Mouvement à force centrale
###############################
import matplotlib.pyplot as plt
import numpy as np
from pylab import *  # numpy est chargé avec l'alias np
from scipy.integrate import odeint

# Définitions des paramètres
G = 6.67e-11
M = 6.0e24
x0 = -1.2e8
v0 = 5.0e3


# Définition de la fonction F du problème de Cauchy, avec la loi de Newton
def F(Z, t):
    return np.array([Z[2], Z[3], -G * M / (Z[0] ** 2 + Z[1] ** 2) ** 1.5 * Z[0],
                     -G * M / (Z[0] ** 2 + Z[1] ** 2) ** 1.5 * Z[1]])


################################
##a/ Mouvement d'un météore
###############################
# Définition de la base de temps
N = 10  # nombre d'heures
t0 = 0  # instant initial
t1 = N * 3600  # instant final en s
T = np.linspace(t0, t1, 1000)  # en s pour le calcul

plt.figure()
for i in range(501):
    # Définition des conditions initiales
    ZM0 = np.array([x0, 2.0e7 + i * 1e5, v0, 0])

    # Calcul de la trajectoire
    ZM = odeint(F, ZM0, T)

    # Tracé de la trajectoire du météore
    plt.plot(ZM[:, 0], ZM[:, 1], alpha=0.03, color='k')
    if i % 100 == 0:
        plt.plot(ZM[:, 0], ZM[:, 1], alpha=0.6, color='k', linestyle="--", lw=1)
    elif i % 20 == 0:
        plt.plot(ZM[:, 0], ZM[:, 1], alpha=0.3, color='k', linestyle="--", lw=1)


ZM0 = np.array([x0, 2.3e7, v0, 0])
ZM = odeint(F, ZM0, T)
plt.plot(ZM[:, 0], ZM[:, 1], color='r', linestyle="--", lw=1)

plt.axis('scaled')  # base orthonormée pour un tracé de trajectoire satisfaisant
plt.xlabel("x (en m)")
plt.ylabel("y (en m)")
plt.title("Trajectoire du météore")
plt.grid()

################################
##b/ Représentation de la Terre
###############################
# Tracé d'un cercle de rayon R
# paramétré par un angle theta variant entre 0 et 2*pi (50 points)
R = 6.4e6
theta = np.linspace(0, 2 * np.pi, 50)
x = R * np.cos(theta)
y = R * np.sin(theta)
plt.plot(x, y, color="b", lw=3)
plt.show()


###################################################
##c/ Distance du météore à la Terre
###################################################
# Calcul de la distance du météore à la Terre
def r(x, y):
    return np.sqrt(np.power(x, 2) + np.power(y, 2)) - R


# Représentation de l'évolution de cette distance en fonction du temps
r = r(ZM[:, 0], ZM[:, 1])
plt.figure()
plt.plot(T, r)
plt.title("Distance du météore à la Terre")
plt.xlabel("temps (en s)")
plt.ylabel("distance (en m)")
plt.grid()


##################################################################################
##d/ Recherche de la distance minimale d'approche par un calcul direct: méthode 1
##################################################################################
# Recherche de la valeur minimale d'un array
def minimum(Y):
    i = 0
    while Y[i - 1] <= Y[i] or Y[i + 1] <= Y[i]:
        i += 1
    return Y[i], i


# Détermination et affichage de la distance minimale d'approche
r_min, min_idx = minimum(r)
print("La valeur minimale d'approche est {}km".format(r_min * 1e-3))
plt.scatter(T[min_idx], r_min)
plt.show()


######################################################################################
##e/ Recherche de la distance minimale d'approche en annulant la dérivée : méthode 2
######################################################################################
# Calcul de la dérivée d'une fonction y(X)
def deriv(Y, X):
    d = []
    for i in range(1, len(Y) - 1):
        d.append((Y[i + 1] - Y[i]) / (X[i + 1] - X[i]))
    return np.array(d)


# Calcul de la dérivée de la distance par rapport au temps
r_prime = deriv(r, T)

# Représentation graphique de la dérivée de la distance par rapport au temps
plt.figure()
plt.plot(T[1:len(T) - 1], r_prime)
plt.grid()
plt.title("Dérivé de la distance du météore à la Terre")
plt.ylabel("dérivé (en m/s)")
plt.xlabel("temps (en s)")


# Calcul de l'annulation de la dérivée de la distance par dichotomie
def dicho(f, a, b, eps):
    while b - a > eps:
        c = (a + b) // 2
        if f[a] * f[c] < 0:
            b = c
        else:
            a = c
    return a


# Détermination et affichage de la distance minimale d'approche
print("La distance minimale d'approche est {}km".format(
    r[dicho(r_prime, int(20000 / 36000 * 1000), int(25000 / 36000 * 1000), 1)]*1e-3))
plt.show()
