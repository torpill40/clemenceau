
def pyramide(n: int) -> tuple[int, int]:
    lvl = 0
    used = 0
    a = (lvl + 1) ** 2
    while n >= a:
        lvl += 1
        used += a
        n -= a
        a += 2 * lvl + 1
    return lvl, used


print(pyramide(20))
