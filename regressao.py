import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler
from statsmodels.stats.outliers_influence import variance_inflation_factor
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import classification_report, confusion_matrix, roc_curve, auc
import os
import warnings
from scipy.stats import shapiro

# Configurações
warnings.filterwarnings("ignore")
plt.style.use('seaborn-v0_8')
os.makedirs('graficos', exist_ok=True)  # Pasta para salvar gráficos

# ======================
# 1. CARREGAR E PREPARAR OS DADOS
# ======================
df = pd.read_csv('modelo.csv')
df = df[['gols', 'assistencias', 'jogos', 'total_titulos', 'gols_por_partida', 'g_a_total', 'ganhou']].dropna()

# Definir variáveis
X = df[['gols', 'assistencias', 'jogos', 'total_titulos']]
y_linear1 = df['gols_por_partida']
y_linear2 = df['g_a_total']
y_logistic = df['ganhou']

# Padronizar
scaler = StandardScaler()
X_scaled = pd.DataFrame(scaler.fit_transform(X), columns=X.columns)
X_scaled = sm.add_constant(X_scaled)

# ======================
# 2. FUNÇÃO PARA REGRESSÃO LINEAR + GRÁFICOS
# ======================
def run_linear_regression(X, y, target_name):
    print(f"\n{'='*50}\n **REGRESSÃO LINEAR: {target_name.upper()}**\n{'='*50}")
    
    # Modelo
    model = sm.OLS(y, X).fit()
    print(model.summary())
    
    # VIF
    vif_data = pd.DataFrame()
    vif_data["Variável"] = X.columns
    vif_data["VIF"] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
    print("\n Fator de Inflação de Variância (VIF):")
    print(vif_data)
    
    # Gráfico de Resíduos
    plt.figure(figsize=(10, 5))
    sns.residplot(x=model.predict(), y=model.resid, lowess=True, line_kws={'color': 'red'})
    plt.title(f'Resíduos vs Ajustados - {target_name}', fontsize=14)
    plt.savefig(f'graficos/residuos_{target_name}.png', dpi=300)
    plt.close()
    
    # Histograma de Resíduos
    plt.figure(figsize=(10, 5))
    sns.histplot(model.resid, kde=True, bins=30)
    plt.title(f'Distribuição dos Resíduos - {target_name}', fontsize=14)
    plt.savefig(f'graficos/hist_residuos_{target_name}.png', dpi=300)
    plt.close()

    stat, p = shapiro(model.resid)
    print(f"\nShapiro-Wilk p-value: {p}")

# ======================
# 3. REGRESSÃO LOGÍSTICA + GRÁFICOS
# ======================
print(f"\n{'='*50}\n **REGRESSÃO LOGÍSTICA: GANHOU**\n{'='*50}")
logit_model = sm.Logit(y_logistic, X_scaled).fit(maxiter=100)
print(logit_model.summary())

# Métricas
y_pred = (logit_model.predict(X_scaled) > 0.5).astype(int)
print("\n Relatório de Classificação:")
print(classification_report(y_logistic, y_pred))

# ======================
# 4. RODAR AS REGRESSÕES LINEARES
# ======================
# Incluindo constante nos X para regressão linear
X_linear = sm.add_constant(X_scaled.drop('const', axis=1))

run_linear_regression(X_linear, y_linear1, 'log_gols_por_partida')

run_linear_regression(X_linear, y_linear2, 'log_g_a_total')

# Matriz de Confusão
plt.figure(figsize=(6, 4))
sns.heatmap(confusion_matrix(y_logistic, y_pred), 
            annot=True, fmt='d', cmap='Blues',
            xticklabels=['Não Ganhou', 'Ganhou'], 
            yticklabels=['Não Ganhou', 'Ganhou'])
plt.title('Matriz de Confusão', fontsize=14)
plt.savefig('graficos/matriz_confusao.png', dpi=300)
plt.close()

# Curva ROC
fpr, tpr, _ = roc_curve(y_logistic, logit_model.predict(X_scaled))
roc_auc = auc(fpr, tpr)
plt.figure(figsize=(8, 6))
plt.plot(fpr, tpr, color='darkorange', lw=2, label=f'AUC = {roc_auc:.2f}')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Curva ROC', fontsize=14)
plt.legend(loc="lower right")
plt.savefig('graficos/curva_roc.png', dpi=300)
plt.close()

# Odds Ratios
odds_ratios = np.exp(logit_model.params).drop('const')
plt.figure(figsize=(10, 5))
odds_ratios.sort_values().plot(kind='barh', color='skyblue')
plt.axvline(x=1, color='red', linestyle='--')
plt.title('Impacto das Variáveis (Odds Ratios)', fontsize=14)
plt.savefig('graficos/odds_ratios.png', dpi=300)
plt.close()

novo_jogador = {
    'gols': 24,
    'assistencias': 11,
    'jogos': 39,
    'total_titulos': 3
}

# Converter o novo jogador em DataFrame
X_novo = pd.DataFrame([novo_jogador])

# Padronizar com o mesmo scaler usado no treino
X_novo_scaled = pd.DataFrame(scaler.transform(X_novo), columns=X_novo.columns)

# Adicionar a constante
X_novo_scaled = sm.add_constant(X_novo_scaled, has_constant='add')

# Fazer a previsão da probabilidade
probabilidade = logit_model.predict(X_novo_scaled)[0]

print(f"Probabilidade de ganhar a Bola de Ouro: {probabilidade:.4f}")

