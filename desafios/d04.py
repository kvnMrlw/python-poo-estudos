from rich import print
from rich.traceback import install
install()

class Livro:
    def __init__(self, titulo, num_pag):
        self.titulo = titulo
        self.num_pag = num_pag
        self.pag_atual = 1

        print(f":open_book:Você acobou de abrir o livro {self.titulo}\n ele tem {self.num_pag} páginas \n ele começa aqui na página {self.pag_atual}")


    def passar_pagina(self, pag):
        if self.pag_atual == 1:
            for i in range(1, pag+1):
                self.pag_atual += 1
                print(f"[red] pag{i} [/]", end=">")
                if i == self.num_pag:
                    print("\n[pink] O livro acabou [/]")
                    break

        else:
            destino = self.pag_atual + pag
            for i in range(self.pag_atual, destino):
                self.pag_atual += 1
                print(f"[red] pag{i} [/]", end=">")
                if i == self.num_pag:
                    print("\n[pink] O livro acabou [/]")


l = Livro("o rei", 12)
l.passar_pagina(5)
l.passar_pagina(2)
l.passar_pagina(5)
