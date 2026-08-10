from classes import *
from rich import inspect

def main():
    c = ContaBancaria(1, "kevin", 1000, "123")
    c.nome = "lucas"
    c.sacar(10, "123")
    print(c)

if __name__ == "__main__":
    main()