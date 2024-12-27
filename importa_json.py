import pandas as pd

# 1 - Importando o arquivo JSON

df = pd.read_json("data/series.json")

print(df)

# 2 - Utilizando o json_normalize para aplanar dados alinhados

df_series = pd.json_normalize(
    df["series"],
    "Temporadas",
    ["Titulo", "Genero", "Ano de Lançamento"]
)
# O json_normalize() serve para aplanar os dados alinhados
# O primeiro argumento diz que quero aplanar a coluna temporadas. Aplanar significa transformar em colunas
# O segundo argumento diz que quero aplanar a coluna temporadas
# O terceiro argumento diz que quero aplanar a coluna Titulo, Genero e Ano de Lançamento

print(df_series)
