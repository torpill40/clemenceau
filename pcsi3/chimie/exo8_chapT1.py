import numpy as np
import matplotlib.pyplot as plt


K = 1.43e-4


def f(tau: float, p: float) -> float:
    return (3 - 2 * tau) ** 2 * tau * 1.00 ** 2 / (4 * (1 - tau) ** 3 * p ** 2) - K


if __name__ == '__main__':
    p_arr = np.linspace(1, 1_000, 10_000)
    tau_eq = np.zeros(len(p_arr))
    prec = 1e-16
    for i, p in enumerate(p_arr):
        a, b = 0, 1
        while np.abs(f_tau := f((tau := ((a + b) / 2)), p)) > prec:
            if f_tau > 0:
                b = tau
            else:
                a = tau

        tau_eq[i] = tau
        print(f"{p=:.2f},\t{tau=:.1%}")

    plt.grid(True)
    plt.gca().set_axisbelow(True)
    plt.plot(p_arr, tau_eq)
    plt.xlim(0, np.max(p_arr) * 1.1)
    plt.ylim(0, 1.1)
    plt.show()
