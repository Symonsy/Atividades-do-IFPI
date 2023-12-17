'''5. Escreva um programa que leia uma quantidade n, seguido da leitura de uma lista com n valores. O programa
deve imprimir LISTA ORDENADA ou LISTA NÃO ORDENADA, conforme o caso.
IMPORTANTE: Crie uma função chamada esta_ordenado() que recebe uma lista como parâmetro e
retorne True se a lista estiver classificada em ordem crescente, e False se não for o caso. Por exemplo:

esta_ordenado([1, 2, 3])
True
esta_ordenado("b", "a")
False'''


# a função "estaordenada" vai receber a lista e verficar se ela é igual a quando está ordenada através da  função "sorted"
def estaordenada(x):
    return x == sorted(x)

# nessa função, de acordo com o número digitado pelo usuário (x), ele vai poder inserir apenas a quantidade que digitou.
def calc(x):

# os numeros inseridos são armazenados nessa lista a cada iteração do loop logo abaixo.
    l1 = []

    for i in range(x):
        num = str(input())
# adiciona os números digitados na lista "l1"
        l1.append(num)

# verifica o resultado da função "estaordenada" e imprime na tela a mensagem correspondente.
    if estaordenada(l1):
        print("LISTA ORDENADA")
    else:
        print("LISTA NÃO ORDENADA")

# o range é definido pela variável "val"
def main():
    
    val = int(input())
    calc(val)

if __name__=="__main__":
    main()