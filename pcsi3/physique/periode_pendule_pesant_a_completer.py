###########################################
## Pendule pesant ##
###########################################
#  Capacité numérique réalisée par le groupe D :
#  - DERVAL Louis-Maël
#  - JOSSE Ghislain
#  - BOCQUEL Enzo
###########################################
import numpy as np
from pylab import *
from scipy.integrate import odeint
from scipy.integrate import quad

# Définition des paramètres
g = 9.81  # en m.s-2
m = 50e-3  # en kg
l = 40e-2  # en m
J = 8.0e-3  # kg.m-2
N = 8  # nombres de conditions initiales


###########################################
## question a
###########################################
# Définition de la fonction F associée au pendule pesant
def F(Z, t):
    return np.array([
        Z[1],
        -m * g * l / J * sin(Z[0])
    ])


# Définition de la base de temps
T0 = 2
t0 = 0  # instant initial
t1 = 3 * T0  # instant final
p = T0 / 100  # pas d'intégration
n = int((t1 - t0) / p)
T = np.linspace(t0, t1, n + 1)

# Calcul de la solution de l'équation différentielle pour différentes CI et représentation graphique
plt.title(r"Evolution de l'angle du pendule pesant en fonction du temps")
plt.xlabel(r"$t$ (en s)")
plt.ylabel(r"$\theta$ (en rad)")
for i in range(2, N + 2):
    plt.plot(T, odeint(F, np.array([np.pi / i, 0]), T)[:, 0], label=r"$\theta_0 = \frac{\pi}{" + str(i) + "}$",
             c="#{:06x}".format((i - 2) * 0xb0 // N << 16 | (i - 2) * 0xc4 // N << 8 | (i - 2) * 0xde // N))
plt.legend()
plt.grid()
plt.show()


###########################################
## question b
###########################################
# Définition de la fonction à intégrer
def f_wrapper(theta_0):
    def f(theta):
        return 1 / (cos(theta) - cos(theta_0)) ** 0.5
    return f


# Calcul de la période  pour différentes CI
def periode(theta_0):
    return (2 * J / (m * g * l)) ** 0.5 * quad(f_wrapper(theta_0), -theta_0, theta_0)[0]


###########################################
## question c
###########################################
# Calculs des listes associées à l'amplitude et la periode d'oscillations
theta_0 = np.linspace(0, np.pi / 2, 1000)
periodes = np.array([periode(theta) for theta in theta_0])

# Tracé du graphe donnant la période en fonction de l'amplitude

plt.figure()
plt.plot(theta_0, periodes)
plt.xlabel(r"$\theta_0$ (en rad)")
plt.ylabel(r"$T$ (en s)")
plt.title(r"Période des oscillations $T$ en fonction de $\theta_0$")
plt.grid()
plt.show()
