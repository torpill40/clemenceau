import numpy as np


def celerite(l_onde, f_onde):
    return l_onde * f_onde


N = 10_000_000
f, u_f = 40_983, 94
l, u_l = 0.840e-2, 0.041e-2
Delta_f, Delta_l = u_f * 3 ** 0.5, u_l * 3 ** 0.5

x = (np.random.uniform(f - Delta_f, f + Delta_f, N), np.random.uniform(l - Delta_l, l + Delta_l, N))
y = celerite(x[0], x[1])
moy = np.mean(y)
std = np.std(y, ddof=1)

print(f"c={moy}m/s")
print(f"u(c)={std}m/s")
