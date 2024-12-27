import pandas as pd

# 1 - Dados ficticios (Livros)

dados = {
    "Titulo": ["It a coisa", "Outsider", "Misery", "O Instituto", "Bazar dos sonhos ruins"],
    "Autor": ["Stephen King", "Stephen King", "Stephen King", "Stephen King", "Stephen King"],
    "Genero": ["Terror", "Terror", "Terror", "Terror", "Terror"],
    "Ano": [1986, 2018, 1987, 2019, 2015],
    "Preço": [120.00, 80.00, 75.00, 90.00, 65.00],
    "Quantidade": [10, 20, 15, 25, 30]
}

# 2 - Criando um dataframe

df = pd.DataFrame(dados)

print(df)
# OU
# nome_livro = "livros.xlsx"

df.to_excel("data/livros.xlsx", index=False)
print("Planilha criada com sucesso!")
