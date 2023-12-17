# Escreva um programa que leia um caractere e mostra o valor booleano True (verdadeiro) se for uma LETRA (vogal
# ou consoante) ou o valor booleano False (falso) caso contrário.


# A função 'alfabeto' é criada com o parâmetro 'caractere' que é definido pela leitura do valor da variável de mesmo nome, após isso a função é chamada para execução na variável 'resultado'. Na função é criado um conjunto e verificado se o caractere digitado pertence ao conjunto para exibir o resultado, True: se for letra do alfabeto, False: se não for.


def alfabeto(caractere):

    alfabeto = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"}

    return caractere in alfabeto


caractere = input()

resultado = alfabeto(caractere)

print(resultado)
