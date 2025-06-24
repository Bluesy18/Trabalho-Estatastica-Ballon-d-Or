import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

n = 68
p = float(31/n)
p0 = 0.5

z = (p - p0)/(((p0*(1 - p0))/n)**0.5)

# Exemplo: z calculado
alpha = 0.05

# Valores para x
x = np.linspace(-4, 4, 1000)
y = norm.pdf(x, 0, 1)

plt.figure(figsize=(8,5))
plt.plot(x, y, label='Distribuição Normal Padrão')

# Região crítica (para teste bicaudal)
z_critico = norm.ppf(1 - alpha/2)

plt.fill_between(x, y, where=(x <= -z_critico), color='red', alpha=0.3, label='Região de Rejeição (Esquerda)')
plt.fill_between(x, y, where=(x >= z_critico), color='red', alpha=0.3, label='Região de Rejeição (Direita)')

# Marcando o z calculado
plt.axvline(z, color='blue', linestyle='--', label=f'z calculado = {z:.2f}')

plt.title('Distribuição Normal Padrão - Teste de Proporção')
plt.xlabel('z')
plt.ylabel('Densidade de Probabilidade')
plt.legend()

# Salva a figura em um arquivo sem mostrar na saída
plt.savefig('graficos/teste_proporcao.png', dpi=300, bbox_inches='tight')
plt.close()  # Fecha a figura para liberar memória