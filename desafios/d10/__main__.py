from classes import *

def main():

    dis = 20

    m = Moto(dis)
    print (f"O frete de {type(m).__name__} em {dis}km = R${m.calcular_frete()}")


if "__main__" == __name__:
    main()