# A função 'invertenumero' é criada com o parâmetro 'num', que é definido pela variável que recebe o número a ser convertido pela função, que é chamada na 13° linha.


def invertenumero(num):
    num = num[::-1]
    return num


def main():

    numero = int(input())
    numero = str(numero)
    print(invertenumero(numero))


if __name__ == "__main__":
    main()
