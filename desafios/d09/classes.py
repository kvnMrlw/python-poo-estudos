from abc import ABC, abstractmethod

class BebidaQuente(ABC):

    def preparar(self):
        print ("____Preparar a bebida_____")
        self.ferver_agua()
        self.misturar()
        self.servir()
        print("____bebida pronta!____")


    def ferver_agua(self):
        print (f"1. a água ferveu a 100 graus para preparar essa bebida")


    @abstractmethod
    def misturar(self):
        pass


    @abstractmethod
    def servir():
        pass


class Cafe(BebidaQuente):
    
    def misturar(self):
        print (f"2. O pó do café foi passado com aguá no coador")

    def servir(self):
        print (f"3. O café foi servido em uma xicara e está pronto para beber")

class Cha(BebidaQuente):

    def misturar(self):
        print (f"2. O saquinho de cha foi adicionado a água e se misturou")


    def servir(self):
        print (f"3. O cha foi colocado em uma caneca e está pronto para beber")


class Leite(BebidaQuente):
    def misturar(self):
        print (f"2. Foi passado com vapor pressurizado pelo bico de leite")


    def servir(self):
        print (f"3. Foi servido em uma caneca grande com café")