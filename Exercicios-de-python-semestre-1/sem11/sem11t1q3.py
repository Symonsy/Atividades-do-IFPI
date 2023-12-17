'''
03. Escreva um programa que leia uma quantidade indefinida de números inteiros positivos terminada pelo
número 0 (zero). Ao final, o programa deve mostrar o maior e o menor de todos os números lidos
(excluindo o zero).
Dica: use repetição com teste no final
'''

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

# a variável 'maior' vai receber depois do fim do loop o maior numero da lista através da função embutida 'max()', e a variável 'menor', através da função embutida 'min()', vai receber o menor da lista
    maior = max(numeros)
    menor = min(numeros)

# retorna os numeros obtidos
    return f'{maior}\n{menor}'

# imprime o resultado
print(media())