from classes import *

def main():

    p1 = Guerreiro("Kevin", 2000)
    p2 = Mago("Tiu", 1000)

    p1.atacar(p2, 23)
    p1.mostrar_status(p2)
    


if __name__ == "__main__":
    main()