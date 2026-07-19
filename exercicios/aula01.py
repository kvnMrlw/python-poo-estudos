#Declaração de classe
class MinhaClasse:
    def __init__(self, idade=0, nome=""):#Método construtor 
        self.idade = idade
        self.nome = nome
    
#Método de instância
    def aniversario(self):
        self.idade += 1

    def __str__(self):
        return (f"O gafanhoto {self.nome} tem {self.idade} anos")
    
#Declaração de objetos
g1 = MinhaClasse(16, "kevin")
g1.aniversario()
print(g1.menssagem())