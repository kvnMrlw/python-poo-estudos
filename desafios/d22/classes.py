from rich import print
from rich.panel import Panel

class Menssagem:
    def __init__(self, menssagem: str):
        self.menssagem = menssagem


    def mostrar(self):
        print (Panel(self.menssagem, title="Menssagem", expand=False, style="White on black"))


class Erro(Menssagem):
    def mostrar(self):
        print (Panel(self.menssagem, title="ERROR!", expand=False, style="yellow on red"))


class Alerta(Menssagem):
    def mostrar(self):
        print (Panel(self.menssagem, title="ALERT!", expand=False, style="red on yellow"))
        
        