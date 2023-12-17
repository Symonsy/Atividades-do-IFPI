'''Escreva um programa que leia 10 números inteiros e os armazene em uma lista. Imprima a lista, o maior
elemento e a posição que ele se encontra.
'''
def calc():

# esta lista armazenará os números digitados
    list = []

# nesse loop os número serão recebidos e adicionados a lista
    for i in range(10):
        num = int(input())
        list.append(num)

# a variável "higher_num" receberá, através da função "max()", o maior número da lista, e a variável "ind", com a função "index()", receberá o índice desse elemento
    higher_num = max(list)
    ind = list.index(higher_num)

# a lista o moior número e seu índice são retornados
    return f'{list}\n{higher_num}\n{ind}'

# o retorno é imprimido
print(calc())