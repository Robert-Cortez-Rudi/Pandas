import pandas as pd

# 1 - Importando dataset com delimitador ","

df = pd.read_csv("data/Pedidos1.csv")
print(df)

# 2 - Importar com delimitador ";"

# df2 = pd.read_csv("data/Pedidos2.csv", sep=";")
# print(df2)

# 3 - Leitura dos primeiros registros

print(df.head())

# 4 - Leitura dos últimos registros

print(df.tail())
# O tail() exibe os últimos registros do dataset

print(df.shape)
# O shape() exibe a quantidade de linhas e colunas do dataset

print(df.dtypes)
# O dtypes() exibe os tipos de dados de cada coluna do dataset

# 5 - Ordenação de valores

print(df.sort_values(by="Unidades", ascending=False))
# O sort_values() ordena os valores de acordo com a coluna informada

# 6 - Estados com mais vendas

print(df["Estado"].value_counts())
# O value_counts() exibe a quantidade de registros de cada valor da coluna
