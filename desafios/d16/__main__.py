from classes import *
from rich import inspect, print

def main():
    c=ContaBancaria(1, "kevin", 1000)
   
    
    while True:
        print("""
        [1] [purple]trocar nome do titular[/]
        [2] [red1]sacar[/]
        [3] [blue]depositar[/]
        [4] [green3]mostrar dados da conta[/]
        [5] [red]sair[/]
        """)
        opcao = int(input("escolha uma opção: "))
        match opcao:
            case 1:
                nome = str(input("Digite o novo nome: "))
                c.nome = nome
                print(c.nome)

            case 2:
                valor = float(input("Insira quanto você quer sacar: "))
                print(c.sacar(valor))

            case 3:
                valor = float(input("Insira o valor que deseja depositar: "))
                print(c.depositar(valor))

            case 4:
                print(c)

            case 5:
                print("Tchau, volte sempre!")
                break

            case _:
                print("Opação invalida!")

    

if __name__ == "__main__":
    main()