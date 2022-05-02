import numpy as np
import matplotlib.pyplot as plt

for i in range(-15, 16):
    for j in range(-5, 6):
        # plt.quiver(i + 5, j, -j, i, scale=2e2, width=1e-3)
        plt.quiver(i, j, -j * np.sqrt(j ** 2 + (i + 5) ** 2), (i - 5) * np.sqrt(j ** 2 + (i + 5) ** 2), scale=2e2,
                   width=1e-3, color='r')
        plt.quiver(i, j, j * np.sqrt(j ** 2 + (i - 5) ** 2), -(i + 5) * np.sqrt(j ** 2 + (i - 5) ** 2), scale=2e2,
                   width=1e-3, color='b')
plt.gca().set_aspect(1)
plt.show()
