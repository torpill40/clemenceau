from __future__ import annotations

from typing import Callable

import matplotlib.pyplot as plt
import numpy as np
import numpy.typing as npt
from matplotlib.lines import Line2D
from matplotlib.widgets import Slider


def multiple_formatter(denominator: np.int64 = 2, number: np.float64 = np.pi, latex: str = r"\pi"):
    def gcd(a: np.int64, b: np.int64):
        while b:
            a, b = b, a % b
        return a

    def _multiple_formatter(val: np.float64, pos: np.int64) -> str:
        den = denominator
        num = np.int64(np.rint(den * val / number))
        com = gcd(num, den)
        (num, den) = (int(num / com), int(den / com))
        if den == 1:
            if num == 0:
                return r"$0$"
            if num == 1:
                return r"$%s$" % latex
            elif num == -1:
                return r"$-%s$" % latex
            else:
                return r"$%s%s$" % (num, latex)
        else:
            if num == 1:
                return r"$\frac{%s}{%s}$" % (latex, den)
            elif num == -1:
                return r"$\frac{-%s}{%s}$" % (latex, den)
            else:
                return r"$\frac{%s%s}{%s}$" % (num, latex, den)
    return _multiple_formatter


h = np.float64(10.)
D = np.float64(20.)


def alpha(lambda_: np.float64 | npt.NDArray[np.float64]) -> np.float64 | npt.NDArray[np.float64]:
    return np.arcsin(lambda_ / (2 * h))


def lambda_cursor_changed(system: Line2D, system_alpha: Line2D) -> Callable[[np.float64], None]:
    def _lambda_cursor_changed(x0: np.float64):
        y0 = alpha(x0)
        # FIXME duplicated code
        origin = (0., 0.)
        a = (h * np.cos(y0), h * np.sin(y0))
        b = (0., x0)
        c = (0., x0 + D)
        #
        system_alpha.set_data(x0, y0)
        system.set_data((origin[0], a[0], b[0], c[0]), (origin[1], a[1], b[1], c[1]))
        plt.draw()
    return _lambda_cursor_changed


def main() -> None:
    x = np.linspace(0, 2 * h, 1_000)
    y = alpha(x)
    x0 = np.float64(12.)
    y0 = alpha(x0)
    # FIXME duplicated code
    origin = (0., 0.)
    a = (h * np.cos(y0), h * np.sin(y0))
    b = (0., x0)
    c = (0., x0 + D)
    #
    plt.figure(0, figsize=(16, 6))
    ax_main = plt.subplot(1, 2, 1)
    plt.grid(which="major")
    plt.grid(which="minor", linestyle="--", lw=0.5)
    plt.plot(x, y, label=r"$\alpha=f(\lambda)$")
    system_alpha, = ax_main.plot(x0, y0, marker="o", color="k")
    plt.title(r"Evolution de l'angle $\alpha$ en fonction de la position du vérin $\lambda$")
    plt.xlabel(r"$\lambda$ (cm)")
    plt.ylabel(r"$\alpha$ (rad)")
    ax_main.set_axisbelow(True)
    ax_main.set_xlim(0, x[-1] * 1.2)
    ax_main.set_ylim(0, y[-1] * 1.2)
    ax_main.xaxis.set_major_locator(plt.MultipleLocator(5))
    ax_main.xaxis.set_minor_locator(plt.MultipleLocator(2.5))
    ax_main.yaxis.set_major_locator(plt.MultipleLocator(np.pi / 8))
    ax_main.yaxis.set_minor_locator(plt.MultipleLocator(np.pi / 16))
    ax_main.yaxis.set_major_formatter(plt.FuncFormatter(multiple_formatter(16)))
    plt.legend()

    ax = plt.subplot(1, 2, 2)
    ax_l, ax_b, ax_w, ax_h = ax.get_position().bounds
    ax.set_position([ax_l, ax_b + 0.15, ax_w, ax_h - 0.15])
    ax.set_aspect(1.0)
    ax.set_xlim(-35, 35)
    ax.set_ylim(-5, 45)
    system, = ax.plot((origin[0], a[0], b[0], c[0]), (origin[1], a[1], b[1], c[1]), marker="o", mfc="k", mec="k")
    ax_lambda = plt.axes([ax_l, ax_b, ax_w, 0.05])
    lambda_cursor = Slider(ax_lambda, r"$\lambda$ (cm)", 5., 17.5, valinit=12.)
    lambda_cursor.on_changed(lambda_cursor_changed(system, system_alpha))
    plt.show()


if __name__ == "__main__":
    main()
