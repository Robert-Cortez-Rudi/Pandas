import pandas as pd

# Caminho para o arquivo Excel

caminho_arquivo = "data/livros.xlsx"
df = pd.read_excel(caminho_arquivo)

print(df)

# 1 - Genero - Quantidade de livros e preço médio por livro

genero_info = df.groupby("Genero").agg({
    "Titulo": "count",
    "Preço": "mean"
})
# O método agg() é utilizado para agregar os dados de acordo com as colunas especificadas
# O count retorna a quantidade de livros por genero
# O mean retorna o preço médio dos livros por genero

print(genero_info)

# 2 - Livro mais caro e mais barato

livro_mais_caro = df[df["Preço"] == df["Preço"].max()]
livro_mais_barato = df[df["Preço"] == df["Preço"].min()]

print(livro_mais_caro)
print(livro_mais_barato)


# 3 - Distribuição de ano de publicação

print(df["Ano"].value_counts())

# 4 - Relação entre preço e quantidade

correlacao = df["Preço"].corr(df["Quantidade"])
print(correlacao)
