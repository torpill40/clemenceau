#############################################################
## Variations de température et pression dans l'atmosphère ##
#############################################################
# DERVAL Louis-Maël
###########################################

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import scipy.integrate as sci

###########################################
## question a
###########################################
# Définition des paramètres
M = (0.8 * 14.0 * 2 + 0.2 * 16.0 * 2) * 1e-3  # Masse molaire de l'air en kg/mol
g = 9.81  # Champ de pesanteur en m/s
R = 8.314  # Constante des GP en J.mol^(-1).K^(-1)
T_sol = 288  # Température au sol en K
P_sol = 1.013e5  # Pression au niveau du sol en Pa
k_ISA_list = [(85e3, 0), (71e3, -2.0e-3), (51e3, -2.8e-3), (47e3, 0), (32e3, 2.8e-3), (20e3, 1.0e-3), (11e3, 0), (0, -6.5e-3)]  # Gradient thermique en fonction de l'altitude en K/km


def k_ISA(z):
    for altitude, grad in k_ISA_list:
        if z >= altitude:
            return grad


###########################################
## question b
###########################################
# Définition de la fonction F définissant le système différentiel
def F(TP, z):
    return np.array([
        k_ISA(z),
        -M * g / (R * TP[0]) * TP[1]
    ])


##########################################
## question c
###########################################
# Définition du tableau des z entre 0 et 85000 m  z exprimé en m
z_0 = 0  # m
z_1 = 85000  # m
pas = 1  # m
Z = np.linspace(z_0, z_1, int((z_1 - z_0) // pas) + 1)

##########################################
## question d
###########################################
# Calcul de la solution avec odeint
TP_0 = np.array([T_sol, P_sol])
TP = sci.odeint(F, TP_0, Z)
T = np.array(TP[:, 0])
P = np.array(TP[:, 1])

##########################################
## question e
###########################################
# Représentation graphique de la température
plt.figure(figsize=(12, 8.5))
gs = GridSpec(2, 10)
gs.update(wspace=1.8, hspace=0.35)
plt.subplot(gs[0, :5])
plt.title("Evolution de la pression en fonction de l'altitude")
plt.xlabel(r"Température $T \: (K)$")
plt.ylabel(r"Altitude $z \: (km)$")
plt.grid(which='major')
plt.grid(which='minor', linestyle='--', linewidth=0.5)
plt.minorticks_on()
plt.plot(T, Z * 1e-3)

###########################################
## question f
###########################################
# Représentation graphique de la pression
plt.subplot(gs[0, 5:])
plt.title("Evolution de la température en fonction de l'altitude")
plt.xlabel(r"Pression $P \: (Pa)$")
plt.ylabel(r"Altitude $z \: (km)$")
plt.gca().semilogx()
plt.grid(which='major')
plt.grid(which='minor', linestyle='--', linewidth=0.5)
plt.minorticks_on()
plt.plot(P, Z * 1e-3, label=r'$P_{ISA}(z)$')


###########################################
## question g
###########################################
# Calcul de la pression dans le modèle de l'atmosphère isotherme avec odeint
def F(P, z):
    return -M * g / (R * T_sol) * P


P_iso = np.array(sci.odeint(F, P_sol, Z)[:, 0])

# Comparaison graphique entre les deux modèles
plt.plot(P_iso, Z * 1e-3, label=r'$P_{iso}(z)$')
plt.legend()

###########################################
## question h
###########################################
# Calcul de l'écart relatif entre les deux modèles
ecart = np.abs(P - P_iso) / P

# Représentation graphique de l'écart relatif entre 0 et 20 km
idx = int(20000 // pas) + 1
plt.subplot(gs[1, 1:9])
plt.title("Ecart relatif en fonction de l'altitude dans la troposphère et la tropopause")
plt.xlabel(r"Altitude $z \: (km)$")
plt.ylabel(r"Ecart relatif $\frac{|P-P_{iso}|}{P}$")
plt.grid(which='major')
plt.grid(which='minor', linestyle='--', linewidth=0.5)
plt.minorticks_on()
plt.plot(Z[:idx] * 1e-3, ecart[:idx])
plt.show()
