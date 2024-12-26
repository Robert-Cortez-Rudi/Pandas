import pandas as pd

# 1 - Importando dataset com delimitador ","

df = pd.read_csv("data/Pedidos1.csv")
print(df)

# 2 - Importar com delimitador ";"

# df = pd.read_csv("data/Pedidos2.csv", sep=";")
# print(df)
