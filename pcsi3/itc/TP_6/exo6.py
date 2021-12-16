
def triangle1(n: int):
    print("*" * n)
    if n > 0:
        triangle1(n - 1)


def triangle2(n: int):
    if n > 0:
        triangle2(n - 1)
    print("*" * n)


triangle1(7)
triangle2(7)
