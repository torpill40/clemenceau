from pylab import *

N, N_exp = 16, 10_000

moy = np.zeros(N_exp)
std = np.zeros(N_exp)

for i in range(N_exp):
    data = np.random.uniform(10, 11, N)
    moy[i], std[i] = np.mean(data), np.std(data, ddof=1)

u_moy = np.std(moy, ddof=1)
print(np.abs(1 / N ** 0.5 - np.mean(u_moy / std)))
