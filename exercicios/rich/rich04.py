from rich import print
from rich.table import Table
from rich.traceback import install
install()


tabela = Table(title="Tabela de preços")

tabela.add_column("Nome")
tabela.add_column("Preço")
nome = str(input("Digite seu nome: "))
preco = float(input("Digite o preço do produto: "))

tabela.add_row(nome, preco)

print(tabela)

