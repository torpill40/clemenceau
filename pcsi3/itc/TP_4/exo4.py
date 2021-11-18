import numpy as np
import numpy.typing as npt
import matplotlib.pyplot as plt


r = 183
d = 595
h = 155


def io_law(alpha_list: npt.NDArray[float]) -> npt.NDArray[float]:
    return np.sqrt(
        np.power(d - r * np.sin(np.deg2rad(alpha_list)), 2) + np.power(r * np.cos(np.deg2rad(alpha_list)) - h, 2)
    )


time = []
x_mes = []
alpha_mes = []

file = open("Pilote.txt", 'r')
file.readline()
for line in file:
    data = line.split()
    time.append(float(data[0]))
    x_mes.append(float(data[1]))
    alpha_mes.append(float(data[2]))
file.close()

time = np.array(time, dtype=np.float64)
x_mes = np.array(x_mes, dtype=np.float64)
alpha_mes = np.array(alpha_mes, dtype=np.float64)

plt.figure(0, figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.title("Performances mesurées")
plt.xlabel("temps (s)")
plt.grid(True)
plt.gca().set_axisbelow(True)
plt.plot(time, x_mes, label="Position (mm)")
plt.plot(time, alpha_mes, label="Angle (°)")
plt.xlim(0, 12)
plt.ylim(-100, 150)
plt.legend()

plt.subplot(1, 2, 2)
plt.title("Position en fonction de l'angle")
plt.xlabel("angle (°)")
plt.ylabel("position (mm)")
plt.grid(True)
plt.gca().set_axisbelow(True)
plt.plot(alpha_mes, x_mes)
plt.xlim(-40, 40)
plt.ylim(-100, 150)

x_th = io_law(alpha_mes)

plt.figure(1, figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.title("Position en fonction de l'angle")
plt.xlabel("angle (°)")
plt.ylabel("position (mm)")
plt.grid(True)
plt.gca().set_axisbelow(True)
plt.plot(alpha_mes, x_mes, label="Mesuré")
plt.plot(alpha_mes, x_th, label="Simulé")
plt.xlim(-40, 40)
plt.ylim(-100, 700)
plt.legend()

idx_0 = 0
for i in range(len(alpha_mes)):
    if alpha_mes[i] >= 0:
        idx_0 = i

x_mes_0 = (x_mes[idx_0 - 1] + x_mes[idx_0]) / 2
x_mes_rec = x_mes - x_mes_0

x_th_0 = (x_th[idx_0 - 1] + x_th[idx_0]) / 2
x_th_rec = x_th - x_th_0

plt.subplot(1, 2, 2)
plt.title("Positions recalées en fonction de l'angle")
plt.xlabel("angle (°)")
plt.ylabel("position (mm)")
plt.grid(True)
plt.gca().set_axisbelow(True)
plt.plot(alpha_mes, x_mes_rec, label="Mesuré")
plt.plot(alpha_mes, x_th_rec, label="Simulé", ls="dashed")
plt.xlim(-40, 40)
plt.ylim(-150, 150)
plt.legend()

idx_lim_inf = idx_0
epsilon = np.abs(x_mes_rec - x_th_rec)
for i in range(idx_0, len(alpha_mes)):
    if epsilon[i] >= 1:
        idx_lim_inf = i
        break

idx_lim_sup = idx_0
epsilon = np.abs(x_mes_rec - x_th_rec)
for i in range(idx_0, 0, -1):
    if epsilon[i] >= 1:
        idx_lim_sup = i
        break

print(f"[{alpha_mes[idx_lim_inf]}, {alpha_mes[idx_lim_sup]}]")

plt.show()
