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
fc = 1 / (2 * np.pi * tau)  # Fréquence de coupure en kHz
fe = 100  # Fréquence d'échantillonnage en kHz
f = 0.100


# Définition du signal d'entrée
def e(t, f):
    return A1 * np.cos(2 * np.pi * f * t + phi1) + A2 * np.cos(4 * np.pi * f * t + phi2)


# Représentation graphique du signal d'entrée
T = 1 / f
dt = 3 * T
t = np.linspace(0, dt, 500)

plt.figure(figsize=(11, 6))
plt.title("Signal d'entrée en fonction du temps")
plt.grid(True)
plt.xlabel("Temps (s)")
plt.ylabel("Tension d'entrée (V)")
plt.plot(t, e(t, f), label=r"$e(t)$")
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
def s(t, f):
    return G(f) * A1 * np.cos(2 * np.pi * f * t + phi1 + phi(f)) + \
           G(2 * f) * A2 * np.cos(4 * np.pi * f * t + phi2 + phi(2 * f))


# Comparaison des signaux d'entrée et de sortie
plt.figure(figsize=(13, 6))
plt.subplot(1, 2, 1)
plt.title("Comparaison des signaux d'entrée et de sortie en fonction du temps")
plt.grid(True)
plt.xlabel("Temps (s)")
plt.ylabel("Tension (V)")
plt.plot(t, e(t, f), label=r"$e(t)$")
plt.plot(t, s(t, f), label=r"$s(t)$")
plt.fill_between(t, e(t, f), s(t, f), color="lightsteelblue", alpha=0.2, label="Différence")
plt.legend()
plt.xlim(0, dt)
plt.ylim(A1 + A2, -A1 - A2)
plt.xticks([i * T / 2 for i in range(7)], [r"$0$", r"$\frac{T}{2}$", r"$T$", r"$\frac{3T}{2}$", r"$2T$",
                                           r"$\frac{5T}{2}$", r"$3T$"])
plt.subplot(1, 2, 2)
plt.grid(True)
plt.xlabel("Temps (s)")
plt.ylabel("Différence de tension (V)")
plt.plot(t, e(t, f) - s(t, f), label=r"$e(t)-s(t)$", color="lightsteelblue")
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
f = 100
T = 1 / f
dt = 3 * T
t = np.linspace(0, dt, 500)

plt.figure(figsize=(11, 6))


ax = plt.axes([0.1, 0.15, 0.8, 0.8])
plt.title("Comparaison des signaux d'entrée et de sortie en fonction de la fréquence")
plt.grid(True)

e_f, = ax.plot(t, e(t, f), label=r"$e(t)$")
s_f, = ax.plot(t, s(t, f), label=r"$s(t)$")
ax.set_xlim(0, dt)
ax.set_ylim(A1 + A2, -A1 - A2)
plt.xticks([i * T / 2 for i in range(7)], [r"$0$", r"$\frac{T}{2}$", r"$T$", r"$\frac{3T}{2}$", r"$2T$",
                                           r"$\frac{5T}{2}$", r"$3T$"])

ax_slider = plt.axes([0.25, 0.05, 0.6, 0.03])
slider = Slider(ax_slider, "Fréquence", 1.e-4, 1.e4, valinit=f)


def update_freq(evt):
    f = slider.val
    T = 1 / f
    dt = 3 * T
    t = np.linspace(0, dt, 500)
    e_f.set_data(t, e(t, f))
    s_f.set_data(t, s(t, f))
    ax.set_xlim([0, dt])
    ax.set_xticks([i * T / 2 for i in range(7)])
    ax.set_xticklabels([r"$0$", r"$\frac{T}{2}$", r"$T$", r"$\frac{3T}{2}$", r"$2T$", r"$\frac{5T}{2}$", r"$3T$"])
    plt.draw()


slider.on_changed(update_freq)
plt.show()


###########################################
## question f
###########################################
# Définition du signal carre
def signal_carre(t, f, n):
    carre = 0
    for i in range(n + 1):
        carre += np.sin((2 * i + 1) * 2 * np.pi * f * t) / (1 + 2 * i)
    return (4 / np.pi) * carre


# Allure du signal carre(t) pour différentes valeurs de n
f = 100
T = 1 / f
dt = 2 * T
t = np.linspace(0, dt, 500)

plt.figure(figsize=(11, 6))
nmax = 8
for j in range(nmax):
    plt.subplot(2, 4, j + 1)
    plt.plot(t, signal_carre(t, f, j))
    if j == 1:
        plt.title(str(j) + " harmonique")
    else:
        plt.title(str(j) + " harmoniques")
    plt.xticks([i * T / 2 for i in range(5)], [r"$0$", r"$\frac{T}{2}$", r"$T$", r"$\frac{3T}{2}$", r"$2T$"])
plt.show()


###########################################
## question g
###########################################
# Calcul du signal en sortie
def s_carre(t, f):
    carre = 0
    for i in range(n + 1):
        carre += G(2 * i * f) * np.sin((2 * i + 1) * 2 * np.pi * f * t + phi(2 * i * f)) / (1 + 2 * i)
    return (4 / np.pi) * carre


# Allure du signal en sortie
plt.figure(figsize=(11, 6))
plt.title("Passage d'un signal carré par le filtre")
plt.plot(t, signal_carre(t, f, 6), label=r"$e(t)$")
plt.plot(t, s_carre(t, 100), label=r"$s(t)$")
plt.grid(True)
plt.legend()
plt.show()

# Influence de la fréquence sur le signal de sortie
f = 100
T = 1 / f
dt = 3 * T
t = np.linspace(0, dt, 500)

plt.figure(figsize=(11, 6))

ax = plt.axes([0.1, 0.15, 0.8, 0.8])
plt.title("Influence de la fréquence sur le signal de sortie")
plt.grid(True)

e_f, = ax.plot(t, signal_carre(t, f, 6))
s_f, = ax.plot(t, s_carre(t, f))
ax.set_xlim([0, dt])
ax.set_xticks([i * T / 2 for i in range(7)])
ax.set_xticklabels([r"$0$", r"$\frac{T}{2}$", r"$T$", r"$\frac{3T}{2}$", r"$2T$", r"$\frac{5T}{2}$", r"$3T$"])

ax_slider = plt.axes([0.25, 0.05, 0.6, 0.03])
slider = Slider(ax_slider, "Fréquence", 1.e-4, 3.e3, valinit=f)


def update_freq_enzo(evt):
    f = slider.val
    T = 1 / f
    dt = 3 * T
    t = np.linspace(0, dt, 500)
    e_f.set_data(t, signal_carre(t, f, 6))
    s_f.set_data(t, s_carre(t, f))
    ax.set_xlim([0, dt])
    ax.set_xticks([i * T / 2 for i in range(7)])
    ax.set_xticklabels([r"$0$", r"$\frac{T}{2}$", r"$T$", r"$\frac{3T}{2}$", r"$2T$", r"$\frac{5T}{2}$", r"$3T$"])
    plt.draw()


slider.on_changed(update_freq_enzo)
plt.show()
