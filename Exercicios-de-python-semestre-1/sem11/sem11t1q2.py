'''
02. Escreva um programa que leia uma quantidade indefinida de números inteiros positivos terminada pelo
número 0 (zero). Ao final, o programa deve mostrar a média aritmética de todos os números lidos
(excluindo o zero).
Dica: use repetição com teste no final
'''

# cria uma fun~ção que verifica se tem zero no numero

# como posso ver quantas vezs uma variável foi executada, ou quantas entradas ela recebeu em um loop?


# estrutura geral:

# 1 - função que verfica se tem zero no final
# 2 - função que com loop recebe os números, armazena eles numa lista e o divisor vai ser cquantos número tem na lista, e dar um jeito de tirar o zero do numero
#  nessa função vai ter uma variável 'media' inicializada como '0' 
#  colocar o teste no final como:
# se a função que verifica se tem número não não for verdadeira: 'break'


# a função media é criada sem parâmetros
def media():

# a lista 'numeros' é criada vazia para armazenar os valores digitados pelo usuário    
    numeros = []

# o loop é iniciado pedindo um número inteiro para o usúario, e se ele for zero o loop é encerrado, mas antes disso todos os valores digitados antes do zero adicionados na lista
    while True:
        num = int(input())
        if num == 0:
            break
        numeros.append(num)

# a variável 'divisor' vai receber depois do fim do loop o número de elementos da lista através da função embutida 'len()', e a variável 'soma', através da função embutida 'sum()', vai receber a soma dos elemtnetos da lista
    divisor = len(numeros)
    soma = sum(numeros)

# a vriável 'res' recebe a média calculada e é retornada após isso., de acordo com a formatação pedida
    res = soma / divisor
    return f'{res:.2f}'

# imprime o resultado
print(media())