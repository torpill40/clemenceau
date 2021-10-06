from random import randint # randint renvoie un entier au hasard entre 2 bornes
import time


# fonction qui recherche le maximum dans une liste avec le 1er algorithme
def f_Maximum1(L):
    Taille = len(L)
    for i in range(Taille):
        est_plus_grand = True   # est_plus_grand est une variable booléenne 
        for j in range(Taille):
            if L[i]<L[j]:
                est_plus_grand = False
        if est_plus_grand:
            return L[i]


# fonction qui recherche le maximum dans une liste avec le 2ème algorithme
def f_Maximum2(L):
    Taille = len(L)
    max_prev = L[0]
    for i in range(1, Taille):
        if L[i] > max_prev:
            max_prev = L[i]
    return max_prev
    

def perf(f, L) -> float:
    t0 = time.perf_counter()
    f(L)
    t1 = time.perf_counter()
    return t1 - t0


N = 4000 # taille de la liste
L = [randint(0,10*N) for i in range(N)] # création de la liste L par compréhension

# maximum directement avec Python, et oui ça existe :))
max_python = max(L)

# test de la fonction Maximum1
# print(L)
# print(max_python)

# Performances
print("Max1:", perf(f_Maximum1, L), "\nMax2:", perf(f_Maximum2, L))
print("-"*32)

for i in range(1, 5):
    L = [randint(0,10**j) for j in range(10**i)]
    print("i = ", i, "\nMax1:", perf(f_Maximum1, L), "\nMax2:", perf(f_Maximum2, L))
