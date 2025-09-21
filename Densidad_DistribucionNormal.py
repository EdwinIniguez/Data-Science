# Cálculo de la probabilidad de que un hombre mida más de 1.85m
from scipy.stats import norm

mu_altura = 1.75  # media en metros
sigma_altura = 0.1  # desviación estándar en metros
x_val = 1.85  # altura a evaluar

# Calcular el z-score
z = (x_val - mu_altura) / sigma_altura
print(f"z-score para {x_val} m: {z:.2f}")

# Probabilidad de que mida más de 1.85m
prob_mayor_185 = 1 - norm.cdf(x_val, loc=mu_altura, scale=sigma_altura)
print(f"Probabilidad de que un hombre mida más de {x_val} m: {prob_mayor_185:.4f}")

# Ejemplo: Probabilidad de que la estatura esté entre 1.70m y 1.85m
x1 = 1.70  # límite inferior
x2 = 1.85  # límite superior

# Calcular z-scores
z1 = (x1 - mu_altura) / sigma_altura
z2 = (x2 - mu_altura) / sigma_altura
print(f"z-score para {x1} m: {z1:.2f}")
print(f"z-score para {x2} m: {z2:.2f}")

# Probabilidad acumulada para cada z-score
prob_x1 = norm.cdf(x1, loc=mu_altura, scale=sigma_altura)
prob_x2 = norm.cdf(x2, loc=mu_altura, scale=sigma_altura)

# Probabilidad de estar entre x1 y x2
prob_entre = prob_x2 - prob_x1
print(f"Probabilidad de que la estatura esté entre {x1} m y {x2} m: {prob_entre:.4f}")

import numpy as np
import matplotlib.pyplot as plt

# Parámetros de la distribución normal
mu = 0      # media
sigma = 1   # desviación estándar

# Valores de x
x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)

# Función de densidad de probabilidad (PDF)
def normal_pdf(x, mu, sigma):
	return (1/(sigma * np.sqrt(2 * np.pi))) * np.exp(-((x - mu)**2) / (2 * sigma**2))

y = normal_pdf(x, mu, sigma)

# Graficar la PDF
plt.plot(x, y, label=f'N({mu}, {sigma}²)')
plt.title('Función de Densidad de Probabilidad - Distribución Normal')
plt.xlabel('x')
plt.ylabel('Densidad de probabilidad')
plt.legend()
plt.grid(True)
plt.show()
