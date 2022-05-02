import numpy as np
import matplotlib
import matplotlib.pyplot as plt

font = {'family': 'calibri',
        'weight': 'bold',
        'size': 15}

matplotlib.rc('font', **font)

fn = np.array([108, 216, 429, 860])
n = np.array([1, 2, 4, 8])
L = 64.7e-2

lambdan = 2 * L / n
print(lambdan)

reg = np.polyfit(1 / fn, lambdan, deg=1)
print(reg)

plt.scatter(1 / fn, lambdan, marker='x', color='b')
plt.plot([0, 1 / fn[0]], [reg[1], reg[0] / fn[0] + reg[1]], color='r')
plt.title("Longueur d'onde en fonction de la période")
plt.xlabel(r"Période $\frac{1}{f_n}$ (en s)")
plt.ylabel(r"Longueur d'onde $\lambda_n$ (en m)")
plt.grid()
plt.show()
