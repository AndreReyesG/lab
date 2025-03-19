nuevo_mensaje = "free cable tv today"
#nuevo_mensaje = "request energy price data"
#nuevo_mensaje = "free cable tv today califragilisticoespialidoso"
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

    for mensaje in mensajes:
        if mensaje[0] == "spam":
            total_spam += 1
        else:
            total_ham += 1

    probabilidad_spam = total_spam / total_mensajes
    probabilidad_ham = total_ham / total_mensajes
    
    # [Palabra, contador spam, contador ham]
    palabras = [[i, 0, 0] for i in nuevo_mensaje.split()]

    # [P(palabra|spam), P(palabra|ham)]
    probabilidad_palabras = []

    for palabra in palabras:
        for mensaje in mensajes:
            if palabra[0] in mensaje[1]:
                if mensaje[0] == "spam":
                    palabra[1] += 1
                else:
                    palabra[2] += 1
        probabilidad_palabras.append([palabra[1] / total_spam, palabra[2] / total_ham])

    print(f"Palabras con contador de spam y ham: {palabras}")
    print(f"Probabilidad de palabras que sean SPAM o HAM: {probabilidad_palabras}")

    probabilidad_total_spam = probabilidad_spam
    probabilidad_total_ham = probabilidad_ham

    for i in probabilidad_palabras:
        probabilidad_total_spam *= i[0]
        probabilidad_total_ham *= i[1]

    print(f"Probabilidad que sea SPAM: {probabilidad_total_spam}")
    print(f"Probabilidad que sea HAM: {probabilidad_total_ham}")

    if probabilidad_total_spam > probabilidad_total_ham:
        print(f"Mensaje '{nuevo_mensaje}' catalogado como SPAM")
    else:
        print(f"Mensaje '{nuevo_mensaje}' catalogado HAM")
