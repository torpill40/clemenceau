import matplotlib.pyplot as plt
import numpy as np

f = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8, 1.9, 2.0]
u_ug = [1.7, 1.95, 2.4, 2.98, 4.36, 5.48, 4.37, 3.19, 2.26, 1.8, 1.35]

plt.figure(figsize=(8, 5))
plt.title(r"Rapport $\frac{U}{U_G}$ par rapport à la fréquence")
plt.grid(True)
plt.scatter(f, u_ug, marker='x')
plt.xlabel("Fréquence (en kHz)")
plt.ylabel(r"$\frac{U}{U_G}$")
plt.xlim(0, 3)
plt.ylim(0, 6)

f = [1.20, 1.25, 1.30, 1.35, 1.40, 1.45, 1.50, 1.55, 1.60, 1.65, 1.70, 1.75, 1.80]
u_ug = [0.200, 0.220, 0.257, 0.314, 0.371, 0.448, 0.515, 0.540, 0.495, 0.430, 0.379, 0.337, 0.291]

plt.figure(figsize=(8, 5))
plt.title(r"Rapport $\frac{U}{U_G}$ par rapport à la fréquence")
plt.grid(True)
plt.scatter(f, u_ug, marker='x')
plt.xlabel("Fréquence (en kHz)")
plt.ylabel(r"$\frac{U}{U_G}$")
plt.xlim(0, 3)
plt.ylim(0, 0.6)
y_c = max(u_ug) / (2 ** 0.5)
plt.axhline(y_c, ls="--", c="grey")
plt.axvline(1.4, ls="--", c="grey")
plt.axvline(1.7, ls="--", c="grey")
plt.annotate(text="", xy=(1.4, y_c), xytext=([1.7, y_c]), arrowprops=dict(arrowstyle='<->', color='salmon', lw=2))
plt.text(1.5, y_c + 0.01, r"$\Delta f$")

f = np.array([0.28, 0.86, 0.85, 0.15, 0.49, 1.036, 1.093])
xm = np.array([1.13, 4.00, 4.08, 1.06, 1.73, 2.2, 1.58]) / 10 * 38e-2

plt.figure(figsize=(8, 5))
plt.title(r"Résonance en élongation")
plt.grid(True)
plt.scatter(f, xm, marker='x')
plt.xlabel(r"Fréquence (en Hz)")
plt.ylabel(r"$X_m$ (en m)")
plt.xlim(0, 2)
plt.ylim(0, 0.2)

vm = xm * f

plt.figure(figsize=(8, 5))
plt.title(r"Résonance en vitesse")
plt.grid(True)
plt.scatter(f, vm, marker='x')
plt.xlabel("Fréquence (en Hz)")
plt.ylabel(r"$V_m$ (en $m.s^{-1})$")
plt.xlim(0, 2)
plt.ylim(0, 0.15)
y_c = max(vm) / (2 ** 0.5)
plt.axhline(y_c, ls="--", c="grey")
plt.axvline(0.73, ls="--", c="grey")
plt.axvline(0.99, ls="--", c="grey")
plt.annotate(text="", xy=(0.73, y_c), xytext=([1.01, y_c]), arrowprops=dict(arrowstyle='<->', color='salmon', lw=2))
plt.text(0.86, y_c + 0.01, r"$\Delta f$")

plt.show()
