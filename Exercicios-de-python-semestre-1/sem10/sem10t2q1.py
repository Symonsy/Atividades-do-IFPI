'''01. Escreva um programa que gera a letra da canção muito popular entre os programadores:
99 bugs no software, pegue um deles e conserte...
100 bugs no software, pegue um deles e conserte...
101 bugs no software, pegue um deles e conserte...
...
Faça o programa de forma a gerar a letra da música com o número de bugs no software variando de 99 a
250.'''

# a função 'musica' é criada
def musica():

# a variavel versos é criada pra armazenar os versos da canção
    versos = ""

# as condicionais são criadas para que não haja quebra de linha no final do código e adicionar o final na proxiam linha.
    for i in range(98, 250):
        if i == 249:
            versos += f"{i+1} bugs no software, pegue um deles e conserte..."
        else:
            versos += f"{i+1} bugs no software, pegue um deles e conserte...\n"

# retorna a varivel 'versos'
    return versos

# imprime a função
print(musica())

