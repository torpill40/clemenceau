import time


# Question 1 : exp
def exp(x, n):
    return x ** n


# Question 2 : exp1
def exp1(x, n):
    res = 1
    for i in range(0, n):
        res *= x
    return res


def exp1_2(x, n):
    return 1 if n == 0 else exp1_2(x, n - 1) * x


# Question 3 : exp2
def exp2(x, n):
    res = 1
    x2 = x * x
    for i in range(n // 2):
        res *= x2
    if n % 2 == 1:
        res *= x
    return res


# Question Bonus : exp3
def exp3(x, n):
    if n == 0:
        return 1
    elif n == 1:
        return x
    elif n % 2 == 0:
        x2 = exp3(x, n // 2)
        return x2 * x2
    else:
        x2 = exp3(x, n // 2)
        return x2 * x2 * x


# Test de la validité des fonctions
x = 2
n = 200_000

print('Résultat du calcul avec la fonction exp  : ', exp(x, n))
print('Résultat du calcul avec la fonction exp1 : ', exp1(x, n))
print('Résultat du calcul avec la fonction exp2 : ', exp2(x, n))
print('Résultat du calcul avec la fonction exp3 : ', exp3(x, n))

# Question 4 : complexité

tic = time.perf_counter()
exp(x, n)
toc = time.perf_counter()
T = toc - tic
print("Temps de calcul avec la fonction exp : ", T)

tic = time.perf_counter()
exp1(x, n)
toc = time.perf_counter()
T1 = toc - tic
print("Temps de calcul avec la fonction exp1 : ", T1)

tic = time.perf_counter()
exp2(x, n)
toc = time.perf_counter()
T2 = toc - tic
print("Temps de calcul avec la fonction exp2 : ", T2)

tic = time.perf_counter()
exp3(x, n)
toc = time.perf_counter()
T3 = toc - tic
print("Temps de calcul avec la fonction exp3 : ", T3)

print('Rapport des temps exp1/exp :', T1 / T)
print('Rapport des temps exp2/exp :', T2 / T)
print('Rapport des temps exp3/exp :', T3 / T)
