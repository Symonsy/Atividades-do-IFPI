'''2. Escreva um programa que leia uma lista com 100 números. Ao término da leitura o programa deve fazer a
ordenação dos números lidos. Após a ordenação, crie uma lista onde os elementos de índice par são
multiplicados por 3 e os elementos de índice ímpar são multiplicados com 5.
DICA: Use a função a sorted() ou o método sort() para realizar a ordenação dos valores.
'''
def calc():

# a lista "l1" vai armazenar os items na ordem que foram digitados e "l2" vai receber os números após a ordenação
    l1 = []
    l2 = []

# nesse loop os número são recebidos e mandados pra lista "l1"
    for i in range(100):
        numero = int(input())
        l1.append(numero)
    
# a listas "l1" é ordenada com a função "sorted()"
    l1 = sorted(l1)

# nesse loop a cada iteração os itens de "l1" são verificados, multiplicados por 3 ou pro 5 se forem parres ou ímperes, respectivamente, e adicionados a "l2"
    for i in range(len(l1)):
        if i % 2 == 0:
            l2.append(l1[i]*3)
        else:
            l2.append(l1[i]*5)
    
# retorna a função "l2"
    return f'{l2}'

# imprime o retorno
print(calc())