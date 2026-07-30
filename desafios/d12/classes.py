from abc import ABC, abstractmethod
import random
from rich import print

class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []


    def atacar(self, alvo, forca):
        if self.vida > 0 and alvo.vida > 0:
            golpe = random.choice(self.golpes)

            print (f"{self.nome} atacou {alvo.nome} com o golpe [yellow]{golpe}[/]")

            alvo.receber_dano(forca)
        else:
            print("[red]Esse ataca é invalido, morto não fala![/]")



    def receber_dano(self, dano):
        fator = random.randint(0, dano)
        self.vida = self.vida - fator
        if self.vida < 0:
            self.vida = 0
        print (f"[blue]{self.nome}[/] recebeu um [red]dano de fator {fator}[/]")


    def mostrar_status(self, personagem):
        print(f"Esse é o estado do {personagem.nome}, vida = {personagem.vida} ")

    @abstractmethod
    def curar(self):
        pass


class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Espadada", "Estocada", "Pefurada"]

    def curar(self):
        return super().curar()


class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ["Julgamento", "Bola de fogo", "Sangue sugua"]


    def curar(self):
        return super().curar()