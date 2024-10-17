def comprobar_entero(cadena : str) -> bool:
    cadena = cadena.strip()
    return cadena.isdigit() or (cadena.startswith("-") and cadena[1:].isdigit())

def dame_entero() -> int:
    cadena = input("Dame un entero: ")
    if comprobar_entero(cadena):
       return int(cadena)
    else:
       return 0

def main():
    num = dame_entero()
    print(f"escriste un numero {num}")


if __name__ == "__main__":
 main()