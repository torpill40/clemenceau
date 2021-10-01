import numpy as np


def distance(x_1, x_2):
    return x_1 - x_2


N = 10_000_000
x1, x2 = 19.5, 11.1
Delta_x = 0.5

x = (np.random.uniform(x1 - Delta_x, x1 + Delta_x, N), np.random.uniform(x2 - Delta_x, x2 + Delta_x, N))
y = distance(x[0], x[1])
moy = np.mean(y)
std = np.std(y, ddof=1)

print(f"l={moy}cm")
print(f"u(l)={std}cm")
