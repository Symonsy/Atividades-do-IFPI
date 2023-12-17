# A função 'caracteres' é criada com o parâmetro 'caractere' que é definido pela leitura do valor da variável de mesmo nome, após isso a função é chamada para execução na variável 'resultado'. Na função é criado um conjunto e verificado se o caractere digitado pertence ao conjunto para exibir o resultado, True: se for letra do alfabeto ou um número de um a 9, False: se não for.

def caraceteres(caractere):
    carat3res = {"a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q",
                 "r", "s", "t", "u", "v", "w", "x", "y", "z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
    return caractere in carat3res


caractere = input()
resultado = caraceteres(caractere)
print(resultado)
