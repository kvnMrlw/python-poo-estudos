from abc import ABC, abstractmethod
from babel.numbers import format_currency

class Pagamento(ABC):
    def __init__(self, valor):
        self._valor = valor


    @property
    def fvalor(self):
        return f"{format_currency(self._valor, 'BRL', locale='pt_BR')}"


    def pagar(self):
        print(f"O pagamento de {self.fvalor} foi confimado no {self.__class__.__name__}")
        


class Pix(Pagamento):
   pass


class Credito(Pagamento):
    pass


class Pix(Pagamento):
    pass


