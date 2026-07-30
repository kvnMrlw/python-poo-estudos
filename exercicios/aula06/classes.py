
class ContaBancaria:
    """
    Cria uma conta bancaria 
    """

    def __init__(self, id=0, nome="", saldo=0):
        self.id = id
        self._nome = nome
        self.__saldo = saldo

    def deposito(self, valor=0):
        valor = abs(valor)
        self.__saldo += valor
    
    def saque(self, valor=0):
        if self.__saldo < valor:
            print(f"Valor negado, você só tem R${self.__saldo}")
        else:
            self.__saldo -= valor
            print(f"Saque feito com sucesso!")

    def __str__(self):
        return f"Esse é o status {self.__dict__}"
    




