nombre = input("Escribe un nombre: ")
edad = -1
while (edad < 0 or edad > 125):
    edad = int(input("Escribe una edad entre 0 y 125 años: "))
if(nombre == ""):
    nombre = "desconocido"
if ( edad > 0 or edad < 125):
    print(f"**Te llamas {nombre}  y tienes {edad} años, te quedan aún {125-edad} años por cumplir**.")
