class Retangulo:
    def __init__(self, base=1, altura=1, area=1):
        self._base = base
        self._altura = altura
        self._area = area


    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, valor):
        if valor < 0:
            raise ValueError("Digite um número válido")
        if isinstance(valor, (str, bool)):
            raise ValueError("Digite um número válido")
        else:
            self._base = valor
            return valor


    @property
    def altura(self):
        return self._altura

    @altura.setter
    def altura(self, valor):
        if valor < 0:
            raise ValueError("Digite um número válido")
        if isinstance(valor, (str, bool)):
            raise ValueError("Digite um número válido")
        else:
            self._altura = valor
        return valor


    @property
    def medida(self):
        print(f"""
Base = {self.base}
Altura = {self.altura}
Area = {self.area} """)

    @medida.setter
    def medida(self, valores:tuple):
        if not isinstance(valores, tuple):
            raise TypeError ("As medidas devem ser informadas dentro de uma tupla")
        if len(valores) != 2:
            raise TypeError ("Devem ser passados dois atributos na tupla")
        if not isinstance(valores[0], (str, bool)):
            self._base = valores[0]
        else:
            raise TypeError ("O primeiro valor deve ser um número")
        if not isinstance(valores[1], (str, bool)):
                    self._altura = valores[1]
        else:
            raise TypeError ("O segundo valor tenque ser um número")


    @property
    def area(self):
        return self._base * self._altura
