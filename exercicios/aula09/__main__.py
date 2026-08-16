from classes import *
from rich import print

def main():
    c1 = Carteira(1000)
    c2 = Carteira(10000)
    c1 += 50
    c1 -= 40

    if (c1 <= c2):
       print (f"c1 é menor que c2, c1={c1.saldo} e c2={c2.saldo}")
    else:
       print (f"c2 é menor que c1, c2={c2.saldo} e c1={c1.saldo}")

    print (c1)


if __name__ == "__main__":
    main()