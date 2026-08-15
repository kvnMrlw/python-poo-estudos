from functools import singledispatchmethod

class Analisar:

    @singledispatchmethod
    def analisar(self, valor):
        print (f"Não foi possivel acessar o analisador do {valor}, coloque um valor válido")


    @analisar.register
    def _(self, valor: str):
        print (f"O valor {valor} é uma string")


    @analisar.register
    def _(self, valor: float):
        print (f"{valor} é um número real")

    @analisar.register
    def _(self, valor: int):
        print (f"O valor {valor} é um número inteiro")


    @analisar.register
    def _(self, valor: tuple|list):
        print (f"{valor} é uma coleção de dados")