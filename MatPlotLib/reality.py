import pandas as pd
import matplotlib.pyplot as plt
#META: GRAFICO DE FATURAMENTO POR VENDEDOR
df = pd.read_csv(r"C:\Users\Pichau\Downloads\basedatamat.txt")
df['total'] = df['preco'] * df['quantidade']

fatvend = pd.pivot_table(df,index="vendedor",values="total",aggfunc="sum"
                         ).sort_values(by="total",ascending=False).reset_index()


plt.bar(fatvend["vendedor"],fatvend["total"])
plt.title("Faturamento por Vendedor")
plt.xlabel("Vendedores")
plt.ylabel("Faturamento")
plt.show()


catvend = df.groupby("categoria").agg(
    quantidade_total = ("quantidade","sum")
).reset_index()

print(catvend)

plt.barh(catvend["categoria"],catvend["quantidade_total"])
plt.title("Quantidade Total por Categoria")
plt.xlabel("Quantidade Total")
plt.ylabel("Categoria")
plt.show()