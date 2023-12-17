'''2. Escreva um programa que leia uma lista com 10 números reais, calcule e mostre a lista, a quantidade de
números negativos e a soma dos números positivos dessa lista'''

def calc():
    
    list_ = [] # esta lista armazenará os números digitados, a variável "count1" a quantidade de numeros negatvos, e "count2" a soma dos positivos
    count1 = 0
    count2 = 0

# nesse loop, os 10 números serão digitados e adicionados na lista "list_" e se forem menores que 0, mais 1 será somado a variável "count1", se não, esse número será somado a variável "count2"
    for i in range(10):
        num = int(input())
        list_.append(num)
        if num < (0):
            count1 += 1
        else:
            count2 += num

# a lista, a quantidade de números negativos e a soma dos números positivos são retornados
    return f'{list_}\n{count1}\n{count2}'

# o retorno é imprimido
print(calc())