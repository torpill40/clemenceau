#################################################
## Action d'un filtre sur un signal périodique ##
#################################################
import numpy as np  # numpy est chargé avec l'alias np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

G0 = 1
fc = 1  # Fréquence de coupure en kHz


###########################################
## question a
###########################################
# Définition de la fonction gain G(f,n) f = fréquence, n = ordre du filtre
def gain(f, n):
    return G0 / ((1 + (f / fc) ** (2 * n)) ** 0.5)


# Tracé du graphe G(f,n) en fonction de f pour différentes valeurs de n
f = np.linspace(0, 2, 500)

plt.figure(figsize=(11, 6))
plt.title("Gain en fonction de la fréquence")
plt.xlabel("Fréquence (en kHz)")
plt.ylabel("Gain")
plt.grid(True)
plt.plot(f, gain(f, 1), label=r"$G(f,1)$")
plt.legend()
plt.xlim(0, 2)
plt.show()

###########################################
## question b
###########################################
# Tracé du graphe GdB en fonction de f (échelle log) pour différentes valeurs de n
f = np.logspace(-2, 1, 500)  # Pour répartir régulièrement les points  calculés sur une échelle log
n = 7

plt.figure(figsize=(11, 6))
plt.title("Diagramme de Bode du filtre en fonction de son ordre")
plt.xlabel("Fréquence (en kHz)", loc="right")
plt.ylabel("Gain (en dB)", loc="bottom")
plt.grid(True, which='both')
for i in range(n):
    plt.plot(f, 20 * np.log(gain(f, i + 1)), label=r"$G_{dB}(f,{" + str(i + 1) + "})$",
             c="#{:06x}".format(i * 0xb0 // n << 16 | i * 0xc4 // n << 8 | i * 0xde // n))
ax = plt.gca()
ax.spines["left"].set_position(("data", 1))
ax.spines["bottom"].set_position("zero")
plt.legend()
plt.semilogx()  # échelle logarithmique pour la fréquence
plt.xlim(1.e-2, 1.e1)
plt.show()

###########################################
## question c
###########################################
# Définition des paramètres
R = 5 * 10 ** 3
C = 5 * 10 ** -8
A1 = 2
A2 = 3
tau = R * C
phi1 = np.pi / 6
phi2 = 2 * np.pi / 3
fc = 1 / (2 * np.pi * tau)  # Fréquence de coupure en Hz
fe = 100  # Fréquence d'échantillonnage en Hz


# Définition du signal d'entrée
def e(t):
    return A1 * np.cos(2 * np.pi * fe * t + phi1) + A2 * np.cos(4 * np.pi * fe * t + phi2)


# Représentation graphique du signal d'entrée
T = 1 / fe
dt = 3 * T
t = np.linspace(0, dt, 500)

plt.figure(figsize=(11, 6))
plt.title("Signal d'entrée en fonction du temps")
plt.grid(True)
plt.xlabel("Temps (s)")
plt.ylabel("Tension d'entrée (V)")
plt.plot(t, e(t), label=r"$e(t)$")
plt.legend()
plt.xlim(0, dt)
plt.ylim(A1 + A2, -A1 - A2)
plt.xticks([i * T / 2 for i in range(7)], [r"$0$", r"$\frac{T}{2}$", r"$T$", r"$\frac{3T}{2}$", r"$2T$",
                                           r"$\frac{5T}{2}$", r"$3T$"])
plt.show()


###########################################
## question d
###########################################
def G(f):  # Calcul du gain à la fréquence f
    return 1 / ((1 + (f / fc) ** 2) ** 0.5)


def phi(f):  # Calcul du déphasage à la fréquence f
    return -np.arctan(f / fc)


# Calcul du signal de sortie
def s(t):
    return G(fe) * A1 * np.cos(2 * np.pi * fe * t + phi1 + phi(fe)) + \
           G(2 * fe) * A2 * np.cos(4 * np.pi * fe * t + phi2 + phi(2 * fe))


# Comparaison des signaux d'entrée et de sortie
plt.figure(figsize=(13, 6))
plt.subplot(1, 2, 1)
plt.title("Comparaison des signaux d'entrée et de sortie en fonction du temps")
plt.grid(True)
plt.xlabel("Temps (s)")
plt.ylabel("Tension (V)")
plt.plot(t, e(t), label=r"$e(t)$")
plt.plot(t, s(t), label=r"$s(t)$")
plt.fill_between(t, e(t), s(t), color="lightsteelblue", alpha=0.2, label="Différence")
plt.legend()
plt.xlim(0, dt)
plt.ylim(A1 + A2, -A1 - A2)
plt.xticks([i * T / 2 for i in range(7)], [r"$0$", r"$\frac{T}{2}$", r"$T$", r"$\frac{3T}{2}$", r"$2T$",
                                           r"$\frac{5T}{2}$", r"$3T$"])
plt.subplot(1, 2, 2)
plt.grid(True)
plt.xlabel("Temps (s)")
plt.ylabel("Différence de tension (V)")
plt.plot(t, e(t) - s(t), label=r"$e(t)-s(t)$", color="lightsteelblue")
plt.legend()
plt.xlim(0, dt)
plt.ylim(A1 + A2, -A1 - A2)
plt.xticks([i * T / 2 for i in range(7)], [r"$0$", r"$\frac{T}{2}$", r"$T$", r"$\frac{3T}{2}$", r"$2T$",
                                           r"$\frac{5T}{2}$", r"$3T$"])
plt.show()

###########################################
## question e
###########################################
# Comparaison des signaux d'entrée et de sortie pour différentes fréquences f
...

###########################################
## question f
###########################################
# Définition du signal carre
...

# Allure du signal carre(t) pour différentes valeurs de n
...

###########################################
## question g
###########################################
# Calcul du signal en sortie
...

# Allure du signal en sortie
...

# Influence de la fréquence sur le signal de sortie
...
