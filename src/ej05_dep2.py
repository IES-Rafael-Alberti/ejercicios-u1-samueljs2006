def calcular_precio(importe: float , iva: float) -> str:
    if iva < 0 or iva > 100:
        iva = 21
    precio_final = importe +(importe * iva / 100)

    resultado = f"El precio final del artículo con IVA ({iva:.2f}) es {precio_final:.2f}€."
    return (resultado)
 

def main():
    importe = float(input("Escribe el importe sin IVA: "))

    iva = float(input("Escribe el porcentaje de IVA a aplicar: "))

    resultado = calcular_precio(importe, iva)
    print(resultado)


if __name__ == "__main__":
    main()