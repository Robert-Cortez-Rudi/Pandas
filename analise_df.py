import pandas as pd

dados_titulos = {
    "Real Madrid": 34,
    "Barcelona": 26,
    "Liverpool": 19,
    "Juventus": 36,
    "Bayern Munich": 30
}

dados_anos = {
    "Real Madrid": [1956, 1957, 1958, 1959, 1960],
    "Barcelona": [1992, 2006, 2009, 2011, 2015],
    "Liverpool": [1977, 1978, 1981, 1984, 2005],
    "Juventus": [1958, 1985, 1996, 2011, 2015],
    "Bayern Munich": [1974, 1975, 1976, 2001, 2013]
}

series_titulos = pd.Series(dados_titulos)
series_anos = pd.Series(dados_anos)

print(series_titulos)
print(series_anos)

data = {
    "Títulos": series_titulos,
    "Anos": series_anos
}

df = pd.DataFrame(data)

# 1 - Média de Titulos

media_titulos = df["Títulos"].mean()
# O mean() é um método que calcula a média dos valores de uma coluna de um DataFrame.
print(f"A média de titulos: {media_titulos}")

# 2 - Time com mais Titulos

mais_titulos = df["Títulos"].idxmax()
# O idxmax() é um método que retorna o índice do valor máximo de uma coluna de um DataFrame.

qtd_titulos = df["Títulos"].max()
# O max() é um método que retorna o valor máximo de uma coluna de um DataFrame.

print(f"O time com mais titulos: {mais_titulos} com {qtd_titulos} titulos")

# 3 - Ano com mais Titulos

todos_anos = df["Anos"].explode()
# O explode() é um método que retorna um DataFrame com uma coluna para cada valor de uma coluna de um DataFrame.

ano_mais_titulos = todos_anos.mode()[0]
# O mode() é um método que retorna o valor mais frequente de uma coluna de um DataFrame. O [0] é para pegar o primeiro valor, caso tenha mais de um valor mais frequente.

print(f"O ano com mais titulos: {ano_mais_titulos}")
