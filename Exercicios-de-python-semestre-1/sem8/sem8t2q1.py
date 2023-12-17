# A função "num" recebe um número inteiro como entrada.
def num(n1):

    # Inicializa uma variável "val" com valor 0.
    val = 0

    # Verifica se o número é par (resto da divisão por 2 é 0) e, se for, adiciona 5 a ele.
    if n1 % 2 == 0:
        val = n1 + 5
    # Se o número não for par (ímpar), adiciona 8 a ele.
    if n1 % 2 == 1:
        val = n1 + 8
    
    # Retorna o valor resultante após a adição.
    return val

# Solicita um número inteiro ao usuário.
numero = int(input())

# Chama a função "num" com o número fornecido para realizar a adição conforme a condição.
res = num(numero)

# Imprime o resultado da operação.
print(res)
