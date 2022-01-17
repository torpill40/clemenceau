#################################################
## Action d'un filtre sur un signal périodique ##
#################################################
import numpy as np  # numpy est chargé avec l'alias np
import matplotlib.pyplot as plt

G0 = 1
fc = 1


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
n = 6

plt.figure(figsize=(11, 6))
plt.title("Diagramme de Bode du filtre en fonction de son ordre")
plt.xlabel("Fréquence (en kHz)")
plt.ylabel("Gain")
plt.grid(True, which='both')
for i in range(n):
    plt.plot(f, gain(f, i), label=r"$G(f,{})$".format(i),
             c="#{:06x}".format(i * 0xb0 // n << 16 | i * 0xc4 // n << 8 | i * 0xde // n))
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
phi1 = 2
phi2 = 3
fc = 1 / (2 * np.pi * tau)  # Fréquence de coupure en Hz
fe = 100  # Fréquence d'échantillonnage en Hz

# Définition du signal d'entrée
f_ini = 0.100


def e(t):
    return A1 * np.cos(2 * np.pi * f_ini * t + phi1) + A2 * np.cos(4 * np.pi * f_ini * t + phi2)


# Représentation graphique du signal d'entrée
dt = 3 * 1 / f_ini
t = np.linspace(0, dt, 500)

plt.figure(figsize=(11, 6))
plt.title("Signal d'entrée en fonction du temps")
plt.grid(True)
plt.xlabel("Temps (s)")
plt.ylabel("Tension d'entrée (V)")
plt.plot(t, e(t), label=r"$e(t)$")
plt.legend()
plt.xlim(0, dt)
plt.show()


###########################################
## question d
###########################################
def G(f):  # Calcul du gain à la fréquence f
    return 1 / ((1 + (f / fc) ** 2) ** 0.5)


def phi(f):  # Calcul du déphasage à la fréquence f
    return -np.arctan(f / fc)


# Calcul du signal de sortie
...

# Comparaison des signaux d'entrée et de sortie
...

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
