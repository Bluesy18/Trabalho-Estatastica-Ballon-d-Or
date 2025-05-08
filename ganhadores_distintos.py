import pandas as pd
import matplotlib.pyplot as plt

# Lendo o arquivo CSV
df = pd.read_csv('ballondor.csv', encoding='utf-8')

df['Década'] = (df['Ano'] // 10) * 10

vencedores_por_decada = df.groupby('Década')['Jogador'].nunique()

# Configurar o gráfico de barras
plt.figure(figsize=(12, 6))
bars = plt.bar(
    vencedores_por_decada.index.astype(str) + 's',  
    vencedores_por_decada.values,
    color='#1E90FF', 
    edgecolor='black',
    linewidth=1
)

plt.title('Número de Vencedores Distintos da Bola de Ouro por Década', pad=20, fontsize=14)
plt.xlabel('Década', fontsize=12)
plt.ylabel('Número de Vencedores', fontsize=12)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.ylim(0, vencedores_por_decada.max() + 1)

plt.savefig('ganhadores_distintos.png', dpi=300, bbox_inches='tight')

