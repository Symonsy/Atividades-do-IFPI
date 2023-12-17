'''
Escreva um programa que leia um número inteiro entre 100 e 999, mostre quantos dígitos pares existem nesse número. Por exemplo: 245 tem 2 dígitos pares;
135 tem 0 dígitos pares; 134 tem 1 dígito par.
centenas: C 456//100
dezenas: D = (456 // 10) % 10
unidades: U = 456 % 10

'''

# A função "num" recebe um valor inteiro "val" como entrada.
def num(val):
    # Separa o valor em centenas, dezenas e unidades.
    c = val // 100
    d = (val // 10) % 10
    u = val % 10

    # Se o valor estiver entre 0 e 99, retorna "0".
    if 0 <= val <= 99:
        return "0"

    # Inicializa uma variável para contar os dígitos pares.
    num_pares = 0

    # Verifica se cada dígito é par e incrementa a contagem se for.
    if c % 2 == 0:
        num_pares += 1
    if d % 2 == 0:
        num_pares += 1
    if u % 2 == 0:
        num_pares += 1

    # Retorna o número de dígitos pares como uma string.
    return f"{num_pares}"

# Obtém um número inteiro da entrada do usuário.
number = int(input())

# Chama a função "num" com o número fornecido e armazena o resultado.
result = num(number)

# Imprime o resultado.
print(result)
