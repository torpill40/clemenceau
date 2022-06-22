import matplotlib.pyplot as plt
import numpy as np


def peak(x_, y_, x_0, y_0, w, h, s=1.0):
    return h * (4 * (np.exp(((x_ - x_0) ** 2 + (y_ - y_0) ** 2) ** 0.5 / w)) / ((1 + np.exp(((x_ - x_0) ** 2 + (y_ - y_0) ** 2) ** 0.5 / w)) ** 2)) ** s


def f(x_, y_):
    return peak(x_, y_, 0, 0, 2.5, 25, 0.25) + peak(x_, y_, 3, 5, 1, 15) + peak(x_, y_, 3, -1, 2, 17, 2) + peak(x_, y_, -3, 0, 1, 12)


def surface(ax_, f_, x_, y_, cmap='inferno'):
    z_ = np.zeros((len(x_), len(x_[0])))
    for i in range(len(x_)):
        for j in range(len(x_[i])):
            z_[i, j] = f_(x_[i, j], y_[i, j])
    ax_.plot_surface(x_, y_, z_, cmap=cmap)


lim_x, lim_y = (-20, 20), (-20, 20)
dx, dy = 0.1, 0.1
x, y = np.mgrid[lim_x[0]:lim_x[1] + dx:dx, lim_y[0]:lim_y[1] + dy:dy]
_, ax = plt.subplots(subplot_kw=dict(projection='3d'))
surface(ax, f, x, y)
ax.set_zlim(-10, 50)
plt.show()
