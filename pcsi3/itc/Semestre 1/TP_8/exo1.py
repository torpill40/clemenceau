import numpy as np
import matplotlib.pyplot as plt

N = 8
echiquier = np.zeros((N, N))
for i in range(N):
    for j in range(N):
        echiquier[i][j] = (i + j) % 2 == 1
plt.imshow(echiquier, interpolation='none', cmap='Greys')
plt.show()
