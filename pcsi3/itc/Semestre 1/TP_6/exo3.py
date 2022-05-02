
def puissance_rapide_recursif(x: float, n: int) -> float:
    if n == 0:
        return 1
    x_2 = puissance_rapide_recursif(x, n // 2)
    if n % 2 == 0:
        return x_2 * x_2
    else:
        return x_2 * x_2 * x


print(puissance_rapide_recursif(2, 999_999))
