from matplotlib import pyplot as plt
from matplotlib.patches import Circle, Polygon
import numpy as np


R = 1.0
n = 1.5
a = R / n
density = 1000

for j in range(int(np.ceil(-a / 2 * density)), int(np.floor(a / 2 * density) + 1)):
    d = j / density
    i = np.arcsin(d / R)
    r = np.arcsin(n * np.sin(i))

    x0, y0 = -2, d
    x1, y1 = R * np.cos(i), y0

    if r != i:
        xA = R * np.cos(i) + np.sin(i) / np.tan(r - i)
        m = d / (x1 - xA)
        p = d * xA / (xA - x1)
    else:
        m = 0
        p = 0

    x2 = 4
    y2 = m * x2 + p

    plt.plot([x0, x1, x2], [y0, y1, y2], color="black", alpha=0.015)

ax = plt.gca()
plt.ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.add_patch(Circle((0, 0), 1, lw=2, color='grey'))
ax.add_patch(Polygon(((-2, 2), (0, 2), (0, -2), (-2, -2)), color="white"))

plt.plot([-2, 4], [0, 0], linestyle="dashed", color="black")

plt.show()
