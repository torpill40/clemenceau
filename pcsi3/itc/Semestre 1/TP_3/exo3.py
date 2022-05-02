from random import randint as rint
import time
from matplotlib import pyplot as plt


def f_Tri_bulles_1(L):
    L_cop = L.copy()
    T = len(L_cop)
    swap = True
    # n = 0
    while swap:
        # print(f"Parcourt {n}: {L_cop}")
        swap = False
        for i in range(T - 1):
            if L_cop[i] > L_cop[i + 1]:
                swap = True
                L_cop[i], L_cop[i + 1] = L_cop[i + 1], L_cop[i]
        # n += 1
    return L_cop


def f_Tri_bulles_2(L):
    L_cop = L.copy()
    T = len(L_cop)
    swap = True
    n = 0
    while swap:
        # print(f"Parcourt {n}: {L_cop}")
        swap = False
        for i in range(T - 1 - n):
            if L_cop[i] > L_cop[i + 1]:
                swap = True
                L_cop[i], L_cop[i + 1] = L_cop[i + 1], L_cop[i]
        n += 1
    return L_cop


def perf(f, L):
    t0 = time.perf_counter()
    ret = f(L)
    t1 = time.perf_counter()
    return t1 - t0, ret


N = 30_000
range_N = range(N)
L1 = [rint(0, N * 10) for _ in range_N]
# L1 = [N - i for i in range(N)]
# print(L1)
print(f"Performance 1: {perf(f_Tri_bulles_1, L1)[0]}")
p2, L2 = perf(f_Tri_bulles_2, L1)
print(f"Performance 2: {p2}")

plt.figure(figsize=(17, 6))

plt.subplot(1, 2, 1)
plt.title("Avant tri")
plt.scatter(range_N, L1, s=0.2)

plt.subplot(1, 2, 2)
plt.title("Après tri")
plt.scatter(range_N, L2, s=0.2)

plt.show()
