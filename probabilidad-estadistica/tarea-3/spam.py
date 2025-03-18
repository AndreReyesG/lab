nuevo_mensaje = "free cable today"
mensajes = []

with open("enron_spam_filtrado.csv", mode="r", encoding="utf-8") as archivo:
    lineas = archivo.readlines()
    for i in range(1, len(lineas)):
        linea = lineas[i]
        columnas = linea.split(",")
        tipo_mensaje = columnas[0]
        mensaje = columnas[1]
        mensajes.append([tipo_mensaje, mensaje])

    total_mensajes = len(mensajes)
    total_spam = 0
    total_ham = 0

    for i in range(total_mensajes):
        if mensajes[i][0] == "spam":
            total_spam += 1
        else:
            total_ham += 1

    probabilidad_spam = total_spam / total_mensajes
    probabilidad_ham = total_ham / total_mensajes
    
    # [Palabra, contador spam, contador ham]
    palabras = [[i, 0, 0] for i in nuevo_mensaje.split()]
    
    for i in range(len(mensajes)):
        if mensajes[i][0] == "spam":
            tipo_mensaje = 1
        else:
            tipo_mensaje = 2

        for palabra in mensajes[i][1].split():
            for j in range(len(palabras)):
                if palabras[j][0] == palabra:
                    palabras[j][tipo_mensaje] += 1

    print(f"Palabras: {palabras}")

    # [P(palabra|spam), P(palabra|ham)]
    probabilidades_palabras = [[palabra[1] / total_spam, palabra[2] / total_ham] for palabra in palabras]

    print(f"Probabilidad palabras: {probabilidades_palabras}")

    probabilidad_total_spam = probabilidad_spam
    probabilidad_total_ham = probabilidad_ham

    for i in probabilidades_palabras:
        probabilidad_total_spam *= i[0]
        probabilidad_total_ham *= i[1]

    if probabilidad_total_spam > probabilidad_total_ham:
        print(f"Mensaje '{nuevo_mensaje}' catalogado como SPAM")
    else:
        print(f"Mensaje '{nuevo_mensaje}' catalogado como mensaje normal")
