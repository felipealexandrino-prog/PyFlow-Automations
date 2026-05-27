import pandas as pd
geral_df = pd.read_csv(r"C:\Users\Pichau\Downloads\basedata.txt")
produto_df = pd.read_csv(r"C:\Users\Pichau\Downloads\basedata_produto.txt")


#Teste!
geral_df['total'] = geral_df['preco'] * geral_df['quantidade']
info_df = geral_df.groupby('vendedor').agg(
    faturamento_total=('total','sum'),
    quantidade_total=('quantidade','sum'),
    ticket_medio=('total','mean')
).reset_index().sort_values('faturamento_total', ascending=False)


#TableProduto
produto_df['total'] = produto_df['preco'] * produto_df['quantidade']
categoria_df = produto_df.groupby("categoria").agg(
    faturamento_total = ("total","sum")
).reset_index().sort_values('faturamento_total',ascending=False)
print(f"\nTabela de Faturamento por categoria:\n{categoria_df}")


top_df = produto_df.groupby("categoria")["produto"].max().reset_index()
print(f"\nItens mais vendidos por categoria: \n{top_df}")
top_cidade = produto_df.groupby("categoria")["cidade"].max().reset_index()
print(f"\nCidade mais vendeu por categoria: \n{top_cidade}")