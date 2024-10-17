def conventir_temperatura():
    fahrenheit = float(input("Escribe un grado en Fahrenheit:"))
    
    celsius = (fahrenheit -32) * 5/9

    return f"{celsius:.2f}ºC ({fahrenheit:.2f}ºF)"



def main():
    resultado = conventir_temperatura()
    print(resultado) 


if __name__=="__main__":
    main()