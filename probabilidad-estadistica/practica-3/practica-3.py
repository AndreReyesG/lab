from random import randint
import matplotlib.pyplot as plt

N = 10000

tabla = [0, 0, 0, 0, 0, 0]

for i in range(N):
    idx = randint(1, 6)
    tabla[idx - 1] += 1

tabla = [(i / N) for i in tabla]

plt.bar([1,2,3,4,5,6], [i for i in tabla])
