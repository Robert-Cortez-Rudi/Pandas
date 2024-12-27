import pandas as pd
from sqlalchemy import create_engine

engine = create_engine("sqlite:///pedidos.db")

# 1 - Total de vendas por região

consulta_1 = "SELECT Regiao, SUM(Unidades) AS Total_unidades_vendidas FROM pedidos GROUP BY Regiao"
resultado_1 = pd.read_sql_query(consulta_1, engine)

print("Total de vendas por região:")
print(resultado_1)

# 2 - Vendedor com maior numero de vendas

consulta_2 = "SELECT Vendedor, SUM(Unidades) AS Total_unidades_vendidas FROM pedidos GROUP BY Vendedor ORDER BY Total_unidades_vendidas DESC LIMIT 1"
# O DESC serve para ordenar os resultados em ordem decrescente
# O LIMIT serve para limitar o numero de resultados

resultado_2 = pd.read_sql_query(consulta_2, engine)

print("Vendedor com maior numero de vendas:")
print(resultado_2)

# 3 - Total de vendas por item

consulta_3 = "SELECT Item, SUM(Unidades) AS Total_unidades_vendidas FROM pedidos GROUP BY Item ORDER BY Total_unidades_vendidas DESC"
resultado_3 = pd.read_sql_query(consulta_3, engine)

print("Total de vendas por item:")
print(resultado_3)

# 4 - Média de preço por item

consulta_4 = "SELECT Item, AVG(PrecoUnidade) AS Media_preco_unidade FROM pedidos GROUP BY Item"
# O AVG() serve para calcular a média
resultado_4 = pd.read_sql_query(consulta_4, engine)

print("Média de preço por item:")
print(resultado_4)
