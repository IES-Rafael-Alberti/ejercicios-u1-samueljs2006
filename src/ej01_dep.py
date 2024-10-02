def saludo(nom):
    return "hola," + nom + "."

def main():
    nombre = input("escribe tu nombre:")
    print(saludo(nombre))



if __name__=="__main__":
    main()