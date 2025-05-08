import pandas as pd
import matplotlib.pyplot as plt

# Lendo o arquivo CSV
df = pd.read_csv('ballondor.csv', encoding='utf-8')

# Contando a frequência de cada etnia
etnia_counts = df['Etnia'].value_counts()

plt.figure(figsize=(8, 8))
plt.pie(etnia_counts, 
        labels=etnia_counts.index, 
        autopct='%1.1f%%', 
        startangle=140, 
        colors=['#FF0000', '#1E90FF', '#32CD32', '#FFD700', '#9370DB'],
        wedgeprops={'width': 1, 'edgecolor': 'white', 'linewidth': 1}
)

# Adicionando título
plt.title('Distribuição de Etnias dos Vencedores da Bola de Ouro (1956-2024)', pad=20)

plt.savefig('etnia.png', dpi=300, bbox_inches='tight')
