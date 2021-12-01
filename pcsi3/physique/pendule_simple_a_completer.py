###########################################
## Pendule simple ##
###########################################
import matplotlib.pyplot as plt
import numpy as np
from pylab import *  # numpy est chargé avec l'alias np
from scipy.integrate import odeint


# Algorithme d'EULER explicite
def euler_vect(f, z0, t):
    n = len(t)
    z = [z0]
    for i in range(n - 1):
        p = t[i + 1] - t[i]
        z += [z[i] + p * f(z[i], t[i])]
    return array(z)


###########################################
## question a
###########################################

# Définition des paramètres
l = 0.10  # Longueur du pendule en m
g = 9.81  # Champ de pesanteur en m/s
w0 = sqrt(g / l)  # Pulsation propre en rad/s
T0 = 2 * pi / w0  # Période des petites oscillations en s


# Définition de la fonction F associée au pendule simple
def F(z, t):
    return array([z[1], -w0 ** 2 * sin(z[0])])


# Définition de la base de temps
t0, t1 = 0, 3 * T0
pas = T0 / 100
T = linspace(t0, t1, int((t1 - t0) / pas) + 1)

# Calcul de la solution par la méthode d'Euler
Y0 = [pi / 12, 0]  # Conditions initiales
Y = euler_vect(F, Y0, T)

# Tracé de la solution par méthode d'Euler
plt.figure(1, figsize=(14, 6))
ax = plt.subplot(1, 2, 1)
plt.grid(True)
ax.set_axisbelow(True)
plt.plot(T, Y[:, 0], label="Euler")
plt.xlabel(r'$temps \: (s)$')
plt.ylabel(r'$\theta \: (rad)$')
plt.title('Pendule simple')


###########################################
## question b
###########################################
# Calcul de la solution dans l'approximation linéaire
def solan(t):
    return pi / 12 * cos(w0 * T)


solan_T = solan(T)
# Représentation graphique
plt.plot(T, solan_T, ls="dashed", label=r"$\theta(t) = \theta_0 \cdot \cos(\omega_0 t)$")
plt.fill_between(T, solan_T, Y[:, 0], where=Y[:, 0] > solan_T, fc='lightsteelblue', alpha=0.3)
plt.fill_between(T, solan_T, Y[:, 0], where=Y[:, 0] < solan_T, fc='lightsteelblue', alpha=0.3)
plt.legend()

ax = plt.subplot(1, 2, 2)
plt.grid(True)
ax.set_axisbelow(True)
plt.plot(T, Y[:, 0] - solan_T, color='lightsteelblue', label="Comparaison")
plt.xlabel(r'$temps \: (s)$')
plt.ylabel(r'$\theta \: (rad)$')
plt.title("Comparaison solution analytique - méthode d'Euler")
plt.legend()
plt.show()

###########################################
## question c
###########################################
# Calcul de la solution avec odeint
Y = np.array(odeint(F, Y0, T))
# Représentation graphique
plt.figure(2, figsize=(14, 6))
ax = plt.subplot(1, 2, 1)
plt.grid(True)
ax.set_axisbelow(True)
plt.plot(T, Y[:, 0], label="odeint")
plt.plot(T, solan_T, ls="dashed", label=r"$\theta(t) = \theta_0 \cdot \cos(\omega_0 t)$")
plt.xlabel(r'$temps \: (s)$')
plt.ylabel(r'$\theta \: (rad)$')
plt.title('Pendule simple')
plt.fill_between(T, solan_T, Y[:, 0], where=Y[:, 0] > solan_T, fc='lightsteelblue', alpha=0.3)
plt.fill_between(T, solan_T, Y[:, 0], where=Y[:, 0] < solan_T, fc='lightsteelblue', alpha=0.3)
plt.legend()

ax = plt.subplot(1, 2, 2)
plt.grid(True)
ax.set_axisbelow(True)
plt.plot(T, Y[:, 0] - solan_T, color='lightsteelblue', label="Comparaison")
plt.xlabel(r'$temps \: (s)$')
plt.ylabel(r'$\theta \: (rad)$')
plt.title("Comparaison solution analytique - odeint")
plt.legend()
plt.show()

###########################################
## question d
###########################################
plt.figure(3, figsize=(10, 7))
plt.grid(True)
plt.gca().set_axisbelow(True)

wc = 6
Y[0] = 0
n = 7
for i in range(n, 0, -1):
    Y0[1] = i * wc / n
    Y = np.array(odeint(F, Y0, T))
    plt.plot(T, Y[:, 0], label=rf"${i=}$", c=f"#{i * 0xb0 // n << 16 | i * 0xc4 // n << 8 | i * 0xde // n:06x}")

plt.xlabel(r'$temps \: (s)$')
plt.ylabel(r'$\theta \: (rad)$')
plt.title('Pendule simple')
plt.legend()
plt.show()
