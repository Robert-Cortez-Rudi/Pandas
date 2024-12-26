import pandas as pd

# Insights:
# 1 - Desempenho de vendas por região
# 2 - Vendedor mais produtivo
# 3 - Total de Unidades vendidas por item
# 4 - Preço médio por item
# 5 - Correlação entre unidade vendida/preço unitário

df = pd.read_csv("data/Pedidos1.csv")

# Convertendo para tipo numerico
df["Unidades"] = pd.to_numeric(df["Unidades"])
df["PrecoUnidade"] = pd.to_numeric(df["PrecoUnidade"])

# 1 - Desempenho de vendas por região

vendas_regiao = df.groupby("Regiao")["Unidades"].sum()

print(vendas_regiao)

# 2 - Vendedor mais produtivo

vendedor_produtivo = df.groupby("Vendedor")["Unidades"].sum().idxmax()

print(vendedor_produtivo)

# 3 - Total de Unidades vendidas por item

produtos_mais_vendidos = df.groupby("Item")["Unidades"].sum()

print(produtos_mais_vendidos)

# 4 - Preço médio por item

preco_medio_por_item = df.groupby("Item")["PrecoUnidade"].mean()

print(preco_medio_por_item)

# 5 - Correlação entre unidade vendida/preço unitário

"""
A correlação pode variar entre -1 e 1, indicando a direção e a 
força da relação linear entre as variáveis.
Um valor próximo de 1 indica uma correlação positiva forte,
enquanto próximo de -1 indica correlação negativa forte.
Um valor próximo a 0 indica uma correlação fraca.
"""

correlacao = df["Unidades"].corr(df["PrecoUnidade"])
# O corr serve para calcular a correlação entre duas variáveis

print(correlacao)

# 6 - Exportando para csv

vendas_regiao = df.groupby("Regiao")["Unidades"].sum()
print(type(vendas_regiao))

# Converter Series para DataFrame

vendas_regiao_df = vendas_regiao.reset_index()
# O reset_index serve para transformar o índice em uma coluna

vendas_regiao_df.columns = ["Região", "TotalUnidadesVendidas"]
# O columns serve para renomear as colunas

print(type(vendas_regiao_df))

vendas_regiao_df.to_csv("data/vendas_regiao.csv", index=False)
# O index=False serve para não salvar o índice do DataFrame
