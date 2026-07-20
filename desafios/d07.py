from rich import print
from rich.panel import Panel

class ControleRemoto:
    canal_min:int = 1
    canal_max:int = 5
    volume_min:int = 1
    volume_max:int = 5

    def __init__(self, canal = 1, volume = 2):
        self.canal_atual:int = canal
        self.volume_atual:int = volume
        self.ligado:bool = False
        

    def ligar(self):
        self.ligado = not self.ligado

    
    def canal_mais(self):
        if self.ligado == True:
            if self.canal_atual == ControleRemoto.canal_max:
                self.canal_atual = ControleRemoto.canal_min
            else:
                self.canal_atual += 1

    
    def canal_menos (self):
        if self.ligado == True:
            if self.canal_atual == ControleRemoto.canal_min:
                self.canal_atual = ControleRemoto.canal_max
            else:
                self.canal_atual -= 1

    
    def volume_mais(self):
        if self.ligado == True:
            if self.volume_atual != ControleRemoto.volume_max:
                self.volume_atual += 1
    

    def volume_menos(self):
        if self.ligado == True:
            if self.volume_atual != ControleRemoto.volume_min:
                self.volume_atual -= 1

    def mostrar_tv(self):
        conteudo = ""

        if self.ligado == False:
            conteudo = ":atom_symbol: A tv está desligada!"
        else:
            conteudo = "CANAL = "
            for canal in range(ControleRemoto.canal_min, ControleRemoto.canal_max + 1):
                if canal == self.canal_atual:
                    conteudo += f"[black on yellow] {canal} [/]"
                elif canal > ControleRemoto.canal_max:
                    pass
                else:
                    conteudo += f" {canal} "

            conteudo += f"\n"

            conteudo += f"\nVOLUME = "
            for volume in range (ControleRemoto.volume_min, ControleRemoto.volume_max + 1):
                if volume <= self.volume_atual:
                    conteudo += f"[black on cyan] [/]"
                else:
                    conteudo += f"[black on white] "

        tv = Panel(conteudo, title="TV", expand=False)
        print(tv)


tv = ControleRemoto()
while True:
    tv.mostrar_tv()
    comando = str(input(f" < CH{tv.canal_atual} >   - VOL{tv.volume_atual} + "))
    match comando:
        case "sair":
            print ("\n volte sempre!")
            break
        case "@":
            tv.ligar()
        case ">":
            tv.canal_mais()
        case "<":
            tv.canal_menos()
        case "+":
            tv.volume_mais()
        case "-":
            tv.volume_menos()
    print("\n" * 10)