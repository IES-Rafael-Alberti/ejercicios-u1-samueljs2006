def calcular_precio_con_iva(sin_iva, tipo_iva):
    iva = sin_iva * (tipo_iva /  100)
    precio_con_iva = sin_iva + iva

    print(f"Precio final : {precio_con_iva:.2f}")

def main():
    sin_iva = float(input("Escribe el importe sin IVA: "))

    tipo_iva = float(input("Escribe el porcentaje de IVA a aplicar: "))

    calcular_precio_con_iva(sin_iva, tipo_iva)


if __name__ == "__main__":
    main()