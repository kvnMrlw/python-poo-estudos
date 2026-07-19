from rich import print
from rich.panel import Panel
from rich.align import Align


class Produto:
    def __init__(self, produto="", preco="0,00"):
        self.produto = produto
        self.preco = preco


    def etiqueta(self):
        conteudo = (f"""
{self.produto.center(20, "-")} 
{self.preco.center(20,"-")}    """)
        return Panel(conteudo, title="Produto", expand=False,)
    

var = Produto("levin")
print(var.etiqueta())
        
