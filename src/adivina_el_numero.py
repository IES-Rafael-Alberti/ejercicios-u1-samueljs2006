import random

def main():
    numero_secreto = random.randint(1, 100)
    intentos = 0
    ultimo_intento = None

    print("¡Adivina el número entre 1 y 100!")

    while True:
        entrada = input("Ingresa tu número: ")

        if entrada.isdigit():
            adivinanza = int(entrada)
            if 1 <= adivinanza <= 100:
                intentos += 1

                if adivinanza == numero_secreto:
                    print(f"¡Felicidades! Adivinaste el número {numero_secreto} en {intentos} intentos.")
                    break

                if ultimo_intento is not None:
                    if (adivinanza > ultimo_intento) != (numero_secreto > adivinanza):
                        print("Frío.")
                    else:
                        print("Caliente.")
                    if (numero_secreto > adivinanza >= numero_secreto - 10) or (numero_secreto < adivinanza <= numero_secreto + 10):
                        print("¡Muy caliente!")
                
                ultimo_intento = adivinanza
            else:
                print("Fuera de rango. Elige entre 1 y 100.")
        else:
            print("Error: Ingresa un número válido.")

if __name__ == "__main__":
    main()