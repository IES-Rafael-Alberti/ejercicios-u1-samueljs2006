import random


def dame_un_numero_aleatrio(min, max):
    return random.randint(min, max)



def main():
    min = int(input("Dame el minimo: "))
    max = int(input("Dame el maximo: "))

    num_aleatorio = dame_un_numero_aleatrio(min, max)
    print(f"Cálculo de un número aleatorio entre dos valores : {num_aleatorio} " )

if __name__ == "__main__":
    main()