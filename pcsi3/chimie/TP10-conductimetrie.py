import numpy as np
import matplotlib
import matplotlib.pyplot as plt

font = {'family': 'calibri',
        'weight': 'bold',
        'size': 15}

matplotlib.rc('font', **font)

y = np.array(
    [2.01, 1.96, 1.83, 1.82, 1.73, 1.70, 1.66, 1.65, 1.60, 1.58, 1.57, 1.56, 1.55, 1.54, 1.53, 1.52, 1.52, 1.51, 1.51,
     1.50, 1.51, 1.52, 1.53, 1.54, 1.55, 1.56, 1.56, 1.57, 1.58, 1.59, 1.59, 1.60, 1.68, 1.85, 2.02, 2.19, 2.35, 2.50,
     2.64, 2.81, 2.98, 3.11, 3.33, 3.43, 3.68, 3.73, 3.92, 4.02])
x = np.array([0.0] + [i * 0.5 + 1.0 for i in range(47)])

domaine = ((0, 8), (10, 18), (18, 31), (31, 47))
regs = []

plt.title(
    r"Dosage  conductimétrique de 20mL de CO3$^{2-}$(0.03 mol.L$^{-1}$), HO$^{-}$(0.02 mol.L$^{-1}$) par 24mL de "
    r"H3O$^{+}$(0.1 mol.L$^{-1}$)")
plt.xlabel("Volume d'acide versé (en mL)")
plt.ylabel(r"Conductivité de la solution (en mS.cm$^{-1}$)")
plt.scatter(x, y, marker='x', color='b', lw=3)
for d in domaine:
    reg = np.polyfit(x[d[0]:d[1]], y[d[0]:d[1]], deg=1)
    regs.append(reg)
    a, b = reg[0], reg[1]
    plt.plot([0, 25], [b, a * 25 + b], color="k", linestyle='--')
# plt.plot([0, 25], [y[36] - x[36] * (y[42] - y[36]) / (x[42] - x[36]),
#                    (y[42] - y[36]) / (x[42] - x[36]) * 25 + y[36] - x[36] * (y[42] - y[36]) / (x[42] - x[36])],
#          color="k", lw=0.5, linestyle='--')
for i in range(1, len(regs)):
    Ve = (regs[i][1] - regs[i - 1][1]) / (regs[i - 1][0] - regs[i][0])
    plt.axvline(Ve, color='b')
    plt.text(Ve, 1.2, f"{Ve:.2f}")
plt.grid()
plt.xlim(0, 25)
plt.ylim(1, 4.5)
plt.show()
