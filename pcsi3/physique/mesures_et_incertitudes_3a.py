import numpy as np


def frequence(t):
    return 1 / t


N = 10_000_000
T = 24.4e-6
Delta_T = 0.1e-6

x = np.random.uniform(T - Delta_T, T + Delta_T, N)
y = frequence(x)
moy = np.mean(y)
std = np.std(y, ddof=1)

print(f"f={moy}Hz")
print(f"u(f)={std}Hz")
