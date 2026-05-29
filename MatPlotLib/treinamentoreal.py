import pandas as pd
import matplotlib.pyplot as plt

basedf = pd.read_csv(r"C:\Users\Pichau\Downloads\exceldata.txt")
basedf["total"] = basedf["preco"] * basedf["quantidade"]
print(basedf)
#Faturamento por vendedor
faturamentovendedor = basedf.groupby("vendedor").agg(
    faturamento_vendedor = ("total","sum")
).sort_values(by="faturamento_vendedor",ascending=False).reset_index()
print(f"Tabela de Faturamento por Vendedor\n{faturamentovendedor}\n")
plt.bar(faturamentovendedor["vendedor"],faturamentovendedor["faturamento_vendedor"])
plt.title("Faturamento por Vendedor")
plt.xlabel("Vendedor")
plt.ylabel("Faturamento")
plt.show()

#Quantidade Total por Categoria
quantidade_total_categoria = pd.pivot_table(basedf,index="categoria",values="quantidade",aggfunc="sum").reset_index().sort_values(by="quantidade",ascending=False)
print(f"Tabela Quantidade por Categoria \n{quantidade_total_categoria}\n")

plt.barh(quantidade_total_categoria["categoria"],quantidade_total_categoria["quantidade"])
plt.title("Quantidade Total Por Categoria")
plt.xlabel("Quantidade Total")
plt.ylabel("Categoria")
plt.show()


#Faturamento por Cidade
faturamento_por_cidade = basedf.groupby("cidade").agg(
    faturamento_total = ("total","sum")
).sort_values(by="faturamento_total",ascending=False).reset_index()
print(f"Faturamento Por Cidade \n{faturamento_por_cidade}\n")
plt.bar(faturamento_por_cidade["cidade"],faturamento_por_cidade["faturamento_total"])
plt.title("Faturamento por Cidade")
plt.xlabel("Cidade")
plt.ylabel("Faturamento")
plt.show()


#Passagem para o excel!

with pd.ExcelWriter("Relatório_Teste.xlsx") as writer:
    basedf.to_excel(writer,sheet_name="Dados Brutos",index=False)
    
    faturamentovendedor.to_excel(writer,sheet_name="Dados Faturamento por Vendedor",index=False)
    
    quantidade_total_categoria.to_excel(writer,sheet_name="Quantidade por Categoria",index=False)
    
    faturamento_por_cidade.to_excel(writer,sheet_name="Faturamento por Cidade",index=False)