def numero(n1, n2):
    if n1 == n2:
        return 0
    elif n1 > n2 :
        return n1
    else:
        return n2


def main():
    n1 = 6
    n2 = 4
    print(numero(n1, n2))


if __name__ == "__main__":
    main()