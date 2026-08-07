
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
        return self.__senha

    def trocar_senha(self, senha_atual, nova_senha):
        if senha_atual == self.__senha:
            self.__senha = nova_senha
        else:
            raise PermissionError("Essa não é a senha atual")




        


