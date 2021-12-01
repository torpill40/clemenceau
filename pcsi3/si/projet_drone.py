import matplotlib.pyplot as plt
import numpy as np

masses = np.array([20, 30, 40, 50, 60, 70, 80, 100, 120, 150])

mga_moy, mdr_moy = [], []

for m in masses:
    mga, mdr = [], []
    with open(f"drone_{m}g.csv", "r") as file:
        lines = file.readlines()
        del lines[0:20]
        for line in lines:
            data = line.split(";")
            mga += [float(data[1])]
            mdr += [float(data[2])]
    mga = np.array(mga)
    mdr = np.array(mdr)
    mga_moy += [mga.mean()]
    mdr_moy += [mdr.mean()]

mga_moy = np.array(mga_moy)
mdr_moy = np.array(mdr_moy)

epsilon = mdr_moy - mga_moy
reg = np.polyfit(masses, epsilon, 1)

plt.figure(1, figsize=(14, 5))
plt.subplot(1, 2, 1)
plt.title("Commande des moteurs en fonction de la masse")
plt.xlabel("Masse (g)")
plt.ylabel("Commande moteur")
plt.scatter(masses, mga_moy, label="MGA")
plt.scatter(masses, mdr_moy, label="MDR")
plt.legend()

plt.subplot(1, 2, 2)
plt.title("Différence de commande des moteurs en fonction de la masse")
plt.xlabel("Masse (g)")
plt.ylabel("Commande moteur")
plt.scatter(masses, epsilon, label="Ecart")
plt.plot(masses, reg[0] * masses + reg[1], label=rf"$\epsilon = {round(reg[0], 2)} * m {'+' if reg[1] > 0 else '-'} "
                                                 rf"{abs(round(reg[1], 2))}$")
plt.legend()

plt.show()
