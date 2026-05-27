import pandas as pd

database = pd.read_csv(r"C:\Users\Pichau\Downloads\datafunc.txt")
bonus_df = pd.DataFrame({
    "funcionario": ["Lucas", "Marina", "Pedro", "Julia"],
    "bonus": [1000, 800, 1500, 1200]
})
print(bonus_df)
print(database)



pivot = pd.pivot_table(database,index=["funcionario","cidade"],values="custo_extra",aggfunc="sum").reset_index()
intermediaria = pivot.groupby("funcionario")["custo_extra"].idxmax()
maior_custo = pivot.loc[intermediaria]
maior_custo = maior_custo.rename(columns={
    "cidade" : "Cidade_Maior_Custo",
    "custo_extra" : "Maior_Custo"
})
print(maior_custo)

tabelafinal = pd.merge(bonus_df,maior_custo,on="funcionario")

tabelafinal = tabelafinal.rename(columns={
                                 "funcionario" : "Funcionario_Analisado",
                                 "bonus":"Bonus_Funcionario"})
print(tabelafinal)