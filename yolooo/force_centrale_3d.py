import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt


def F(Z, t):
    return np.array([
        Z[3],
        Z[4],
        Z[5],
        -G * M / (Z[0] ** 2 + Z[1] ** 2) ** 1.5 * Z[0],
        -G * M / (Z[0] ** 2 + Z[1] ** 2) ** 1.5 * Z[1],
        -G * M / (Z[0] ** 2 + Z[1] ** 2) ** 1.5 * Z[2]
    ])


G = 6.67e-11
M = 6.0e24
R = 6.4e6
v0 = 1.2e3
n = 10
a = np.random.standard_normal(n) * 60 * R
b = np.random.standard_normal(n) * 60 * R

N = 2000
t0 = 0
t1 = N * 3600
T = np.linspace(t0, t1, 10000)

u = np.linspace(0, 2 * np.pi, 13)
v = np.linspace(0, np.pi, 7)

x = R * np.outer(np.cos(u), np.sin(v))
y = R * np.outer(np.sin(u), np.sin(v))
z = R * np.outer(np.ones(np.size(u)), np.cos(v))

fig, ax = plt.subplots(subplot_kw={'projection': '3d'})
ax.plot_surface(x, y, z, rstride=1, cstride=1, color='b')
for i in range(n):
    x0 = 0
    ZM0 = np.array([
        x0,
        a[i],
        b[i],
        v0,
        0,
        0
    ])
    ZM = spi.odeint(F, ZM0, T)
    ax.plot3D(ZM[:, 0], ZM[:, 1], ZM[:, 2], color=f"#{i * 0xb0 // n << 16 | i * 0xc4 // n << 8 | i * 0xde // n:06x}")
ax.set_box_aspect(aspect=(1, 1, 1))
ax.set_xlim(-1.5e8, 1.5e8)
ax.set_ylim(-1.5e8, 1.5e8)
ax.set_zlim(-1.5e8, 1.5e8)
plt.show()
