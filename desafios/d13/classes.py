from rich.console import Console

console = Console()

class Termostato:
    temperatura_min = 16
    temperatura_max = 30

    def __init__(self):
        self.__temperatura = 24


    @property
    def temperatura(self):
        return self.__temperatura


    @temperatura.setter
    def temperatura(self, valor):
        if valor % 0.5 != 0:
            raise ValueError (f"A temperatura {valor} é invalida ela deve ser inteira ou terminar em .5")
        if valor < Termostato.temperatura_min:
            self.__temperatura == self.temperatura_min
        elif valor > Termostato.temperatura_max:
            self.temperatura_max == self.temperatura_max
        else:
            self.__temperatura == valor


    @property
    def ftemperatura(self):
        fechar = "/"
        if self.__temperatura <= 20:
            cor = "blue"
        else:
            cor = "red"
        
        console.print(f"[{cor}] {self.__temperatura}°C [{fechar}]")