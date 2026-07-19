from rich import print
from rich.panel import Panel

jogos = []

class FichaGame:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick 

    
    def adicionar_jogos(self, game):
        jogos.append(game)

    
    def ficha(self):
        conteudo = f"Nome: {self.nome}"
        for i in jogos:
            conteudo += f"\n :video_game: {i}"
        return Panel(conteudo, title= f"jogador: {self.nick}", expand=False)
        


g = FichaGame("kevin", "kvnz")
g.adicionar_jogos("valorante")
g.adicionar_jogos("cs go")
print (g.ficha())