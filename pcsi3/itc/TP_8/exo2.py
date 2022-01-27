import numpy as np
import matplotlib.pyplot as plt

N = 512
R = 128

cercle = np.zeros((N, N))
for i in range(N):
    for j in range(N):
        d = ((i - N / 2) ** 2 + (j - N / 2) ** 2) ** 0.5
        if int(d - R) == 0:
            cercle[i][j] = 1
plt.imshow(cercle, interpolation='none', cmap='Greys')
plt.show()
