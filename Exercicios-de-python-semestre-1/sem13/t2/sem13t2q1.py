'''1. Escreva um programa que leia uma quantidade indeterminada de números inteiros, terminada pela leitura
de um número 0 (zero). Depois, leia um valor inteiro constante. O programa deve mostrar uma nova lista
onde cada valor da lista original é a multiplicado pelo valor da constante.'''

def calc():

# a lista "l1" vai armazenar os itens digitados primeiro, depois a lista "l2" os numeros ja multiplicados
    l1 =[]
    l2 = []


# nesse loop enquanto a entrada de "val" não for "0", os números serão adicionados na lista "l1", quando for "0", a constante será pedida.
    while True:
        val = int(input())
        if val == 0: break
        l1.append(val)
        l1.remove(0)
        const = int(input())

# nesse loop, a cada iteração, cada elemento de "l1" é multiplicado pela constante e adicionado a "l2"
    for i in range(len(l1)):
        l2.append(l1[i]*const)
    
# retorna a lista     
    return f'{l2}'

# imprime o retorno
print(calc())
