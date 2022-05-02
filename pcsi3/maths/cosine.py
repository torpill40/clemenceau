from math import pi, cos
import matplotlib.pyplot as plt
import numpy as np
import timeit


def cosine(x):
    x1 = x
    s = 1
    if x1 < 0:
        x1 = -x1
    x1 = x1 - 2 * int(x1 / pi / 2) * pi
    if x1 >= pi:
        x1 -= pi
        s = -1
    if x1 >= pi / 2:
        x1 = pi - x1
        s *= -1
    x2 = x1 * x1
    x4 = x2 * x2
    x8 = x4 * x4
    x16 = x8 * x8
    return s * ((x16 * x4) / 2_432_902_008_176_640_000 - (x16 * x2) / 6_402_373_705_728_000 +
                x16 / 20_922_789_888_000 - (x8 * x4 * x2) / 87_178_291_200 + (x8 * x4) / 479_001_600 -
                (x8 * x2) / 3_628_800 + x8 / 40320 - (x4 * x2) / 720 + x4 / 24 - x2 / 2 + 1)


N = 5_000_000
print(timeit.timeit(lambda: cosine(pi / 2), number=N))
print(timeit.timeit(lambda: cos(pi / 2), number=N))

t = np.linspace(-2 * pi, 2 * pi, 100_000)
plt.plot(t, [cosine(i) for i in t])
plt.show()
