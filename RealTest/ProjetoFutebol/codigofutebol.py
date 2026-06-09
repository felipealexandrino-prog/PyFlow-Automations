import pandas as pd
import matplotlib.pyplot as plt

bruto_df = pd.read_csv(r"C:\Users\Pichau\Downloads\databaseenterprise.txt")
bruto_df["Participações_Gol"] = bruto_df["gols"] + bruto_df["assistencias"]
print(bruto_df)

#jogador/participacoes_totais
info_jogador = bruto_df.groupby("jogador").agg(
    participações_totais = ("Participações_Gol","sum")
).sort_values(by="participações_totais",ascending=False).reset_index()
print(info_jogador)

#posicao/participacoes_totais
info_posicao = pd.pivot_table(bruto_df,index="posicao",values="Participações_Gol",aggfunc="sum").reset_index().rename(columns={
    "posicao" : "Posição",
})
print(info_posicao)

#Cidade onde cada jogador teve o MELHOR desempenho.
melhores_cidades = pd.pivot_table(bruto_df,index=["jogador","cidade_estadio"],values="Participações_Gol",aggfunc="sum").reset_index()
intermediaria = melhores_cidades.groupby("jogador")["Participações_Gol"].idxmax()
melhor_cidade_desempenho =  melhores_cidades.loc[intermediaria]
print(melhor_cidade_desempenho)


#Graficos
#Grafico Jogador x Participações Totais
plt.figure(figsize=(9,6))
plt.bar(info_jogador["jogador"],info_jogador["participações_totais"])
plt.savefig("Gráfico_Jogador_Participações")
plt.title("Participações Totais por Jogador")
plt.xlabel("Jogador")
plt.ylabel("Participações G+A")
plt.show()

#Grafico Posição x Participações Totais
plt.figure(figsize=(9,7))
plt.barh(info_posicao["Posição"],info_posicao["Participações_Gol"])
plt.savefig("Gráfico_Posição_Participações")
plt.title("Participação em Gol por Posição")
plt.xlabel("Participações em Gol")
plt.ylabel("Posições")
plt.show()


with pd.ExcelWriter("Relatório_Futebol.xlsx") as writer:
    bruto_df.to_excel(writer,index=False,sheet_name="Dados_Brutos_Desempenho"),
    info_jogador.to_excel(writer,index=False,sheet_name="Análise_Participação_Jogadores"),
    info_posicao.to_excel(writer,index=False,sheet_name="Análise_Participação_Posição"),
    melhor_cidade_desempenho.to_excel(writer,index=False,sheet_name="Análise_Cidade_Participações")

#FRASE AUTOMATICA
analisemvp = info_jogador["participações_totais"].idxmax()
melhor_jogador = info_jogador.loc[analisemvp]
print(melhor_jogador)