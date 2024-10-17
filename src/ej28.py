num1 = int(input("Escribe un numero: "))
num2 = int(input("Escribe otro numero: "))

if (num1 == num2):
    print("**Los números no pueden ser iguales**.")
elif (num1 > num2):
    print(f"**El número menor es el {num2} y entre ellos existen {num1-num2} números enteros**")
else:
    print(f"**El número menor es el {num1} y entre ellos existen {num2-num1} números enteros**")

    