
def exo1(p: int):
    c = 0
    v = lambda a, b: 2 * a + 3 * b
    while p > 0:
        print(v(p, c))
        if c == 0:
            p = p - 2
            c = 1
        else:
            p = p + 1
            c = 0
    print(v(p, c))


def exo2(n: int):
    # v = lambda x: x - 2 * ((x + 1) % 2) + 1 if n != 1 else 0
    v = lambda x: (x - (-1) ** x) if x > 1 else 0
    assert n > 0
    while n > 1:
        a = n
        if n % 2 == 0:
            n = n // 2
        else:
            n = n + 1
        print(f"{a}: {v(a)};{v(n)}")


def exo3(c: int, n: int):
    v = lambda a, b: 21 * a - 2 * b + 182 if b < 10 * a + 91 else a
    # v = lambda a, b: a + (10 * a - b + 91) * (abs(182 + 20 * a - 2 * n - 1) // (182 + 20 * a - 2 * n - 1) + 1)
    assert c > 0
    while c > 0:
        a, b = c, n
        if n > 100:
            n = n - 10
            c = c - 1
        else:
            n = n + 11
            c = c + 1
        print(f"{a, b}: {v(a, b)};{v(c, n)}")
        assert v(a, b) > v(c, n)


# exo1(36)
# exo2(587)
exo3(94, 1028)
