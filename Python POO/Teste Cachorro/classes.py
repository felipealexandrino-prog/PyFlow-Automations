class Cachorro():
    def __init__(self,nome,idade=0):
        self.nome = nome
        self.ida = idade
        if self.ida < 0:
            print(f"Idade inválida!")
            self.ida = 0
        else:
            print(f"OK")    
    def demonstrar(self):
        print(f"O nome do cachorro é {self.nome} e possui {self.ida} anos")
        if self.ida >= 8:
            print(f"O cachorro {self.nome} já ultrapassou sua maioridade")
        else:
            print(f"O cachorro {self.nome} ainda não ultrapassou sua maioridade!!!")            
    
    def latir(self):
        # complete aqui
        print(f"AUAU")

    def fazer_aniversario(self):
        self.ida += 1
        print(f"Hoje é aniversario do {self.nome} vamos cantar paraubens auau!")
        return f"{self.nome} agora tem {self.ida} anos"
    def idade_humana(self):
        idade_humana = self.ida * 7 
        print(f"{idade_humana} anos é sua idade humana!")