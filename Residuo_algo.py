import math

# Función para calcular el residuo de la linea estadistica segun una observacion
def residuo(cociente,constante, puntox, puntoy):
    expected = cociente * puntox + constante
    return puntoy - expected


x = 85.0
y = 79

cociente = 0.59
constante = 41

print(residuo(cociente, constante, x, y))