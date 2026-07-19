from rich import print

class Caneta:
    def __init__(self, cor="azul"):
        escolha = ""
        match cor.lower().strip():
            case "azul":
                escolha = "[blue]"
            case "vermelho":
                escolha = "[red]"
            case "verde":
                escolha = "[green]"
            case _ :
                escolha = "[white]"
        self.cor = escolha
        self.tampada = True

    
    def destampar_caneta(self):
        if self.tampada == True:
            self.tampada = False
        
    
    def escrever(self, msg):
        if self.tampada == True:
            print (f":lock: A caneta esta tampada")
        else:
            print (f"{self.cor}{msg}")

    def pular_linha(self, quant):
        for _ in range (0, quant):
            print("\n")


   


v = Caneta("verde")
v.destampar_caneta()
v.escrever("olá")
v.pular_linha(3)

a = Caneta("")
a.destampar_caneta()
a.escrever("olá nada zé")
