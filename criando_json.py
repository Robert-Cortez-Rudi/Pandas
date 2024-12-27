import json

# 1 - Dados ficticios

dados_series = {
    "series": [
        {
            "Titulo": "Stranger Things",
            "Genero": "Ficção Científica",
            "Ano de Lançamento": 2016,
            "Temporadas": [
                {"numero": 1, "episodios": 8},
                {"numero": 2, "episodios": 9},
                {"numero": 3, "episodios": 8},
                {"numero": 4, "episodios": 9}
            ]
        },
        {
            "Titulo": "La Casa de Papel",
            "Genero": "Ação",
            "Ano de Lançamento": 2017,
            "Temporadas": [
                {"numero": 1, "episodios": 8},
                {"numero": 2, "episodios": 9},
                {"numero": 3, "episodios": 8},
                {"numero": 4, "episodios": 9},
                {"numero": 5, "episodios": 10},
                {"numero": 6, "episodios": 8}
            ]
        }
    ]
}

# 2 - Exportar para arquivo JSON

with open("data/series.json", "w") as arquivo_json:
    json.dump(dados_series, arquivo_json)
    # O dump() serve para exportar os dados para um arquivo JSON

print("Arquivo JSON criado com sucesso!")
