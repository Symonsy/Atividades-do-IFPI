# Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for um SÍMBOLO (o
# que não é letra ou número) ou o valor booleano False (falso) caso contrário.
# A função 'careceteres' é criada com o parâmetro 'caractere' que é definido pela leitura do valor da variável de mesmo nome, após isso a função é chamada para execução na variável 'resultado'. Na função é criado um conjunto e verificado se o caractere digitado pertence ao conjunto para exibir o resultado, False: se for letra do alfabeto ou um numero de um a nove, True: se não for.

def caraceteres(caractere):
    carat3res = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
                 "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}

    if caractere in carat3res:
        return False
    else:
        return True


caractere = input()
resultado = caraceteres(caractere)
print(resultado)
