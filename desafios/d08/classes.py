from abc import ABC, abstractmethod

class Poligono(ABC):

    def __init__(self, quantidade_lados):
        self.quantidade_lados = quantidade_lados

    @abstractmethod
    def perimetro(self):
        pass


    @abstractmethod
    def area(self):
        pass



class Quadrado(Poligono):
    def __init__(self, lado):
        super().__init__(quantidade_lados = 4)
        self.quantidade_lados = self.quantidade_lados
        self.lado = lado


    def perimetro(self):
        perimetro = self.lado * self.quantidade_lados
        return f"O perimetro desse poligno é de {perimetro} cm"


    def area(self):
        area = self.lado ** 2
        return f"A área desse poligno é {area} cm"



class Circulo(Poligono):
    
    def __init__(self, raio):
        super().__init__(quantidade_lados = 0)
        self.raio = raio
        self.pi = 3.14
        

    def perimetro(self):
        perimetro = 2 * self.pi * self.raio
        return f"O perimetro desse poligno é de {perimetro} cm" 


    def area(self):
        area = self.pi * self.raio ** 2
        return f"A área desse poligno é {area} cm"
        