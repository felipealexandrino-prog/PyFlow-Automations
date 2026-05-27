import pandas as pd

dataframe = pd.read_csv(r"c:\Users\Pichau\Downloads\datafix.txt")


pivot = pd.pivot_table(dataframe,index=["vendedor","cidade"],values="total",aggfunc="sum").reset_index()
intermediario = pivot.groupby("vendedor")["total"].idxmin()

menor = pivot.loc[intermediario]
menor = menor.rename(columns={
    "cidade" : "Pior_Cidade",
    "total" : "Pior_Total"
})
print(menor)