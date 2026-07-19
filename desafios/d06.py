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
            case _:
                escolha = "[white]"
        self.cor = escolha
        self.tampada = True

    
    def destampar(self):
        if self.tampada:
            self.tampada = False



    def escrever(self, msg):
        if self.tampada:
            print(f":prohibited: A {self.cor} caneta[/] esta tampada")
        else:
            print(f"{self.cor}{msg}[/]", end="")


    def quebra_linha(self, quant= 1):
        for _ in range(0, quant):
            print("\n")


g1= Caneta("azul")
g2= Caneta("vermelho")
g1.destampar()
g2.destampar()

g1.escrever("oi")
g1.quebra_linha(2)
g2.escrever("fala ai")