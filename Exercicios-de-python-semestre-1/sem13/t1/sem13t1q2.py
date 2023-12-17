'''Escreva um programa que leia um número n. Considere uma lista com n posições, e então:

a) preencha com 0 (zero) e imprima a lista;
b) preencha com os números de 1 a n e imprima a lista;
c) preencha com valores lidos pelo teclado e imprima a lista;
d) preencha na ordem inversa com valores lidos pelo teclado e imprima a lista;
dica: use insert para sempre incluir os elementos no início da lista;
'''

def calc (n):

# as listas vão armazenar as repostas indicadas pelas letras
    l1 = [] #a)
    l2 = [] #b)
    l3 = [] #c)
    l4 = [] #d)

#a) cada item no intervalo "n" vai ser igualdado a "0" e será adicionado na lista "l1"
    for i in range(n):
        i = 0
        l1.append(i)

#b) cada item no intervalo "n" será mandado para a lista "l2", começando do número "1".
    for i in range(n):
        l2.append(i+1)     

#c) em um intervalo "n", o usuário irá digitar "n" números e eles serão adicionados a lista "l3"
    for i in range(n):
        i = int(input())
        l3.append(i)

#d) em um intervalo "n", o usuário irá digitar "n" números, e a acada iteração eles serão adicionados na lista "l4" na posição "0" fazendo com que os que foram digitados antes sejam "empurrados" pra direita, "invertendo" a lista.
    for i in range (n):
        i = int(input())
        l4.insert(0, i)

# retorna as listas    
    return f'{l1}\n{l2}\n{l3}\n{l4}'



def main():
# a veriável "val" recebe o número "n" e a variável "res" recebe o resultado da função, depois é imprimida.
    val = int(input())
    res = calc(val)
    print(res)

if __name__ == '__main__':
    main()
