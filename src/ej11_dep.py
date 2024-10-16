def calcular_suma(num):
    suma = (num * (num + 1)) /2

    return  f"Resultado: {suma:.2f}"


def main():
    num = int(input("Introduze un numero: "))

    resultado = calcular_suma(num)

    print(resultado)



if __name__ == "__main__":
    main()