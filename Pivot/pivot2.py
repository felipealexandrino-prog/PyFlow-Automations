import pandas as pd
dataframe = pd.read_csv(r"C:\Users\Pichau\Downloads\database.txt")
dataframe["total"] = dataframe["preco"] * dataframe["quantidade"]
print(dataframe)
tableint = dataframe.groupby("vendedor").agg(
    faturamento_total = ("total","sum"),
    ticket_medio = ("total","mean")
)
print(tableint)

pivot = pd.pivot_table(dataframe,index=["vendedor","cidade"],values="total",aggfunc="sum").reset_index()

menor = pivot.groupby("vendedor")["total"].idxmin()
worst = pivot.loc[menor]
print(worst)
juntos = pd.merge(
    tableint,
    worst,
    on="vendedor")
print(juntos)