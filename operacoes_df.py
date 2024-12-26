import pandas as pd
import matplotlib.pyplot as plt

# 1 - Criando Dataframe de exemplo

data = {
    "Nome": ["Robert", "Orlando", "Giovanna", "Mariana", "Lucas"],
    "Idade": [19, 17, 9, 22, 23],
    "Cargo": ["Estagiário", "Estagiário", "Gerente", "Analista", "Analista"],
    "Salario": [6800, 7000, 9000, 3000, 1000]
}

df = pd.DataFrame(data)

print(df)

# 2 - Visualizando as primeiras linhas do dataframe

print(df.head(3))
# O método head() retorna as primeiras linhas do dataframe, por padrão retorna as 5 primeiras linhas

# 3 - Informações sobre o Dataframe

print(df.info())
# O método info() retorna informações sobre o dataframe, como o nome das colunas, o tipo de dados de cada coluna e o tamanho do dataframe

# 4 - Estatisitcas Descritiva

print(df.describe())
# O método describe() retorna estatísticas descritivas sobre o dataframe, como média, desvio padrão, mínimo, máximo, etc.

# 5 - Condição em DataFrame (Salário > 5000)

print(df[df["Salario"] > 5000])

# 6 - Realizar ordenação (Idade)

print(df.sort_values(by="Idade", ascending=False))

# 7 - Adicionando coluna calculada

df["Bonus"] = df["Salario"] * 0.1
print(df)

# 8 - Agrupamento e Agregação

print(df.groupby("Cargo")["Salario"].mean())
# O método groupby() agrupa os dados por uma coluna específica e o método mean() calcula a média dos salários de cada grupo

# 9 - Visualização basica

df.plot(
    kind="bar",
    x="Nome",
    y="Salario",
    title="Salario dos funcionarios",
    rot=45
)

plt.show()
