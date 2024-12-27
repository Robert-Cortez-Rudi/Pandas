import pandas as pd

# 1 - Importando o arquivo JSON

df = pd.read_json("data/series.json")

# 2 - Analise total de episodios por serie

temporadas_expandidas = []

for serie in df["series"]:
    total_episodios = sum(temporada["episodios"] for temporada in serie["Temporadas"])
    serie_info = {
        "titulo": serie["Titulo"],
        "genero": serie["Genero"],
        "total_episodios": total_episodios
    }
    temporadas_expandidas.append(serie_info)

# print(temporadas_expandidas)

df_expandido = pd.DataFrame(temporadas_expandidas)

print(df_expandido)
