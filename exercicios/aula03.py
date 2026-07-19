class ContaBancaria:
    """
    Cria uma conta bancaria 
    """

    def __init__(self, id=0, nome="", saldo=0):
        self.id = id
        self.nome = nome
        self.saldo = saldo

    def deposito(self, valor=0):
        self.saldo += valor
    
    def saque(self, valor=0):
        if self.saldo < valor:
            print(f"Valor negado, você só tem R${self.saldo}")
        else:
            self.saldo -= valor
            print(f"Saque feito com sucesso!")

    def __str__(self):
        return f"O id da conta é {self.id}, o nome do proprietário é {self.nome} e o saldo é de R${self.saldo}"
    

c1 = ContaBancaria(1, "kevin", 1000)
c1.saque(500)
c1.deposito(1000000)
print(c1)


