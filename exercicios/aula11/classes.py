class Numero:
    def __init__(self, valor):
        self.valor = valor

    def dobrar(self):
        self.valor *= 2

    def __str__ (self):
        return f"Tenho o número {self.valor} dentro de número"


class Texto:
    def __init__(self, texto):
        self.texto = texto

    def dobrar(self):
        self.texto += self.texto

    def __str__ (self):
        return f"Tenho o texto {self.texto} dentro de texto"
    

class Lista: 
    def __init__(self, lts=[]):
        self.lista = lts

    def dobrar(self):
        self.lista += self.lista

    def __str__ (self):
        return f"Tenho a lista {self.lista} dentro de lista"


class Papel:
    def __init__(self):
        self.dobrado = False

    def dobrar(self):
        self.dobrado = True

    def __str__ (self):
        return f"O papel está dobrado? {self.dobrado}"


class Casa:
    def __init__(self):
        pass

    def __str__ (self):
        return f"Era uma casa, muito engraçada não tinha teto, não tinha nada..."


def Tente_dobrar(objeto):
    try:
        objeto.dobrar()
    except:
        print(f"Encontrei um erro ao tentar dobrar {objeto.__class__.__name__}")