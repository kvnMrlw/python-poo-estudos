from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, salario: float|int):
        self.nome = nome
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario

    @abstractmethod
    def calcular_bonus():
        pass

    def __str__(self):
        return f"O {self.__class__.__name__} com seu salário de R${self.salario} recebera R${self.calcular_bonus()} de bônus"


class Gerente(Funcionario):

    def calcular_bonus(self):
        return self.salario * 0.15


class Designer(Funcionario):
    
    def calcular_bonus(self):
        return self.salario * 0.08


class Desenvolvedor(Funcionario):
    
    def calcular_bonus(self):
        return self.salario * 0.10

    