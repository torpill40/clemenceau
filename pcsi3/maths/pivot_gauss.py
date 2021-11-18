import numpy as np
import numpy.typing as npt


def gauss(s: npt.NDArray[float]):
    n, p, z = len(s), len(s[0]), 0
    for j in range(p - 1):
        for k in range(j - z, n):
            if (a := s[k][j]) != 0:
                s[j - z], s[k] = s[k].copy(), s[j - z].copy()
                for i in range(j - z + 1, n):
                    s[i] = a * s[i].copy() - s[i][j] * s[j - z].copy()
                break
        else:
            z += 1


if __name__ == '__main__':
    s = np.array([
        [1, 2, 3, 1],
        [4, 5, 6, 4],
        [7, 8, 10, -1]
    ])
    gauss(s)
    print(s)
