import pandas as pd
import matplotlib.pyplot as plt

# Carregar o arquivo CSV
df = pd.read_csv('ballondor.csv', delimiter=',')

# Dicionário para padronizar nomes de títulos
padroes_titulos = {
    'Champions League': 'Champions League',
    'UEFA Champions League': 'Champions League',
    'European Cup': 'Champions League',
    'Copa do Mundo': 'Copa do Mundo',
    'Mundial': 'Copa do Mundo',
    'La Liga': 'La Liga',
    'Eurocopa': 'Eurocopa',
}

# Extrair e padronizar títulos
titulos = []
for index, row in df.iterrows():
    for col in ['Titulos', 'Unnamed: 10', 'Unnamed: 11']:
        titulo = str(row.get(col, '')).strip()
        if titulo and titulo != 'nan':
            titulo_padronizado = padroes_titulos.get(titulo, titulo)
            titulos.append(titulo_padronizado)

# Contar títulos e remover duplicidades
contagem_titulos = pd.Series(titulos).value_counts()
contagem_titulos = contagem_titulos[~contagem_titulos.index.isin(['', '0', 'nan'])]
contagem_titulos = contagem_titulos.sort_values(ascending=False)

plt.figure(figsize=(12, 6))
bars = plt.bar(contagem_titulos.index, contagem_titulos, edgecolor='black')
plt.title('Títulos Vencidos pelos Ganhadores do Ballon d\'Or (1956-2024)', fontsize=14)
plt.xlabel('Título', fontsize=12)
plt.ylabel('Quantidade', fontsize=12)
plt.xticks(rotation=45, ha='right')
plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.savefig('titulos.png', dpi=300, bbox_inches='tight')

