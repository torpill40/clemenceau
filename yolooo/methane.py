import numpy as np
import scipy.integrate as spi
import matplotlib.pyplot as plt
import matplotlib.animation as mpla

r_0 = 1.09e-10
E_0 = -6.86e-19 * 4
e = 1.6022e-19
m = 1.6611e-24
R = r_0
eps_0 = 8.8542e-12
A = -r_0 ** 12 * E_0
B = -2 * r_0 ** 6 * E_0
h = 1.00e-11

u = np.linspace(0, 2 * np.pi, 13)
v = np.linspace(0, np.pi, 7)


def F(Z, t):
    r2_1 = Z[0] ** 2 + Z[1] ** 2 + Z[2] ** 2
    r2_2 = Z[6] ** 2 + Z[7] ** 2 + Z[8] ** 2
    r2_3 = Z[12] ** 2 + Z[13] ** 2 + Z[14] ** 2
    r2_4 = Z[18] ** 2 + Z[19] ** 2 + Z[20] ** 2
    d2_1_2 = (Z[0] - Z[6]) ** 2 + (Z[1] - Z[7]) ** 2 + (Z[2] - Z[8]) ** 2
    d2_1_3 = (Z[0] - Z[12]) ** 2 + (Z[1] - Z[13]) ** 2 + (Z[2] - Z[14]) ** 2
    d2_1_4 = (Z[0] - Z[18]) ** 2 + (Z[1] - Z[19]) ** 2 + (Z[2] - Z[20]) ** 2
    d2_2_3 = (Z[6] - Z[12]) ** 2 + (Z[7] - Z[13]) ** 2 + (Z[8] - Z[14]) ** 2
    d2_2_4 = (Z[6] - Z[18]) ** 2 + (Z[7] - Z[19]) ** 2 + (Z[8] - Z[20]) ** 2
    d2_3_4 = (Z[12] - Z[18]) ** 2 + (Z[13] - Z[19]) ** 2 + (Z[14] - Z[20]) ** 2
    a1 = 6 / (r2_1 ** 4) * (2 * A / (r2_1 ** 3) - B)
    a2 = 6 / (r2_2 ** 4) * (2 * A / (r2_2 ** 3) - B)
    a3 = 6 / (r2_3 ** 4) * (2 * A / (r2_3 ** 3) - B)
    a4 = 6 / (r2_4 ** 4) * (2 * A / (r2_4 ** 3) - B)
    b_1_2 = e ** 2 / (4 * np.pi * d2_1_2 ** 1.5 * eps_0)
    b_1_3 = e ** 2 / (4 * np.pi * d2_1_3 ** 1.5 * eps_0)
    b_1_4 = e ** 2 / (4 * np.pi * d2_1_4 ** 1.5 * eps_0)
    b_2_3 = e ** 2 / (4 * np.pi * d2_2_3 ** 1.5 * eps_0)
    b_2_4 = e ** 2 / (4 * np.pi * d2_2_4 ** 1.5 * eps_0)
    b_3_4 = e ** 2 / (4 * np.pi * d2_3_4 ** 1.5 * eps_0)
    return np.array([
        Z[3],
        Z[4],
        Z[5],
        (a1 * Z[0] - b_1_2 * (Z[6] - Z[0]) - b_1_3 * (Z[12] - Z[0]) - b_1_4 * (Z[18] - Z[0]) - h * Z[3]) / m,
        (a1 * Z[1] - b_1_2 * (Z[7] - Z[1]) - b_1_3 * (Z[13] - Z[1]) - b_1_4 * (Z[19] - Z[1]) - h * Z[4]) / m,
        (a1 * Z[2] - b_1_2 * (Z[8] - Z[2]) - b_1_3 * (Z[14] - Z[2]) - b_1_4 * (Z[20] - Z[2]) - h * Z[5]) / m,

        Z[9],
        Z[10],
        Z[11],
        (a2 * Z[6] - b_1_2 * (Z[0] - Z[6]) - b_2_3 * (Z[12] - Z[6]) - b_2_4 * (Z[18] - Z[6]) - h * Z[9]) / m,
        (a2 * Z[7] - b_1_2 * (Z[1] - Z[7]) - b_2_3 * (Z[13] - Z[7]) - b_2_4 * (Z[19] - Z[7]) - h * Z[10]) / m,
        (a2 * Z[8] - b_1_2 * (Z[2] - Z[8]) - b_2_3 * (Z[14] - Z[8]) - b_2_4 * (Z[20] - Z[8]) - h * Z[11]) / m,

        Z[15],
        Z[16],
        Z[17],
        (a3 * Z[12] - b_1_3 * (Z[0] - Z[12]) - b_2_3 * (Z[6] - Z[12]) - b_3_4 * (Z[18] - Z[12]) - h * Z[15]) / m,
        (a3 * Z[13] - b_1_3 * (Z[1] - Z[13]) - b_2_3 * (Z[7] - Z[13]) - b_3_4 * (Z[19] - Z[13]) - h * Z[16]) / m,
        (a3 * Z[14] - b_1_3 * (Z[2] - Z[14]) - b_2_3 * (Z[8] - Z[14]) - b_3_4 * (Z[20] - Z[14]) - h * Z[17]) / m,

        Z[21],
        Z[22],
        Z[23],
        (a4 * Z[18] - b_1_4 * (Z[0] - Z[18]) - b_2_4 * (Z[6] - Z[18]) - b_3_4 * (Z[12] - Z[18]) - h * Z[21]) / m,
        (a4 * Z[19] - b_1_4 * (Z[1] - Z[19]) - b_2_4 * (Z[7] - Z[19]) - b_3_4 * (Z[13] - Z[19]) - h * Z[22]) / m,
        (a4 * Z[20] - b_1_4 * (Z[2] - Z[20]) - b_2_4 * (Z[8] - Z[20]) - b_3_4 * (Z[14] - Z[20]) - h * Z[23]) / m
    ])


def animate_(fig, animation_rate):
    def wrapper(frame):
        fig.clear()
        ax = fig.add_subplot(111, projection='3d')
        ax.set_box_aspect(aspect=(1, 1, 1))
        x = R * 0.9 * np.outer(np.cos(u), np.sin(v))
        y = R * 0.9 * np.outer(np.sin(u), np.sin(v))
        z = R * 0.9 * np.outer(np.ones(np.size(u)), np.cos(v))
        ax.plot_surface(x, y, z, rstride=1, cstride=1, color='k', alpha=0.6)
        for i in range(4):
            x = R * 0.4 * np.outer(np.cos(u), np.sin(v)) + ZM[:, 0 + i * 6][frame * animation_rate]
            y = R * 0.4 * np.outer(np.sin(u), np.sin(v)) + ZM[:, 1 + i * 6][frame * animation_rate]
            z = R * 0.4 * np.outer(np.ones(np.size(u)), np.cos(v)) + ZM[:, 2 + i * 6][frame * animation_rate]
            ax.plot_surface(x, y, z, rstride=1, cstride=1, color='w', alpha=0.6)
        lim = 1.1 * R
        ax.set_xlim(-lim, lim)
        ax.set_ylim(-lim, lim)
        ax.set_zlim(-lim, lim)
    return wrapper


def animate(ZM, animation_rate=1, frames=-1):
    fig = plt.figure()
    _ = mpla.FuncAnimation(fig, animate_(fig, animation_rate), frames=frames if frames > 0 else len(ZM) // animation_rate - 1, interval=1)
    plt.show()


def save(ZM, file, animation_rate=1, frames=-1):
    fig = plt.figure()
    anim = mpla.FuncAnimation(fig, animate_(fig, animation_rate), frames=frames if frames > 0 else len(ZM) // animation_rate - 1, interval=1)
    writer = mpla.PillowWriter(fps=60)
    anim.save(file, writer=writer)
    print("Animation saved")


def draw(ZM):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_box_aspect(aspect=(1, 1, 1))
    x = R * 1.0 * np.outer(np.cos(u), np.sin(v))
    y = R * 1.0 * np.outer(np.sin(u), np.sin(v))
    z = R * 1.0 * np.outer(np.ones(np.size(u)), np.cos(v))
    ax.plot_surface(x, y, z, rstride=1, cstride=1, color='k', alpha=0.6)
    for i in range(4):
        # ax.plot3D(ZM[:, 0 + i * 6], ZM[:, 1 + i * 6], ZM[:, 2 + i * 6])
        x = R * 0.4 * np.outer(np.cos(u), np.sin(v)) + ZM[:, 0 + i * 6][-1]
        y = R * 0.4 * np.outer(np.sin(u), np.sin(v)) + ZM[:, 1 + i * 6][-1]
        z = R * 0.4 * np.outer(np.ones(np.size(u)), np.cos(v)) + ZM[:, 2 + i * 6][-1]
        ax.plot_surface(x, y, z, rstride=1, cstride=1, color='w', alpha=0.6)
    lim = 1.1 * R
    ax.set_xlim(-lim, lim)
    ax.set_ylim(-lim, lim)
    ax.set_zlim(-lim, lim)
    plt.show()


Z_0 = np.array([
    0, 0, R, 0, 0, 0,
    R, 0, 0, 0, 0, 0,
    0, R, 0, 0, 0, 0,
    0, 0, -R, 0, 0, 0
])

t0 = 0
t1 = 0.000000001
T = np.linspace(t0, t1, 10000000)

ZM = spi.odeint(F, Z_0, T)

animate(ZM, 100)
# save(ZM, "CH4.gif", 100, 100)
# draw(ZM)
