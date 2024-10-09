nombre_producto = input("Nombre del producto: ")

precio_unitario = float(input("Precio unitario: "))

unidades = int(input("Número de unidades: "))

coste_total = precio_unitario * unidades

print(nombre_producto, f"- {precio_unitario:.2f} € | Unidades: {unidades} | Total: {coste_total:.2f} €")