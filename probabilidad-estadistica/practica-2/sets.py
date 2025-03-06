'''Implementación con "set"
Se ha hecho una encuesta a 755 personas sobre sus hábitos de conducción del último año
'''

conjunto_si_celular = {25, 280}     # Sí usa el celular al manejar
conjunto_no_celular = {45, 405}     # No usa el celular al manejar
conjunto_si_infraccion = {25, 45}   # Sí tiene infracción
conjunto_no_infraccion = {280, 405} # No tiene infracción

total_personas = 755

# A. Probablidad de que sí use un celular al manejar
A = sum(conjunto_si_celular) / total_personas
print(f"Problema A: {A}")

# B. Probablidad de que no tenga infracción
B = sum(conjunto_no_infraccion) / total_personas
print(f"Problema B: {B}")

# C. Probablidad de que no tenga infracción y que si use celular al manejar
C = sum(conjunto_no_infraccion & conjunto_si_celular) / total_personas
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
E = sum(conjunto_si_infraccion & conjunto_si_celular) / sum(conjunto_si_infraccion)
print(f"Problema E: {E}")

# F. Probabilidad que no tenga una infracción dado que no usa el celular (sugerencia: ocupar probablidad condicional)
# P(no infracción / no celular) = P(no infracción & no celular) / P(no celular)
#                               = (no infracción & no celular)  / (no celular)
F = sum(conjunto_no_celular & conjunto_no_infraccion) / sum(conjunto_no_celular)
print(f"Problema F: {F}")
