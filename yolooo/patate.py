import matplotlib.pyplot as plt
import numpy as np

n = 100
prixunitaire = 3.99
reduction = 1.99
facteur_du_patator = 10

patates = np.array(range(n))
prix = (prixunitaire * patates + np.sin(patates * 2 * np.pi / 10) * facteur_du_patator) + np.power(patates, 2) / 25
reduit = prix - prix // 12 * reduction

plt.figure(figsize=(14, 7))
plt.title("Evolution non-linéaire du prix des patates en fonction du nombre de patates achetées avec une réduction de "
          "la totalité du prix des patates\nà chaque douzaine de patates achetées dans la quantité totale de patates "
          "achetées avec un facteur de patator égal à {}".format(facteur_du_patator))
plt.plot(patates, prix)
plt.plot(patates, reduit)
plt.show()
