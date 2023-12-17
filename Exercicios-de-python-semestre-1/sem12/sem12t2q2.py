'''02. A Sequência de Fibonacci é uma sequência de números inteiros, começando por 0 e 1, na qual, cada termo
subsequente corresponde à soma dos dois anteriores (0, 1, 1, 2, 3, 5, 8, 13, ...). Escreva um programa que
leia um número n, calcule e mostre os n primeiros termos da sequência de Fibonacci. O valor lido para n
sempre será maior ou igual a 2.'''
def calc(n):
    res = [1]  # Inicializa uma lista 'res' com o primeiro elemento 1
    n1 = 0    # Inicializa a variável 'n1' com 0
    n2 = 1    # Inicializa a variável 'n2' com 1
    n -= 1    # Subtrai 1 de 'n' para considerar os próximos números na sequência

    while n > 1:
        # Calcula o próximo número na sequência Fibonacci somando 'n1' e 'n2'
        new_res = n1 + n2
        n1 = n2   # Atualiza 'n1' para o valor anterior de 'n2'
        n2 = new_res  # Atualiza 'n2' para o novo número calculado
        n -= 1    # Decrementa 'n' para avançar na sequência
        res.append(new_res)  # Adiciona o novo número à lista 'res'

    res = tuple(res)  # Converte a lista 'res' em uma tupla

    return res  # Retorna a tupla contendo a sequência de Fibonacci

val = int(input())  # Lê um número inteiro 'val' a partir da entrada
res = calc(val)     # Chama a função 'calc' com 'val' como argumento e armazena o resultado em 'res'

# Imprime a sequência de Fibonacci
print("0, " + ', '.join(map(str, res)))

