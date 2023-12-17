'''Calcular H = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n, escreva um programa para calcular o valor de H com 4 (quatro) casas decimais. O número n é lido.
'''

# Define uma função 'calc' que recebe um número 'n' como parâmetro
def calc(n):
    # Inicializa a variável 'h' que irá armazenar o resultado da soma
    h = 0
    # Inicializa a variável 'x' para controlar o loop
    x = 1

    # Enquanto 'x' for menor ou igual a 'n', continue somando os termos
    while x <= n:  
        # Adiciona o termo 1/x ao resultado 'h'
        h += 1.0 / x  
        # Incrementa 'x' para passar para o próximo termo
        x += 1

    # Retorna o valor de 'h' com 4 casas decimais formatado como uma string
    return f'{h:.4f}'

# Lê o valor de 'n' a partir da entrada padrão
val = int(input())
# Chama a função 'calc' com o valor lido e armazena o resultado em 'res'
res = calc(val)
# Imprime o resultado com 4 casas decimais
print(res)

