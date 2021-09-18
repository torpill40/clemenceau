from pylab import *

N = 10_000
a = 1

data = np.random.uniform(2, 4, N)
u_x = np.std(data, ddof=1)

print(np.abs(a / 3 ** 0.5 - u_x))

plt.hist(data, bins="rice")
plt.show()
