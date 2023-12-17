'''3. Escreva um programa que leia uma lista com 20 números inteiros. Escreva os elementos da lista eliminando
elementos repetidos.'''

def calc():

# a 1° lista armazenará os números digitados, e a 2° os elementos únicos
    lista = []
    new_list = []

# nesse loop os números são recebidos e adicionados a primeira lista
    for i in range(20):
        num = int(input())
        lista.append(num)

# nesse loop os números da 1° lista são adicionados a 2° caso não estejam nela    
    for i in lista:
        if i not in new_list:
            new_list.append(i)

# retorna a lista sem numeros repetidos
    return new_list

print(calc())