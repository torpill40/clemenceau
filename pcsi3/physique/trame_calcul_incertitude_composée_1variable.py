from pylab import * # numpy est chargé avec l'alias np 


# Entrez la variable
X = 4  # unité
# Entrez la précision sur la variable (demi intervalle de la distribution uniforme)
DeltaX = 1   # unité


# Entrez la fonction de composition
def f(x):
    return 1/x

# Entrez le nombre de simulation que vous voulez effectuer 
N = 100000

# Calculs avec une distribution de probabilité uniforme
Calcul=[]
for i in range(N):
    x = np.random.uniform(X-DeltaX,X+DeltaX)
    Calcul.append(f(x))

# Histogramme de la grandeur calculée
plt.figure()
plt.hist(Calcul,bins = 'rice')
plt.title('Résultat du tirage de la grandeur calculée')
plt.xlabel('grandeur calculée (unité)')
plt.show()

# Calcul et affichage moyenne et écart type
moy = np.mean(Calcul)
std = np.std(Calcul,ddof=1)
print("Moyenne = {:.2f} unité".format(moy))
print("Ecart-type  = {:.2f} unité".format(std))



