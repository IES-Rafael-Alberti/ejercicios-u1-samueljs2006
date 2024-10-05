precio = float(input("Introduce el precio del producto en euros (con dos decimales): "))

euros = int(precio)
centimos = int((precio * 100) % 100)

print("Euros:", euros)
print("Céntimos:", centimos)