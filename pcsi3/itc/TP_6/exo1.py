
def som_iteratif(n: int) -> int:
    res = 0
    for i in range(n + 1):
        res += i
    return res


def som_recursif(n: int) -> int:
    if n == 0:
        return 0
    return som_recursif(n - 1) + n


print(som_iteratif(5))
print(som_recursif(5))
