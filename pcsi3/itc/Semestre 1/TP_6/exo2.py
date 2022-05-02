
def puissance_iteratif(x: float, n: int) -> float:
    res = 1
    for _ in range(n):
        res *= x
    return res


def puissance_recursif(x: float, n: int) -> float:
    if n == 0:
        return 1
    return puissance_recursif(x, n - 1) * x


print(puissance_iteratif(2, 1000))
print(puissance_recursif(2, 1000))
