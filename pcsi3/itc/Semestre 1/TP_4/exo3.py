import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 100)

plt.figure(0, figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.title("Sinus")
plt.xlabel("abscisses")
plt.ylabel("ordonnées")
plt.grid(True)
plt.gca().set_axisbelow(True)
plt.scatter([-np.pi / 2, np.pi / 2], [-1, 1], c='k')
plt.plot(x, np.sin(x), c='r', ls='dashed')
plt.text(-np.pi / 2 - 0.45, -1.2, "minimum")
plt.text(np.pi / 2 - 0.45, 1.2, "maximum")
plt.xlim(-np.pi, np.pi)
plt.ylim(-1.5, 1.5)
plt.xticks([np.pi / 2 * i for i in range(-2, 3)], [r"$-\pi$", r"$-\pi/2$", r"0", r"$\pi/2$", r"$\pi$"])

plt.subplot(1, 2, 2)
plt.title("Cosinus")
plt.xlabel("abscisses")
plt.ylabel("ordonnées")
plt.grid(True)
plt.gca().set_axisbelow(True)
plt.scatter([-np.pi, 0, np.pi], [-1, 1, -1], c='k')
plt.plot(x, np.cos(x), color='b')
plt.text(-np.pi + 0.1, -1.2, "minimum")
plt.text(-0.45, 1.2, "maximum")
plt.text(3 * np.pi / 4 - 0.1, -1.2, "minimum")
plt.xlim(-np.pi, np.pi)
plt.ylim(-1.5, 1.5)
plt.xticks([np.pi / 2 * i for i in range(-2, 3)], [r"$-\pi$", r"$-\pi/2$", r"0", r"$\pi/2$", r"$\pi$"])

plt.show()
