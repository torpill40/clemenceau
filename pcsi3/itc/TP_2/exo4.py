from random import randint as rint
import matplotlib.pyplot as plt


def double_max(arr: list) -> tuple:
    if len(arr) == 0:
        return None, None
    if len(arr) == 1:
        return arr[0], None
    curr_mx = [arr[0], arr[1]]
    for i in arr:
        if i > curr_mx[0]:
            curr_mx[1], curr_mx[0] = curr_mx[0], i
        elif i > curr_mx[1] and i != curr_mx[0]:
            curr_mx[1] = i
    if curr_mx[0] == curr_mx[1]:
        return curr_mx[0], None
    return curr_mx[0], curr_mx[1]


N = 20
L = [rint(0, 10 * N) for _ in range(N)]

f_max, s_max = double_max(L)
print(L, "\nLe maximum de la liste L vaut", f_max, "\nLe second maximum de la liste L vaut", s_max, "\n")

plt.scatter(range(N), L)
plt.plot([0, N], [f_max, f_max], color="r")
plt.plot([0, N], [s_max, s_max], color="r")
plt.show()
