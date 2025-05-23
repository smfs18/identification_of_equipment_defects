# Desafio 05 - Equipamento Defeituoso

## 📋 Descrição do Problema

A planilha apresenta 4 equipamentos (denominados “Object 1” a “Object 4”) e valores de sensores (denominados “Band 1” a “Band 17”). O objetivo do desafio é identificar qual dos equipamentos está com defeito com base nos resultados apresentados. 

A grande dificuldade está na vastidão de informações, o que torna difícil tomar uma decisão concreta apenas pela observação direta dos dados.

---

## 🧪 Abordagem Adotada

### 1. Análise Exploratória de Dados (EDA)

Inicialmente, verifiquei os dados para identificar algum padrão, ou até mesmo semelhanças. Calculei a média de cada sensor e verifiquei quais equipamentos estavam abaixo da média. Dois equipamentos apresentaram o mesmo comportamento, então comparei os dois e identifiquei aquele com menor valor médio dos sensores.

> Pela minha análise inicial, o **Object 2** seria o equipamento defeituoso. No entanto, esse método era superficial, então fui em busca de uma abordagem mais robusta.

---

### 2. Tecnologia Utilizada: Detecção de Anomalias

Descobri a técnica de **detecção de anomalias**, baseada na suposição de que equipamentos saudáveis apresentam comportamentos semelhantes, enquanto um equipamento com defeito possui valores que se desviam significativamente dos demais.

---

### 3. Técnica Aplicada: Análise de Distância e PCA

Para representar os dados de forma que os padrões anômalos se destacassem, utilizei:

- **PCA** (Análise de Componentes Principais), para redução de dimensionalidade;
- **Distância de Mahalanobis**, para identificação de padrões fora do comum (outliers).

---

## ⚙️ Como a Técnica Foi Aplicada

1. Transpus os dados para obter um vetor de leitura por equipamento.
2. Padronizei os dados com z-score.
3. Apliquei PCA para reduzir a dimensão dos dados para duas componentes principais.
4. Calculei a **distância de Mahalanobis** entre os equipamentos no espaço PCA.
5. O equipamento com **maior distância média em relação aos demais** foi classificado como defeituoso.

---

## 📚 Justificativa das Técnicas

### 🔹 PCA - Análise de Padrões Comportamentais

- Compacta informações e descarta redundâncias.
- Agrupa medidas parecidas.
- Permite visualizar os dados em 2D ou 3D sem perder a estrutura essencial.
- Matematicamente, encontra autovetores da matriz de covariância dos dados, que representam as direções de maior variância.

### 🔹 Outliers

- Pontos que se desviam significativamente da distribuição normal dos dados.
- No espaço PCA, aparecem distantes do aglomerado principal.

### 🔹 Distância de Mahalanobis

- Mede o quão distante um ponto está da média do grupo, considerando dispersão e correlação entre variáveis.
- Ideal para detectar outliers com variância diferente em múltiplas dimensões.

---

### 📌 Diferenças entre Distância Mahalanobis e Euclidiana

| Característica              | Mahalanobis                      | Euclidiana                        |
|----------------------------|----------------------------------|----------------------------------|
| Considera escala           | Sim                              | Não                              |
| Considera correlação       | Sim                              | Não                              |
| Tipo de distância          | Desvio padrão                    | Linha reta                       |
| Ideal para                 | Dados com variância diferente    | Dados normalizados               |

> **Curiosidade**: A distância Mahalanobis foi criada por **Prasanta Chandra Mahalanobis** em 1936 para estudar crânios humanos.

---

## ✅ Conclusão

Com base na análise PCA combinada com a métrica de distância de Mahalanobis, o **equipamento 2 (Object 2)** foi identificado como o que apresenta comportamento anômalo em relação aos demais.

Isso indica que o Object 2 está **potencialmente com defeito**, apresentando padrões de leitura de sensores significativamente diferentes dos outros equipamentos operando normalmente.

---

## 🛠 Tecnologias

- Python 3
- Pandas
- NumPy
- scikit-learn
- matplotlib

## ▶️ Como Executar

```bash
Linux e macOS: source venv/bin/activate                           # Ativar a venv Linux e Mac.
Windows: .venv\Scripts\activate                                    # Ativar a venv Windows.   
pip install pandas numpy scikit-learn matplotlib openpyxl         # Instala as dependências.
Executar.
