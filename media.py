import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

# Valores para o gráfico
df = 25  # graus de liberdade aproximados para o Welch
x = np.linspace(-5, 10, 500)
y = stats.t.pdf(x, df)

# Valor t calculado
t_calculado = 7.7

# Criação do gráfico
plt.figure(figsize=(10, 6))
plt.plot(x, y, label='Distribuição t (df ≈ 25)', color='black')

# Área de rejeição (α = 0.05, teste unilateral)
t_critico = stats.t.ppf(0.95, df)
x_fill = np.linspace(t_critico, 10, 200)
y_fill = stats.t.pdf(x_fill, df)
plt.fill_between(x_fill, y_fill, color='red', alpha=0.3, label='Região de rejeição (α = 0,05)')

# Linha para o valor t calculado
plt.axvline(x=t_calculado, color='blue', linestyle='--', linewidth=2, label='t calculado = 7,7')

# Linha para o valor crítico
plt.axvline(x=t_critico, color='red', linestyle='--', label=f't crítico ≈ {t_critico:.2f}')

# Detalhes do gráfico
plt.title('Distribuição t e valor calculado do teste')
plt.xlabel('t')
plt.ylabel('Densidade de probabilidade')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()