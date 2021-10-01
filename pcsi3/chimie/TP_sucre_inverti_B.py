# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 09:52:14 2021

@author: valer
"""

#TP 2
#Exploitation d'un étalonnage - recherche d'un modèle

#étape 1: Rechercher les bibliothèques utiles.
import numpy as np   #pour effectuer des calculs
import matplotlib.pyplot as plt    #pour obtenir des graphiques

#étape 2: Compléter le script suivant en entrant les valeurs expérimentales

# Entrer les valeurs de concentrations et des mesures expérimentales de la grandeur notée y, séparées par des virgules
C = np.array([20, 40, 80, 100, 120, 160])              
y = np.array([1.3, 3.5, 5.05, 6.3, 8.1, 10.1])

#étape 3: Faire calculer l'incertitude-type sur y à partir de l'évaluation de la demi-étendue de sa mesure

# Demi-étendue (ou tolérance) de chaque mesurage de y (à compléter)
delta_y = 0.05
# Incertitude-type sur y, on néglige celle sur C
u_y = delta_y / np.sqrt(3) 

#étape 4: Rechercher un modèle affine proche des valeurs expérimentales par la fonction polyfit
#Obtenir le coefficient directeur et l'ordonnée à l'origine de ce modèle (ajouter les unités)

# Régression linéaire de y en fonction de C (équation: y = mod[0]*C + mod[1])
mod = np.polyfit(C, y, 1)   
print('Le coefficient directeur de la droite est', mod[0], '')
print('L"ordonnée à l" origine de la droite est', mod[1], '')

#étape 5: Faire tracer sur le même graphique les points expérimentaux avec leur barre d'incertitude et le modèle affine (appelé droite de régression)
#Ajouter l'intervalle des valeurs de y (y à tracer entre ymin et ymax), une légende sur les axes puis un titre au graphique.

# Tracé des points expérimentaux avec barres d'incertitude 
plt.errorbar(C, y, yerr = u_y, fmt = ',', color = 'r', label= "points expérimentaux")
plt.grid()
plt.xlabel(r'Concentration en masse $(g.L^{-1})$')
plt.ylabel(r'Rotation du plan de polarisation $(°)$')
ymin=0
ymax=12
ax=plt.gca()
ax.set_xlim(0, 1.1*np.max(C))
ax.set_ylim(ymin,ymax)

plt.text(130, 8, r"$\alpha=" + str(round(mod[0], 3)) + "*C_m+" + str(round(mod[1], 3)) + "$")

# Tracé de la droite de régression en pointillés 
plt.plot(C, np.polyval(mod,C),'--', label= "droite de régression") 
plt.title('Rotation du plan de polarisation en fonction de la concentration')
plt.legend()
plt.show()


#étape 6:Tracer le graphique des résidus, en ajoutant les barres d'incertitude correspondantes
#Ajouter une légende sur les axes

# Tracé des résidus 
res = (y-np.polyval(mod,C))
plt.subplot(1, 2, 1)
plt.errorbar(C, res, yerr=u_y, fmt='.m')  
plt.plot(C, np.zeros(len(C)))   #Tracé de la ligne d'ordonnée 0          
plt.xlabel(r'Concentration en masse $(g.L^{-1})$')
plt.ylabel(r'Résidu $(°)$')
plt.grid()

#étape 7: Tracer le graphique des écarts normalisés
#Ajouter une légende sur les axes

#Tracé des écarts normalisés
z = (y-np.polyval(mod,C))/(u_y)
plt.subplot(1, 2, 2)
plt.axhline(y = 2,color='g')
plt.axhline(y = -2,color='g')
plt.plot(C, z,'bo')  
      
plt.xlabel(r'Concentration en masse $(g.L^{-1})$')
plt.ylabel('Ecart normalisé')
plt.grid()
plt.show()

