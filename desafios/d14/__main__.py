from classes import *
from rich import print
from rich import inspect

def main():
    d = Diario()
    d.escrever("Hoje foi um dia incrível!")
    d.escrever("Aprendi muito sobre Python.")
    d.trocar_senha (123, 234)
    print(d.senha)
    

if __name__ == "__main__":
    main()