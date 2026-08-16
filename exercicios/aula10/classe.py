class Porta:
    def abrir(self):
        print ("Gire a maçaneta para abirir a porta")

class Ovo:
    def abrir(self):
        print ("Bata o ovo para abrilo")

class Empresa:
    def abrir(self):
        print ("Va a uma instituição responsavel com a documentação para fazer um cnpj")

class Pedra:
    pass


def tentar_abrir(objeto):
    try:
        objeto.abrir()
    except:
        print(f"Encontrei problemas ao tentar abrira o objeto {objeto.__class__.__name__}") 