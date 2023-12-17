'''01. Escreva um programa que calcule o fatorial de um número inteiro lido, sabendo-se que:
N ! = 1 x 2 x 3 x ... x N-1 x N
0 ! = 1
'''

def calc(n):

    res = 1

    while n >= 1:
        
        res *= n  # Multiplica o resultado 'res' pelo valor atual de 'n'
        n -= 1   # Decrementa 'n' em 1 unidade

    return res  # Retorna o resultado final após o loop

val = int(input())  # Solicita a entrada de um número inteiro
r = calc(val)       # Chama a função 'calc' com 'val' como parâmetro e armazena o resultado em 'r'
print(r)            # Imprime o resultado
