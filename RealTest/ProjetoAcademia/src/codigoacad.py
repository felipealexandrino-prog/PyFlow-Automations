import pandas as pd
import matplotlib.pyplot as plt

# ==================================================
# LEITURA E TRATAMENTO DOS DADOS
# ==================================================

academia_df = pd.read_csv(r"ProjetoAcademia/Dados_Academia/database_acad.txt")

# Receita gerada por aluno
academia_df["receita"] = (
    academia_df["aulas_frequentadas"]
    * academia_df["valor_mensalidade"]
)

print("\nDados Brutos:")
print(academia_df)

# ==================================================
# ANÁLISE 1 - RECEITA POR ALUNO
# ==================================================

receita_aluno_df = academia_df.groupby("aluno").agg(
    Receita_Total=("receita", "sum")
).reset_index().sort_values(
    by="Receita_Total",
    ascending=False
)

# Melhor aluno
idx_aluno = receita_aluno_df["Receita_Total"].idxmax()
aluno_top = receita_aluno_df.loc[idx_aluno]

print("\nReceita por Aluno:")
print(receita_aluno_df)

print(
    f"\nO aluno com maior receita foi "
    f"{aluno_top['aluno']} "
    f"com R$ {aluno_top['Receita_Total']:.2f}."
)

# Gráfico
plt.figure(figsize=(8, 5))

plt.bar(
    receita_aluno_df["aluno"],
    receita_aluno_df["Receita_Total"]
)

plt.title("Receita por Aluno")
plt.xlabel("Aluno")
plt.ylabel("Receita")

plt.savefig("ProjetoAcademia/Graficos_Academia/grafico_receita_aluno.png")
plt.show()

# ==================================================
# ANÁLISE 2 - RECEITA POR MODALIDADE
# ==================================================

receita_modalidade_df = academia_df.groupby("modalidade").agg(
    Receita_Total=("receita", "sum")
).reset_index().sort_values(
    by="Receita_Total",
    ascending=False
)

idx_modalidade = receita_modalidade_df["Receita_Total"].idxmax()
modalidade_top = receita_modalidade_df.loc[idx_modalidade]

print("\nReceita por Modalidade:")
print(receita_modalidade_df)

print(
    f"\nA modalidade mais lucrativa foi "
    f"{modalidade_top['modalidade']} "
    f"com R$ {modalidade_top['Receita_Total']:.2f}."
)

# Gráfico
plt.figure(figsize=(8, 5))

plt.bar(
    receita_modalidade_df["modalidade"],
    receita_modalidade_df["Receita_Total"]
)

plt.title("Receita por Modalidade")
plt.xlabel("Modalidade")
plt.ylabel("Receita")

plt.savefig("ProjetoAcademia/Graficos_Academia/grafico_receita_modalidade.png")
plt.show()

# ==================================================
# ANÁLISE 3 - MELHOR UNIDADE POR MODALIDADE
# ==================================================

receita_modalidade_unidade_df = academia_df.groupby(
    ["modalidade", "unidade"]
).agg(
    Receita_Total=("receita", "sum")
).reset_index()

# Para cada modalidade, encontrar a unidade com maior receita
idx_melhor_unidade = receita_modalidade_unidade_df.groupby(
    "modalidade"
)["Receita_Total"].idxmax()

melhor_unidade_modalidade_df = (
    receita_modalidade_unidade_df.loc[idx_melhor_unidade]
)

print("\nMelhor Unidade por Modalidade:")
print(melhor_unidade_modalidade_df)

# ==================================================
# ANÁLISE EXTRA - UNIDADE COM MAIOR RECEITA GERAL
# ==================================================

receita_unidade_df = academia_df.groupby("unidade").agg(
    Receita_Total=("receita", "sum")
).reset_index()

idx_unidade = receita_unidade_df["Receita_Total"].idxmax()
unidade_top = receita_unidade_df.loc[idx_unidade]

print(
    f"\nA unidade com maior receita foi "
    f"{unidade_top['unidade']} "
    f"com R$ {unidade_top['Receita_Total']:.2f}."
)

# ==================================================
# EXPORTAÇÃO PARA EXCEL
# ==================================================

with pd.ExcelWriter("ProjetoAcademia/Relatorio_Academia/Relatorio_Academia.xlsx") as writer:

    academia_df.to_excel(
        writer,
        sheet_name="Dados_Brutos",
        index=False
    )

    receita_aluno_df.to_excel(
        writer,
        sheet_name="Receita_Aluno",
        index=False
    )

    receita_modalidade_df.to_excel(
        writer,
        sheet_name="Receita_Modalidade",
        index=False
    )

    melhor_unidade_modalidade_df.to_excel(
        writer,
        sheet_name="Melhor_Unidade",
        index=False
    )

print("\nRelatório Excel gerado com sucesso!")