'''1. Leia uma lista de 10 (dez) números inteiros, mostre os números, sua soma e a multiplicação.'''

def calc():

# a lista "numeros" é criada pra armazenar os valores
    numeros = []

# a variável "mult" é criada pra multiplicar os valores a cada iteração, e o valor um é pra evitar a multiplicação por zero.
    mult = 1

# este loop tem 10 iterações, e em cada uma delas um valor será lidao pelo usuáio e será adicionado na lista e multiplicado pela variável "mult"
    for i in range(10):
        val = int(input())
        numeros.append(val)
        mult *= val

# a variável "soma" vai armazenar a soma dos valores da lista usando a função "sum()"
    soma = sum(numeros)

# retorna os valores da lista, soma e multiplicação
    return f'{numeros}\n{soma}\n{mult}'

# a função print é usada para imprimir o resultado da função
print(calc())