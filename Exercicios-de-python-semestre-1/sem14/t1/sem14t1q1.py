'''
1. As estruturas básicas de programação são sequência, condição e repetição. Usando apenas as
estruturas básicas de programação, reescreva as funções abaixo (sem utilizá-las):
a) len(), que recebe uma lista e retorna número de itens;
b) reverse(), que recebe uma lista e retorna uma lista com os itens na ordem invertida;
c) min(),que recebe uma lista e retorna o menor valor
d) max(), que recebe uma lista retorna o maior valor
e) sum(), que recebe uma lista retorna a soma dos valores
Faça a leitura dos valores necessários pelo teclado, a leitura de um número 0 (zero) encerra a
leitura dos elementos da lista. Para cada uma das opções, imprima a lista que foi lida e o
resultado encontrado.
Dica: Você pode usar esses nomes para suas funções: comprimento(), inverter(),
minimo(), maximo(), soma().
'''

def calc():

# A lista "l1" receberá os número digitados sem nenhuma alteração, "l2"a reposta da letra b)(l1 ao contrário), e a variável "count" vai servir como um contador pra reponder a letra a)
    l1 = []
    l2 = []
    count = 0

# nesse loopsão 
    while True:
        val = int(input())
        l1.append(val)
        if val == 0: break
    
    l1.remove(0)

#a) nessa parte do código, é adicionado mais um na variável "count" para cada elemento da lista, obtendo assim o seu tamanho
    for i in l1:
        count+=1

#b) nesse loop, a acada iteração os elementos de "l1" serão adicionados na lista "l2" na posição "0" fazendo com que os que foram digitados antes sejam "empurrados" pra direita, "invertendo" a lista.
    for i in(l1):
        l2.insert(0, i)

#c) o primeiro valor da lista é o ponto de partida para a comparação com os outros valores da "l2". A cada iteração a variável "menor" receberá o elemento "i" da lista "l2" que está sendo comparado, mas só se for "i" for menor que o valor da variável "menor". Assim no final todos os elementos serão verificados e a variável "menor" conterá o menor valor de "l2".
    menor = l2[0]
    for i in(l2):
        if i < menor:
            menor = i
#d) o primeiro valor da lista é o ponto de partida para a comparação com os outros valores da "l2". A cada iteração a variável "maior" receberá o elemento "i" da lista "l2" que está sendo comparado, mas só se for "i" for maior que o valor da variável "maior". Assim no final todos os elementos serão verificados e a variável "maior" conterá o menor valor de "l2".
    maior = l2[0]
    for i in(l2):
        if i > maior:
            maior = i

#e) A cada iteração os valores de "l1" são somados na variável "acumulador"
    acumulador = 0
    for i in l1:
        acumulador += i

# retorna a lista normal, a quantidade de elementos, a lista invertida, o menor valor, o maior valor, e a soma dos elementos da lista
    return f'{l1}\n{count}\n{l2}\n{menor}\n{maior}\n{acumulador}'

# imprime o retorno
print(calc())