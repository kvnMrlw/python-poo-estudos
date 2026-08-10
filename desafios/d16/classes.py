from hashlib import sha256

class ContaBancaria:
    def __init__(self, id, titular, saldo, chave = None):
        self._id = id 
        self._titular = titular
        self.__saldo = saldo
        if chave is None:
            chave = self.pede_senha()
        self.__hash = sha256(chave.encode("utf-8")).hexdigest()


    @property
    def nome (self):
        return self._titular


    @nome.setter
    def nome (self, novo_nome):
            self.pede_senha()
            if self.validar_senha(self.pede_senha()) == True:
                self._titular = novo_nome
        

    def validar_senha(self, chave):
        hash = sha256(chave.encode("utf-8")).hexdigest()
        if hash != self.__hash:
            raise PermissionError("Senha errada")
        else:
            return True


    def pede_senha(self):
        while True:
            senha = str(input("digite sua senha em formato str: "))
            if len(senha) > 0:
                break
            
        return senha


    def __str__(self):
        return f"Estado atual da conta: {self.__dict__}"

    
    def sacar(self, valor, chave=None):
        valor = abs(valor)

        if chave is None:
            self.pede_senha(chave)

        if self.validar_senha(chave):
            if valor > self.__saldo:
                return f"Saldo insuficiente"
            else:
                self.__saldo -= valor
        


    def depositar(self, valor):
        valor = abs(valor)
        if valor > 0:
            self.__saldo +=  valor
        else:
            return f"O deposito de {valor} é invalido!"
        return f"deposito de {valor}"