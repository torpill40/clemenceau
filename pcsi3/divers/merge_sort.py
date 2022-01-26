from math import log2
from random import randint as rd

z = 0


def merge(a: list[float], b: list[float]) -> list[float]:
    global z
    c = []
    n_a, n_b = len(a), len(b)
    i, j = 0, 0
    for _ in range(n_a + n_b):
        z += 1
        if j >= n_b or (i < n_a and a[i] < b[j]):
            c += [a[i]]
            i += 1
        else:
            c += [b[j]]
            j += 1
    return c


def sort(x: list[float]) -> list[float]:
    n = len(x)
    if n > 1:
        return merge(sort(x[: n // 2]), sort(x[n // 2:]))
    else:
        return x


def main():
    x = [rd(0, 2 ** 32 - 1) for _ in range(2 ** 16)]
    n = len(x)
    s = sort(x)
    if n < 10:
        print(f"sort{x} = {s}")
    else:
        fmt = lambda lst: (str(lst[: 4]) + "..." + str(lst[n - 4:])).replace("]...[", ", ..., ")
        print(f"sort{fmt(x)} = {fmt(s)}")
    print(f"{z} ops, {n} elements | {n} * log2({n}) = {n * log2(n)}")


if __name__ == '__main__':
    main()
