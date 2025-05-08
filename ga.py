import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Lendo o arquivo CSV
df = pd.read_csv('ballondor.csv', encoding='utf-8')

if df['G/A'].dtype == object:
    df['G/A'] = df['G/A'].str.replace(',', '.').astype(float)
else:
    df['G/A'] = df['G/A'].astype(float)

# Criando o boxplot
plt.figure(figsize=(12, 8))
ax = sns.boxplot(x=df['G/A'], whis=1.5)

# Identificando outliers
q1 = df['G/A'].quantile(0.25)
q3 = df['G/A'].quantile(0.75)
iqr = q3 - q1
lower_bound = q1 - (1.5 * iqr)
upper_bound = q3 + (1.5 * iqr)

outliers = df[(df['G/A'] < lower_bound) | (df['G/A'] > upper_bound)]

# Adicionando anotações para os outliers
for _, row in outliers.iterrows():
    ax.text(row['G/A'], 0, f"{int(row['Ano'])}", 
            ha='center', va='center', fontweight='bold', 
            bbox=dict(facecolor='yellow', alpha=0.5))

# Configurações do gráfico
plt.title('Distribuição de Gols + Assistências (G/A) dos Vencedores da Bola de Ouro (1956-2024)', pad=20)
plt.xlabel('Gols + Assistências (G/A)')
plt.yticks([])  

plt.savefig('ga.png', dpi=300, bbox_inches='tight')


