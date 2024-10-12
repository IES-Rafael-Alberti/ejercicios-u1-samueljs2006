def calcular_importe_total(horas_de_trabajos, coste_por_hora):
    return horas_de_trabajos *coste_por_hora

def main():
    horas_de_trabajos = int (input ("cuantas horas trabajas: "))
    coste_por_hora = int (input ("cuanto te paga: "))

    importe_total= calcular_importe_total(horas_de_trabajos, coste_por_hora)


    print(f"importe_total: {importe_total}")




if __name__=="__main__":
    main()