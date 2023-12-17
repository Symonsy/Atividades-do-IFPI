'''
01. Escreva um programa que leia um conjunto de números inteiros e exiba a soma dos mesmos. Observação:
A condição de saída do laço será a leitura do valor 0 (flag)
'''
# a função media é criada sem parâmetros
def media():

# a variável 'soma' é criada vazia para armazenar os valores digitados pelo usuário    
    soma = 0

# o loop é iniciado pedindo um número inteiro para o usúario, e se ele for zero o loop é encerrado, mas antes disso todos os valores digitados antes do zero são adicionados na variavel 'soma'
    while True:
        num = int(input())
        soma +=num
        if num == 0:
            return soma

# imprime o resultado
print(media())