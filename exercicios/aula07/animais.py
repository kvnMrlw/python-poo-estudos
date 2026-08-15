from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome):
        self.nome = nome


    @abstractmethod
    def emitit_som(self):
        pass


class Pato(Animal):
    def emitit_som(self):
            return f"O pato s{self.nome} feZ QUAK, QUAK"


class Cachorro(Animal):
    def emitit_som(self):
            return f"O cachorro {self.nome} feZ AU, AU"


class Gato(Animal):
    def emitit_som(self):
            return f"O gato {self.nome} feZ MIAU, MIAU"


class Galinha(Animal):
    def emitit_som(self):
        return f"A galinha {self.nome} feZ PÓ, PÓ"