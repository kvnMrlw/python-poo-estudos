from rich import print
from rich.panel import Panel


class ControleRemoto:
    canal_min:int = 1
    canal_max:int = 5
    volume_min:int = 1
    volume_max:int = 5

    def __init__(self, canal = 1, volume = 2):
        self.canal_atual:int = canal
        self.volume_atual:int = volume
        self.ligado:bool = False
        

    def ligar(self):
        self.ligado = not self.ligado


    def mostrar_tv(self):
        conteudo = ""

        if self.ligado == False:
            conteudo = "A tv está desligada!"
        else:
            conteudo = "Volume Canal"

        tv = Panel(conteudo, title="TV", width=35)
        print(tv)


tv = ControleRemoto()
tv.ligar()
tv.mostrar_tv()