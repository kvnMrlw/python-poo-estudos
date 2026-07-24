from abc import ABC, abstractmethod


class Transporte(ABC):
    def __init__(self, distancia, frete=0):
        self.distancia = distancia
        self.frete = frete


    @abstractmethod
    def calcular_frete(self):
        pass


class Moto(Transporte):
    fator = 0.50
    def __init__(self, distancia, frete):
        super().__init__(distancia, frete)
        

    def calcular_frete(self):
        frete = Moto.fator * self.distancia
        return frete


class Caminhao(Transporte):
    fator = 1.20
    def __init__(self, distancia, frete=0):
        super().__init__(distancia, frete=0)


    def calcular_frete(self):
        if self.distancia > 50:
            frete = Caminhao.fator * self.distancia
        else:
            return "O caminhão faz entregas a no minimo 50 km de distância"

        return frete   


class Drone(Transporte):
    fator = 9.50
    def __init__(self, distancia, frete):
        super().__init__(distancia, frete)


    def calcular_frete(self):
        if self.distancia < 10:
            frete = Drone.fator * self.distancia
        else:
            return "O drone faz entregas com menos de 10 km"

        return frete
