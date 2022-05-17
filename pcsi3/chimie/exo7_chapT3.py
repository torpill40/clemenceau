import matplotlib.pyplot as plt
import numpy as np


k = 0.1
a = 1
b = 0.01
n = 10_000


def euler(F, Z0, start, end, num):
    Z = np.zeros(num + 1)
    T = np.linspace(start, end, num + 1)
    step = (end - start) / num
    Z[0] = Z0
    for i in range(num):
        Z[i + 1] = Z[i] + step * F(Z[i], T[i])
    return T, Z


def avancement(Z, t):
    return k * (a - Z) * (b + Z)


def derivate(Z, t):
    n = len(Z) - 1
    dZ_dt = np.zeros(n)
    for i in range(n):
        dZ_dt[i] = (Z[i] - Z[i + 1]) / (t[i] - t[i + 1])
    return dZ_dt


def main():
    t, x = euler(avancement, 0, 0, 100, n)
    plt.subplot(1, 2, 1)
    plt.title('Avancement au cours du temps')
    plt.xlabel(r'Temps $(s)$')
    plt.ylabel(r'Avancement volumique $(mol.L^{-1})$')
    plt.grid(True)
    plt.plot(t, x)

    v = derivate(x, t)
    plt.subplot(1, 2, 2)
    plt.title('Vitesse de la réaction au cours du temps')
    plt.xlabel(r'Temps $(s)$')
    plt.ylabel(r'Vitesse volumique $(mol.L^{-1}.s^{-1})$')
    plt.grid(True)
    plt.plot(t[:-1], v)
    plt.show()


if __name__ == '__main__':
    main()
