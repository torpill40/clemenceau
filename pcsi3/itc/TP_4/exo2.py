# Importation des modules
import numpy as np  # importation du module numpy


def moyenne(liste: list[float]) -> float:
    res = 0
    for x in liste:
        res += x
    return res / len(liste)


def ecart_type(liste: list[float]) -> float:
    res = 0
    moy = moyenne(liste)
    for x in liste:
        res += (x - moy) ** 2
    res /= len(liste)
    return res ** 0.5


# Récupération des données
monfichier = open('NotesDS1.txt','r')
# On créé 2 listes vides pour stocker les noms et les notes.
prenoms = []
notes = []

for ligne in monfichier:
    # On sépare le nom et la note de l'étudiant et on stocke la liste obtenu dans une variable.
    data = ligne.split()
    # On ajoute le nom de l'étudiant à la liste des prénoms
    prenoms.append(data[0])
    # On converti en flottant puis on ajoute la note à la liste des notes.
    notes.append(float(data[1]))

# On ferme le fichier pour libérer l'espace mémoire
monfichier.close()

# Calculs statistiques avec les focntions du modules numpy
print("numpy")
print(np.mean(notes))  # Affichage de la moyenne des notes
print(np.std(notes))   # Affichage de l'écart type des notes
print("moi")
print(moyenne(notes))  # Affichage de la moyenne des notes
print(ecart_type(notes))   # Affichage de l'écart type des notes
