class Carteira:
    def __init__(self, saldo):
        self.__saldo = saldo


    def __str__(self):
        return f"Você tem uma saldo de R${self.__saldo:.2f}"

    @property
    def saldo(self):
        return self.__saldo

    @saldo.setter
    def saldo(self, valor):
        return "Você não pode alterar o valor desse jeito"


    def __eq__(self, outro):
        if self.__saldo == outro.__saldo:
            return True
        else:
            return False


    def __iadd__(self, valor: int|float):
        self.__saldo = self.__saldo + valor 
        return self


    def __isub__(self, valor: int|float):
        self.__saldo = self.__saldo - valor
        return self


    def __le__(self, outro: int|float):
        if self.__saldo <= outro.__saldo:
            return True
        else:
            return False


    