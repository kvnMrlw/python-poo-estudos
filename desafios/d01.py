from rich import print

class Funcionario:
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo

    
    def apresentacao(self):
        return f":+1: Olá meu nome é {self.nome} estou no setor {self.setor} e esse é meu cargo {self.cargo}"
    

f1 = Funcionario("kevin", "vendas", "markenting")
print(f1.apresentacao())