import pandas as pd
import matplotlib.pyplot as plt

# Lendo o arquivo CSV
df = pd.read_csv('ballondor.csv', encoding='utf-8')

# Contar a frequência de cada posição (com repetições)
posicao_counts = df['Posição'].value_counts()

cores = ['#FF0000', '#1E90FF', '#32CD32', '#FFD700']

# Criar o gráfico de pizza
plt.figure(figsize=(10, 8))
plt.pie(
    posicao_counts,
    labels=posicao_counts.index,
    autopct='%1.1f%%',
    startangle=90,
    colors=cores,
    wedgeprops={'edgecolor': 'white', 'linewidth': 1},
    textprops={'fontsize': 12}
)

# Adicionar título
plt.title('Distribuição das Posições dos Vencedores da Bola de Ouro (1956-2024)\n(Contando todas as ocorrências)', 
          pad=20, fontsize=14)

plt.savefig('posicoes.png', dpi=300, bbox_inches='tight')

