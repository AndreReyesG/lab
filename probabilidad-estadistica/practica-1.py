from random import randint

total_experimentos = 1000000
contador_evento = 0

examen = [randint(1, 3) for i in range(10)]

for i in range(total_experimentos):
    calificacion = 0

    for respuesta in examen:
        if (randint(1, 3) == respuesta):
            calificacion = calificacion + 1

    if calificacion == 6:
        contador_evento = contador_evento + 1

print(contador_evento / total_experimentos)
