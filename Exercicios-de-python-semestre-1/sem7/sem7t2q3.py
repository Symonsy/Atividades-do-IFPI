'''
Escreva um programa que leia um número inteiro entre 10 e 99, mostre uma das mensagens, a seguir, conforme o número lido.

Nenhum dígito é ímpar.
Apenas um dígito é ímpar.
Os dois dígitos são ímpares.

'''


# A função "num" recebe um valor inteiro "val" como entrada.
def num(val):
    # Separa o valor em dezenas e unidades.
    d = val // 10
    u = val % 10

    # Verifica se o valor está entre 10 e 99.
    if 10 <= val <= 99:
        return "Nenhum dígito é ímpar."
    # Verifica as combinações de paridade dos dígitos.
    elif d % 2 == 0 and u % 2 == 0:
        return "Nenhum dígito é ímpar."
    elif d % 2 == 0 and u % 2 == 1:
        return "Apenas um dígito é ímpar."
    elif d % 2 == 1 and u % 2 == 0:
        return "Apenas um dígito é ímpar."
    elif d % 2 == 1 and u % 2 == 1:
        return "Os dois dígitos são ímpares."

# Solicita um valor inteiro ao usuário.
valor = int(input("Digite um valor entre 10 e 99: "))

# A variável result chama a função "num".
result = num(valor)

# Imprime o resultado.
print(result)
