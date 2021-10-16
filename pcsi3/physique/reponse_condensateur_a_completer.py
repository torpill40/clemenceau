####################################################
#  Réponse d'un système linéaire du premier ordre  #
####################################################
import numpy as np
from pylab import *  # numpy est chargé avec l'alias np
from scipy import *  # non utilisé ici


def euler(F, x0, t0, t1, pas):  # Algorithme d'EULER explicite
    n = int((t1 - t0) / pas)
    T = np.linspace(t0, t1, n + 1)
    x = np.zeros(n + 1)
    x[0] = x0
    for i in range(n):
        x[i + 1] = x[i] + pas * F(x[i], T[i])
    return T, x


#################################
#  Cas a : charge du condensateur
#################################
# Définition des paramètres
E = 10.
u0 = 0.
R = 1.e2
C = 50.e-9
tau = R * C


# Définition de la fonction f(x,t) du problème de Cauchy
def f1(x, t):
    return (E - x) / tau


# Définition de la fonction solan(t0,t1,pas) = solution analytique
def solan1(t0, t1, pas):
    n = int((t1 - t0) / pas)
    T = np.linspace(t0, t1, n + 1)
    x = np.zeros(n + 1)
    for i in range(n + 1):
        x[i] = E * (1 - np.exp(-T[i] / tau))
    return T, x


# Tracé de la figure
plt.figure(figsize=(13, 4))
plt.subplot(1, 3, 1)
T, u = euler(f1, u0, 0, 10 * tau, tau / 100)  # Tracé de la solution numérique (Euler)
plt.plot(T, u, label="Euler, pas = tau/100")
TT, v = solan1(0, 10 * tau, tau / 100)  # Tracé de la solution analytique
plt.plot(TT, v, label="Solution analytique", linestyle='--')
plt.legend()
plt.xlabel('temps(s)')
plt.ylabel('tension (V)')
plt.title('Charge du condensateur')

#################################
#  Cas b : régime libre
#################################
# Définition des paramètres
u0 = E


# E, R, C et tau restent inchangés


# Définition de la fonction f(x,t) du problème de Cauchy
def f2(x, t):
    return -x / tau


# Définition de la fonction solan(t0,t1,pas) = solution analytique
def solan2(t0, t1, pas):
    n = int((t1 - t0) / pas)
    T = np.linspace(t0, t1, n + 1)
    x = np.zeros(n + 1)
    for i in range(n + 1):
        x[i] = E * np.exp(-T[i] / tau)
    return T, x


# Tracé de la figure
plt.subplot(1, 3, 2)
T, u = euler(f2, u0, 0, 10 * tau, tau / 100)
plt.plot(T, u, label="Euler, pas = tau/100")
TT, v = solan2(0, 10 * tau, tau / 100)
plt.plot(TT, v, label="Solution analytique", ls="--")
plt.legend()
plt.xlabel("temps(s)")
plt.ylabel("tension (V)")
plt.title("Décharge du condensateur")

#################################
#  Cas c : excitation sinusoïdale
#################################
# Définition des paramètres
u0 = 0.
omega = 1.e-5
# E, R, C et tau restent inchangés par rapport au cas précédent


# Définition de e(t)
def e(t):
    return E * np.cos(omega * t)


# Définition de la fonction f(x,t) du problème de Cauchy
def f3(x, t):
    return (e(t) - x) / tau


# Définition de la fonction solan(t0,t1,pas) = solution analytique
def solan3(t0, t1, pas):
    n = int((t1 - t0) / pas)
    T = np.linspace(t0, t1, n + 1)
    x = np.zeros(n + 1)
    for i in range(n + 1):
        x[i] = -E * np.exp(-T[i] / tau)\
            + (E * np.cos(omega * T[i]) + tau * omega * E * np.sin(omega * T[i])) / (tau ** 2 * omega ** 2 + 1)
    return T, x


# Tracé de la figure
plt.subplot(1, 3, 3)
T, u = euler(f3, u0, 0, 10 * tau, tau / 100)
plt.plot(T, u, label="Euler, pas = tau/100")
TT, v = solan3(0, 10 * tau, tau / 100)
plt.plot(TT, v, label="Solution analytique", ls="--")
plt.legend()
plt.xlabel("temps(s)")
plt.ylabel("tension (V)")
plt.title("Excitation sinusoïdale")
plt.show()
