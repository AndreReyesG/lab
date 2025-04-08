import random
from matplotlib import pyplot as plt
N = 10000

a = 0
b = 10

tabla = []
for _ in range(N):
    tabla.append(random.randint(a, b))

plt.hist(tabla, density=True)
plt.show()
