import math

def densidad_general(mu, sigma, muestra, inferior, superior):

    z_inferior = (inferior - mu) / (sigma / math.sqrt(muestra))
    z_superior = (superior - mu) / (sigma / math.sqrt(muestra))

    p_inferior = 0.5 * (1 + math.erf(z_inferior / math.sqrt(2)))
    p_superior = 0.5 * (1 + math.erf(z_superior / math.sqrt(2)))

    probabilidad = p_superior - p_inferior

    return probabilidad

mu = 100  # media de la poblacion
sigma = 15  # desviacion estandar de la poblacion
muestra = 64  # tamaño de la muestra
inferior = 97  # limite inferior
superior = 103  # limite superior

probabilidad = densidad_general(mu, sigma, muestra, inferior, superior)

print(f"Probabilidad de que la media muestral esté entre {inferior} y {superior}: {probabilidad:.4f}")