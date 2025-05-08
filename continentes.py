import pandas as pd
import matplotlib.pyplot as plt

# Lendo o arquivo CSV
df = pd.read_csv('ballondor.csv', encoding='utf-8')

# Filtrar dados a partir de 1995
df_from_1995 = df[df['Ano'] >= 1995]

# Mapear nacionalidades para continentes
continent_mapping = {
    # Europa
    'França': 'Europa', 'Alemanha': 'Europa', 'Portugal': 'Europa', 'Espanha': 'Europa',
    'Itália': 'Europa', 'Inglaterra': 'Europa', 'Holanda': 'Europa', 'Ucrânia': 'Europa',
    'Tchéquia': 'Europa', 'Croácia': 'Europa', 'Bulgária': 'Europa', 'Dinamarca': 'Europa',
    # América do Sul
    'Brasil': 'América do Sul', 'Argentina': 'América do Sul',
    # África
    'Libéria': 'África'
}

df_from_1995['Continente'] = df_from_1995['Nacionalidade'].map(continent_mapping)

continent_counts = df_from_1995['Continente'].value_counts().dropna()

colors = ['#FF0000', '#1E90FF', '#32CD32', '#FFD700'][:len(continent_counts)]

plt.figure(figsize=(10, 8))
plt.pie(
    continent_counts,
    labels=continent_counts.index,
    autopct='%1.1f%%',
    startangle=90,
    colors=colors,
    wedgeprops={'width': 1, 'edgecolor': 'white', 'linewidth': 1} 
)

# Título
plt.title('Distribuição por Continente dos Vencedores da Bola de Ouro (1995-2024)', pad=20)

plt.savefig('continentes.png', dpi=300, bbox_inches='tight')
