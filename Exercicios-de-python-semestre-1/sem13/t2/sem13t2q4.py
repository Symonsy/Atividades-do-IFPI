'''4. Escreva um programa que leia uma quantidade indeterminada de números reais, terminada pela leitura de
um número 0 (zero). O programa deve mostrar uma nova lista onde cada elemento é a soma dos elementos
anteriores da lista original.
IMPORTANTE: Crie uma função chamada soma_cumulativa() que receba a lista original e retorna
uma lista com a soma cumulativa. Por exemplo:
minha_lista =  [1, 2, 3, 4, 5]
soma_cumulativa = [1, 3, 6, 10, 15]'''



def calc():
# a listas "l1" vai armazenar os numeros digitados antes de soma-los ja a "l2", armazena os elementos já somados
    l1 = []
    l2 = []

# este loop irá receber os numeros para a lista "l1" at´que "0" seja digitado.
    while True:
        val = int(input())
        if val == 0: break
        l1.append(val)

# depois dos numeros serem digitados na lista "l1", um loop finito vai se iniciar com "l1" sendo o conjunto a ser percorrido, e a cada iteração, um digito é adicionado na lista "l2", e na próxima, o elemento é definido como: ao que foi adicionado, mais o próximo elemento da primeira lista, "l1", depois é adicionado na na lista "l2".
    n = 0 
    for i in (l1):
        n += i
        l2.append(n)    

# retorna a lista "l2"
    return f'{l2}'

# imprime o retorno
print(calc())


