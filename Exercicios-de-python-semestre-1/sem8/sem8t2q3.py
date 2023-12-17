# A função "num" recebe um número inteiro como entrada.
def num(val):
    # Verifica se o número é igual a zero.
    if val == 0:
        return "0"
    # Verifica se o número é divisível por três e por cinco ao mesmo tempo.
    if val % 3 == 0 and val % 5 == 0:
        return "FIZZBUZZ"
    # Verifica se o número é divisível por três.
    if val % 3 == 0:
        return "FIZZ"
    # Verifica se o número é divisível por cinco.
    if val % 5 == 0:
        return "BUZZ"
    # Se o número não for divisível por três ou por cinco, retorna o próprio número.
    if val % 3 != 0 and val % 5 != 0:
        return val

# Solicita um número inteiro ao usuário.
numero = int(input())

# Chama a função "num" com o número fornecido para determinar a resposta.
res = num(numero)

# Imprime a resposta.
print(res)
