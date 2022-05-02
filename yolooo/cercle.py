import matplotlib.pyplot as plt
import numpy as np


R = 25
t = np.linspace(0, 2 * np.pi, 50)
x, y = R * np.cos(t), R * np.sin(t)

plt.plot(x, y)
plt.gca().set_aspect(1)
plt.xlim(-50, 50)
plt.ylim(-30, 30)
plt.show()
