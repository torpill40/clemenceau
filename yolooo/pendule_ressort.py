import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt


def F(Z, t):
    return np.array([
        Z[2],
        Z[3],
        g * np.cos(Z[1]) + (Z[3] ** 2 - k / m) * Z[0] + k * l0 / m - K * Z[2] / m,
        -g / Z[0] * np.sin(Z[1]) - (2 * Z[3] + K / m) * Z[2] / Z[0]
    ])


g = 9.81
m = 5
k = 500
l0 = 5e-1
D = 2.0e-1
mu = 1.49
K = 3 * np.pi * mu * D

T = 10
Z0 = np.array([
    6e-1,
    3 * np.pi / 4,
    0,
    0
])

t = np.linspace(0, T, int(T * 1000))
Z = spi.odeint(F, Z0, t)

fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
ax.plot(Z[:, 1], Z[:, 0])
ax.set_theta_zero_location("S")
ax.grid(True)
ax.set_title(f"Mouvement d'une boule de {m}kg de diamètre {D}m accroché à un pendule à ressort dans de la glycérine")
plt.show()
