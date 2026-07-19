#Declaração da classe
class Gafanhoto:
    """
    Essa classe cria uma pessoa e a atribui nome e idade

    Para criar uma pessoa você deve criar uma variavel para a classe e depois dentro dos parenteses extanciarlo

    Ex:
        variavel = Gafanhoto(nome, idade)
    """
    def __init__(self, nome="", idade=0): #metodo condtrutor
        #Atribuição da classe
        self.nome = nome
        self.idade = idade

    #Metodos de instância
    def aniversario(self):
        self.idade += 1


    def __str__(self):
        return f"{self.nome} é gafanhoto e tem {self.idade} anos de idade."
    
    

g1 = Gafanhoto("kevin", 16)
g1.aniversario()
print(g1)

g2 = Gafanhoto("mauro")
print(g2)

