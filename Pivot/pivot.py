import pandas as pd
dataframe = pd.read_csv(r"C:\Users\Pichau\Downloads\dados_pivot.txt")
dataframe["total"] = dataframe["preco"] * dataframe["quantidade"]


pivot_city = pd.pivot_table(dataframe,index="cidade",values="quantidade",aggfunc="sum").reset_index()


pivot_multiplo = pd.pivot_table(
    dataframe,
    index=["categoria","cidade"],
    values="quantidade",aggfunc="sum"
    ).reset_index().sort_values("quantidade",ascending=False)



maior = pivot_multiplo.groupby("categoria")["quantidade"].idxmax()
pivot_top = pivot_multiplo.loc[maior]




#///////////////////////////////////////////////

basedados = pd.read_csv(r"C:\Users\Pichau\Downloads\basedatatst.txt")

basedados["total"] = basedados["preco"] * basedados["quantidade"]
#TABELA BASE INICIAL
tabelabase = basedados.groupby("vendedor").agg(
    faturamento_total=("total","sum"),
    ticket_medio=("total","mean")
)


#TABELA INTERMEDIARIA
pivotint = pd.pivot_table(basedados,index=["vendedor","cidade"],values="total",aggfunc="sum").reset_index()


#TABELA FINAL É PELO LOC
maior = pivotint.groupby("vendedor")["total"].idxmax()
cidade_top = pivotint.loc[maior]
print(cidade_top)