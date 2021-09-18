from pylab import * # numpy est chargé avec l'alias np 



# Entrez les variables
A = 1 # unité
B = 2 # unité
# Entrez les précisions (demi intervalle de la distribution uniforme)
DeltaA = 0.5 # unité
DeltaB = 0.5 # unité

# Entrez la fonction de composition
def g(a,b):
    return a+b

# Entrez le nombre de simulation que vous voulez effectuer 
N = 100000

# Calculs avec une distribution de probabilité uniforme
Calcul = []
for i in range(N):
    a = np.random.uniform(A-DeltaA,A+DeltaA)
    b = np.random.uniform(B-DeltaB,B+DeltaB)
    Calcul.append(g(a,b))
plt.figure()
plt.hist(Calcul,bins = 'rice')
plt.title('Résultat du tirage aléatoire de la grandeur calculée')
plt.xlabel("grandeur calculée (unité)")
plt.show()

# Calcul et affichage moyenne et écart type
moy = np.mean(Calcul)
std = np.std(Calcul,ddof=1)
print("Moyenne = {:.2f} unité".format(moy))
print("Ecart type = {:.2f} unité".format(std))


