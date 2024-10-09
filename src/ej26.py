productos = input("Introduce los productos de la cesta de la compra, separados por comas: ")

lista_productos = productos.split(',')

for producto in lista_productos:
    print(producto.strip()) 