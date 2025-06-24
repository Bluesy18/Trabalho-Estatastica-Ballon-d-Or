import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

n = 68
p = float(31/n)
p0 = 0.5

# Estatística de teste (z calculado)
z = (p - p0)/(((p0*(1 - p0))/n)**0.5)

alpha = 0.05

# Valor crítico para teste unilateral (cauda direita)
z_critico = norm.ppf(1 - alpha)

print(f"z calculado: {z:.4f}")
print(f"z crítico (unilateral direita, alpha={alpha}): {z_critico:.4f}")

# p-valor unilateral
p_valor = 1 - norm.cdf(z)
print(f"p-valor unilateral: {p_valor:.4f}")

# Plotando a distribuição
x = np.linspace(-4, 4, 1000)
y = norm.pdf(x, 0, 1)

plt.figure(figsize=(8,5))
plt.plot(x, y, label='Distribuição Normal Padrão')

# Região crítica (só à direita)
plt.fill_between(x, y, where=(x >= z_critico), color='red', alpha=0.3, label='Região de Rejeição (Direita)')

# Linha do z calculado
plt.axvline(z, color='blue', linestyle='--', label=f'z calculado = {z:.2f}')

plt.title('Teste de Proporção - Unilateral Direita (p > 0,5)')
plt.xlabel('z')
plt.ylabel('Densidade de Probabilidade')
plt.legend()

plt.savefig('graficos/teste_proporcao_unilateral.png', dpi=300, bbox_inches='tight')
plt.close()
