import pandas as pd

# Caminho para o arquivo Excel

caminho_arquivo = "data/livros.xlsx"

df = pd.read_excel(caminho_arquivo)

print(df)

# 1 - Visão geral dos dados

print(df.head())
print(df.tail())

# 2 - Verificando os tipos de dados

print(df.dtypes)

# 3 - Estatisticas descritivas

print(df.describe())

print(df[["Preço", "Quantidade"]].describe())
