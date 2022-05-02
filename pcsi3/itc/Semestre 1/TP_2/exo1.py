from random import randint as rint


N = 10
L = [rint(0, 10 * N) for _ in range(N)]


def avg(arr: list) -> float:
    res = 0
    for i in arr:
        res += i
    return res / len(arr)
    

print("Liste:", L, "\nMoyenne:", avg(L))
