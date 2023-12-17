# A função 'consoante' é criada com o parâmetro 'caractere' que é definido pela leitura do valor da variável de mesmo nome, após isso a função é chamada para execução na variável 'resultado'. Na função é criado um conjunto e verificado se o caractere digitado pertence ao conjunto para exibir o resultado, True: se for consoante, False: se não for.



def consoante(caractere):

    alfabeto = {"b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"}

    return caractere in alfabeto


caractere = input()

resultado = consoante(caractere)

print(resultado)
