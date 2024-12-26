"""
Funcionalidades de uma series
1 - Armazenamento de dados unidimensionais - os dados unidimensionais são armazenados em uma série
2 - Utilizado em operações vetorizadas
3 - Focado em dados estruturados
"""

import pandas as pd

# 1 - Dados dos time e suas quantidades de titulos

dados = {
    "Real Madrid": 34,
    "Barcelona": 26,
    "Liverpool": 19,
    "Juventus": 36,
    "Bayern Munich": 30
}

# 2 - Criando uma serie a partir de um dicionario

series_times = pd.Series(dados)

print(series_times)
print(type(series_times))

# 3 - Selecionar time por indice

print(series_times["Liverpool"])
print(series_times.iloc[3])
# o .iloc serve para selecionar pelo indice

# 4 - Selecionando por fatiamento

print("\n")
print(series_times["Barcelona":"Juventus"]) # Fatiamento inclusivo

# 5 - Selecionar por condição

print("\n")
print(series_times[series_times > 30])
