import pandas as pd
import matplotlib.pyplot as plt
dataframe = pd.read_csv(r"C:\Users\Pichau\Downloads\basedata.txt")

dataframe["total"] = dataframe["preco"] * dataframe["quantidade"]
print(dataframe)

plt.bar(dataframe["produto"],dataframe["quantidade"])
plt.title("Total de Estoque")
plt.xlabel("Produtos Analisados")
plt.ylabel("Quantidade Estocada")
plt.show()