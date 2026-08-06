
class Diario:
    def __init__(self):
        self.__segredos = []
        self.__senha = 123


    def escrever(self, valor):
        self.__segredos.append(valor)


    def ler(self, senha):
        if self.__senha == senha:
            for i in self.__segredos:
                print(f"- {i}", end="\n")
        else:
           raise PermissionError("Senha incorreta!")


    @property
    def senha(self):
        if not self.__senha:
            raise PermissionError("Você não pode ler o diario")


    @senha.setter
    def trocar_senha(self, senha_atual):
        if senha_atual == self.__senha:
            nova_senha = input("digite sua nova senha")
        self.__senha = nova_senha


    


        


