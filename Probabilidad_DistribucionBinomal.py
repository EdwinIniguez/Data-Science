# Cálculo de la probabilidad de obtener exactamente 7 caras en 10 lanzamientos de una moneda imparcial
import math

def probabilidad_binomial(n, k, p):
	"""
	Calcula la probabilidad de obtener exactamente k éxitos en n ensayos
	con probabilidad p de éxito en cada ensayo (distribución binomial).
	"""
	combinaciones = math.comb(n, k)
	prob = combinaciones * (p ** k) * ((1 - p) ** (n - k))
	return prob

if __name__ == "__main__":
	n = 20  # número de lanzamientos
	k = 17   # número de caras deseadas
	p = 0.75 # probabilidad de cara en cada lanzamiento
	resultado = probabilidad_binomial(n, k, p)
	print(f"La probabilidad de obtener exactamente {k} en {n} es: {resultado:.4f}")
