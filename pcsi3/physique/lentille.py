import numpy as np
import numpy.typing as npt
import matplotlib.pyplot as plt


class Rayon:
    __slots__ = ["m", "p", "color", "alpha"]

    def __init__(self, m: float, p: float, color: str = 'k', alpha: float = 1.):
        self.m = m
        self.p = p
        self.color = color
        self.alpha = alpha

    def draw(self, x1: float, x2: float):
        plt.plot([x1, x2], [self.m * x1 + self.p, self.m * x2 + self.p], color=self.color, alpha=self.alpha)


class Lentille:
    __slots__ = ["focal", "radius", "x", "y"]

    def __init__(self, focal: float, radius: float, x: float, y: float):
        self.focal = focal
        self.radius = radius
        self.x = x
        self.y = y

    def refracted(self, rayon: Rayon) -> Rayon:
        y_intersect = rayon.m * self.x + rayon.p
        if (self.y - y_intersect) ** 2 > self.radius ** 2:
            return rayon
        else:
            y_focal = rayon.m * self.focal
            m = (y_focal - y_intersect) / self.focal
            return Rayon(m, y_intersect - m * self.x, rayon.color, rayon.alpha)

    def draw(self):
        plt.arrow(self.x, self.y, 0, self.radius, head_width=0.3, head_length=0.3)
        plt.arrow(self.x, self.y, 0, -self.radius, head_width=0.3, head_length=0.3)
        plt.scatter([self.x - self.focal, self.x + self.focal], [self.y, self.y])


if __name__ == '__main__':
    x0 = -5
    x1 = -3
    x2 = 4
    l0 = Lentille(-3, 1, x0, 4)
    l1 = Lentille(5, 6, x1, 0)
    l2 = Lentille(2, 6, x2, 0)

    plt.figure(0, figsize=(12, 6))
    plt.xlim(-10, 10)
    plt.arrow(-9, 0, 18, 0, head_width=0.3, head_length=0.3)
    l0.draw()
    l1.draw()
    l2.draw()

    for i in range(-500, 550):
        r1 = Rayon(-1 / 2, i * 0.4 / 50, alpha=0.02)
        r2 = l0.refracted(r1)
        r3 = l1.refracted(r2)
        r4 = l2.refracted(r3)
        r1.draw(-9, x0)
        r2.draw(x0, x1)
        r3.draw(x1, x2)
        r4.draw(x2, 9)

    plt.show()
