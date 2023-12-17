#Escreva um programa que leia um conjunto de 100 números inteiros positivos e determine o maior deles.

# a função 'ver' é criada
def ver():

# a lista 'números' é criada para armazenar a sequencia
    numeros = [0]

# um loop de cem vezes é criado
    for i in range(100):

# a cada repetição recebe a entrada do usuário
        val = int(input())

# adiciona a entrada a lista
        numeros.append(val)
# ja fora do loop, a variável 'res' recebe o número da lista extraido pela função'max' 
    res = max(numeros)

# retorna a variavel 'res'
    return res

# imprime a função
print(ver())
