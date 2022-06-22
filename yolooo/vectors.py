import numpy as np
import matplotlib.pyplot as plt


z = np.linspace(0, 5, 101
                )
y = -np.cos(np.pi / 2 * z)
u = 1 / (np.pi ** 2 / 4 * np.sin(np.pi / 2 * z) ** 2 + 1) ** 0.5
v = -u * np.pi / 2 * np.sin(np.pi / 2 * z)
plt.figure()
plt.gca().set_aspect('equal')
plt.plot(y, z)
plt.quiver(y, z, u, v, scale=50, width=0.001)
plt.xlim(-5, 5)
plt.show()
