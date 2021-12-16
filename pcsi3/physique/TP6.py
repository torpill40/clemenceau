import matplotlib.pyplot as plt
import numpy as np

# Abscisse
f = np.array([1, 20])
u_f = np.array([0.1, 0.2])
f_sq = f ** 2
u_f_sq = u_f ** 2

# Ordonnée
Z = np.array([6, 7])
u_Z = np.array([0.1, 0.2])
Z_sq = Z ** 2
u_Z_sq = u_Z ** 2

# Calcul de la valeur centrale de la mesure par régression linéaire y = ax+b
reg = np.polyfit(f_sq, Z_sq, 1)
L_sq, r_sq = reg[0], reg[1]

# Nombre de simulations pour estimer l'incertitude-type
N = 1000

# Initialisation des listes
liste_L_sq, liste_r_sq = [], []

# Mise ne oeuvre des N régressions linéaires
for i in range(0, N):
    m = len(f_sq)
    my = Z_sq + u_Z_sq * np.sqrt(3) * np.random.uniform(-1, 1, m)
    mx = f_sq + u_f_sq * np.sqrt(3) * np.random.uniform(-1, 1, m)
    p = np.polyfit(mx, my, 1)
    liste_L_sq.append(p[0])
    liste_r_sq.append(p[1])

# Calcul des incertitudes-type sur a et b
u_L_sq = np.std(liste_L_sq, ddof=1)
u_r_sq = np.std(liste_r_sq, ddof=1)

L = np.sqrt(L_sq)
u_L = np.sqrt(u_L_sq)
r = np.sqrt(r_sq)
u_r = np.sqrt(u_r_sq)

# Graphique
plt.figure(figsize=(16, 7))
plt.subplot(1, 2, 1)
xfit = np.linspace(min(f_sq), max(f_sq), 2)  # 2 points suffisent pour tracer la droite
yfit = L_sq * xfit + r_sq
plt.plot(xfit, yfit, 'r', label=r"$L^2 = {:.2e} \pm {:.2e} H^2, r^2 = {:.2e} \pm {:.2e} \Omega^2$"
         .format(L_sq, u_L_sq, r_sq, u_r_sq))
plt.errorbar(f_sq, Z_sq, xerr=u_f_sq, yerr=u_Z_sq, fmt='b+', zorder=2, label='Mesures')
plt.title("Régression linéaire y = ax+b")
plt.xlabel(r"$f^2 \: (Hz^2)$")
plt.ylabel(r"$Z^2 \: (\Omega^2)$")
plt.legend()

# Résultat de la régression linéaire
print("L = {:.2e} +/- {:.2e} H".format(L, u_L))
print("r = {:.2e} +/- {:.2e} ohm".format(r, u_r))

# Tracé des résidus
res = Z_sq - (L_sq * f_sq + r_sq)
plt.subplot(1, 2, 2)
plt.plot(xfit, [0, 0], 'r')
plt.errorbar(f_sq, res, xerr=None, yerr=u_Z_sq, fmt='b+', zorder=2, label='Résidus')
plt.title("Résidus")
plt.xlabel(r"$f^2 \: (Hz^2)$")
plt.ylabel(r"résidus")
plt.legend()
plt.show()
