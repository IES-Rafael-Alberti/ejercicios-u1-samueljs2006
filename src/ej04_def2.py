def convertir_temperatura(fahrenheit: float) -> float :
    
    celsius = (fahrenheit -32) * 5/9

    return round (celsius, 2)  



def main():
    fahrenheit = float(input("Escribe un grado en Fahrenheit:"))
    grados_celsius = convertir_temperatura(fahrenheit)
    print("Los grados farenheit {:.2f} = {:.2f} ºC".format(fahrenheit, grados_celsius) )


if __name__=="__main__":
    main()