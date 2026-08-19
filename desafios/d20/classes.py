from abc import ABC

class Arquivo(ABC):
    def __init__(self, nome, tamanho):
        self.nome = nome
        self.tamanho = tamanho

    @property
    def converter_b(self):
        return self.tamanho / 1_000_000

    def abrir(self):
        print (f"Abrindo o arquivo '{self.nome}.{self._extensao}' ({self.converter_b:.4f}) MB")

class DOC(Arquivo):
    def __init__(self, nome, tamanho):
        super().__init__(nome, tamanho)
        self._extensao = "docx"

class PDF(Arquivo):
      def __init__(self, nome, tamanho):
        super().__init__(nome, tamanho)
        self._extensao = "pdf"


def abrir(objeto):
    try:
        objeto.abrir()
    except AttributeError as erro:
        print(f"Encontrei um erro ao tentar entrar em {objeto.__class__.__name__}: {erro}")