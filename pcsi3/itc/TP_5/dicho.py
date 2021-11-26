
def dicho(f, a, b, eps):
    while a - b > eps:
        m = (a + b) / 2
        if f(a) * f(m) < 0:
            b = m
        else:
            a = m
    return a
