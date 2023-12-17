'''5. Faça um programa que leia duas listas de 10 elementos. Crie uma lista que seja a união entre as 2 listas 
anteriores, ou seja, que contêm os números das duas listas. Não deve conter números repetidos.
'''

def calc():

    l1 = [] # l1 e l2 amazenarão os dois conjuntos de números
    l2 = []
    l3 = [] # l3 = l1+l2
    l4 = [] # será "l3" sem números repetidos

# os dois próximos loops servirão para receber os 2 conjuntos
    for _ in range(10):
        n1 = int(input())
        l1.append(n1)

    for _ in range(10):
        n2 = int(input())
        l2.append(n2)

# aqui as listas serão unidas
    l3 = l1 + l2

# a cada iteração deste loop, somente se o elemento em questão não estiver em "l4" ele será adicionado a ela
    for _ in l3:
        if _ not in l4:
            l4.append(_)

# retorna "l4"
    return f'{l4}'

# imprime o retorno
print(calc())