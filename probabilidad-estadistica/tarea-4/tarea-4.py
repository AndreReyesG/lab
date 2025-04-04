from scipy.stats import binom
from matplotlib import pyplot as plt

from random import random

N = 1000

n = 10
p = 0.5

exitos_posibles = range(0, n + 1)

probabilidades = []

for k in exitos_posibles:
    probabilidades.append(binom.pmf(k, n, p))

fig, (ax1, ax2) = plt.subplots(1, 2)
ax1.bar(exitos_posibles, probabilidades)

# Objetivo 2
tabla_frecuencia = [0 for _ in exitos_posibles]

for _ in range(N):
    exitos = sum(1 for _ in range(n) if random() < p)
    tabla_frecuencia[exitos] += 1

#print(tabla_frecuencia)
tabla_frecuencia = [t / N for t in tabla_frecuencia]
#print(tabla_frecuencia)
ax2.bar(exitos_posibles, tabla_frecuencia)
