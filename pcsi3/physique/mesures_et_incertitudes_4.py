import numpy as np
import matplotlib.pyplot as plt


x = [0.01, 2.50, 5.00, 7.50, 10.00]
y = [2.20, 7.70, 12.40, 17.70, 21.10]
u_y = [0.5, 0.4, 0.4, 0.6, 0.8]

reg = np.polyfit(x, y, 1)
a, b = reg[0], reg[1]

print(f"a={a}, b={b}")

ax = plt.gca()
ax.set_xlim(0, 12)
ax.set_ylim(0, 25)
plt.grid()
plt.scatter(x, y)
plt.errorbar(x, y, yerr=u_y)
plt.plot([0.00, 10.00], [b, a * 10.00 + b])
plt.show()
