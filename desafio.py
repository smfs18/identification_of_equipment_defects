import pandas as pd #Pandas, biblioteca de análise de dados.
import numpy as np
from sklearn.preprocessing import StandardScaler #Biblioteca para fazer o pré processamento.
from sklearn.decomposition import PCA #Biblioteca de Análise de Componentes Princiais
from sklearn.covariance import MinCovDet #Biblioteca de co variância
import matplotlib.pyplot as plt #Biblioteca de Gráficos

# Carregar os dados
df = pd.read_excel('identification_of_equipment_defects/Failing_Equipment_Exercise.xlsx', index_col=0)

# Transpor para ter equipamentos como observações e bandas como features
data = df.T

# 1. Normalização dos dados, serve para padronizar)
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)

# 2. Aplicar PCA - Reduz a dimensalidade de um conjunto de variáveis correlacionadas em um conjunto menor de variáveis não correlacionadas
pca = PCA(n_components=2)
principal_components = pca.fit_transform(data_scaled)
pca_df = pd.DataFrame(data=principal_components, 
                      columns=['PC1', 'PC2'], 
                      index=data.index)

# 3. Calcular distâncias de Mahalanobis para detecção de outliers (São pontos que se desviam significamente da ditribuição normal dos dados)
robust_cov = MinCovDet().fit(principal_components)
pca_df['mahalanobis'] = robust_cov.mahalanobis(principal_components)

# 4. Visualização
plt.figure(figsize=(10, 6))
scatter = plt.scatter(pca_df['PC1'], pca_df['PC2'], 
                      c=pca_df['mahalanobis'], 
                      s=100, cmap='viridis')

for i, txt in enumerate(pca_df.index):
    plt.annotate(txt, (pca_df['PC1'][i], pca_df['PC2'][i]), 
                 textcoords="offset points", xytext=(0,10), ha='center')

plt.colorbar(scatter, label='Distância de Mahalanobis')
plt.xlabel('Primeiro Componente Principal (%.2f%%)' % (pca.explained_variance_ratio_[0]*100))
plt.ylabel('Segundo Componente Principal (%.2f%%)' % (pca.explained_variance_ratio_[1]*100))
plt.title('PCA de Equipamentos com Métrica de Mahalanobis')
plt.grid()
plt.show()

# Exibir resultados
print("Variância explicada por cada componente:", pca.explained_variance_ratio_)
print("\nDistâncias de Mahalanobis:")
print(pca_df['mahalanobis'])