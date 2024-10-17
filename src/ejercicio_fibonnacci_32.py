def fibonacci_hasta_n(n):
    serie = [0, 1]
    
    while serie[-1] + serie[-2] <= n:
        siguiente = serie[-1] + serie[-2]  
        serie.append(siguiente)
    
    return serie

def main():
    numero = int(input("Ingresa un número: "))
    serie_fibonacci = fibonacci_hasta_n(numero)
    print(f"Serie de Fibonacci hasta {numero}: {serie_fibonacci}")

if __name__ == "__main__":
    main()