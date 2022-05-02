import numpy as np
import matplotlib
import matplotlib.pyplot as plt

font = {'family': 'calibri',
        'weight': 'bold',
        'size': 15}

matplotlib.rc('font', **font)

V = [0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.2, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0,
     9.4, 9.6, 9.7, 9.8, 9.9, 9.95, 10.0, 10.05, 10.1, 10.2, 10.3, 10.4, 10.5, 10.7, 11.0, 11.4, 11.7, 12.0, 12.5, 13.0,
     13.5, 14.0, 14.5, 15.0, 15.5, 16.0, 16.3, 16.35, 16.45, 16.65, 16.7, 16.75, 16.8, 16.9, 17.0, 17.1, 17.4, 17.8,
     18.0, 18.4, 18.8, 19.0, 19.5, 20.0, 20.5, 21.0, 21.5, 22.0, 22.5, 23.0, 23.5, 24.0]
pH = [12.09, 12.01, 11.94, 11.84, 11.74, 11.60, 11.34, 11.23, 11.11, 11.01, 10.90, 10.81, 10.74, 10.63, 10.44, 10.30,
      10.17, 10.05, 9.93, 9.80, 9.65, 9.49, 9.28, 9.08, 8.84, 8.76, 8.61, 8.39, 8.26, 8.13, 8.01, 7.90, 7.76, 7.59,
      7.47, 7.42, 7.25, 7.06, 6.89, 6.80, 6.71, 6.55, 6.40, 6.27, 6.14, 5.97, 5.81, 5.58, 5.19, 4.74, 4.30, 3.67, 3.20,
      3.14, 3.07, 3.01, 2.92, 2.85, 2.77, 2.64, 2.51, 2.45, 2.36, 2.28, 2.26, 2.20, 2.14, 2.08, 2.04, 2.01, 1.98, 1.95,
      1.91, 1.89, 1.88]

derivee = []
volume = []
for i in range(1, len(V) - 1):
    derivee.append((pH[i - 1] - pH[i + 1]) / (V[i - 1] - V[i + 1]))
    volume.append(V[i])

domaine = ((0, 20), (20, 40), (40, 60))

plt.subplot(1, 2, 2)
plt.plot(volume, derivee, '+', color='red')
for d in domaine:
    print(pH[np.where(derivee == np.min(derivee[d[0]:d[1]]))[0][0] + 1])
    i = np.where(derivee == np.min(derivee[d[0]:d[1]]))[0][0] + 1
    plt.axvline(V[i], color='r')
    plt.text(V[i], 0.02, f"{V[i]}")

plt.title("Dérivée du pH en fonction du volume d'acide")
plt.xlabel("Volume d'acide versé (en mL)")
plt.ylabel(r"$\frac{dpH}{dV}$")
plt.grid()

plt.subplot(1, 2, 1)
plt.plot(V, pH, '+', color='blue')
for d in domaine:
    print(pH[np.where(derivee == np.min(derivee[d[0]:d[1]]))[0][0] + 1])
    i = np.where(derivee == np.min(derivee[d[0]:d[1]]))[0][0] + 1
    plt.axvline(V[i], color='b')
    plt.text(V[i], 2.2, f"{V[i]}")

plt.title(
    r"Dosage de 20mL de CO3$^{2-}$(0.03 mol.L$^{-1}$), HO$^{-}$(0.02 mol.L$^{-1}$) par 24mL de "
    r"H3O$^{+}$(0.1 mol.L$^{-1}$)")
plt.xlabel("Volume d'acide versé (en mL)")
plt.ylabel("pH de la solution")
plt.grid()
plt.show()
