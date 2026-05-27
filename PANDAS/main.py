import pandas as pd

arquivo = pd.read_csv(r"C:\Users\Pichau\Downloads\vendasnew.csv")
arquivo['total'] = arquivo['preco'] * arquivo['quantidade']

tabelafinal = arquivo.groupby('vendedor').agg({
    'total' : ['sum','mean'],
    'quantidade' : 'sum',
    'cidade' : 'max'
    
}).reset_index().rename(columns={
    'vendedor' : 'Vendedor_Analisado',
    'total' : 'Total_Faturado',
    'quantidade' : 'Quantidade_Vendas',
    'cidade' : 'Cidade_Tops'
})
print(tabelafinal)