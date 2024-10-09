correo = input("Introduce tu correo electrónico: ")

nombre = correo.split('@')

nuevo_correo = f"{nombre}@ceu.es"

print("Tu nuevo correo electrónico es:", nuevo_correo)