cores_permitidas = ["VERDE", "AZUL", "PRETO"]

class Chuteira:
    def __init__(self, cor, cadarcos, palmilha, birro):
        self.cor = cor.upper()
        self.cadarcos = cadarcos
        self.palmilha = palmilha
        self.birro = birro

    def verificar_cadarco(self):
        if self.cadarcos:
            return "Sua chuteira tem cadarço e está amarrado."
        else:
            return "Sua chuteira não tem cadarço, estiloso!"

    def verificar_palmilha(self):
        if self.palmilha:
            return "Você colocou a palmilha."
        else:
            return "Você não colocou a palmilha. Vai ficar desconfortável!"

    def verificar_cor(self):
        if self.cor in cores_permitidas:
            return "Ótima escolha, você tem estilo!"
        else:
            return "Melhore seu estilo."

    def verificar_birro(self):
        if self.birro:
            return "Vai correr muito com essas travas!"
        else:
            return "Muito certinho."

    def __str__(self):
        return f"Chuteira {self.cor}"
    
    
jog1 = Chuteira("Verde", cadarcos=True, palmilha=False, birro=True)
jog2 = Chuteira("Preto", cadarcos=False, palmilha=True, birro=True)
print(jog1)
print(jog1.verificar_cadarco())
print(jog1.verificar_palmilha())
print(jog1.verificar_cor())
print(jog1.verificar_birro())
print(jog2)
print(jog2.verificar_cadarco())
print(jog2.verificar_palmilha())
print(jog2.verificar_cor())
print(jog2.verificar_birro())



class Emprestimo:
    def __init__(self,valor,meses,juros):
        self.valor = valor
        self.meses = meses
        self.juros = juros
    def quant_valor(self):
        return f"O valor do seu empréstimo foi de R$ {self.valor}!"
    def quant_meses(self):
        return f"O prazo do emprestimo é de {self.meses} meses"
    def cont_juros(self):

        return f"Juros de {self.juros} porcento ao mês" 

    def calcular(self):
        juros_total = self.valor * (self.juros / 100) * self.meses
        total = self.valor + juros_total
        return total
             
        
cli1 = Emprestimo(1000,2,1.7)
print(cli1.valor)
print(cli1.meses)
print(cli1.juros)
print(cli1.calcular())
