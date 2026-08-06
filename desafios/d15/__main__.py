from classes import *

def main():
    c = Credencial()
    c.senha = "teste"
    print(c.senha)
    c.validar("test")


if __name__ == "__main__":
    main()