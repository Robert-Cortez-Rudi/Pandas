import pandas as pd
import sqlalchemy
from sqlalchemy.engine import create_engine

engine = create_engine("sqlite:///pedidos.db")
# O create_engine() serve para criar um engine. Uma engine é uma conexão com o banco de dados.

df = pd.read_csv("data/Pedidos1.csv")

# 1 - Exportando para tabela

df.to_sql("pedidos", engine, index=False)
