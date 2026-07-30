from classes import *

def main():
    c1= ContaBancaria(1,"kevin",2000)
    c1.deposito(-100)
    c1.saldo = 1
    print(c1)


if __name__ == "__main__":
    main()