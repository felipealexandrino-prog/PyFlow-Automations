import pandas as pd
def titulo(frase):
    frase = frase.upper()
    print(f"\nTABELA {frase}\n")
archive_df = pd.read_csv(r"C:\Users\Pichau\Downloads\vendasnew.csv")
archive_df['total'] = archive_df['preco'] * archive_df['quantidade']

vendedor_df = archive_df.groupby('vendedor').agg({
    'total' : 'sum'
}).sort_values(by='total', ascending=False).reset_index().rename(columns={
    'vendedor' : 'Vendedor_Analisado',
    'total' : 'Faturamento_Vendedor'
})
print(f"{titulo('vendedor')}{vendedor_df}")

categoria_df = archive_df.groupby('categoria').agg({
    'total' : 'sum'
}).sort_values(by='total',ascending=False).reset_index().rename(columns={
    'categoria' : 'Categoria_Analisada',
    'total' : 'Faturamento_Categoria',
})

print(f"{titulo('categoria')}{categoria_df}")

vendedorfoco_df = archive_df.groupby('vendedor').agg({
    'total' : 'sum',
    'quantidade' : 'sum'
}).reset_index().rename(columns={
    'vendedor' : 'Vendedor_Analisado',
    'total' : 'Faturamento_Vendedor',
    'quantidade' : 'Quantidade_Vendas'
    
})

print(f"{titulo('Vendedor_Foco')} {vendedorfoco_df}")

archive_df['media'] = archive_df['total']
vendedorrank_df = archive_df.groupby('vendedor').agg({
    'total' : 'sum',
    'media' : 'mean'
}).sort_values(by='total',ascending=False).reset_index().rename(columns={
    'vendedor' : 'Vendedor_Analisado',
    'total' : 'Faturamento_Vendedor',
    'media' : 'Ticket_Médio'
})
print(f"{titulo('Ranking_Vendedores')} {vendedorrank_df}")
print(f"Vendedor com maior lucro {vendedorrank_df['Vendedor_Analisado'][0]} com {vendedorrank_df['Faturamento_Vendedor'][0]} R$")