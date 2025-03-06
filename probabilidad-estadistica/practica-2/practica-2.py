total_personas = 755
info = [[25, 280], [45, 405]]
# A. Probablidad de que sí use un celular al manejar
A = sum(info[0]) / total_personas
print(f"Problema A: {A}")

# B. Probablidad de que no tenga infracción
B = (info[0][1] + info[1][1]) / total_personas
print(f"Problema B: {B}")

# C. Probablidad de que no tenga infracción y que si use celular al manejar
C = info[0][1] / total_personas
print(f"Problema C: {C}")

# D. Probablidad de que no tenga una infracción o que sí use el celular
# Regla de la unión: P(A | B) = P(A) + P(B) - P(A & B)
D = A + B - C
print(f"Problema D: {D}")

"""Probabilidad Condicional
Intuitivamente se refiere a la probabilidad de que ocurra un evento B, dado que ocurrió un evento A
P(B/A) = P(A & B) / P(A)
"""

# E. Probabilidad que sí use el celular dado que sí tiene una infracción (sugerencia: ocupar probablidad condicional)
# P(sí celular / sí infracción) = P(sí celular & sí infracción) / P(sí infracción)
#                               = ((sí celular & sí infracción) / total_personas) / (sí infracción / total_personas)
#                               = ((sí celular & sí infracción) * total_personas) / (sí infracción * total_personas)
#                               = (sí celular & sí infracción)  / (sí infracción)
E = info[0][0] / (info[0][0] + info[1][0])
print(f"Problema E: {E}")

# F. Probabilidad que no tenga una infracción dado que no usa el celular (sugerencia: ocupar probablidad condicional)
# P(no infracción / no celular) = P(no infracción & no celular) / P(no celular)
#                               = (no infracción & no celular)  / (no celular)
F = info[1][1] / sum(info[1])
print(f"Problema F: {F}")
