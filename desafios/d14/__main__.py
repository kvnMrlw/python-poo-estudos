from classes import *
from rich import print

def main():
    d = Diario()
    d.escrever("Hoje foi um dia incrível!")
    d.escrever("Aprendi muito sobre Python.")
    d.trocar_senha = 123
    

if __name__ == "__main__":
    main()