from abc import ABC, abstractmethod
from rich import print
from rich.panel import Panel


class Funcionario(ABC):
    salario_min = 1612
    inss = 0.075

    def __init__(self, nome, sal_bruto, salario=0):
        self.nome = nome
        self.sal_bruto = sal_bruto
        self.salario = salario


    @abstractmethod
    def calcurlar_sal(self):
        pass


    def analisar(self):
        conteudo = f"""O salário de [blue]{self.nome}[/] [purple]{self.__class__.__name__}[/] é de
[green]{self.salario}[/] e corresponde a [yellow]{self.salario / Funcionario.salario_min:.2f}[/] salarios mínimos"""
        painel = Panel(conteudo, title="Analise", expand=False)

        print (painel)

class Horista(Funcionario):
    def __init__(self, nome, valor_hora, horas_trabalhadas):
        super().__init__(nome, sal_bruto=0, salario=0)
        self.valor_hora = valor_hora
        self.horas_trabalhadas = horas_trabalhadas


    def calcurlar_sal(self):
        self.salario = self.valor_hora * self.horas_trabalhadas
        return self.salario


class Mensalista(Funcionario):

    def calcurlar_sal(self):
        self.salario = self.sal_bruto - self.sal_bruto * Funcionario.inss
        return self.salario
