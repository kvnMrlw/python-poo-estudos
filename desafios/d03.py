from rich import print
from rich.panel import Panel

class Churrasco:
    consumo_padrao = 0.400
    preco_kilo = 82.00
    def __init__(self, titulo, pessoas):
        self.titulo = titulo
        self.pessoas = pessoas

    def __str__(self):
        return f"esse é o {self.titulo} com {self.pessoas} pessoas"
    
    
    def calcular_qtd_carne(self):
        return self.pessoas * Churrasco.consumo_padrao
    
    def custo_total(self):
        return self.calcular_qtd_carne() * __class__.preco_kilo
    
    def preço_pessoa(self):
        return self.custo_total() / self.pessoas
    
    def painel(self):
        conteudo = f"""O churrasco {self.titulo} com {self.pessoas} pessoas 
tera um consumo padrão de {Churrasco.consumo_padrao} kilos
e preço do kilo foi considerado {Churrasco.preco_kilo}
serão necessarios {self.calcular_qtd_carne()} gramas
o custo total será de R${self.custo_total()} reais
e o preço por pessoa será de {self.preço_pessoa()}"""
        
        painel = Panel(conteudo, title=self.titulo, expand=False)
        print(painel)


c = Churrasco("Churras", 10)
c.painel()