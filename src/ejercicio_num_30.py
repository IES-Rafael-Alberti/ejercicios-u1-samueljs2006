def es_primo(n, divisor=None):
    if divisor is None:
        divisor = n - 1
    if n < 2:
        return False
    if divisor == 1:
        return True
    if n % divisor == 0:
        return False
    
    return es_primo(n, divisor -1)



def main():
    numero = int(input("Introduce un numero: "))
    if es_primo(numero):
        print(f"{numero} es un número primo")
    else:
        print(f"{numero} no es un número primo")




if __name__ == "__main__":
    main()