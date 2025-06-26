import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# Dados fornecidos
titulos = [0,1,1,2,1,1,0,0,0,1,1,0,1,1,1,2,1,1,0,1,1,0,0,0,0,1,1,0,1,1,0,0,1,1,1,0,1,1,1,0,2,1,1,1,0,3,1,1,1,1,1,1,2,2,1,2,1,0,1,2,2,2,1,1,1,2,1,2]
g_a = [3,41,25,42,26,38,18,0,61,58,30,36,47,27,61,53,18,40,32,33,13,33,27,25,40,39,25,28,35,30,23,25,43,44,25,44,39,42,34,26,11,59,25,44,29,32,28,29,37,31,5,30,54,56,62,78,103,70,66,78,66,54,15,73,58,59,48,23]

# Configurações do gráfico
plt.figure(figsize=(10, 6))
plt.style.use('seaborn-v0_8-whitegrid')

# Gráfico de dispersão
scatter = plt.scatter(titulos, g_a, c=titulos, cmap='viridis', alpha=0.7, s=50, edgecolors='w', linewidth=0.5)

# Linha de tendência
z = np.polyfit(titulos, g_a, 1)
p = np.poly1d(z)
plt.plot(titulos, p(titulos), "r--", linewidth=2)

# Estatísticas no gráfico
slope, intercept, r_value, p_value, std_err = stats.linregress(titulos, g_a)
plt.text(2.5, 95, f'y = {slope:.1f}x + {intercept:.1f}\n'
         f'r = {r_value:.2f} (p = {p_value:.3f})\n'
         f'R² = {r_value**2:.2f}', 
         bbox=dict(facecolor='white', alpha=0.8))

# Personalização
plt.title('Correlação entre Títulos e Gols+Assistências (G/A)\nVencedores do Ballon d\'Or', pad=20)
plt.xlabel('Número de Títulos', labelpad=10)
plt.ylabel('Gols + Assistências (G/A)', labelpad=10)
plt.colorbar(scatter, label='Nível de Títulos')
plt.xticks([0,1,2,3])
plt.ylim(0, 110)

# Destacar pontos extremos
max_idx = np.argmax(g_a)
plt.annotate(f'{g_a[max_idx]} G/A', 
             xy=(titulos[max_idx], g_a[max_idx]), 
             xytext=(titulos[max_idx]-0.5, g_a[max_idx]+3.75),
             arrowprops=dict(arrowstyle='->'))

plt.tight_layout()
plt.show()