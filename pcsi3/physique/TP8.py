import numpy as np
import matplotlib.pyplot as plt


def y(a, b):
    return np.log(a / b)


T = np.array([1, 2, 3, 4, 5])
u_T = 0.5
Delta_T = u_T * 3 ** 0.5

t = np.array([2, 2, 2, 2, 2])
u_t = 0.5
Delta_t = u_t * 3 ** 0.5


# Abscisse
x = np.array([3, 5, 7, 9, 11])
u_x = 0.5

# Calculs avec une distribution de probabilité uniforme
N = 1000
C = len(T)

Calcul = np.zeros((N, C))
for i in range(N):
    T_i = np.random.uniform(T - Delta_T, T + Delta_T)
    t_i = np.random.uniform(t - Delta_t, t + Delta_t)
    calc = y(T_i, t_i)
    for j in range(C):
        Calcul[i][j] = calc[j]

# Ordonnée
# y = y(T, t)
# u_y = y(u_T, u_t)
y = np.array([np.mean(Calcul[:, i]) for i in range(C)])
u_y = np.array([np.std(Calcul[:, i], ddof=1) for i in range(C)])
print(y)

# Calcul de la valeur centrale de la mesure par régression linéaire y = ax+b
a, b = np.polyfit(x, y, 1)

# Nombre de simulations pour estimer l'incertitude-type
N = 1000

# Initialisation des listes
liste_a, liste_b = [], []

# Mise ne oeuvre des N régressions linéaires
for i in range(0, N):
    m = len(x)
    my = y + u_y * np.sqrt(3) * np.random.uniform(-1, 1, m)
    mx = x + u_x * np.sqrt(3) * np.random.uniform(-1, 1, m)
    p = np.polyfit(mx, my, 1)
    liste_a.append(p[0])
    liste_b.append(p[1])

# Calcul des incertitudes-type sur a et b
u_a = np.std(liste_a, ddof=1)
u_b = np.std(liste_b, ddof=1)

# Graphique
xfit = np.linspace(min(x), max(x), 2)  # 2 points suffisent pour tracer la droite
yfit = a * xfit + b
plt.figure()
plt.plot(xfit, yfit, 'r', label="a = {:.2e} +/- {:.2e} rad-1, b = {:.2e} +/- {:.2e}".format(a, u_a, b, u_b))
plt.errorbar(x, y, xerr=u_x, yerr=u_y, fmt='b+', zorder=2, label='Mesures')
plt.title(r"Régression linéaire $\ln \frac{T}{t} = ax+b$")
plt.xlabel(r"$\alpha$ en $rad^{-1}$")
plt.ylabel(r"$\ln \frac{T}{t}$")
plt.legend()
plt.show()

# Résultat de la régression linéaire
print("pente = {:.2e} +/- {:.2e} rad-1".format(a, u_a))
print("ordonnée = {:.2e} +/- {:.2e}".format(b, u_b))

# Tracé des résidus
res = y - (a * x + b)
plt.figure()
plt.plot(xfit, [0, 0], 'r')
plt.errorbar(x, res, xerr=None, yerr=u_y, fmt='b+', zorder=2, label='Résidus')
plt.title("Résidus (écarts verticaux à la droite de régression)")
plt.xlabel(r"$\alpha$ en $rad^{-1}$")
plt.ylabel(r"$\ln \frac{T}{t}$")
plt.legend()
plt.show()

# Tracé des écarts normalisés
ecart = (y - (a * x + b)) / u_y
plt.figure()
plt.plot(xfit, [2, 2], 'r')
plt.plot(xfit, [-2, -2], 'r')
plt.scatter(x, ecart)
plt.title("Ecarts normalisés")
plt.xlabel(r"$\alpha$ en $rad^{-1}$")
plt.ylabel("écart norm.")
plt.show()
