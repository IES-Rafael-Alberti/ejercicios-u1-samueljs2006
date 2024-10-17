def obtener_divisores(n, divisor=1, divisores=None):
    if divisores is None:
        divisores = []
    
    if divisor > n:
        return divisores
    
    if n % divisor == 0:
        divisores.append(divisor)
    
    return obtener_divisores(n, divisor + 1, divisores)

def main():
    numero = int(input("Ingresa un número: "))
    divisores = obtener_divisores(numero)
    
    if divisores:
        print(f"Los divisores de {numero} son: {divisores}")
    else:
        print(f"{numero} no tiene divisores")

if __name__ == "__main__":
    main()