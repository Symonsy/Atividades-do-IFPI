# 03. Escreva um programa que leia um conjunto de 100 números inteiros e exiba o valor médio dos mesmos
# (com duas casas decimais).

# a função 'num' é criada
def num():

# a variável 'media' é inicializada com o valor 0
    media = 0

# um loop de 100 vezes é estabelecido    
    for k in range (1,101):

# a variável 'val' recebe as entradas do usuário
        val = int(input())

# a variável media recebe todos os valores digitados        
        media += val

# retorna a media do numero com 2 casas decimais
    return f'{media/100:.2f}'

# imprime a função       
print(num())