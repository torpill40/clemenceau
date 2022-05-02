
def sapin_pas_decorer(n: int, i: int = 0):
    if i < n:
        sapin_pas_decorer(n, i + 1)
        print((' ' * i) + ('*' * (2 * (n - i) - 1)))


def sapin_decorer(n: int, i: int = 0):
    if i < n:
        sapin_decorer(n, i + 1)
        print((' ' * i) + 'o' + ('*' * (2 * (n - i) - 1)) + 'o')


sapin_pas_decorer(7)
print()
sapin_decorer(7)
